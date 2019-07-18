#! /usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")

#sunduk = browser.find_element_by_id("treasure")
#number = sunduk.get_attribute("valuex")

number = browser.find_element_by_id("input_value")
number = number.text
y = calc(number)

butt = browser.find_element_by_css_selector("button.btn")
#browser.execute_script("return arguments[0].scrollIntoView(true);", butt)
browser.execute_script("window.scrollBy(0, 200);")

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()
option2 = browser.find_element_by_id("robotsRule")
option2.click()

#butt = browser.find_element_by_css_selector("button.btn")
#browser.execute_script("return_arguments[0].scrollIntoView(true);", butt)
butt.click()
