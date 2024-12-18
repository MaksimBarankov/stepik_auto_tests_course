from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/get_attribute.html")

x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
x = x_element.get_attribute("valuex")
y = calc(x)
answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)
checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox .click()
radiobutton = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
radiobutton .click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
sleep(30)

