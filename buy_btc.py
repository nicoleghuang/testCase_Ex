#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from testCase_Ex import account

import os,time
for k,v in account.diction().items():
    browser = webdriver.Chrome()
    #browser.maximize_window()
    #open website
    browser.get(account.website())
    print(k,v)
    browser.implicitly_wait(60)

    #switch to english version
    #browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[3]/a').click()
    #time.sleep(3)
    #browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[3]/ul/li[2]/a').click()
    #login
    browser.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div[3]/div/div[3]/div/div[2]/form/div[2]/div[1]/div/input').send_keys(k)
    browser.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div[3]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/input').send_keys(v)
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('//*[@id="__nuxt"]/div[2]/div[3]/div/div[3]/div/div[2]/form/div[4]/button').click()
    time.sleep(15)
    #browser.implicitly_wait(10)

    #enter contract trading market
    browser.implicitly_wait(10)
    id_trade='//*[@id="__nuxt"]/div[2]/div[1]/nav/ul[1]/li[2]/a'
    browser.find_element_by_xpath(id_trade).click()
    #browser.implicitly_wait(10)
    #browser.find_element_by_xpath('/html/body/div/div[1]/div/ul/li[4]/a').click()
    #print 'enter trading market successfully'

    # choose L3
    #browser.find_element_by_xpath('/html/body/div/div[2]/div[1]/ul/li[2]/a').click()

    # buy btc
    id_price='//*[@id="__nuxt"]/div[2]/div[3]/div/section/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[6]/input'

    id_quantity='//*[@id="__nuxt"]/div[2]/div[3]/div/section/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[7]/input'

    id_submit='//*[@id="__nuxt"]/div[2]/div[3]/div/section/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[9]/button'
    for i in range(100):
        m=5.01+i*0.001
        #print m
        n=0.01+i*0.1
        #n=0.01
        #print n
        browser.implicitly_wait(10)
        #browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/span[2]/input').send_keys(m)
        browser.find_element_by_xpath(id_price).send_keys(Keys.CONTROL, 'a')
        browser.find_element_by_xpath(id_price).send_keys(str(m))
        #browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[4]/span[2]/input').send_keys(n)
        #browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[6]/a').click()
        #browser.find_element_by_xpath(id_quantity).clear()
        browser.find_element_by_xpath(id_quantity).send_keys(str(n))
        browser.find_element_by_xpath(id_submit).click()

        time.sleep(3)
        #browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[4]/button').click()
        #browser.switch_to_alert().accept()
        #browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[4]/button')
print('finished...')