from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time
import datetime

def write_into_file(filename, data):
    with open(filename, 'a', encoding="utf-8") as file: 
        if data == None:
            print("There was no data passed!")
            return None
        for item in data:
                file.write(str(item) + '\n')
    return f"{len(data)} entries Has been written into a {filename}!"


def data_formatting(elements):
    for elem in elements:
        try:
            selected_element = elem.find_element(By.CLASS_NAME, "title")
            a_elem = selected_element.find_element(By.XPATH, ".//a")
            data_to_file.append((selected_element.text, elem.find_element(By.CSS_SELECTOR, "div.score.unvoted").text, 
                                a_elem.get_attribute('href')))
        except NoSuchElementException:
            print("Element not found for one or more items. Skipping.")
            # You might want to handle this case depending on your requirements
    return data_to_file

if __name__ == "__main__":     
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    current_time = datetime.datetime.now()
    filename = current_time.strftime("DATA-%m-%d_%H-%M.txt")

    valid_subreddit = False
    while not valid_subreddit:
        crawl = input("Enter your subreddit: ")
        answer = "yes"
        driver.get(f"https://old.reddit.com/r/{crawl}")
        subreddit_no_posts = driver.find_elements(By.CSS_SELECTOR, '[data-context="listing"]')
        if(subreddit_no_posts == []):
            print("There is no posts in the subreddit, Try putting another one")
        else:
            valid_subreddit = True

    target_className = "title"
    while answer[0].upper() == "Y":
        for i in range(1,3):
            WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-context="listing"]'))
            )
            data_to_file = []
            elements = driver.find_elements(By.CSS_SELECTOR, '[data-context="listing"]')
            print("Elements here >>> ",elements)
            data_to_file = data_formatting(elements)

            print(f"Writing them into a file... \n {data_to_file}")
            write_into_file(filename, data_to_file) 
            driver.find_element(By.CSS_SELECTOR, 'div.nav-buttons>.nextprev>.next-button>a').click()  

            answer = input("Do you want to proceed further?")
            
        driver.find_element(By.CSS_SELECTOR, 'div.nav-buttons>.nextprev>.next-button>a').click()  

    driver.quit()

#def saveData( data ) -> enteries { savedata? } needed


# make a tuple that looks like (title, votes, link_to_post) 
# call write_into_file

