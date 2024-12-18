from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
sleep(30)