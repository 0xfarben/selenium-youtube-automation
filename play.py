import time
import unittest
from skip_ad import YoutubeSkipTest◘
from selenium.webdriver.common.by import By

class YoutubeplayTest(unittest.TestCase):

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None

    def skips(self):
        self.skipping = YoutubeSkipTest(self.email, self.password, self.phone_number)
        self.skipping.run_test()
        self.driver = self.skipping.driver

    def play_pause(self):
        driver = self.driver
        try:
            pause_button = driver.find_element(By.TAG_NAME, 'body')
            pause_button.send_keys('k')
            print("Successfully Video paused")
        except:
            print("Pause button not found")
        print("Staying on the screeen for 7 seconds")
        time.sleep(7)

        try:
            play_button = driver.find_element(By.TAG_NAME, 'body')
            play_button.send_keys('k')
            print("Successfully Video played")
            print("Staying on the screeen for 7 seconds")
            time.sleep(7)
        except:
            print("Play button not found")
            
        try:
            print("Pausing for the last time")
            play_button = driver.find_element(By.TAG_NAME, 'body')
            play_button.send_keys('k')
            print("Pasue for last time for confirmation")
            print("Play/pause execution is successfully executed")
            print("Test passed")
            time.sleep(10)
        except:
            print("Unable to pause for last time")
    
    def run_test(self):
        self.skips()
        self.play_pause()

# Uncomment the below lines to test the search independently
# if __name__ == "__main__":
#     email = ''
#     password = ''
#     phone_number = ''
#     youtube_test = YoutubeplayTest(email, password, phone_number)
#     youtube_test.run_test()
