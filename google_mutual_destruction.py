# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:33:22 2019

@author: yunod
"""



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv



base_path = r'C:\Users\yunod\OneDrive\桌面\old pc 20190908\complex network 2018\2019\complex network modeling\policy network n political computation\hk_research_20191126'
excel = open(base_path+'\google經濟攬炒20191230big5.csv', mode='a+', newline='', errors='ignored',encoding='utf-8-sig')  # gb18030  #utf-8-sig #big5
google_writer = csv.writer(excel, delimiter=',')
google_writer.writerow(['title','url','date','text'])
# 攬炒  # in traditional pc -> big5  # in simplified pc ->utf8

options = webdriver.ChromeOptions()
#driver.set_page_load_timeout(7)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#options.add_argument("--headless") 
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(base_path+'\chromedriver.exe',chrome_options=options)
driver.set_page_load_timeout(5)
#driver.get("https://lihkg.com/profile/216907")
#driver.get('https://www.google.com/search?q=%E6%94%AC%E7%82%92&oq=%E6%94%AC%E7%82%92&aqs=chrome..69i57j0j35i39j0l2j69i60l3.1096j0j7&sourceid=chrome&ie=UTF-8')
#driver.get('https://www.google.com/search?q=%E6%94%AC%E7%82%92&filter=0&biw=929&bih=889') # https://www.google.com/search?q=攬炒&filter=0&biw=929&bih=889
#base_url = 'https://www.discuss.com.hk/search.php?searchsubmit=true&srchtxt=攬炒&orderby=dateline&page=1'
#driver.get('https://www.google.com/search?q=%E5%8B%87%E6%AD%A6&sxsrf=ACYBGNR5o_0b4E-1drP-MuSZEpKt5UQfrQ:1577685351489&ei=Z5EJXtC6HYCDr7wP--WR0AY&start=0&sa=N&filter=0&ved=2ahUKEwiQisX319zmAhWAwYsBHftyBGo4KBDy0wN6BAgMEC0&biw=2133&bih=1022')
driver.get('https://www.google.com/search?q=經濟攬炒&sxsrf=ACYBGNS45CdSmhH1-1jbB233nBVRVw0ZbQ:1577934065351&filter=0&biw=2133&bih=1076')

for page in range(1,50):
    for title in range(1,15):
        try:
            url = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[%s]/div/div/div[1]/a[1]'%str(title)).get_attribute('href')
            print('url: ',url)
            url_text = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[%s]/div/div/div[1]/a[1]/h3'%str(title)).text
            print('url_text: ',url_text)
            time.sleep(1)
            google_writer.writerow([str(url_text),str(url)])
            print('index :',title)
        except NoSuchElementException:
            pass
        except LookupError:
            pass
    try:
        next_page = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[5]/div/span[1]/div/table/tbody/tr/td[11]/a').click()
    except:
        next_page = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[5]/div/span[1]/div/table/tbody/tr/td[10]/a').click()

# click the reveal button
#driver.get('https://www.google.com/search?q=%E6%94%AC%E7%82%92&filter=0&biw=929&bih=889') # https://www.google.com/search?q=攬炒&filter=0&biw=929&bih=889
for page in range(1,150):
    for title in range(1,15):
        try:
            url = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[%s]/div/div/div[1]/a[1]'%str(title)).get_attribute('href')
            print('url: ',url)
            url_text = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[%s]/div/div/div[1]/a[1]/h3'%str(title)).text
            print('url_text: ',url_text)
            time.sleep(1)
            google_writer.writerow([str(url_text),str(url)])
            print('index :',title)
        except NoSuchElementException:
            pass
        except LookupError:
            pass
    try:
        next_page = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[5]/div/span[1]/div/table/tbody/tr/td[12]/a').click()
    except:
        try:
            next_page = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[5]/div/span[1]/div/table/tbody/tr/td[12]/a').click()
        except:
            pass





# =============================================================================
# 
# /html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/div[1]/a[1]
# /html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/a[1]
# 
# 
# /html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/a[1]/h3
# /html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/div[1]/a[1]/h3
# 
# /html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[5]/div/span[1]/div/table/tbody/tr/td[11]/a
# 
# =============================================================================
