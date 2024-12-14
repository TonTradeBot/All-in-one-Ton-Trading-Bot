import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Notifier:
    """
    Sends notifications to administrators in case of critical events or errors.
    """

    def __init__(self, notification_settings):
        self.smtp_server = notification_settings.get("smtp_server", "smtp.gmail.com")
        self.smtp_port = notification_settings.get("smtp_port", 587)
        self.email = notification_settings.get("email", "")
        self.password = notification_settings.get("password", "")
        self.recipient = notification_settings.get("recipient", "")

    def send_email(self, subject, message):
        """
        Sends an email with the given subject and message.
        """
        if not self.email or not self.password or not self.recipient:
            print("Email settings are incomplete. Notification not sent.")
            return

        try:
            # Create the email message
            msg = MIMEMultipart()
            msg["From"] = self.email
            msg["To"] = self.recipient
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)

            print(f"Notification sent to {self.recipient}: {subject}")
        except Exception as e:
            print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        settings = {
            "smtp_server": "smtp.gmail.com",
            "smtp_port": 587,
            "email": "your_email@gmail.com",
            "password": "your_password",
            "recipient": "admin@example.com"
        }

        notifier = Notifier(settings)
        notifier.send_email("Test Notification", "This is a test notification from the Solana bot.")
    except Exception as e:
        print(f"Error: {e}")
