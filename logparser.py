from datetime import datetime
import email, smtplib,ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

errLines=[]
currentdate=datetime.today().strftime('%Y-%m-%d')
print(currentdate)
tomcatlogs="/usr/share/tomcat/logs/catalina"+"."+currentdate+"."+"log"
#==================mail configuration================================
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
subject = "An email with attachment from mail server"
body = "This is an email with attachment sent from Python"
sender_email = "tahashiniesl@gmail.com"
receiver_email="tahashinfreelancer@gmail.com"
# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))
#====================mail configuration end here================================

#========================Prepare error file======================================
def searchError(readfilename,word,writefile):
    with open(readfilename,'r') as fp:
        lines=fp.readlines()
        for line in lines:
            #print(line)
            if word.upper() in line or word.lower() in line:
                errLines.append(line)
                #print(errLines)
        writeinfile(errLines,writefile)

def writeinfile(errors,erorfile):
    with open(erorfile,'w') as eror:
        for line in errLines:
            eror.write(line)

#================= Email send=========================================
def sendMail(fromAddress,toAddress,attachedFile):
    password = input("Type your password and press enter: ")
    # Try to log in to server and send email
    with open(attachedFile, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachedFile}",
    )
    # TODO: Send email here
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    # Log in to server using secure context and send email
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
    except Exception as e:
        # Print any error messages to stdout
        print(e)
         
    

#searchError("apache.log","Error","error.log")
#errLines.clear()
#print(errLines)
#searchError("/usr/share/tomcat/logs/catalina.2022-09-23.log","Severe","severe.log")
sendMail(sender_email,receiver_email,"error.log")