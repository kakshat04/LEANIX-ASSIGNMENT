from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

baseURL = "https://demo-eu.leanix.net/akkDemo /"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get(baseURL)

element = driver.find_element_by_name("j_username")
element.send_keys("kumar.akshat04@gmail.com")

sleep(1)

element = driver.find_element_by_name("j_password")
element.send_keys("Knight@riders1")

sleep(1)

driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()
sleep(2)

driver.find_element_by_id("menuLink").click()
sleep(2)

driver.find_element_by_xpath("//div[@id='appNavbarCollapse']//span[text()='Administration']").click()
sleep(2)

driver.find_element_by_xpath("//a[contains(@class,'integrationApiLink')]").click()
sleep(2)

driver.find_element_by_xpath("//a[contains(text(),'cloudockit')]").click()
sleep(5)


jsonToEnter = {
    "system_service": "SD",
    "version": "1.0.0",
    "checksum": "",
    "machineConfig": {
        "subscriptions": {
            "sinumerik_hf_data": {
                "payload": [{
                    "sinumerikUid": "hfdd_data",
                    "period": 2
                }],
                "source": "communicationAdapter",
                "quality": "high_performance",
                "isCloudMessage": "SDSD"
            }
        }
    }
}

jsonToEnter = json.dumps(jsonToEnter)
z = driver.find_element_by_xpath("/html/body//div[2]/div[2]/div[1]//div[1]/textarea")
z.send_keys(Keys.CONTROL + 'a')
z.send_keys(Keys.DELETE)
pyperclip.copy(jsonToEnter)
z.send_keys(Keys.CONTROL + 'v')

sleep(4)

# Click on run
run_button = "//button[contains(text(),'Run')]"
driver.find_element_by_xpath(run_button).click()





