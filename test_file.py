#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/file_input.html")

#sunduk = browser.find_element_by_id("treasure")
#number = sunduk.get_attribute("valuex")

#number = browser.find_element_by_id("input_value")
#number = number.text
#y = calc(number)

option1 = browser.find_element_by_name("firstname")
option1.send_keys("kek")
option2 = browser.find_element_by_name("lastname")
option2.send_keys("l")
option3 = browser.find_element_by_name("email")
option3.send_keys("@")

files = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
files.send_keys(file_path)

butt = browser.find_element_by_css_selector("button.btn")
butt.click()
