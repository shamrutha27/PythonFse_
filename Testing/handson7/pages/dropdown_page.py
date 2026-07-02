from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):

    # --------------------------------------------------
    # Locators
    # --------------------------------------------------

    DROPDOWN = (By.ID, "select-demo")

    # --------------------------------------------------
    # Constructor
    # --------------------------------------------------

    def __init__(self, driver):
        super().__init__(driver)

    # --------------------------------------------------
    # Open Dropdown Demo Page
    # --------------------------------------------------

    def open(self, base_url):
        """
        Opens the Select Dropdown List page.
        """
        self.navigate_to(base_url + "select-dropdown-demo")

    # --------------------------------------------------
    # Select Day
    # --------------------------------------------------

    def select_day(self, day_name):
        """
        Selects a day from the dropdown.

        Example:
        page.select_day("Wednesday")
        """
        dropdown_element = self.wait_for_element(self.DROPDOWN)

        select = Select(dropdown_element)
        select.select_by_visible_text(day_name)

    # --------------------------------------------------
    # Get Selected Day
    # --------------------------------------------------

    def get_selected_day(self):
        """
        Returns the currently selected option.
        """
        dropdown_element = self.wait_for_element(self.DROPDOWN)

        select = Select(dropdown_element)

        return select.first_selected_option.text