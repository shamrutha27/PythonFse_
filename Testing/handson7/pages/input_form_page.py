from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InputFormPage(BasePage):

    # --------------------------------------------------
    # Locators
    # --------------------------------------------------

    NAME = (By.ID, "name")

    EMAIL = (By.ID, "inputEmail4")

    PASSWORD = (By.NAME, "password")

    COMPANY = (By.NAME, "company")

    WEBSITE = (By.NAME, "website")

    COUNTRY = (By.NAME, "country")

    CITY = (By.NAME, "city")

    ADDRESS1 = (By.ID, "inputAddress1")

    ADDRESS2 = (By.ID, "inputAddress2")

    STATE = (By.ID, "inputState")

    ZIP = (By.ID, "inputZip")

    SUBMIT = (
    By.CSS_SELECTOR,
    "button[type='submit']"
)

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".success-msg, .success-msg.hidden, p.success-msg"
    )

    # --------------------------------------------------
    # Constructor
    # --------------------------------------------------

    def __init__(self, driver):
        super().__init__(driver)

    # --------------------------------------------------
    # Open Page
    # --------------------------------------------------

    def open(self, base_url):
        """
        Opens the Input Form Submit page.
        """
        self.navigate_to(base_url + "input-form-demo")

    # --------------------------------------------------
    # Fill Form
    # --------------------------------------------------

    def fill_form(
        self,
        name,
        email,
        phone,
        address
    ):
        """
        Fills the mandatory fields of the form.
        """

        self.enter_text(self.NAME, name)

        self.enter_text(self.EMAIL, email)

        # Password field is mandatory
        self.enter_text(self.PASSWORD, "Password@123")

        # Company
        self.enter_text(self.COMPANY, "Cognizant")

        # Website
        self.enter_text(self.WEBSITE, "https://www.cognizant.com")

        # Country
        self.wait_for_element(self.COUNTRY).send_keys("United States")

        # City
        self.enter_text(self.CITY, "Chennai")

        # Address
        self.enter_text(self.ADDRESS1, address)

        # Address Line 2
        self.enter_text(self.ADDRESS2, "Near Bus Stand")

        # State
        self.enter_text(self.STATE, "Tamil Nadu")

        # ZIP Code
        self.enter_text(self.ZIP, phone)

    # --------------------------------------------------
    # Submit Form
    # --------------------------------------------------

    def submit_form(self):
        """
        Clicks the Submit button.
        """
        self.click(self.SUBMIT)

    # --------------------------------------------------
    # Get Success Message
    # --------------------------------------------------

    def get_success_message(self):
        """
        Returns the success message displayed after
        successful submission.
        """
        return self.get_text(self.SUCCESS_MESSAGE)