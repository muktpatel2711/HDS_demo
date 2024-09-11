import os.path
from datetime import datetime

from selenium import webdriver

import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# report

def pytest_configure(config):
    config._metadata['Project Name'] = 'Demo_Project'
    config._metadata['Module Name'] = "HDS"
    config._metadata['Tester'] = "Mukt"

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Generate report path with timestamp
    config.option.htmlpath = os.path.abspath(os.curdir) + "//reports//" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"

# You don't need pytest_metadata, instead use pytest_html_results_summary if needed
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Project: Demo_Project", f"Module: HDS", f"Tester: Mukt"])