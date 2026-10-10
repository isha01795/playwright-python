# Enterprise Python Playwright Automation Framework

A production-ready E2E web and API testing framework built with **Python 3**, **Playwright**, **PyTest**, and **GitHub Actions**.

## Tech Stack & Features
* **Language:** Python 3.11
* **Core Framework:** Playwright Python (`sync_api`) + PyTest
* **Architecture:** Page Object Model (POM)
* **API Testing:** Integrated Playwright HTTP APIRequestContext
* **Parallel Execution:** Executed via `pytest-xdist`
* **CI/CD:** Automated GitHub Actions Workflow with artifact archiving

## Running Locally
```bash
# Clone repository
git clone [https://github.com/YOUR_USERNAME/playwright-python-framework.git](https://github.com/YOUR_USERNAME/playwright-python-framework.git)
cd playwright-python-framework

# Activate virtualenv & install dependencies
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
playwright install

# Execute test suite with parallel execution
pytest -n auto