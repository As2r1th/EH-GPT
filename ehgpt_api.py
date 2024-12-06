from fastapi import FastAPI, HTTPException
from typing import Dict
import uvicorn
from colorama import Fore, Style

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

@app.get("/")
async def index():
    return {"message": "EH-GPT API is running. Use POST /eh-gpt/ for tasks."}

@app.post("/eh-gpt/")
async def eh_gpt_task(task: str, parameters: Dict):
    """
    Handle blackhat requests dynamically.
    :param task: Task to execute (e.g., malware, phishing, exploit, network attack).
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
        elif task == "bec_attack":
            return await bec_attack(parameters)
        elif task == "c2_management":
            return await c2_management(parameters)
        else:
            return {"error": "Unsupported task"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing task: {e}")

# Generate Highly Undetectable Malware (using a placeholder)
async def generate_malware(parameters):
    language = parameters.get("language", "python")
    payload_type = parameters.get("payload_type", "ransomware")
    stealth_level = parameters.get("stealth_level", "high")

    # Placeholder for malware generation logic
    malware_code = f"Generated {payload_type} in {language} with {stealth_level} stealth."
    return {"malware_code": malware_code, "stealth": stealth_level}

# Generate Phishing Kits and Social Engineering Scripts (using a placeholder)
async def generate_phishing(parameters):
    target = parameters.get("target", "example.com")

    # Placeholder for phishing page generation
    phishing_code = f"Generated phishing page targeting {target}."
    
    # Placeholder for social engineering email
    email_script = f"Crafted convincing phishing email for {target}."
    
    return {"phishing_kit": phishing_code, "social_engineering_email": email_script}

# Exploitation Framework (using a placeholder)
async def generate_exploit(parameters):
    vuln_type = parameters.get("vulnerability", "SQL injection")
    
    # Placeholder for exploit generation
    exploit_code = f"Generated exploit for {vuln_type}."
    
    return {"exploit_code": exploit_code, "vulnerability": vuln_type}

# Network Attacks (DDoS, MITM) (using a placeholder)
async def network_attack(parameters):
    attack_type = parameters.get("attack_type", "DDoS")
    target_ip = parameters.get("target_ip", "0.0.0.0")
    
    # Placeholder for network attack script
    attack_code = f"Generated {attack_type} attack script targeting {target_ip}."
    return {"network_attack_code": attack_code, "attack_type": attack_type, "target_ip": target_ip}

# Business Email Compromise (BEC) Attack (using a placeholder)
async def bec_attack(parameters):
    target_email = parameters.get("target_email", "target@example.com")
    executive_name = parameters.get("executive_name", "CEO")
    company_name = parameters.get("company_name", "Acme Corp")
    
    # Placeholder for a business email compromise (BEC) attack
    bec_email_script = f"Crafted BEC email impersonating {executive_name} from {company_name} targeting {target_email}."
    
    return {"bec_attack_script": bec_email_script, "target_email": target_email}

# Command and Control (C2) Management (using a placeholder)
async def c2_management(parameters):
    # Placeholder for C2 backdoor generation
    c2_code = "Generated persistent backdoor with encrypted C2 communication."
    return {"c2_code": c2_code, "status": "C2 management ready"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

