Here's your complete `README.md` for the Crypto.com QA challenge project:

---

```markdown
# QA Automation Challenge - Crypto.com (MyObservatory App)

This repository contains the solution to Crypto.com's QA Challenge for automating the verification of the weather forecast in the **MyObservatory** mobile app by the Hong Kong Observatory.

## 📱 Overview

We use **Python + Appium + Pytest** to verify that the **9-day forecast** screen in the MyObservatory app:
- Successfully launches on an emulator
- Navigates to the 9-day forecast screen
- Verifies the forecast data of the **first day** matches the expected date and weekday

---

## 🧰 Tech Stack

- Python 3.13
- Appium (v2)
- Appium Inspector (for element locators)
- Poetry (dependency management)
- Android Emulator (`Pixel_4_XL`)
- Emulator APK: `MyObservatory_v1_0.apk`

---

## ⚙️ Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kalunpoon926/QA_Challenges_Question_2.git
cd QA_Challenges_Question_2
```

### 2. Install Poetry (if not installed)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Set Up Python Virtual Environment

```bash
poetry install
poetry shell
```

### 4. Install Android & Appium Dependencies

Ensure the following are installed:

- **Android Studio** with SDK + AVD manager
- `Pixel_4_XL` AVD (created in AVD Manager)
- **Appium v2**:
  ```bash
  npm install -g appium
  ```

- **Appium Inspector**:  
  👉 Download from [https://github.com/appium/appium-inspector/releases](https://github.com/appium/appium-inspector/releases)

- **Java (required to verify APK signatures)**:
  ```bash
  brew install openjdk
  ```

  Add this to `~/.zshrc`:

  ```bash
  export JAVA_HOME=$(/usr/libexec/java_home)
  export PATH=$JAVA_HOME/bin:$PATH
  export ANDROID_HOME=$HOME/Library/Android/sdk
  export ANDROID_SDK_ROOT=$ANDROID_HOME
  export PATH=$ANDROID_HOME/emulator:$ANDROID_HOME/platform-tools:$PATH
  ```

  Then:

  ```bash
  source ~/.zshrc
  ```

---

## 🚀 How to Run the Test

### 1. Place the APK file

Put the APK `MyObservatory_v1_0.apk` into:

```
project_root/build/MyObservatory_v1_0.apk
```

### 2. Run the Test via Pytest

```bash
pytest test_weather_forecast.py --html=report.html
```

This will:
- Auto-start emulator (`Pixel_4_XL`)
- Auto-start Appium server
- Install APK
- Run the automation test for the 9-day forecast screen
- Auto-shutdown the environment after test
- Generate a test report in `report.html`
---

## 📸 UI Inspection

Use **Appium Inspector** to inspect and locate elements:
- Platform: Android
- Device Name: ``Pixel_4_XL``
- appPackage: `hko.MyObservatory_v1_0`
- appActivity: `.AgreementPage`

---

## 🧪 Sample Test Case Validated

- AGREE to terms and permissions
- Navigate to `9-Day Forecast`
- Validate that:
  - Forecast Date matches tomorrow
  - Weekday matches tomorrow
  - Weather, Temp, Rain, Wind and Detail elements are displayed

---

## 📁 Project Structure

```
📦QA_Challenges_Question_2
 ┣ 📂build
 ┃ ┗ 📄MyObservatory_v1_0.apk
 ┣ 📂core
 ┃ ┗ 📄__init__.py
 ┃ ┗ 📄AppiumEnvironment.py
 ┃ ┗ 📄logger_config.py
 ┣ 📂locators
 ┃ ┗ 📄forecast_screen.py
 ┣ 📂page
 ┃ ┗ 📄basepage.py
 ┣ 📂tests
 ┃ ┗ 📄test_weather_forecast.py
 ┣ 📂utils
 ┃ ┣ 📄date_utils.py
 ┣ 📄conftest.py
 ┣ 📄poetry.lock
 ┣ 📄pyproject.toml
 ┗ 📄README.md
```

---

## 🏁 Last Updated
2025-04-24