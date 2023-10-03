import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from test_data.homepage_data import HomePageData

driver = None #driver is made global so that screenshot methods can use the same driver

#to decide browser from command line, browser_name is variable can be anything but pass same key in command line
# in cmd line: py.test --browser_name chrome(value should be same in below if block)
# if no value is given cmd prmpt, then chrome is taken as default browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def browser_access(request):
    browser = request.config.getoption("--browser_name")
    global driver #driver is set to global
    if browser =="chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service_chrome = Service('C:\\Users\\Anil-Teju\\PycharmProjects\\drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=service_chrome,options=chrome_options)
    elif browser == "firefox":
        pass #code for gecko webdriver
    elif browser == "edge":
        service_obj = Service('C:\\Users\\Anil-Teju\\PycharmProjects\\drivers\\msedge.exe')
        driver = webdriver.Edge(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    #request obj will link driver to actual testcase, now driver is python class variable(cls) so we can access with self.
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(params=HomePageData.registration_data)
def get_data(request):
    return request.param

'''
#with excel data
@pytest.fixture(params=HomePageData.get_excel_data("Testcase2"))
def get_data(request):
    return request.param
'''
# pytest_runtest_makereport and _capture_screenshot methods are to capture error screenshots
#@pytest.mark.hookwrapper deprecated
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

