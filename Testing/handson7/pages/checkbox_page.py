from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxPage(BasePage):

    # --------------------------------------------------
    # Locator for all checkboxes
    # --------------------------------------------------

    CHECKBOXES = (By.XPATH, "//input[@type='checkbox']")

    # --------------------------------------------------
    # Constructor
    # --------------------------------------------------

    def __init__(self, driver):
        super().__init__(driver)

    # --------------------------------------------------
    # Open Checkbox Demo Page
    # --------------------------------------------------

    def open(self, base_url):
        """
        Opens the Checkbox Demo page.
        """
        self.navigate_to(base_url + "checkbox-demo")

    # --------------------------------------------------
    # Get Checkbox by Index
    # --------------------------------------------------

    def get_checkbox(self, index):
        """
        Returns the checkbox element at the given index.

        Example:
        index = 1 -> First checkbox
        index = 2 -> Second checkbox
        """
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        return checkboxes[index - 1]

    # --------------------------------------------------
    # Check Checkbox
    # --------------------------------------------------

    def check_option(self, index):
        """
        Selects the checkbox if it is not already selected.
        """
        checkbox = self.get_checkbox(index)

        if not checkbox.is_selected():
            checkbox.click()

    # --------------------------------------------------
    # Uncheck Checkbox
    # --------------------------------------------------

    def uncheck_option(self, index):
        """
        Deselects the checkbox if it is selected.
        """
        checkbox = self.get_checkbox(index)

        if checkbox.is_selected():
            checkbox.click()

    # --------------------------------------------------
    # Verify Checkbox State
    # --------------------------------------------------

    def is_option_checked(self, index):
        """
        Returns True if the checkbox is selected,
        otherwise returns False.
        """
        checkbox = self.get_checkbox(index)
        return checkbox.is_selected()