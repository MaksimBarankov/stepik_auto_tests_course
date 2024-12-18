from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element ((By.CSS_SELECTOR, "#price"), '100'))
book_button = browser.find_element(By.CSS_SELECTOR, "#book")
book_button.click()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)
solve_button = browser.find_element(By.CSS_SELECTOR, "#solve")
solve_button.click()
sleep(30)
