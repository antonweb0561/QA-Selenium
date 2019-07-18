#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/redirect_accept.html")

butt = browser.find_element_by_css_selector("button.btn")
butt.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

number = browser.find_element_by_id("input_value")
number = number.text
y = calc(number)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)


butt = browser.find_element_by_css_selector("button.btn")
butt.click()
