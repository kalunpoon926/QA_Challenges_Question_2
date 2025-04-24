# AppiumEnvironment.py

import subprocess
import os
import time
import signal

import conftest


class AppiumEnvironment:
    """
    A class to manage the Appium testing environment, including starting and stopping
    the Android emulator and Appium server.
    """
    def __init__(self):
        """
        Initialize the AppiumEnvironment instance.

        Attributes:
            emulator_process: subprocess.Popen
                - Process object for the Android emulator.
            appium_process: subprocess.Popen
                - Process object for the Appium server.
        """
        self.emulator_process = None
        self.appium_process = None

    def start_emulator(self):
        """
        Start the Android emulator.

        - Launches the emulator using the AVD name specified in `conftest`.
        - Waits for the emulator to boot up.
        """
        print(f"📱 Starting emulator: {conftest.AVD_NAME}")
        self.emulator_process = subprocess.Popen(
            [conftest.EMULATOR_PATH, "-avd", conftest.AVD_NAME],
            stdout=subprocess.DEVNULL,  # Suppress standard output
            stderr=subprocess.DEVNULL   # Suppress error output
        )
        print("⌛ Waiting for emulator to boot...")
        time.sleep(5)


    def start_appium(self):
        """
        Start the Appium server.

        - Launches the Appium server on the specified port.
        - Waits for the server to start.
        """
        print("🚀 Starting Appium server...")
        self.appium_process = subprocess.Popen(
            ["appium", "--port", str(conftest.PORT)],
            stdout=subprocess.DEVNULL,  # Suppress standard output
            stderr=subprocess.DEVNULL,  # Suppress error output
            preexec_fn=os.setsid        # Start the process in a new session
        )
        time.sleep(5) # Wait for the server to initialize
        print("✅ Appium server is running.")

    def start(self):
        """
        Start the testing environment.

        - Starts both the Android emulator and the Appium server.
        """
        self.start_emulator()
        self.start_appium()

    def stop(self):
        """
        Stop the testing environment.

        - Terminates the Appium server and shuts down the Android emulator.
        """
        print("🧹 Tearing down environment...")

        # Stop the Appium server if it is running
        if self.appium_process:
            try:
                if self.appium_process.poll() is None:  # Check if the process is still running
                    os.killpg(os.getpgid(self.appium_process.pid), signal.SIGTERM) # Terminate the process group
                    print("✅ Appium server stopped.")
                else:
                    print("⚠️ Appium server process already stopped.")
            except ProcessLookupError:
                print("⚠️ Appium server process not found (already terminated).")

        # Shut down the Android emulator
        if self.emulator_process:
            try:
                subprocess.call(["adb", "emu", "kill"]) # Send a command to terminate the emulator
                print("✅ Emulator shut down.")
            except FileNotFoundError:
                print("⚠️ adb not found. Emulator might not shut down cleanly.")
