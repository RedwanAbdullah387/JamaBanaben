import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


#@pytest.mark.parametrize("username,password", [
   # ("test", "test"),
   # ("redwan", "1234"),
    #("siyam", "SiyamMia111"),
    #("Aylin", "2020")
#])
def test_none_loop_login(driver):
    driver.get("http://127.0.0.1:8000/login/?next=/")

    username_field = driver.find_element(By.ID, "username")
    passw = driver.find_element(By.ID, "pass")  # Update this ID if necessary
    submit = driver.find_element(By.XPATH, "//input[@value='Login']")

    username_field.send_keys("Aylin")
    passw.send_keys("2020")

    submit.click()

    # Wait for the page to load and assert success
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    assert "Successful" in driver.page_source
