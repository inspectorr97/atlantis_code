import smtplib
from email.message import EmailMessage

# function to send email


def send_email(sender_email, sender_pwd, message, subject, recipient):
    try:
        msg = EmailMessage()
        msg.set_content(str(message))

        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient

        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_pwd)
        server.send_message(msg)
        server.quit()

        return True
    except Exception as e:
        return e


if __name__ == "__main__":
    sender_email = input("Sender's email? ")
    sender_pwd = input("Sender's password? ")
    subject = input("Subject? ")
    body = input("Body? ")
    recipient = input("Recipient? ")
    status = send_email(sender_email, sender_pwd, body, subject, recipient)
    if status == True:
        print("Email sent!")
    else:
        print("exception occured: ", status)
