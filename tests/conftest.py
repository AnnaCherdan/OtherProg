import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options


@pytest.fixture
def get_firefox_options():
    options = firefox_options()
    options.add_argument('firefox') # Use 'headless' if you don't need a brouser UI.
    options.add_argument('--start-maximized')
    options.add_argument('--window-size == 800, 600')
    return options


@pytest.fixture
def get_webdriver(get_firefox_options):
    options = get_firefox_options
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox(executable_path='D:\\AllDoc\\AnnCherdan\\'
    #                                            'Python\\PtojectsPyCharm\\OtherProg\\geckodriver.exe',
    #                            options=options)
    #     https://www.youtube.com/watch?v=dlh7Z9MU3Yc

@pytest.fixture

