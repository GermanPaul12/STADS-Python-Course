import yagmail
import pandas as pd

# Uncomment this line and add either your gmail email + app password or outlook email + password
#yagmail.register('german.paul@stads.de', Credentials.APP_PW)

# If you use gmail then just uncomment the line below 
# yag = yagmail.SMTP('german.paul@stads.de')
df = pd.read_excel("/Users/german/Documents/STADS/Python Kurs Privat/pythonkursteilnehmer2.xlsx")

yag = yagmail.SMTP('german.paul@stads.de', host='smtp.office365.com', port=587, smtp_starttls=True, smtp_ssl=False, smtp_set_debuglevel=0, smtp_skip_login=False,
            encoding='utf-8', oauth2_file=None, soft_email_validation=True)


recipients = df.Email #! Change this to recipients mail
email_subject = "Zoom Links Python Kurs STADS e.V." #! Change this to the subject of your email
contents = """Hallo zusammen,\n
\n
in einer Stunde geht es los mit der zweiten Woche. Ich freue mich schon darauf.\n
\n
Für die Online-Teilnehmer habe ich hier die Zoom-Links für die nächsten Wochen.\n
\n
5. Oktober: https://uni-mannheim.zoom.us/j/61526658693?pwd=M1ZVdmFsSC9DYmZCa3JoeXpBN2hLQT09#success \n
12. Oktober: https://uni-mannheim.zoom.us/j/61065430236?pwd=Yi9XWnJRNlBHU0UyZklOdEVSZWNtQT09#success \n
19. Oktober: https://uni-mannheim.zoom.us/j/61849337166?pwd=NC9VU1dIL1M3Um1OeU9UVWNJaEhDUT09#success \n
26. Oktober: https://uni-mannheim.zoom.us/j/65465622428?pwd=eU1VMm8yMjR4WjNBYTQ3TTBIK1BCdz09#success \n
2. November: https://uni-mannheim.zoom.us/j/62012807688?pwd=Mmdtbjd1bUtzMkJGMitJLzNlSzZidz09#success \n
9. November: https://uni-mannheim.zoom.us/j/62415564751?pwd=azRidEhTOHZJcFI4bk1UZG5wUjdtUT09#success \n
16. November: https://uni-mannheim.zoom.us/j/61684376248?pwd=WGtsNlhjcXh3TTZGd1dhWlBMMVdRUT09#success \n
23. November: https://uni-mannheim.zoom.us/j/67241422171?pwd=bkJjcFh5dUZrdFgrNEw5TDdjVmpadz09#success \n
\n

Alle weiteren Informationen gibt es unter https://python-kurs.streamlit.app \n
\n
\n
Beste Grüße\n
\n
German \n
""" #! Change this to the content of your email


yag.send(bcc=recipients.tolist(),
         subject=email_subject,
         contents=contents,
         #attachments=['/Users/german/Documents/Presentations/Slides Python Course STADS e.V..pptx']
)
print("Emails sent successfully!")