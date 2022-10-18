
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_headers import Headers


def init():
    service = Service("./webdriver/chromedriver")
    options = webdriver.ChromeOptions()
    header = Headers().generate()['User-Agent']
    # options.add_argument('--headless')  # runs browser in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-gpu')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--user-agent={}'.format(header))
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    return driver
