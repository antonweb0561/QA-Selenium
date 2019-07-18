#! /usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
import math
import time 
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.mark.parametrize('numbers', ["897", "898", "899", "903", "904", "905"])
def test_function(browser, numbers):
	link = 'https://stepik.org/lesson/236{}/step/1'.format(numbers)
	browser.get(link)

	time.sleep(15)
	y = math.log(int(time.time()))
	y = str(y)
	answer = browser.find_element_by_css_selector("textarea.textarea")
	answer.send_keys(y)
	time.sleep(5)

	butt = browser.find_element_by_css_selector(".submit-submission")
	butt.click()
	time.sleep(35)
	mess = browser.find_element_by_css_selector("pre.smart-hints__hint")
#	mess1 = mess.text()
	assert mess == 'Correct!', "Value is not 'Correct'"
	print(str(mess))
#	listok.append(mess)
#	return mess
#print(listok)

