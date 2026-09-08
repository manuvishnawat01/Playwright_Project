# Beginner Playwright Python Web Automation Testing Project

Welcome to the **Web Automation Testing Project** built with **Playwright for Python**, **Pytest**, **Pytest-BDD**, **Data-Driven Testing (CSV)**, and the **Page Object Model (POM)** pattern.

---

## 📌 Project Overview

This project automates an e-commerce website flow on **Automation Exercise** (`https://automationexercise.com`).

It demonstrates **three distinct testing approaches**, each equipped with **automated screenshot functionality**:

1. **Test Case 1 — BDD Login Test (`test_login_bdd.py`)**: Gherkin Scenario Outline testing multiple user credentials with step-by-step screenshots saved to `screenshots/bdd/`.
2. **Test Case 2 — CSV Data-Driven Login Test (`test_data_driven_login.py`)**: Data-driven testing reading user credentials from `test_data/login_data.csv` via Pytest parameterization with screenshots saved to `screenshots/data_driven/`.
3. **Test Case 3 — Complete End-to-End Test (`test_complete_flow.py`)**: Automates the full 13-step journey (Launch ➔ Login ➔ Product Search ➔ Add to Cart ➔ Verify Cart ➔ Logout) with milestone screenshots saved to `screenshots/complete_flow/`.
4. **Automatic Failure Screenshot**: Captures a screenshot to `screenshots/failures/` automatically whenever any test step fails.

---

## 🛠️ Technology Stack

* **Python 3.x**: Programming language.
* **Playwright for Python**: Modern web automation library.
* **Pytest**: Test framework and runner.
* **Pytest-BDD**: BDD plugin enabling Gherkin feature files.
* **CSV Data-Driven**: Standard `csv` library integration.
* **Page Object Model (POM)**: Design pattern separating locators/actions from test code.

---

## 📁 Project Directory Structure

```text
PlayWrite_Project/
│
├── pages/                   # Page Object Model classes
│   ├── __init__.py
│   ├── login_page.py        # Login page elements & actions
│   ├── home_page.py         # Home & navigation elements & actions
│   ├── product_page.py      # Product details view elements & actions
│   └── cart_page.py         # Cart table verification & logout
│
├── tests/                   # Pytest test execution modules
│   ├── __init__.py
│   ├── test_complete_flow.py      # Test Case 3: Complete 13-step E2E flow + screenshots
│   ├── test_data_driven_login.py # Test Case 2: CSV Data-Driven test + screenshots
│   └── test_login_bdd.py           # Test Case 1: BDD Login runner + screenshots
│
├── features/                # BDD Gherkin feature files
│   └── login.feature        # Scenario Outline for parameterized login testing
│
├── step_definitions/        # Step definitions mapping Gherkin steps to POM
│   ├── __init__.py
│   └── login_steps.py       # @given, @when, @then implementations + BDD screenshots
│
├── test_data/               # External test data files
│   └── login_data.csv       # CSV file storing 3 user credentials
│
├── utils/                   # Helper utilities
│   ├── __init__.py
│   └── csv_reader.py        # CSV parsing utility for Pytest parameterization
│
├── screenshots/             # Output directory for test screenshots
│   ├── bdd/                 # BDD login & logout screenshots
│   ├── data_driven/         # CSV Data-driven login & logout screenshots
│   ├── complete_flow/       # Milestone screenshots (01 to 06)
│   └── failures/            # Automatic failure screenshots
│
├── conftest.py              # Pytest fixture & failure screenshot hook
├── config.py                # Central constants (URL, credentials, product)
├── requirements.txt         # Project dependencies
├── pytest.ini               # Pytest configuration settings
└── README.md                # Complete project documentation
```

---

## ⚖️ BDD vs. Data-Driven Testing Comparison

| Feature | BDD Testing | CSV Data-Driven Testing |
| :--- | :--- | :--- |
| **Main Purpose** | Describe application behavior in human-readable language | Execute the same test across multiple data sets |
| **Test Data Source** | `features/login.feature` (Gherkin `Examples` table) | `test_data/login_data.csv` (CSV file) |
| **Framework Used** | `pytest-bdd` | `pytest` (`@pytest.mark.parametrize`) |
| **Helper Required** | Step Definitions (`step_definitions/login_steps.py`) | CSV Reader (`utils/csv_reader.py`) |
| **Primary Audience** | Business Analysts, QA, Product Owners | Developers, QA Engineers |

---

## 🖼️ Screenshot Architecture

Screenshots are generated automatically for **ALL THREE TEST CASES**:

1. **BDD Screenshots (`screenshots/bdd/`)**:
   * `user1_playwright_login.png`, `user1_playwright_logout.png`
   * `user2_playwright_login.png`, `user2_playwright_logout.png`
   * `user3_playwright_login.png`, `user3_playwright_logout.png`

2. **CSV Data-Driven Screenshots (`screenshots/data_driven/`)**:
   * `user1_playwright_login.png`, `user1_playwright_logout.png`
   * `user2_playwright_login.png`, `user2_playwright_logout.png`
   * `user3_playwright_login.png`, `user3_playwright_logout.png`

3. **Complete Flow Screenshots (`screenshots/complete_flow/`)**:
   * `01_website_launched.png`
   * `02_login_success.png`
   * `03_product_searched.png`
   * `04_product_added_to_cart.png`
   * `05_cart_opened.png`
   * `06_logout.png`

4. **Failure Screenshots (`screenshots/failures/`)**:
   * Automatically captured via Pytest hook in `conftest.py` whenever any test fails.

---

## 🚀 Setup & Execution Commands

### Step 1: Open VS Code Terminal
Open VS Code in `PlayWrite_Project` and press `Ctrl + ~` to open the terminal.

### Step 2: Create & Activate Virtual Environment
```bash
python -m venv venv
```
* **Windows**: `venv\Scripts\activate`
* **macOS/Linux**: `source venv/bin/activate`

### Step 3: Install Dependencies & Playwright Chromium
```bash
pip install -r requirements.txt
playwright install chromium
```

---

### 🧪 Test Execution Commands

#### 1. Run BDD Login Test (Test Case 1)
```bash
pytest tests/test_login_bdd.py -v
```

#### 2. Run CSV Data-Driven Login Test (Test Case 2)
```bash
pytest tests/test_data_driven_login.py -v
```

#### 3. Run Complete End-to-End Test (Test Case 3)
```bash
pytest tests/test_complete_flow.py -v
```

#### 4. Run ALL Tests Together
```bash
pytest -v
```
