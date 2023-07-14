import psutil, smtplib, configparser
from email.mime.text import MIMEText

def send_mail(subject, body):    
    config = configparser.ConfigParser()
    config.read('config.ini')
    sender = config.get("Credentials", "sender_email")
    recipient = config.get("Credentials", "recipient_email")
    password = config.get("Credentials", "password")
     
    message = MIMEText(body)
    message['Subject'] = subject 
    message['To'] = recipient 
    message['From'] = sender
 
    try: 
        smtp_server = smtplib.SMTP('smtp.office365.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender, password) 
        smtp_server.send_message(message)
        smtp_server.quit()
        print("Alarm email sent successfully!")
    except smtplib.SMTPException as e: 
        print("Error:", str(e))
        
def check_disk_usage(disks):
    for disk in disks:
        disk_usage = psutil.disk_usage(disk)    
        disk_precent = disk_usage.percent
        
        if disk_precent >= 85: 
            subject = f"Alarm! Disk {disk} is {disk_precent}% full"  
            body = "Need to clean up the disk"
            send_mail(subject, body)
            print(f"Disk {disk} is full!")
        else:       
            print(f"Check passed successfully for disk {disk}!")

disks_to_check = ["/home", "/",]

if __name__ == "__main__":
    check_disk_usage(disks_to_check)
        


