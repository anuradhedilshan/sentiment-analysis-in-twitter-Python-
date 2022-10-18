from lib2to3.pgen2 import driver
from tqdm import tqdm
import element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


class Twitter:
    driver = None
    RETWEETCOUNT = 0
    RETWEET = 0

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        if(self.driver):
            self.driver.get("https://twitter.com/i/flow/login")
            try:
                print("Sd")
                username = self.driver.find_element(
                    By.XPATH, element.LOGIN_USERNAME)
                username.send_keys("anuradhedilshan@gmail.com")
                username.send_keys(Keys.ENTER)

                password = self.driver.find_element(
                    By.XPATH, element.LOGIN_PASSWORD)
                password.send_keys("ANURADHA1234567890")
                password.send_keys(Keys.ENTER)
                time.sleep(5)
                if self.driver.current_url != "https://twitter.com/home":
                    raise Exception("Login FAiled")
                else:
                    print("Login Sucessfull")
            except:
                raise Exception("Login Failed")

    def fetch_tweet(self, url):
        retweets = []
        if(self.driver):
            self.driver.get(url)
            el = WebDriverWait(self.driver, timeout=3).until(
                lambda d: d.find_element(By.XPATH, element.RETWEETS_COUNT))
            self.RETWEETCOUNT = int(el.text.replace(',', ''))

            for _ in tqdm(range(self.RETWEETCOUNT//3), desc='Fetching Tweets'):

                articles = elements = self.driver.find_elements(
                    By.CSS_SELECTOR, element.TWEETCANVAS)

                try:
                    for i in elements:
                        tweet = i.find_element(
                            By.CSS_SELECTOR, element.TWEET)

                        user = i.find_element(
                            By.CSS_SELECTOR, element.USER)

                        user_tweet = {
                            "tweet": tweet.text,
                            "user": user.text
                        }
                        self.RETWEET += 1
                        retweets.append(user_tweet)
                except:
                    continue

                self.driver.execute_script(
                    'window.scrollTo(0, document.body.scrollHeight)'
                )
                time.sleep(4)

            return retweets
