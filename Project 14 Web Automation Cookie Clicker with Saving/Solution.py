from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import pyperclip
    

# CONSTANTS
PATH_WHERE_TO_SAVE_GAME_PROGRESS = ""    
    
    
# CHROME DRIVER
    
chrome_driver_path = "/Applications/chromedriver"
options = webdriver.ChromeOptions()

# EDGE DRIVER WITH PROXY
'''
options = webdriver.EdgeOptions()
options.binary_location = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
#options.add_argument('--proxy-server=%s' % PROXY)
chrome_driver_path = "C:/Users/paulg/Downloads/msedgedriver.exe"
PROXY = "http://iproxi.man:80"
driver = webdriver.Edge(service=s, options=options)
'''

options.add_experimental_option('excludeSwitches', ['enable-logging'])

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
wait = WebDriverWait(driver, 60) 
#Get cookie to click on.
cookie = driver.find_element(By.ID, "cookie")

#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
thirty_min = time.time() + 60*5 # 5minutes

#Buttons to Import/Export
wait.until(EC.element_to_be_clickable((By.ID, "importSave")))
import_button = driver.find_element(By.ID, "importSave")
export_button = driver.find_element(By.ID, "exportSave")

count = 0

while True:
    if count == 0:
        try:
            with open(PATH_WHERE_TO_SAVE_GAME_PROGRESS, 'r') as f:
                content = f.read()
            import_button.click()
            time.sleep(0.1)
            pyperclip.copy(content)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.1)
            pyautogui.press('enter') 
            count += 1
            wait.until(EC.element_to_be_clickable((By.ID, "cookie")))
        except:        
            count += 1
        
        
        count += 1
    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:

        #Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        #Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        if len(affordable_upgrades) != 0:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            #print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(By.ID, to_purchase_id).click()
        
        #Add another 5 seconds until the next check
        timeout = time.time() + 5

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > thirty_min:
        export_button.click()
        time.sleep(0.5)
        content = pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)
        pyautogui.press('enter') 
        with open(PATH_WHERE_TO_SAVE_GAME_PROGRESS, 'w+') as f:
            f.write(pyperclip.paste())
        count += 1
        wait.until(EC.element_to_be_clickable((By.ID, "cookie")))
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(f"You achieved to produce {cookie_per_s} cookies per second.")
        break

driver.quit()