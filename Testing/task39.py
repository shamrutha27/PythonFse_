from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT, "Bootstrap Alerts").click()

driver.find_element(
    By.XPATH,
    "//button[contains(text(),'Success Message')]"
).click()

# Fluent Wait (Python equivalent)
wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

alert = wait.until(
    lambda d: d.find_element(
        By.XPATH,
        "//div[contains(@class,'alert-success')]"
    )
)

print("Alert Found!")
print(alert.text)

driver.quit()