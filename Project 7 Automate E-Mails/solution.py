from secret import Credentials
import yagmail

yag = yagmail.SMTP('python.course.stads@gmail.com', Credentials.APP_PW)
recipients = ["automatedbygerman@gmail.com"]
email_subject = "Hello this is a test mail"
contents = "Hallo,\n\nwer ich bin kannst du im Anhang sehen.\n\nBeste Grüße\nGerman"

yag.send(to=recipients,
         subject=email_subject,
         contents=contents,
         attachments=['Project 7 Automate E-Mails\Python_Pro.png']
)