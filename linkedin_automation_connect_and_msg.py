from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 

username_ = input("Enter your linkedin username :")
password_ = input("Enter your linkedin password:")

print("Enter state 0 for create connection / 1 for send the message to connections")
state = int(input("Enter the state for : "))

print("Add the note for before you send the connection this is only for when you going connection request")
note = input("Add a note you want to send :")

print("Enter the name which you want to send MESSAFE OR CONNECTION ")
user_dat  = input("Enter the username: ")

driver = webdriver.Chrome()
driver.get("https://linkedin.com")

# Wait for the username input field to be present
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='session_key']")))
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

time.sleep(2)
username.send_keys(username_)
password.send_keys(password_)
time.sleep(2)

# Click the submit button
submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(2)

# Find the search input field
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

# Send the search query (name) to the input field
search_input.send_keys(user_dat)  # Replace "John Doe" with the name you want to search for


# Submit the search query
search_input.send_keys(Keys.RETURN)

# Wait for search results to load
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'search-result__occluded-item')]"))
    )
    # Perform the desired action with the element, e.g., click
    element.click()
except Exception as e:
    print(f"An error occurred: {e}")
# print(element)
# Click on the first search result
all_buttons = driver.find_elements(By.TAG_NAME,"button")

if state == 1:
    message_btn = [btn for btn in all_buttons if btn.text == "Message"]
    print("Message button found.")
    message_btn[0].click()
    time.sleep(2)

    main_div = driver.find_element(By.XPATH, "//div[starts-with(@class, 'msg-form__msg-content-container')]")
    main_div.click()
    paragraph = driver.find_elements(By.TAG_NAME,"p")
    paragraph[-5].send_keys('testing')

    submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )

    submit_button.click()

if state == 0:
     # Connect with user
    connect_btn = [btn for btn in all_buttons if btn.text in ["Connect", "Follow"]]
    if connect_btn:
        connect_btn[0].click()
        time.sleep(2)
        if not note :
            try:
                send_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Send without a note')]")
                send_button.click()
            except Exception as e:
                print(e)
        else:
            try:
                send_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Add a note')]")
                send_button.click()
                time.sleep(2)
                textarea = driver.find_elements(By.TAG_NAME,"textarea")
                textarea[0].send_keys(note)
                time.sleep(2)
                send_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Send invitation')]")
                send_button.click()
                time.sleep(2)
            except Exception as e:
                print(e)
        
    else:
        print("Connect button not found.")
