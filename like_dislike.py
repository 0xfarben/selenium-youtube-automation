import time
import unittest
from play import YoutubeplayTest◘
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YoutubelikedislikeTest(unittest.TestCase):

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None

    def plays(self):
        self.playing = YoutubeplayTest(self.email, self.password, self.phone_number)
        self.playing.run_test()
        self.driver = self.playing.driver


    def like_dislike(self):
        driver = self.driver
       # Locate and click the like button
        try:
            like_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-level-buttons-computed"]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button'))
            )
            like_button.click()
            print("Video liked")
        except:
            print("Like button not found")
        time.sleep(10)

        # Locate and click the dislike button
        try:
            dislike_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-level-buttons-computed"]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/dislike-button-view-model/toggle-button-view-model/button-view-model/button'))
            )
            dislike_button.click()
            print("Video disliked")
        except:
            print("Dislike button not found")
        time.sleep(10)
    
    def run_test(self):
        self.plays()  
        self.like_dislike()

# Uncomment the below lines to test the like/dislike functionality independently
# if __name__ == "__main__":
#     email = ''
#     password = ''
#     phone_number = ''
#     youtube_test = YoutubelikedislikeTest(email, password, phone_number)
#     youtube_test.run_test()
