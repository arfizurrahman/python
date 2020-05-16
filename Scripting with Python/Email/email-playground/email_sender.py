import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
# p = Path('.')

# print(list(p.glob('**/*.html')))

html = Template(Path('email-playground/index.html').read_text())

email = EmailMessage()
email['from'] = 'Arfizur Rahman'
email['to'] = 'arfizrahman0@gmail.com'
email['subject'] = 'Sending Email via Python'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('rifatrabbi872@gmail.com', 'RifatRabbi872@')
    smtp.send_message(email)
    print('All good boss!')
