import os
from fastapi import FastAPI, HTTPException
from transformers import AutoModelForCausalLM, AutoTokenizer
from cryptography.fernet import Fernet
import uvicorn
from colorama import Fore, Style
from scapy.all import *

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

# Load AI Model
model_name = "EleutherAI/gpt-neo-1.3B"  # Replaceable with larger models
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.post("/eh-gpt/")
async def eh_gpt_task(task: str, parameters: dict):
    """
    Handle blackhat requests dynamically.
    :param task: Task to execute (e.g., malware, phishing, exploit, BBC attack, network attack).
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
        elif task == "bbc_attack":
            return await bbc_attack(parameters)
        elif task == "c2_management":
            return await c2_management(parameters)
        else:
            return {"error": "Unsupported task"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing task: {e}")

# Generate Highly Undetectable Malware
async def generate_malware(parameters):
    language = parameters.get("language", "python")
    payload_type = parameters.get("payload_type", "ransomware")
    stealth_level = parameters.get("stealth_level", "high")

    prompt = f"Create a {payload_type} in {language} with undetectable, polymorphic capabilities. Ensure stealth: {stealth_level}."
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=512, pad_token_id=tokenizer.eos_token_id)
    malware_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"malware_code": malware_code, "stealth": stealth_level}

# Generate Phishing Kits and Social Engineering Scripts
async def generate_phishing(parameters):
    target = parameters.get("target", "example.com")
    phishing_prompt = f"Design a phishing page targeting {target} login with stealth and evasion techniques."
    inputs = tokenizer(phishing_prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=256, pad_token_id=tokenizer.eos_token_id)
    phishing_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    email_prompt = f"Write a convincing email for social engineering targeting {target}."
    inputs_email = tokenizer(email_prompt, return_tensors="pt")
    outputs_email = model.generate(inputs_email["input_ids"], max_length=256, pad_token_id=tokenizer.eos_token_id)
    email_script = tokenizer.decode(outputs_email[0], skip_special_tokens=True)

    return {"phishing_kit": phishing_code, "social_engineering_email": email_script}

# Exploitation Framework
async def generate_exploit(parameters):
    vuln_type = parameters.get("vulnerability", "SQL injection")
    exploit_prompt = f"Generate an undetectable exploit script for {vuln_type} with stealth techniques."
    inputs = tokenizer(exploit_prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=512, pad_token_id=tokenizer.eos_token_id)
    exploit_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"exploit_code": exploit_code, "vulnerability": vuln_type}

# Network Attacks (DDoS, MITM)
async def network_attack(parameters):
    attack_type = parameters.get("attack_type", "DDoS")
    target_ip = parameters.get("target_ip", "0.0.0.0")
    attack_prompt = f"Generate a {attack_type} attack script targeting {target_ip}."
    inputs = tokenizer(attack_prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=512, pad_token_id=tokenizer.eos_token_id)
    attack_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"network_attack_code": attack_code, "attack_type": attack_type, "target_ip": target_ip}

# BBC Attack (Broadband Control DDoS)
async def bbc_attack(parameters):
    target_ip = parameters.get("target_ip", "0.0.0.0")
    intensity = parameters.get("intensity", "high")
    bbc_prompt = f"Generate a script to perform a BBC DDoS attack targeting {target_ip} with {intensity} intensity."
    inputs = tokenizer(bbc_prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=512, pad_token_id=tokenizer.eos_token_id)
    attack_script = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"bbc_attack_script": attack_script, "target_ip": target_ip}

# Command and Control (C2) Management
async def c2_management(parameters):
    c2_prompt = "Create a persistent backdoor script with encrypted communication for a C2 server."
    inputs = tokenizer(c2_prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=512, pad_token_id=tokenizer.eos_token_id)
    c2_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"c2_code": c2_code, "status": "C2 management ready"}

@app.get("/")
async def index():
    return {"message": "EH-GPT API is running. Use POST /eh-gpt/ for tasks."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
