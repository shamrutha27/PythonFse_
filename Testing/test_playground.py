import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# --------------------------------------------------
# Task 42 & 45
# --------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, base_url, message):

    driver.get(base_url)

    driver.find_element(
        By.LINK_TEXT,
        "Simple Form Demo"
    ).click()

    wait = WebDriverWait(driver, 10)

    textbox = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-message")
        )
    )

    textbox.clear()
    textbox.send_keys(message)

    driver.find_element(
        By.ID,
        "showInput"
    ).click()

    output = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )

    assert output.text == message


# --------------------------------------------------
# Task 43
# --------------------------------------------------

def test_checkbox_demo(driver, base_url):

    driver.get(base_url)

    driver.find_element(
        By.LINK_TEXT,
        "Checkbox Demo"
    ).click()

    wait = WebDriverWait(driver, 10)

    checkbox = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "(//input[@type='checkbox'])[1]"
            )
        )
    )

    checkbox.click()

    assert checkbox.is_selected()

    checkbox.click()

    assert not checkbox.is_selected()


# --------------------------------------------------
# Task 49
# --------------------------------------------------

def test_dropdown_selection(driver, base_url):

    driver.get(base_url)

    driver.find_element(
        By.LINK_TEXT,
        "Select Dropdown List"
    ).click()

    wait = WebDriverWait(driver, 10)

    dropdown = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "select-demo")
        )
    )

    select = Select(dropdown)

    select.select_by_visible_text("Wednesday")

    selected = select.first_selected_option.text

    assert selected == "Wednesday"