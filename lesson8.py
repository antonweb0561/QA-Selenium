#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")
#elements = browser.find_elements_by_type("text")
#elements = browser.find_element_by_xpath("//input[@type='text']")
input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
elements = browser.find_element_by_xpath("//button[text()='Отправить']")
#for element in elements:
#    element.send_keys("Мой ответ")

#button = browser.find_element_by_css_selector("button.btn")
elements.click()
# не забывайте добавлять пустую строку в конце каждого файла в Python
