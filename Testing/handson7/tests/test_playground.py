import sys
import os

import pytest



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage


# ---------------------------------------------------------
# Task 55
# Simple Form Demo
# ---------------------------------------------------------

def test_simple_form_submission(driver, base_url):

    page = SimpleFormPage(driver)

    page.open(base_url)

    page.enter_message("Hello Selenium")

    page.click_submit()

    assert page.get_displayed_message() == "Hello Selenium"


# ---------------------------------------------------------
# Task 56
# Checkbox Demo
# ---------------------------------------------------------

def test_checkbox_demo(driver, base_url):

    page = CheckboxPage(driver)

    page.open(base_url)

    page.check_option(1)

    assert page.is_option_checked(1)

    page.uncheck_option(1)

    assert not page.is_option_checked(1)


# ---------------------------------------------------------
# Task 56
# Dropdown Demo
# ---------------------------------------------------------

def test_dropdown_selection(driver, base_url):

    page = DropdownPage(driver)

    page.open(base_url)

    page.select_day("Wednesday")

    assert page.get_selected_day() == "Wednesday"


# ---------------------------------------------------------
# Task 57
# Input Form Demo
# ---------------------------------------------------------

def test_input_form_submit(driver, base_url):

    page = InputFormPage(driver)

    page.open(base_url)

    page.fill_form(
        name="Shams",
        email="shams@test.com",
        phone="600001",
        address="Anna Nagar"
    )

    page.submit_form()

    message = page.get_success_message()

    assert (
        "Thanks" in message
        or
        "successfully" in message
    )


# ---------------------------------------------------------
# Optional Parameterized Test
# ---------------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium",
        "Automation Testing"
    ]
)
def test_multiple_messages(driver, base_url, message):

    page = SimpleFormPage(driver)

    page.open(base_url)

    page.enter_message(message)

    page.click_submit()

    assert page.get_displayed_message() == message
