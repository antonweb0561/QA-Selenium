#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

#butt = browser.find_element_by_css_selector("button.btn")
#butt.click()

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "10000 RUR")
    )

butt = browser.find_element_by_css_selector("button.btn")
butt.click()

browser.execute_script("window.scrollBy(0,100);")

number = browser.find_element_by_id("input_value")
number = number.text
y = calc(number)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)


butt = browser.find_element_by_id("solve")
butt.click()
