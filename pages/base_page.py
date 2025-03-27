import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)

    @allure.step("Find element with locator: {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Find elements with locator: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Click element with locator: {locator}")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Input text: '{text}' into element with locator: {locator}")
    def input_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(text)

    @allure.step("Get value from element with locator: {locator}")
    def get_element_value(self, locator):
        return self.find_element(locator).get_attribute("value")

    @allure.step("Wait for alert, get text and accept")
    def wait_for_alert_and_accept(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text
        
    @allure.step("Take screenshot")
    def take_screenshot(self, name="screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
