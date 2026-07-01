from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ----------------------------------------------------------
# Launch Chrome
# ----------------------------------------------------------

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/")

# ----------------------------------------------------------
# Open Simple Form Demo
# ----------------------------------------------------------

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

time.sleep(2)

print("=" * 60)
print("TASK 32 - LOCATOR STRATEGIES")
print("=" * 60)

# ----------------------------------------------------------
# 1. By.ID
# ----------------------------------------------------------

element_id = driver.find_element(By.ID, "user-message")
print("By.ID ->", element_id.get_attribute("placeholder"))

# ----------------------------------------------------------
# 2. By.NAME
# ----------------------------------------------------------

element_name = driver.find_element(By.NAME, "message")
print("By.NAME ->", element_name.get_attribute("placeholder"))

# ----------------------------------------------------------
# 3. By.CLASS_NAME
# ----------------------------------------------------------

# The input has class "form-control"
element_class = driver.find_element(By.CLASS_NAME, "form-control")
print("By.CLASS_NAME ->", element_class.get_attribute("placeholder"))

# ----------------------------------------------------------
# 4. By.TAG_NAME
# ----------------------------------------------------------

# Finds the first input tag on the page
element_tag = driver.find_element(By.TAG_NAME, "input")
print("By.TAG_NAME ->", element_tag.get_attribute("placeholder"))

# ----------------------------------------------------------
# 5. XPath (Absolute)
# ----------------------------------------------------------
# NOTE:
# Absolute XPath may change if the page structure changes.
# Inspect the page (F12) if this XPath doesn't work.

try:
    element_absolute = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/section[2]/div/div/div[1]/div/div/input"
    )
    print("Absolute XPath ->", element_absolute.get_attribute("placeholder"))
except:
    print("Absolute XPath not found (structure may have changed).")

# ----------------------------------------------------------
# 6. XPath (Relative)
# ----------------------------------------------------------

element_relative = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)

print("Relative XPath ->", element_relative.get_attribute("placeholder"))

# ----------------------------------------------------------
# Enter text to verify all locators work
# ----------------------------------------------------------

element_relative.clear()
element_relative.send_keys("Hello Selenium!")

print("\nText entered successfully using Relative XPath.")

# ----------------------------------------------------------
# TASK 33
# CSS Selectors
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("TASK 33 - CSS SELECTORS")
print("=" * 60)

# ----------------------------------------------------------
# CSS by ID
# ----------------------------------------------------------

css_id = driver.find_element(
    By.CSS_SELECTOR,
    "#user-message"
)

print("CSS by ID ->", css_id.get_attribute("placeholder"))

# ----------------------------------------------------------
# CSS by Attribute
# ----------------------------------------------------------

css_attribute = driver.find_element(
    By.CSS_SELECTOR,
    "input[placeholder='Please enter your Message']"
)

print("CSS by Attribute ->", css_attribute.get_attribute("placeholder"))

# ----------------------------------------------------------
# CSS Parent > Child
# ----------------------------------------------------------

try:
    css_parent = driver.find_element(
        By.CSS_SELECTOR,
        "div#user-message-wrapper > input"
    )

    print("CSS Parent > Child ->", css_parent.get_attribute("placeholder"))

except:
    print("Parent > Child selector may differ depending on page updates.")

# ----------------------------------------------------------
# TASK 34
# Checkbox Demo
# ----------------------------------------------------------

driver.back()

driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()

time.sleep(2)

print("\n" + "=" * 60)
print("TASK 34 - XPATH text() and contains()")
print("=" * 60)

# ----------------------------------------------------------
# XPath using text()
# ----------------------------------------------------------

try:
    option1 = driver.find_element(
        By.XPATH,
        "//label[text()='Option 1']"
    )

    print("XPath text() ->", option1.text)

except:
    print("Option 1 label not found.")

# ----------------------------------------------------------
# XPath using contains()
# ----------------------------------------------------------

option_labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("\nLabels found using contains():")

for label in option_labels:
    print(label.text)

# ----------------------------------------------------------
# TASK 35
# Locator Ranking
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("TASK 35 - LOCATOR RANKING")
print("=" * 60)

print("""
1. ID
   - Best locator.
   - Unique, readable, and fastest.

2. CSS Selector
   - Fast and flexible.
   - Preferred over XPath whenever possible.

3. Name
   - Good if unique.

4. Relative XPath
   - Useful when ID or CSS cannot be used.

5. Class Name
   - Can identify multiple elements.
   - Less reliable.

6. Tag Name
   - Usually returns many elements.
   - Least specific.

7. Absolute XPath
   - Worst locator.
   - Breaks whenever HTML structure changes.
""")

# ----------------------------------------------------------
# Close Browser
# ----------------------------------------------------------

driver.quit()

print("\nCompleted Tasks 32–35 Successfully.")