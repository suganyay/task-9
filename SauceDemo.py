from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
"""
AIM:LOGIN with username and password
STEPS:
1.Fetch the titile of the page
2.Fetch the current URL of the Webpage
3.Extract the content of the webpage and save it in a text file
"""


# Class to hold data
class Data:
    # Login credentials
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    URL = "https://www.saucedemo.com/"


# Class to hold element locators
class Locators:
    USERNAME_BOX = "user-name"  # Updated the name to match actual site
    PASSWORD_BOX = "password"
    LOGIN_BUTTON = '//input[@type="submit"]'


# Main class for handling actions
class SauceDemo(Data, Locators):
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)

            username_box = self.driver.find_element(By.NAME, self.USERNAME_BOX)
            password_box = self.driver.find_element(By.NAME, self.PASSWORD_BOX)
            login_button = self.driver.find_element(By.XPATH, self.LOGIN_BUTTON)

            # Enter credentials and click login
            if username_box and password_box:
                username_box.send_keys(self.USERNAME)
                password_box.send_keys(self.PASSWORD)
                if login_button:
                    login_button.click()
                    sleep(2)  # Allow time for login
                    return self.driver.current_url
        except Exception as error:
            print("ERROR: Something happened!", error)

    def shutdown(self):
        self.driver.quit()

    # Fetch the URL of the current webpage
    def fetch_url(self):
        try:
            return self.driver.current_url
        except Exception as error:
            print("ERROR: Unable to fetch URL!", error)

    # Fetch the title of the current webpage
    def fetch_title(self):
        try:
            return self.driver.title
        except Exception as error:
            print("ERROR: Unable to fetch TITLE!", error)


if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    sauce = SauceDemo(url)
    print("Fetching URL...")
    print(sauce.fetch_url())

    print("Fetching Title...")
    print(sauce.fetch_title())

    print("Attempting to Login...")
    logged_in_url = sauce.login()
    if logged_in_url:
        print(f"Login successful! Current URL: {logged_in_url}")
    else:
        print("Login failed.")
    sleep(5)

    print("Shutting down driver...")
    sauce.shutdown()