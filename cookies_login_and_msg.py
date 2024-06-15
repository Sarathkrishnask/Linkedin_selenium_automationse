from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
import re
from find_offers import *
import time 
import pickle
from endorse import *

print("Enter state 0 for create connection / 1 for send the message to connections")
state = int(input("Enter the state for : "))

print("Add the note for before you send the connection this is only for when you going connection request")
note = input("Add a note you want to send :")

print("Enter the name which you want to send MESSAFE OR CONNECTION ")
user_dat  = input("Enter the username: ")

print("Enter the job profile you want to apply :")
job_post = input("Enter the job role: ")

driver = webdriver.Chrome()
driver.get("https://linkedin.com")
time.sleep(2)

# Load cookies from the file
with open("linkedin_cookies.pkl", "rb") as file:
    cookies = pickle.load(file)

# Add cookies to the current session
for cookie in cookies:
    # Adjust the domain if necessary
    if 'linkedin.com' not in cookie['domain']:
        cookie['domain'] = '.linkedin.com'
    driver.add_cookie(cookie)

# Refresh the page to apply the cookies and login automatically
driver.get("https://www.linkedin.com/feed/")

time.sleep(1)  # Wait for the page to load

# Check if we are logged in by checking for an element that's only visible when logged in
try:
    profile_icon = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='global-nav__me-photo ember-view']"))
    )

    
    print("Logged in successfully.")
except Exception as e:
    
    print("Not logged in, please check your cookies.")

time.sleep(2)



# Find the search input field
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))

# Send the search query (name) to the input field
search_input.send_keys(user_dat)  

# Submit the search query
search_input.send_keys(Keys.RETURN)

# Wait for search results to load
try:
    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'search-result__occluded-item')]"))
    )
    # Perform the desired action with the element, e.g., click
    element.click()
except Exception as e:
    print(f"An error occurred: {e}")

# Click on the first search result
all_buttons = driver.find_elements(By.TAG_NAME,"button")

if state == 1:
    message_btn = [btn for btn in all_buttons if btn.text == "Message"]
    message_btn[0].click()
    time.sleep(2)

    main_div = driver.find_element(By.XPATH, "//div[starts-with(@class, 'msg-form__msg-content-container')]")
    main_div.click()
    paragraph = driver.find_elements(By.TAG_NAME,"p")
    paragraph[-5].send_keys('testing')

    submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
    # driver.find_element(By.XPATH, "/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/footer/div[2]/div[1]/button").click()
    # time.sleep(2)
    submit_button.click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/header/div[4]/button[3]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[5]/header/div/nav/ul/li[1]/a").click()
    time.sleep(1)

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
                driver.find_element(By.XPATH,"/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/header/div[4]/button[3]").click()
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[5]/header/div/nav/ul/li[1]/a").click()
                time.sleep(1)

            except Exception as e:
                print(e)
        
    else:
        print("Connect button not found.")


try:
    profile_icon = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div/div[1]/div[1]/a/div[2]")
    profile_icon.click()
    time.sleep(5)

    # to download profile details:
    more_btn = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div[2]/div")
    more_btn.click()
    time.sleep(1)
    download_butn = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div[2]/div/div/div/ul/li[2]").click()
    time.sleep(3)

    # #create a post
    createpost = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[5]/div[2]/div/div[1]/div[2]/div/div").click()

    time.sleep(1)

    post = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/p")
    post.send_keys("hii linkedin family")
    time.sleep(1)
    submit_post = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='share-box_actions']"))
        )
    
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div[3]/button[2]").click()
    time.sleep(2)
    # submit_post.click()

    #apply job 
    driver.find_element(By.XPATH,"/html/body/div[5]/header/div/nav/ul/li[3]/a").click()
    # # Find the search input field
    search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]")))

    # Send the search query (name) to the input field
    search_input.send_keys(job_post)  

    # Submit the search query
    search_input.send_keys(Keys.RETURN)
    time.sleep(3)

    # find the total amount of results (if the results are above 24-more than one page-, we will scroll trhough all available pages)
    total_results = driver.find_element(By.CLASS_NAME,"display-flex.t-12.t-black--light.t-normal")
    total_results_int = int(total_results.text.split(' ',1)[0].replace(",",""))
    print(total_results_int)

    time.sleep(2)
    # get results for the first page
    current_page = driver.current_url
    results = driver.find_elements(By.CLASS_NAME,"scaffold-layout__list-container")

    # for each job add, submits application if no questions asked
    for result in results:
        hover = ActionChains(driver).move_to_element(result)
        hover.perform() 
        titles = result.find_elements(By.CLASS_NAME,'disabled.ember-view.job-card-container__link.job-card-list__title.job-card-list__title--link')
        for title in titles:
            job_add = title
            print('You are applying to the position of: ', job_add.text)
            job_add.click()
            time.sleep(2)
            
            # click on the easy apply button, skip if already applied to the position
            try:
                #apply
                in_apply = driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[6]/div/div/div/button")
                in_apply.click()
                time.sleep(1)
                #next
                next = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
                next.click()
                time.sleep(1)
                #review
                # next = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]")
                # next.click()
                # time.sleep(1)
    
            except NoSuchElementException:
                print('You already applied to this job, go to next...')
                pass
            time.sleep(1)

            # try to submit if submit application is available...
            try:
                
                time.sleep(1)
                submit = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]")
                submit.send_keys(Keys.RETURN)
                # time.sleep(1)
            
            # ... if not available, discard application and go to next
            except NoSuchElementException:
                print('Not direct application, going to next...')
                try:
                    discard = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/button")
                    discard.send_keys(Keys.RETURN)
                    time.sleep(1)
                    discard_confirm = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div[3]/button[1]")
                    discard_confirm.send_keys(Keys.RETURN)
                    time.sleep(1)
                except NoSuchElementException:
                    pass

            time.sleep(1)

    else:
       driver.close()
    print("Logged in successfully.")
except Exception as e:
    print("Not",e)

