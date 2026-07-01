import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# ---------------------------------------------------------
# Method 1 : Using time.sleep()
# ---------------------------------------------------------

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT, "Bootstrap Alerts").click()

driver.find_element(
    By.XPATH,
    "//button[contains(text(),'Success Message')]"
).click()

start = time.time()

# Hard-coded wait
time.sleep(3)

alert = driver.find_element(By.XPATH, "//div[contains(@class,'alert-success')]")

print("\nAlert Text using time.sleep():")
print(alert.text)

end = time.time()

sleep_time = end - start

driver.quit()

print(f"\nExecution Time using time.sleep(): {sleep_time:.2f} seconds")


# ---------------------------------------------------------
# Method 2 : Using Explicit Wait
# ---------------------------------------------------------

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://www.lambdatest.com/selenium-playground/")

wait.until(
    EC.element_to_be_clickable(
        (By.LINK_TEXT, "Bootstrap Alerts")
    )
).click()

wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Success Message')]")
    )
).click()

start = time.time()

alert = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class,'alert-success')]")
    )
)

print("\nAlert Text using Explicit Wait:")
print(alert.text)

end = time.time()

explicit_time = end - start

driver.quit()

print(f"\nExecution Time using Explicit Wait: {explicit_time:.2f} seconds")


# ---------------------------------------------------------
# Comparison
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("Comparison")
print("=" * 60)

print(f"time.sleep()      : {sleep_time:.2f} seconds")
print(f"Explicit Wait     : {explicit_time:.2f} seconds")

print("\nConclusion:")

if explicit_time < sleep_time:
    print("Explicit Wait is faster because it waits only until the element appears.")
else:
    print("Execution times are similar on this machine, but Explicit Wait is more reliable.")

print("""
Why is Explicit Wait better?

1. It waits only as long as necessary.
2. It makes tests faster on fast systems.
3. It is more reliable on slow systems.
4. It avoids unnecessary delays caused by time.sleep().
""")