"""
===========================================================
Digital Nurture 5.0
Hands-On 4
Selenium WebDriver Setup, Browser Drivers & Basic Commands
===========================================================

Task 24: Selenium Components

1. WebDriver
   - WebDriver is the core component of Selenium.
   - It communicates with the browser using browser drivers
     (e.g., ChromeDriver).
   - It receives commands from the test script and performs
     browser actions.

2. Selenium Grid
   - Selenium Grid is used to execute tests on multiple
     browsers, operating systems, and machines in parallel.
   - It reduces test execution time and supports
     cross-browser testing.

3. Selenium IDE
   - Selenium IDE is a browser extension used for
     record-and-playback testing.
   - It can also generate automation scripts for Selenium.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

# ----------------------------------------------------------
# Task 27 - Configure Chrome (Headless Mode)
# ----------------------------------------------------------

options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# ----------------------------------------------------------
# Task 26 - Implicit Wait
# ----------------------------------------------------------

# Implicit wait applies globally to all element searches.
# It is generally considered a bad practice because it waits
# for every element lookup and can slow execution.
# Explicit waits are preferred because they wait only for
# specific conditions.

driver.implicitly_wait(10)

# ----------------------------------------------------------
# Task 25 - Open Selenium Playground
# ----------------------------------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/")

print("=" * 50)
print("Task 25")
print("Page Title:")
print(driver.title)

# ----------------------------------------------------------
# Task 28 - Navigate to Simple Form Demo
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("Task 28")

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

assert "simple-form-demo" in driver.current_url

print("Successfully navigated to Simple Form Demo")
print("Current URL:")
print(driver.current_url)

driver.back()

print("Returned to Selenium Playground")

# ----------------------------------------------------------
# Task 29 - Open New Tab and Switch
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("Task 29")

driver.execute_script('window.open("https://www.google.com");')

print("Open Window Handles:")
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])

print("Google Tab Title:")
print(driver.title)

# ----------------------------------------------------------
# Task 30 - Switch Back and Take Screenshot
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("Task 30")

driver.switch_to.window(driver.window_handles[0])

driver.save_screenshot("playground_screenshot.png")

if os.path.exists("playground_screenshot.png"):
    print("Screenshot saved successfully.")
else:
    print("Screenshot not found.")

# ----------------------------------------------------------
# Task 31 - Window Size
# ----------------------------------------------------------

print("\n" + "=" * 50)
print("Task 31")

print("Current Window Size:")
print(driver.get_window_size())

driver.set_window_size(1280, 800)

print("Updated Window Size:")
print(driver.get_window_size())

# Keeping a consistent browser window size ensures:
# 1. Responsive UI behaves consistently.
# 2. Elements appear in predictable locations.
# 3. Test results remain consistent across different systems.

# ----------------------------------------------------------
# Close Browser
# ----------------------------------------------------------

driver.quit()

print("\n" + "=" * 50)
print("All Tasks (24–31) Completed Successfully!")
print("=" * 50)