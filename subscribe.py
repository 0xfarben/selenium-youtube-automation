import time
import unittest
from selenium.webdriver.common.by import By
from like_dislike import YoutubelikedislikeTest◘
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YoutubesubscribeTest(unittest.TestCase):

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None

    def likes_dislikes(self):
        self.L_D_instance = YoutubelikedislikeTest(self.email, self.password, self.phone_number)
        self.L_D_instance.run_test()
        self.driver = self.L_D_instance.driver
        
    def subscribe(self):
        driver = self.driver
        try:
            subscribe_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer'))
            )
            subscribe_button.click()
            print("Subscribed to the channel")
        except:
            print("Subscribe button not found")
        time.sleep(10)
    
    def run_test(self):
        self.likes_dislikes()
        self.subscribe()

# Uncomment the below lines to test the subscribe button functionality independently
# if __name__ == "__main__":
#     email = ''
#     password = ''
#     phone_number = ''
#     youtube_test = YoutubesubscribeTest(email, password, phone_number)
#     youtube_test.run_test()
