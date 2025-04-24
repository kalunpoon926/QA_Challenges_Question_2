from appium.webdriver.common.appiumby import AppiumBy

"""Locators for elements on the Forecast screen."""
# Buttons
AGREE_BUTTON = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/btn_agree')
ACCEPT_PERMISSIONS_BUTTON = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
OK_BUTTON = (AppiumBy.ID, 'android:id/button1')
BACK_BUTTON = (AppiumBy.XPATH, '//*[@content-desc="Back"]')
EXIT_BUTTON = (AppiumBy.ID, 'hko.MyObservatory_v1_0:id/exit_btn')
NINE_DAY_FORECAST_BUTTON = (AppiumBy.XPATH, '(//*[@text="9-Day Forecast"])[2]')
BURGER_MENU_BUTTON = (AppiumBy.XPATH, '//*[@resource-id="hko.MyObservatory_v1_0:id/toolbar"]//android.widget.ImageButton')

# Menu Items
FORECAST_WARNING_SERVICES_MENU_ITEM = (AppiumBy.XPATH, '//*[@text="Forecast & Warning Services"]')

# Forecast details
FIRST_DAY_FORECAST_TEXT = (AppiumBy.XPATH, '(//*[@resource-id="hko.MyObservatory_v1_0:id/sevenday_forecast_date"])[1]')
FIRST_WEEKDAY_FORECAST_TEXT = (AppiumBy.XPATH, '(//*[@resource-id="hko.MyObservatory_v1_0:id/sevenday_forecast_day_of_week"])[1]')
FIRST_WEATHER_ICON = (AppiumBy.XPATH, '(//*[@resource-id="hko.MyObservatory_v1_0:id/sevenday_forecast_Icon"])[1]')
FIRST_WEATHER_TEMPERATURE = (AppiumBy.XPATH, '(//*[@resource-id="hko.MyObservatory_v1_0:id/sevenday_forecast_temp"])[1]')
FIRST_WEATHER_RELATIVE_HUMIDITY = (AppiumBy.XPATH, '(//*[@resource-id="hko.MyObservatory_v1_0:id/sevenday_forecast_rh"])[1]')
FIRST_WEATHER_PROBABILITY_OF_SIGNIFICANT_RAIN_ICON = (AppiumBy.XPATH, '(//*[@resource-id="hko.MyObservatory_v1_0:id/psrIcon"])[1]')
FIRST_WEATHER_PROBABILITY_OF_SIGNIFICANT_RAIN_TEXT = (AppiumBy.XPATH, '(//*[@resource-id="hko.MyObservatory_v1_0:id/psrText"])[1]')
FIRST_WEATHER_SEVENDAY_FORECAST_WIND_TEXT = (AppiumBy.XPATH, '(//*[@resource-id="hko.MyObservatory_v1_0:id/sevenday_forecast_wind"])[1]')
FIRST_WEATHER_SEVENDAY_FORECAST_DETAILS_TEXT = (AppiumBy.XPATH, '(//*[@resource-id="hko.MyObservatory_v1_0:id/sevenday_forecast_details"])[1]')

