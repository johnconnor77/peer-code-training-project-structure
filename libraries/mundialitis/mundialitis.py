from libraries.common import act_on_element, capture_page_screenshot
from config import OUTPUT_FOLDER


class Mundialitis():

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance
        self.mundialitis_url = credentials["url"]
        self.mundialitis_login = credentials["login"]
        self.mundialitis_password = credentials["password"]

    def login(self):
        """
        Login to Mundialitis with Bitwarden credentials.
        """
        try:
            self.browser.go_to(self.mundialitis_url)
            self.input_credentials()
            self.submit_form()
        except Exception as e:
            capture_page_screenshot(OUTPUT_FOLDER, "Exception_Mundialitis_Login")
            raise Exception("Login to Mundialitis failed")


    def input_credentials(self):
        """
        Function that writes the credentials in the login form.
        """
        self.browser.click_element('//a[text()="LOGIN"]')
        self.browser.input_text_when_element_is_visible('//input[@id="logusername"]', self.mundialitis_login)
        self.browser.input_text_when_element_is_visible('//input[@id="logpassword"]', self.mundialitis_password)
        return

    def submit_form(self):
        """
        Function that submits the login form and waits for the main page to load.
        """
        self.browser.click_element('//button[@name="login"]')
        act_on_element('//div[@id="main"]', "find_element")
        return
