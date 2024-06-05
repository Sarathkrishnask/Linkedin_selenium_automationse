
from selenium import webdriver
import pickle
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open LinkedIn and manually login
driver.get("https://www.linkedin.com/login")

# Wait for manual login
time.sleep(30)  # Adjust the sleep time as necessary for manual login

# Save cookies after login
cookies = driver.get_cookies()
with open("linkedin_cookies.pkl", "wb") as file:
    pickle.dump(cookies, file)

driver.quit()
