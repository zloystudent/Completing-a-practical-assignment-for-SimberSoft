import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.page_load_strategy = "eager"
    
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    
    allure.attach(
        f"Browser: Chrome\nOptions: {options.arguments}",
        name="Browser Configuration",
        attachment_type=allure.attachment_type.TEXT
    )
    
    
    test_name = request.node.name
    allure.dynamic.title(test_name)
    
    yield driver
    
    
    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    
    setattr(item, f"rep_{rep.when}", rep)
    
    
    if rep.failed:
        allure.attach(
            str(call.excinfo),
            name="Exception Info",
            attachment_type=allure.attachment_type.TEXT
        )
