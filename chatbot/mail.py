import smtplib
import config


def send_email(subject, msg, receiver):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS,receiver, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test subject"
msg = "Hello there, how are you today?"
receiver="ayubayesha07@gmail.com"
send_email(subject, msg, receiver)

#knidhi2196@gmail.com
#rahul4juneruthless@gmail.com