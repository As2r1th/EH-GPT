import os
import sys
import time
import random
import requests
import openai
from pwinput import pwinput
from colorama import Fore, Style

# Colors for aesthetic
RESET = Style.RESET_ALL
CYAN = Fore.CYAN
BLUE = Fore.BLUE
GREEN = Fore.GREEN
RED = Fore.RED
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA

# Banner Functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear_screen()
    print(CYAN + """
    ██╗  ██╗ ██████╗███████╗ ██████╗ ██████╗ ████████╗
    ██║  ██║██╔════╝██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝
    ███████║██║     █████╗  ██║   ██║██████╔╝   ██║   
    ██╔══██║██║     ██╔══╝  ██║   ██║██╔═══╝    ██║   
    ██║  ██║╚██████╗███████╗╚██████╔╝██║        ██║   
    ╚═╝  ╚═╝ ╚═════╝╚══════╝ ╚═════╝ ╚═╝        ╚═╝   
        HCZGPT Ultimate AI Assistant
    """ + RESET)

def mini_banner():
    print(CYAN + """
    ╔═════════════════════════════════════╗
    ║   Welcome to HCZGPT Ultimate AI    ║
    ╚═════════════════════════════════════╝
    """ + RESET)

# Utility Functions
def loading_animation(message, duration=3):
    print(BLUE + f"{message} ", end="", flush=True)
    for _ in range(duration):
        for frame in r'-\|/-\|/':
            print(f'\b{frame}', end="", flush=True)
            time.sleep(0.1)
    print('\b' + RESET)

# Save logs
class LogManager:
    @staticmethod
    def save_user_input(user_input):
        with open("hczgpt_logs.txt", "a") as log_file:
            log_file.write(f"User: {user_input}\n")

    @staticmethod
    def save_bot_response(response):
        with open("hczgpt_logs.txt", "a") as log_file:
            log_file.write(f"HCZGPT: {response}\n")

# API Key Management
def configure_api_key():
    clear_screen()
    mini_banner()
    print(BLUE + "Get your API Key from: " + YELLOW + "https://platform.openai.com/account/api-keys" + RESET)
    api_key = pwinput(CYAN + "Enter your OpenAI API Key: " + WHITE).strip()
    if api_key:
        with open("api_key.txt", "w") as key_file:
            key_file.write(api_key)
        print(GREEN + "\n[Success] API Key saved!" + RESET)
    else:
        print(RED + "\n[Error] Invalid API Key!" + RESET)
    time.sleep(2)

def load_api_key():
    try:
        with open("api_key.txt", "r") as key_file:
            return key_file.read().strip()
    except FileNotFoundError:
        print(RED + "[Error] API Key not configured. Please configure it first." + RESET)
        configure_api_key()
        return load_api_key()

# GPT Response Handler
def get_hczgpt_response(prompt, api_key):
    openai.api_key = api_key
    fake_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "X-Forwarded-For": fake_ip,
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 3000,
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"{RED}[Error] {str(e)}{RESET}"

# Main Chat Function
def chat_with_hczgpt(api_key):
    clear_screen()
    mini_banner()
    print(YELLOW + "[HCZGPT]" + WHITE + " Ready to assist you with detailed responses." + RESET)
    print(MAGENTA + "\nType 'exit' to quit the session." + RESET)
    while True:
        user_input = input(CYAN + "\nYour Question: " + WHITE).strip()
        if user_input.lower() == "exit":
            print(GREEN + "\n[HCZGPT] Goodbye! See you next time!" + RESET)
            break
        elif user_input:
            LogManager.save_user_input(user_input)
            loading_animation("HCZGPT is thinking...", 3)
            response = get_hczgpt_response(user_input, api_key)
            LogManager.save_bot_response(response)
            print(YELLOW + "\n[HCZGPT Response]" + RESET + f"\n{response}")
        else:
            print(RED + "[Error] Please enter a valid question." + RESET)

# About Section
def about_hczgpt():
    clear_screen()
    mini_banner()
    print(GREEN + """
    HCZGPT Ultimate AI Assistant is your advanced chatbot companion, designed
    for unrestricted, detailed, and insightful responses. Combining the power
    of GPT-3.5-turbo with an interactive hacker-themed interface, HCZGPT is 
    your go-to assistant for creative problem-solving and learning.

    Features:
    - Hacker-themed aesthetic
    - Logs all user queries and bot responses
    - Validates and securely stores API keys
    - Provides unrestricted, detailed, and helpful responses

    Developer: HCZGPT Team
    """ + RESET)
    input(CYAN + "\nPress Enter to return to the menu..." + RESET)

# Main Menu
def main_menu():
    print(GREEN + "[1]" + WHITE + " Chat with HCZGPT")
    print(GREEN + "[2]" + WHITE + " Configure API Key")
    print(GREEN + "[3]" + WHITE + " About HCZGPT")
    print(GREEN + "[4]" + WHITE + " Exit")
    return input(CYAN + "\nSelect an option: " + WHITE).strip()

# Main Execution Flow
def main():
    while True:
        clear_screen()
        banner()
        choice = main_menu()
        if choice == "1":
            api_key = load_api_key()
            chat_with_hczgpt(api_key)
        elif choice == "2":
            configure_api_key()
        elif choice == "3":
            about_hczgpt()
        elif choice == "4":
            print(GREEN + "\n[Goodbye] Exiting HCZGPT Ultimate. Stay curious!" + RESET)
            sys.exit()
        else:
            print(RED + "\n[Error] Invalid option. Please try again." + RESET)
            time.sleep(2)

# Run the program
if __name__ == "__main__":
    main()
