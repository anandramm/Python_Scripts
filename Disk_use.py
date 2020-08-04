#Script to alert user for a disk storage breach vi mail
import shutil
import smtplib

path="E:/"

stat = shutil.disk_usage(path)

print(stat)

disk_usage=((stat.used/stat.total)*100)

def check():
   if disk_usage>70:
       return ("Disk space is about to be Filled soon")
   else:
    return ("Disk space is far below the warning level")

def mail():
    sender=example@outlook.com
    receiver=example@gmail.com
    try:
        smtpObj = smtplib.SMTP('smtp-mail-server',587)
        smtpObj.login('example@outlook.com','password')
        smtpObj.sendmail(sender, receiver, check())
        print
        "Successfully sent email"
    except SMTPException:
        print
        "Error: unable to send email"
