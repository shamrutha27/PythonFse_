from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SimpleFormPage(BasePage):

    # --------------------------------------------------
    # Locators (Task 51)
    # --------------------------------------------------

    MESSAGE_INPUT = (By.ID, "user-message")

    SUBMIT_BUTTON = (By.ID, "showInput")

    DISPLAY_MESSAGE = (
    By.CSS_SELECTOR,
    "#message"
)

    # --------------------------------------------------
    # Constructor
    # --------------------------------------------------

    def __init__(self, driver):
        super().__init__(driver)

    # --------------------------------------------------
    # Enter Message
    # --------------------------------------------------

    def enter_message(self, text):
        """
        Enters text into the message input field.
        """
        self.enter_text(self.MESSAGE_INPUT, text)

    # --------------------------------------------------
    # Click Submit Button
    # --------------------------------------------------

    def click_submit(self):
        button = self.wait_until_clickable(self.SUBMIT_BUTTON)

        self.driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        button
    )

        button.click()

    # --------------------------------------------------
    # Get Displayed Message
    # --------------------------------------------------

    def get_displayed_message(self):
        """
        Returns the displayed message after submission.
        """
        return self.get_text(self.DISPLAY_MESSAGE)

    # --------------------------------------------------
    # Optional Helper Method
    # --------------------------------------------------

    def open(self, base_url):
        """
        Opens the Simple Form Demo page directly.
        """
        self.navigate_to(base_url + "simple-form-demo")