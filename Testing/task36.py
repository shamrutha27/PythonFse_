from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ----------------------------------------------------------
# Launch Chrome
# ----------------------------------------------------------

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# ----------------------------------------------------------
# Open Selenium Playground
# ----------------------------------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/")

# ----------------------------------------------------------
# Open Bootstrap Alerts Page
# ----------------------------------------------------------

bootstrap_link = wait.until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Bootstrap Alerts")
    )
)

bootstrap_link.click()

print("Bootstrap Alerts page opened successfully.")

# ----------------------------------------------------------
# Click the Success Message button
# ----------------------------------------------------------

success_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//button[contains(.,'Success Message')]"
        )
    )
)

success_button.click()

print("Success Message button clicked.")

# ----------------------------------------------------------
# Wait for Success Alert
# ----------------------------------------------------------

success_alert = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            "//div[contains(@class,'alert-success')]"
        )
    )
)

alert_text = success_alert.text

print("\nAlert Text:")
print(alert_text)

assert "autocloseable" in alert_text.lower()

print("\nAssertion Passed!")
print("Autocloseable Success Alert displayed.")


# ----------------------------------------------------------
# Close Browser
# ----------------------------------------------------------

driver.quit()

print("\nTask 36 Completed Successfully!")