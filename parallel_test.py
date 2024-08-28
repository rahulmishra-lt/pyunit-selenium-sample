import time
import os
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")

def get_browser(caps):
    hub_url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"
    
    if caps["browserName"].lower() == "chrome":
        options = ChromeOptions()
    elif caps["browserName"].lower() == "edge":
        options = EdgeOptions()
    elif caps["browserName"].lower() == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {caps['browserName']}")
    
    options.set_capability("platformName", caps["platform"])
    options.set_capability("browserVersion", caps["version"])
    options.set_capability("build", caps["build"])
    options.set_capability("name", caps["name"])
    
    return webdriver.Remote(command_executor=hub_url, options=options)

# You can configure your test capabilities here
browsers = [
    {"build": 'PyunitTest sample build', "name": "Test 1", "platform": "Windows 10", "browserName": "Chrome", "version": "latest"},
    {"build": 'PyunitTest sample build', "name": "Test 2", "platform": "Windows 10", "browserName": "edge", "version": "latest"},
    {"build": 'PyunitTest sample build', "name": "Test 3", "platform": "Windows 10", "browserName": "firefox", "version": "latest"}
]

browsers_waiting = []

# Running the test cases
def get_browser_and_wait(browser_data):
    print(f"starting {browser_data['name']}")
    browser = get_browser(browser_data)
    browser.set_window_size(1600, 1200)
    browser.get("https://lambdatest.com")
    browsers_waiting.append({"data": browser_data, "driver": browser})
    print(f"{browser_data['name']} ready")
    
    while len(browsers_waiting) < len(browsers):
        print(f"browser {browser_data['name']} sending heartbeat while waiting")
        browser.get("https://lambdatest.com")
        time.sleep(3)

thread_list = []
for i, browser in enumerate(browsers):
    t = Thread(target=get_browser_and_wait, args=[browser])
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()

for i, b in enumerate(browsers_waiting):
    print(f"browser {b['data']['name']}'s title: {b['driver'].title}")
    b['driver'].quit()