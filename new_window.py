from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CLASS_NAME, 'trollface')
    btn.click()

    wind = browser.window_handles[1]
    browser.switch_to.window(wind)

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