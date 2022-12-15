import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = 'http://suninjuly.github.io/explicit_wait2.html'
  browser = webdriver.Chrome()
  browser.get(link)

  label1 = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
  button1 = browser.find_element(By.ID, 'book')
  button1.click()

  label2 = browser.find_element(By.ID, 'input_value')
  x = label2.text
  x = calc(x)

  input1 = browser.find_element(By.TAG_NAME, 'input')
  input1.send_keys(x)

  button2 = browser.find_element(By.ID, 'solve')
  button2.click()

  print(str(browser.switch_to.alert.text).split(': ')[1])

except Exception as ex:
  s = str(ex)
  with open('Error.txt', 'a') as error:
    error.writelines(s)