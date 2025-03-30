# Web UI Automation Testing Framework
## Overview
This project is a UI automation testing framework for web applications using Python, Selenium WebDriver, and pytest. It supports running tests in both Chrome and Firefox browsers, locally or in a Selenium Grid environment via Docker containers. Test results are reported using Allure for comprehensive visualization and analysis.
## Features
- Cross-browser testing (Chrome and Firefox)
- Flexible execution modes (local or remote via Selenium Grid)
- Parallel test execution
- Detailed test reporting with Allure
- Docker-based setup for consistent test environments
- Page Object Model design pattern implementation
- Automatic screenshots on test failures
- Data-driven testing capabilities

## Prerequisites
- Python 3.8 or higher
- Docker and Docker Compose
- Git

## Project Structure
```
├── conftest.py                      # pytest configuration and fixtures
├── docker-compose.yml               # Docker services configuration
├── Dockerfile                       # Container build instructions
├── pages/                           # Page Object Models
│   └── base_page.py                 # Page object
│   └── manager_page.py              # Page object
│   └── customers_page.py            # Page object
│   └── add_customer_page.py         # Page object
├── tests/                           # Test files
│   └── test_customer_management.py  # Test suite
├── utils/                           # Utility modules
│   └── data_generator.py            # Test data generation
├── constants.py                     # Project constants
├── requirements.txt                 # Python dependencies
├── pytest.ini                       # Python configuration
└── README.md                        # Project documentation
```

## Installation
### Local Setup

1.
Clone the repository:
```
git clone <repository-url>
cd <project-folder>
```
2.
Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3.
Install dependencies:
```
pip install -r requirements.txt
```
## Docker Setup
No additional installation is needed beyond Docker and Docker Compose.
## Running Tests
### Locally
Run tests using pytest directly:
```
# Run all tests with Chrome browser in local mode
pytest --mode local

# Run specific test file
pytest tests/test_customer_management.py --mode local

# Run with Allure reporting
pytest --mode local --alluredir=./allure-results
```
### Using Docker Compose
Run tests in a containerized environment with Selenium Grid:
```
# Start all services and run tests in both Chrome and Firefox
docker-compose up -d

# Run only Chrome tests
docker-compose up -d pytest-chrome

# Run only Firefox tests
docker-compose up -d pytest-firefox

# Run specific test path with Chrome
TEST_PATH=tests/test_customer_management.py docker-compose up -d pytest-chrome

# Control parallel instances
CHROME_INSTANCES=5 docker-compose up -d pytest-chrome
```
## Viewing Test Results
Allure reports are available at http://localhost:5050 after running tests with Docker Compose.
To generate and view Allure reports locally:
```
# Generate report from results
allure generate allure-results -o allure-report

# Open the report
allure open allure-report
```

## Configuration Options
### Command Line Options

- --browser: Specify browser (chrome or firefox)
- --mode: Execution mode (local or remote)

## Environment Variables
When running in Docker:

- SELENIUM_HUB_HOST: Selenium hub hostname (default: selenium-hub)
- SELENIUM_HUB_PORT: Selenium hub port (default: 4444)
- HEADLESS: Run browsers in headless mode (true/false)
- CHROME_INSTANCES: Number of parallel Chrome test instances
- FIREFOX_INSTANCES: Number of parallel Firefox test instances
- TEST_PATH: Specific test path to run

## Test Examples
The framework includes example tests for customer management in a banking application:

- Adding new customers
- Sorting customer lists
- Deleting customers

Each test is documented with Allure annotations for clear reporting and includes detailed steps.
## Customization
### Adding New Page Objects
Create new page object classes in the pages directory:
```
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class YourNewPage(BasePage):
    # Locators
    SOME_ELEMENT = (By.ID, "element-id")
    
    # Actions
    def perform_action(self):
        self.driver.find_element(*self.SOME_ELEMENT).click()
        return self

```

### Adding New Tests
Create new test files in the tests directory following the existing pattern with Allure annotations.
## Browser Support

- Chrome (default)
- Firefox

## Contributing

- 1.Fork the repository
- 2.Create a feature branch
- 3.Make your changes
- 4.Submit a pull request






































