import yagmail
import pandas as pd

# Uncomment this line and add either your gmail email + app password or outlook email + password
#yagmail.register('german.paul@stads.de', Credentials.APP_PW)

# If you use gmail then just uncomment the line below 
# yag = yagmail.SMTP('german.paul@stads.de')
df = pd.read_excel("/Users/german/Documents/STADS/Python Kurs Privat/pythonkursteilnehmer2.xlsx")

yag = yagmail.SMTP('german.paul@stads.de', host='smtp.office365.com', port=587, smtp_starttls=True, smtp_ssl=False, smtp_set_debuglevel=0, smtp_skip_login=False,
            encoding='utf-8', oauth2_file=None, soft_email_validation=True)
recipients = df.Email
email_subject = "Week 1 Material and Review"
contents = """Hallo zusammen,\n
\n
schön, dass insgesamt über 100 Studierende an der ersten Stunde teilgenommen haben. Es hat Spaß gemacht mit Euch zu arbeiten.\n
\n
Anbei auf Euren Wunsch die PowerPoint.\n

Ebenso findet Ihr unter dieser URL wie ich im Kurs erwähnt habe, alle Ressourcen und den Plan für die nächsten Woche. Der konkrete Plan wird immer eine Woche vorher online gestellt.\n
https://python-kurs.streamlit.app \n
\n
Falls Ihr es kaum erwarten könnt weiterzumachen, dann bearbeitet ruhig weiterhin die Ressourcen, die bereits online sind, ich habe genug Nachschub, das heißt Euch wird auch nicht langweilig, wenn Ihr vorarbeitet.\n
\n
Ansonsten sehen wir uns nächste Woche. Ich wünsche Euch einen schönen Sonntag!\n
\n
Beste Grüße\n
\n
German \n
"""


yag.send(bcc=recipients.tolist(),
         subject=email_subject,
         contents=contents,
         attachments=['/Users/german/Documents/Presentations/Slides Python Course STADS e.V..pptx']
)