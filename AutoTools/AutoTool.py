from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://signup.live.com/signup?lic=1&uaid=b0f1da0f5343442b94c90df827ac698d')


def actionWithWeb(xPath):
    path = '/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form'
    return driver.find_element_by_xpath(path + xPath)


actionWithWeb('/div/div[1]/fieldset/div[2]/div/div[3]/a').click()
actionWithWeb('/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/div/select').click()
actionWithWeb('/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/div/select/option[2]').click()
actionWithWeb('/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/input').send_keys('devtest.14541')
actionWithWeb('/div/div[1]/div[2]/div/div/div/div[3]/input').click()

time.sleep(2)

actionWithWeb('/div[3]/div/input[2]').send_keys('145678@devtest123')
actionWithWeb('/div[7]/div/div/div[2]/input').click()

time.sleep(2)

actionWithWeb('/div[1]/div[3]/div[1]/input').send_keys('Developer')
actionWithWeb('/div[1]/div[3]/div[2]/input').send_keys('Python Test')
actionWithWeb('/div[2]/div/div/div[2]/input').click()

time.sleep(2)

# Month
actionWithWeb('/div/div[4]/div[3]/div[1]/select').click()
actionWithWeb('/div/div[4]/div[3]/div[1]/select/option[3]').click()
# Day
actionWithWeb('/div/div[4]/div[3]/div[2]/select').click()
actionWithWeb('/div/div[4]/div[3]/div[2]/select/option[7]').click()
# Year
actionWithWeb('/div/div[4]/div[3]/div[3]/input').send_keys('1995')

actionWithWeb('/div/div[6]/div/div/div[2]/input').click()

time.sleep(2)
actionWithWeb('/div[3]/iframe/html/body/div/div/iframe/html/body/div[2]/div[2]/div[1]/iframe/html/body/div/div/div[1]/button').click()

time.sleep(8)

driver.switch_to.frame("CaptchaFrame")
s = driver.find_element_by_xpath("//body").text
print ("Test inside frame: " + s)

driver.find_element_by_xpath('/html/body/div/div/div[1]/button').click()
