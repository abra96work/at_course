from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )
    btn = browser.find_element(By.ID, "book")
    btn.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, '.form-control#answer')
    answer.send_keys(y)

    sub = browser.find_element(By.CSS_SELECTOR, '.btn[type="submit"]')
    sub.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()