import smtplib

gmail_user = 'hoangnph@gmail.com'
gmail_password = 'H0angnph@123'

sent_from = gmail_user
to = ['hoang.nguyenphu@savis.vn']
subject = 'OMG Super Important Message'
body = "Hey, what's up?\n\n- You"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)


try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    print('Connected...')
    server_ssl.login(gmail_user, gmail_password)
    server_ssl.sendmail(sent_from, to, email_text)
    server_ssl.close()
    print("Email sent!")
except:
    print('Something went wrong...')
