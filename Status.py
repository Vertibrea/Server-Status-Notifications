import subprocess
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time

server_address = "google.com"

def check_server_status(server_address):
    try:
        # Ping the server
        output = subprocess.check_output(["ping", "-c", "1", server_address], text=True)
        print(output)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

#def send_email(subject, body): # !!!!!! JUST A CONCEPTUALIZATION / No password or email included !!!!!!!!
    # Replace these with your email configuration
    sender_email = "**************"
    receiver_email = "***********+"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "pezmonkeylp@gmail.com"
    smtp_password = "**********"

    # Create message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def monitor_servers(servers):
    while True:
        for server in servers:
            if not check_server_status(server):
                subject = f"Server Down - {server}"
                body = f"Server {server} is down at {datetime.now()}. Please investigate."
                send_email(subject, body) #Server Report to ADMIN EMAIL !!!! Only works with credentials !!!!

        # Adjust the interval based on your preferences
        time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    # List of servers to monitor
    servers_to_monitor = ["google.com", "youtube.com"]

    # Start monitoring
    monitor_servers(servers_to_monitor)
