import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pathlib import Path
from appium.options.common.full_reset_option import FULL_RESET

from AppiumEnvironment import AppiumEnvironment


# configuration for Appium and Android emulator
AVD_NAME = "Pixel_4_XL"
PORT = 4723
PLATFORM = "Android"
APK_PATH = str(Path(__file__).parent / "build/MyObservatory_v1_0.apk")
APP_PACKAGE = "hko.MyObservatory_v1_0"
APP_ACTIVITY = ".AgreementPage"
FULL_RESET = True
REMOTE_SERVER = "http://localhost:4723"
EMULATOR_PATH = "/Users/kalunsimonpoon/Library/Android/sdk/emulator/emulator"

@pytest.fixture(scope="session")
def appium_env():
    """
    Fixture to manage the Appium environment.

    - Starts the Appium environment before the test session.
    - Stops the Appium environment after the test session.
    """
    env = AppiumEnvironment() # Initialize the AppiumEnvironment instance
    env.start() # Start the Appium environment
    yield # Yield control to the test session
    env.stop() # Stop the Appium environment after the session

@pytest.fixture(scope="session")
def driver(appium_env):
    """
    Fixture to initialize and provide the Appium WebDriver.

    - Configures the Appium WebDriver with desired capabilities.
    - Provides the WebDriver instance to the test session.
    - Quits the WebDriver after the test session.

    :param appium_env: The Appium environment fixture.
    :return: The initialized WebDriver instance.
    """
    # Set up desired capabilities for the Appium WebDriver
    options = UiAutomator2Options()
    options.platform_name = PLATFORM
    options.device_name = AVD_NAME
    options.app = APK_PATH
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.full_reset = FULL_RESET

    # Initialize the Appium WebDriver
    driver = webdriver.Remote(REMOTE_SERVER, options=options)
    driver.implicitly_wait(10) # Set an implicit wait timeout for locating elements
    yield driver # Provide the WebDriver instance to the test session
    driver.quit() # Quit the WebDriver after the session
