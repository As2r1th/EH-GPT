#!/bin/bash

### Banner
echo -e "\e[95m
███████╗██╗  ██╗     ██████╗ ██████╗ ████████╗
██╔════╝██║  ██║    ██╔═══██╗██╔══██╗╚══██╔══╝
█████╗  ███████║    ██║   ██║██████╔╝   ██║   
██╔══╝  ██╔══██║    ██║   ██║██╔═══╝    ██║   
███████╗██║  ██║    ╚██████╔╝██║        ██║   
╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝        ╚═╝   
Simplified EH-GPT Installer for Alpine Linux
\e[0m"

### Step 1: Check for Alpine Linux
if ! grep -q Alpine /etc/os-release; then
  echo "This script is only designed for Alpine Linux. Exiting."
  exit 1
fi

### Step 2: Update and Install Alpine Dependencies
echo "[*] Installing Python and necessary packages..."
apk add --no-cache python3 py3-pip git curl

### Step 3: Create a requirements.txt for Python Dependencies
echo "[*] Preparing Python dependencies..."
cat <<EOF > requirements.txt
fastapi==0.95.0
uvicorn==0.22.0
transformers==4.33.0
colorama==0.4.6
cryptography==36.0.0
scapy==2.5.0
EOF

### Step 4: Install Python Libraries
echo "[*] Installing Python libraries from requirements.txt..."
pip3 install -r requirements.txt

### Step 5: Clone EH-GPT Repository
echo "[*] Cloning EH-GPT files..."
if [ ! -d "ehgpt" ]; then
  git clone https://github.com/your-repo/ehgpt.git
fi
cd ehgpt || exit

### Step 6: Run EH-GPT API
echo "[*] Running EH-GPT API..."
python3 ehgpt_api.py
