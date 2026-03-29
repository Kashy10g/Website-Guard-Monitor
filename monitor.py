import requests
import urllib3
import time

# 1. SETUP: Silence the warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 2. INPUT: Ask ONCE
target_url = input("Enter the website to monitor: ")

print(f"🕵️ Monitoring started. Check 'site_log.txt' for history.")

while True:
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        response = requests.get(target_url, verify=False, timeout=5)
        
        if response.status_code == 200:
            status_msg = f"[{current_time}] ✅ UP - {target_url}"
        else:
            status_msg = f"[{current_time}] ⚠️ ALERT - Code {response.status_code}"

    except Exception:
        status_msg = f"[{current_time}] 🚨 DOWN - Connection Failed"

    # 3. THE LOGGING: Save to a file
    # 'with open' safely opens and closes the file for us
    with open("site_log.txt", "a") as file:
        file.write(status_msg + "\n")
    
    # Still print to terminal so we can see it live
    print(status_msg)

    # 4. THE WAIT
    time.sleep(60)