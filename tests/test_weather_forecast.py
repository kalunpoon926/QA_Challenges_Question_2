import pytest
from page.basepage import BasePage
from conftest import driver
import locators.forecast_screen as locators
import utils.date_utils as date_utils
from core.logger_config import setup_logger
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logger = setup_logger(__name__)


# Test to verify the first day's forecast date and weekday in the 9-day weather forecast
def test_first_day_forecast_date(driver):
    try:
        # Initialize the BasePage function
        page = BasePage(driver)

        # Navigate through the app to reach the 9-day forecast screen
        logger.info("📱 Navigating to 9-day forecast...")
        page.click(locators.AGREE_BUTTON) # Agree to Disclaimer
        logger.info("📱 Successfully clicked on the AGREE button for Disclaimer.")
        page.click(locators.AGREE_BUTTON) # Agree to Privacy Policy Statements
        logger.info("📱 Successfully clicked on the AGREE button for Privacy Policy Statements.")
        page.click(locators.OK_BUTTON) # Click OK on the Background Access to Location Information pop-up
        logger.info("📱 Successfully clicked OK on the Background Access to Location Information pop-up")
        page.click(locators.ACCEPT_PERMISSIONS_BUTTON) # Accept permissions for location access
        logger.info("📱 Successfully clicked Accept permissions for location access")
        page.click(locators.BACK_BUTTON) # Go back to My Observatory from settings
        logger.info("📱 Successfully clicked back to My Observatory from settings")
        page.click(locators.EXIT_BUTTON) # Click next button on the first page of the overlay
        logger.info("📱 Successfully Click next button on the first page of the overlay")
        page.click(locators.EXIT_BUTTON) # Click the close button on second page of the overlay
        logger.info("📱 Successfully Click close button on second page of the overlay")
        page.click(locators.BURGER_MENU_BUTTON) # Open the burger menu
        logger.info("📱 Successfully Open the burger menu")
        page.click(locators.FORECAST_WARNING_SERVICES_MENU_ITEM) # Select forecast services
        logger.info("📱 Successfully Select forecast services")
        page.click(locators.NINE_DAY_FORECAST_BUTTON) # Navigate to the 9-day forecast
        logger.info("📱 Successfully Navigate to the 9-day forecast")
        # Define the elements to check on the forecast screen
        elements_to_check = {
            "Date": locators.FIRST_DAY_FORECAST_TEXT,
            "Weekday": locators.FIRST_WEEKDAY_FORECAST_TEXT,
            "Weather Icon": locators.FIRST_WEATHER_ICON,
            "Temperature": locators.FIRST_WEATHER_TEMPERATURE,
            "Humidity": locators.FIRST_WEATHER_RELATIVE_HUMIDITY,
            "Rain Icon": locators.FIRST_WEATHER_PROBABILITY_OF_SIGNIFICANT_RAIN_ICON,
            "Rain Text": locators.FIRST_WEATHER_PROBABILITY_OF_SIGNIFICANT_RAIN_TEXT,
            "Wind Text": locators.FIRST_WEATHER_SEVENDAY_FORECAST_WIND_TEXT,
            "Details Text": locators.FIRST_WEATHER_SEVENDAY_FORECAST_DETAILS_TEXT,
        }

        # Verify that all required elements are displayed on first day of the forecast
        for name, locator in elements_to_check.items():
            assert page.is_displayed(locator), f"❌ {name} is not displayed"
            logger.info(f"✅ {name} is displayed")
        logger.info("📱 All required elements are displayed on the first day of the forecast.")

        # Extract the forecast date Text and compare it with the date that generate by get_tomorrow_day_month function
        first_date_and_month = page.get_text(locators.FIRST_DAY_FORECAST_TEXT)
        target_date = date_utils.get_tomorrow_day_month()
        assert first_date_and_month in target_date, f"Expected {target_date} in forecast, but got {first_date_and_month}"
        logger.info("📱 Forecast date verified successfully.")
        # Extract the weekday Text and compare it with the date that generate by get_tomorrow_weekday function
        target_weekday = date_utils.get_tomorrow_weekday()
        first_weekday = page.get_text(locators.FIRST_WEEKDAY_FORECAST_TEXT)
        assert first_weekday in target_weekday, f"Expected {target_weekday} in forecast, but got {first_weekday}"
        logger.info("📱 Forecast weekday verified successfully.")

    except Exception as e:
        # If any exception occurs, fail the test with the error message
        pytest.fail(f"❌ Test failed due to: {e}")