from behave import *
from selenium import webdriver

browser = webdriver.Chrome()
@given(u'that user is in Google')
def step_impl(context):

    browser.get("http://www.google.lk")

@when(u'user types \'Selenium\'')
def step_impl(context):
    browser.find_element_by_name("q").send_keys("Selenium")
    browser.find_element_by_name("q").send_keys(u'\ue007')


@then(u'results should have selenium HQ page')
def step_impl(context):
    browser.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/div/div[1]/a/h3").click()
    assert browser.title == "Selenium - Web Browser Automation"
    browser.close()