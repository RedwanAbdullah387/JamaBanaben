import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://127.0.0.1:8000/user/")

#driver.find_element(By.ID,"")
time.sleep(2)
driver.close()
driver.quit()

print("Done")