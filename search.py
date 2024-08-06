import time
import random
from login import YouTubeLoginTest◘
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YoutubeSearchTest():
    
    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None

    def logining(self):
        self.loggs= YouTubeLoginTest(self.email, self.password, self.phone_number)
        self.loggs.login()
        self.driver = self.loggs.driver

    def test_search(self):
        driver = self.driver
        search_bar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "search_query"))
        )
        time.sleep(10)

        search_bar.send_keys("python programming")
        search_bar.send_keys(Keys.RETURN)
        time.sleep(10)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "filter-menu"))
        )
        print("Search test case is executed")
        time.sleep(10)

        videos = driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
        random_video = random.choice(videos)
        random_video.click()
        time.sleep(10)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'title'))
        )
        print("Random video is selected")
        time.sleep(10)

    def run_test(self):
        self.logining()
        self.test_search()

# Uncomment the below lines to test the search independently
# if __name__ == "__main__":
#     email = ''
#     password = ''
#     phone_number = ''
#     youtube_test = YoutubeSearchTest(email, password, phone_number)
#     youtube_test.run_test()
