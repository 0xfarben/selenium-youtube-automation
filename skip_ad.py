import time
from search import YoutubeSearchTest
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YoutubeSkipTest():

    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None
      
    def searches(self):
        # Initialize and run YoutubeSearchTest
        self.log_search = YoutubeSearchTest(self.email, self.password, self.phone_number)
        self.log_search.run_test()
        self.driver = self.log_search.driver
        pass
        
    def skip_ad(self):
        driver = self.driver
        while True:
            try:
                # Wait for a few seconds to ensure the ad has loaded (adjust time if needed)
                time.sleep(5)
                print("Attempting to locate and click the 'Skip' button.")
                
                # Wait until the "Skip" button is present in the DOM and clickable
                skip_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ytp-skip-ad-button")]'))
                )
                skip_button.click()
                print("Clicked the 'Skip' button.")

                # Break the loop after successfully clicking the "Skip" button
                break
                
            except Exception as e:
                print(f"Could not click on the 'Skip' button. Error: {e}")

            # Wait for a short period to allow any "Skip Ad" buttons to appear
            time.sleep(5)

    def run_test(self):
        self.searches()
        self.skip_ad()

# Uncomment the below lines to test the search independently
# if __name__ == "__main__":
    # email = ''
    # password = ''
    # phone_number = ''
    # youtube_test = YoutubeSkipTest(email, password, phone_number)
    # youtube_test.run_test()
