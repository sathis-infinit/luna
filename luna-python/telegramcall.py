


def telegram_call(telegram_id):

    
    from gettext import find
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys


    option = webdriver.ChromeOptions() 
    option.add_argument("user-data-dir=/Users/sathishkumar/Library/Application Support/Google/Chrome/")
    driver = webdriver.Chrome(options=option)
    driver.get("https://web.telegram.org/z/#1827945413")

    call_btn = driver.find_element(By.XPATH, '//*[@id="MiddleColumn"]/div[3]/div[1]/div[2]/div/button[2]')
    
    call_btn.click()


