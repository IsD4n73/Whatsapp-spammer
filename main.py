import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as Condition
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def spam_message(message, name, spam_number):
    if message is not None and name is not None:
        try:
            x_arg = '//span[contains(@title,\'' + name + '\')]'
            
            group_title = wait.until(Condition.presence_of_element_located((By.XPATH, x_arg)))
            group_title.click()

            inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            input_box = wait.until(Condition.presence_of_element_located((By.XPATH, inp_xpath)))

            for i in range(spam_number):
                input_box.send_keys(message + Keys.ENTER)
                time.sleep(1)
        except:
            print("Errore...")
    return




if __name__ == '__main__':

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    time.sleep(5)

    contact_name = "Pinco Pallino"
    message_string = "Se funziona ti spammo 5 messaggi :)"
    spam_count = 5
    
    spam_message(message=message_string, name=contact_name, spam_number=spam_count)

    driver.quit()
