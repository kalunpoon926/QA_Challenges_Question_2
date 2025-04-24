from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator: tuple):
        """
        Click on an element specified by the locator.

       :param locator: tuple
           - A tuple containing the locator type and value (e.g., (AppiumBy.ID, "element_id")).
       :raises Exception:
           - Raises an exception if the element is not clickable within the timeout period.
       """
        by_type, value = locator
        by = getattr(AppiumBy, by_type.upper())
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            print(f"✅ Clicked: {locator}")

        except TimeoutException:
            raise Exception(f"❌ Timeout: Element not clickable -> {locator}")

    def wait_for_visible(self, locator: tuple):
        """
        Wait for an element to become visible.

        :param locator: tuple
            - A tuple containing the locator type and value (e.g., (AppiumBy.ID, "element_id")).
        :return: WebElement
            - Returns the WebElement if it becomes visible within the timeout period.
        :raises Exception:
            - Raises an exception if the element is not visible within the timeout period.
        """
        by_type, value = locator
        by = getattr(AppiumBy, by_type.upper())
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            raise Exception(f"❌ Timeout: Element not visible -> {locator}")

    def get_text(self, locator):
        """
        Retrieve the text content of an element.

        :param locator: tuple
            - A tuple containing the locator type and value (e.g., (AppiumBy.ID, "element_id")).
        :return: str
            - Returns the text content of the element.
        :raises Exception:
            - Raises an exception if the element is not visible within the timeout period.
        """
        by, value = locator
        print(f"🔍 Getting text from element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        return element.text

    def is_displayed(self, locator, timeout=10):
        """
        Check if an element is displayed within the given timeout.

        :param locator: Tuple(By, value)
        :param timeout: Timeout in seconds
        :return: True if element is visible, False otherwise
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located((getattr(By, locator[0].upper()), locator[1])))
            return element.is_displayed()
        except TimeoutException:
            return False