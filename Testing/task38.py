from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ---------------------------------------------------------
# Launch Chrome
# ---------------------------------------------------------

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# ---------------------------------------------------------
# Open Selenium Playground
# ---------------------------------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/")

# ---------------------------------------------------------
# Open Bootstrap Alerts page
# ---------------------------------------------------------

wait.until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Bootstrap Alerts")
    )
).click()

print("Bootstrap Alerts page opened.")

# ---------------------------------------------------------
# Wait until Success Message button is clickable
# ---------------------------------------------------------

success_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//button[contains(text(),'Success Message')]"
        )
    )
)

print("Success Message button is clickable.")

# Click the button
success_button.click()

print("Clicked the Success Message button.")

# ---------------------------------------------------------
# Wait until Success Alert is visible
# ---------------------------------------------------------

success_alert = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            "//div[contains(@class,'alert-success')]"
        )
    )
)

print("\nAlert Text:")
print(success_alert.text)

# ---------------------------------------------------------
# Verify Alert
# ---------------------------------------------------------

assert success_alert.is_displayed()

print("\nAssertion Passed!")
print("Success Alert is visible.")

# ---------------------------------------------------------
# Close Browser
# ---------------------------------------------------------

driver.quit()

print("\nTask 38 Completed Successfully!")