import smtplib

MY_EMAIL = "cliden.tria@gmail.com"
MY_PASSWORD = "awrm orlk pcua guca"

class NotificationManager:
    def __init__(self):
        pass

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{message}".encode('utf-8')
                )