# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:08:00 2019

@author: yunod
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:44:14 2019

@author: Yu Ho Kwan
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:56:40 2019

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

# =============================================================================
# 
# #driver.get("https://lihkg.com/profile/216907")
# #//*[@id="leftPanel"]/div[2]/div[2]/div[1]/div[2]/div/a[1]
# SCROLL_PAUSE_TIME = 0.5
# 
# base_path = r'C:\Users\Yu Ho Kwan\Desktop\hk gov research'
# excel = open(base_path+'\lihkg'+'20191211_all_fried_date.csv', mode='w', newline='', errors='ignored',encoding='utf-8-sig')  # gb18030  utf-8-sig
# lihkg_writer = csv.writer(excel, delimiter=',')
# lihkg_writer.writerow(['poster','date','tag','page_url','topic_title','topic_like_score','topic_unlike_score','like_no','unlike_no','text'])
# # 攬炒 暴力
# 
# driver = webdriver.Chrome(base_path+'\chromedriver.exe')
# #driver.get("https://lihkg.com/profile/216907")https://lihkg.com/search?q=%E6%94%AC%E7%82%92&type=desc_create_time
# driver.get('https://lihkg.com/search?q=攬炒&type=desc_create_time')# desc_create_time
# windows = driver.window_handles
# time.sleep(3)
# main_window = driver.current_window_handle
# 
# for i in range(1,10000):
#     try:
#         #main_window = driver.current_window_handle
#         driver.switch_to.window(main_window)
#         wait_topic = WebDriverWait(driver, 3)
#         time.sleep(2)
#         topic = wait_topic.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="leftPanel"]/div[2]/div[%s]/div[1]/div[2]/div'%str(i))))
#            #next_page_btn = driver.find_element_by_xpath('//*[@id="page-%s"]/div[3]'%str(page_no))
#         topic_url =  wait_topic.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="leftPanel"]/div[2]/div[%s]/div[1]/div[2]/div/a[1]'%str(i)))).get_attribute('href')
#         print(topic_url)
#         
#         # Open a new window
#         driver.execute_script("window.open('');")
# # Switch to the new window and open URL B
#         driver.switch_to.window(driver.window_handles[-1])
#         driver.get(topic_url)
# # …Do something here
#         print("Current Page Title is : %s" %driver.title)
# 
# 
# #driver.get("https://lihkg.com/profile/216907")
# #//*[@id="leftPanel"]/div[2]/div[2]/div[1]/div[2]/div/a[1]
# SCROLL_PAUSE_TIME = 0.5
# =============================================================================

base_path = r'C:\Users\yunod\OneDrive\桌面\old pc 20190908\complex network 2018\2019\complex network modeling\policy network n political computation\hk_research_20191126'
excel = open(base_path+'\hkdiscuss'+'201912230900big5.csv', mode='a+', newline='', errors='ignored',encoding='utf-8-sig')  # gb18030  #utf-8-sig #big5
hkdiscuss_writer = csv.writer(excel, delimiter=',')
hkdiscuss_writer.writerow(['poster','date','tag','page_url','topic_title','topic viewed','topic response','text'])
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
driver.get('https://www.discuss.com.hk/search.php?searchsubmit=true&srchtxt=攬炒&orderby=dateline&page=1')
base_url = 'https://www.discuss.com.hk/search.php?searchsubmit=true&srchtxt=攬炒&orderby=dateline&page=1'
#try:
for page in range(1,50):
    try:
        input_title_page = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/div[7]/div/div/kbd/input')
        input_title_page.send_keys(str(page))
        input_title_page.send_keys(Keys.RETURN)
        time.sleep(4)
        driver.execute_script("window.stop();")
    except:
        current_url_list = base_url.split('page=')
        #current_url_list2 = current_url_list[1].split('&')[1]
        page_one_url = current_url_list[0] + 'page=%s'%str(page)#+current_url_list2
        driver.get(page_one_url)
        time.sleep(2)
        driver.execute_script("window.stop();")
    for i in range(1,19):
        #https://www.discuss.com.hk/viewthread.php?tid=28463967&feedback=0&num=1
        if len(driver.window_handles)>3:  # closing extra tab
            for i in range(0,len(driver.window_handles)-1):
                driver.switch_to.window(driver.window_handles[1]) 
                driver.close()
            driver.switch_to.window(driver.window_handles[0]) 
        try:
            driver.set_page_load_timeout(5)
            title = driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[2]/span/a'%str(i))
            #/html/body/table[1]/tbody/tr/td/div/div/div[5]/table/tbody/tr[1]/td[2]/span
            title_url = driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[2]/span/a'%str(i)).get_attribute('href')
            title_text = title.text
            print(title.text)
            print(title_url)
            
            title_response,title_viewed = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[5]'%str(i)).text.split(' / ')
            print('title_viewed,title_response',title_viewed,title_response)
            viewed = title_viewed
            response = title_response
            #if int(response)< 15:
                #break
            
    # =============================================================================
    #         driver.execute_script("window.open('');")
    #         time.sleep(1)
    #     # Switch to the new window
    #         driver.switch_to.window(driver.window_handles[1])
    #         driver.get(title_url)
    # =============================================================================
            
            driver.execute_script("arguments[0].click();", title)
                #title.click()
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
        except TimeoutException:
            print('time out')
            driver.execute_script("window.stop();")
            #driver.close()
            #driver.switch_to.window(driver.window_handles[0])
        except NoSuchElementException: # NoSuchElementException
            pass
        

             
        
        
# =============================================================================
#         
#         try:
#         #try:/html/body/table[1]/tbody/tr/td/div/div/div[5]/table/tbody/tr[19]/td[2]/span/a
#             title = driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[2]/span'%str(i))
#             #/html/body/table[1]/tbody/tr/td/div/div/div[5]/table/tbody/tr[1]/td[2]/span
#             title_url = driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[2]/span/a'%str(i)).get_attribute('href')
#             title_text = title.text
#             print(title.text)
#             print(title_url)
#             
#             title_response,title_viewed = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[5]'%str(i)).text.split(' / ')
#             print('title_viewed,title_response',title_viewed,title_response)
#             viewed = title_viewed
#             response = title_response
#             #if int(response)< 15:
#                 #break
#             
#     # =============================================================================
#     #         driver.execute_script("window.open('');")
#     #         time.sleep(1)
#     #     # Switch to the new window
#     #         driver.switch_to.window(driver.window_handles[1])
#     #         driver.get(title_url)
#     # =============================================================================
#             
#             title.click()
#             time.sleep(2)
#             driver.switch_to.window(driver.window_handles[1])
#         except NoSuchElementException:
#             continue
#         
#         except ElementClickInterceptedException:
#             title = driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[2]/span/a'%str(i))
#             #/html/body/table[1]/tbody/tr/td/div/div/div[5]/table/tbody/tr[1]/td[2]/span
#             title_url = driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[2]/span/a'%str(i)).get_attribute('href')
#             title_text = title.text
#             print(title.text)
#             print(title_url)
#             
#             title_response,title_viewed = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[5]'%str(i)).text.split(' / ')
#             print('title_viewed,title_response',title_viewed,title_response)
#             viewed = title_viewed
#             response = title_response
# =============================================================================
            #if int(response)< 15:
                #break
            
    # =============================================================================
    #         driver.execute_script("window.open('');")
    #         time.sleep(1)
    #     # Switch to the new window
    #         driver.switch_to.window(driver.window_handles[1])
    #         driver.get(title_url)
    # =============================================================================

#==============================================================================
#             try:
#                 current_url = driver.current_url
#                 current_url_list = current_url.split('page=')
#                 current_url_list2 = current_url_list[1].split('&')[1]
#             except IndexError:
#                 pass
#             
#             
#             try:
#                 input_page = driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div[6]/div[2]/kbd/input')
#                 input_page.send_keys('1')
#                 input_page.send_keys(Keys.RETURN)
#                 time.sleep(2)
#             except NoSuchElementException:
#                 try:
#                     input_page = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/div[7]/div[2]/div/kbd[1]/input')
#                     input_page.send_keys('1')
#                     input_page.send_keys(Keys.RETURN)
#                     time.sleep(2)
#                 except NoSuchElementException:
#                     try:
#                         current_url = driver.current_url
#                         current_url_list = current_url.split('page=')
#                         current_url_list2 = current_url_list[1].split('&')[1]
#                         page_one_url = current_url_list[0] + 'page=1'+current_url_list2
#                         driver.get(page_one_url)
#                         time.sleep(2)
#                     except IndexError:
#                         pass
# 
# 
#==============================================================================
            
# =============================================================================
#             try:
#                 viewed = driver.find_element_by_xpath('//*[@id="viewthread-number"]/ul/li[1]').text
#                 response = driver.find_element_by_xpath('//*[@id="viewthread-number"]/ul/li[2]').text
#             except NoSuchElementException:
#                 viewed = driver.find_element_by_xpath('//*[@id="mainbox-container-id"]/form/div[1]/div[2]/div[1]/ul/li[1]').text
#                 response = driver.find_element_by_xpath('//*[@id="mainbox-container-id"]/form/div[1]/div[2]/div[1]/ul/li[2]').text
#                 
# =============================================================================
            
            #//*[@id="postorig_511578792"]
            #//*[@id="postorig_511578800"]
            #/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[4]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
            #/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[3]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
    # =============================================================================
    #         /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[1]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span
    #         /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[4]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
    #         /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[6]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
    # =============================================================================
            
    
#==============================================================================
#             try:
#                 last_page =  driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/div[7]/div[2]/div/a[6]').text.split(' ')[1]
#             except NoSuchElementException or IndexError:
#                 try:
#                 #/html/body/table[1]/tbody/tr/td/div/div/div[6]/div[2]/div/a[6]
#                     last_page =  driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div/div[6]/div[2]/div/a[6]').text
#                 except NoSuchElementException:
#                     last_page = int(int(title_response)/15)+1
#==============================================================================


            
            last_page = int(int(title_response)/15)+1
            if last_page == 1:
                last_page = 2
            for one_page in range(1,int(last_page)):
                print('one_page',one_page)
                
                try:
                    input_page = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div[6]/div[2]/kbd/input')
                    input_page.send_keys(one_page)
                    input_page.send_keys(Keys.RETURN)
                    print('changing 1') 
                except NoSuchElementException:
                    try:
                        input_page = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div[7]/div[2]/kbd/input')
                        input_page.send_keys(one_page)
                        input_page.send_keys(Keys.RETURN)
                        print('changing two')
                    except:
                        try:
                            input_page = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/div[6]/div[2]/div/a[2]')
                            input_page.click()
                        except:
                            pass
#==============================================================================
#                 try:
#                     print('one_page',one_page)
#                     last_height = driver.execute_script("return document.body.scrollHeight")
#                     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#                     print('changing next page')
#                     current_url = driver.current_url
#                     current_url_list = current_url.split('page=')
#                     current_url_list2 = current_url_list[1].split('pid')[1]
#                     next_page_url = current_url_list[0] + 'page=%s'%str(one_page)+'&pid'+current_url_list2
#                     print(next_page_url)
#                     #driver.set_page_load_timeout(30)
#                     driver.get(next_page_url)
#                     time.sleep(5)
#                     driver.execute_script("window.stop();")
#                     print(191)
#                 except TimeoutException:
#                     driver.refresh()
#                     time.sleep(5)
#                     driver.execute_script("window.stop();")
# 
#                     print('refreshed')
#                     
#==============================================================================
#==============================================================================
#                 try:
#                     last_height = driver.execute_script("return document.body.scrollHeight")
#                     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#                     print('changing next page')
#                     current_url = driver.current_url
#                     current_url_list = current_url.split('page=')
#                     current_url_list2 = current_url_list[1].split('&')[1]
#                     next_page_url = current_url_list[0] + 'page=%s'%str(one_page)+current_url_list2
#                     driver.get(next_page_url)
#                     time.sleep(2)
#                     print(191)
#                 except IndexError or NoSuchElementException:
#                     pass
#==============================================================================
                
#==============================================================================
#                 try:
#                     input_page = driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div[7]/div[2]/kbd/input')
#                     input_page.send_keys(one_page)
#                     input_page.send_keys(Keys.RETURN)
#                     print(199)
#                     #finally_text_list = []
#                 except  NoSuchElementException:
#                     print('changing next page')
#                     current_url = driver.current_url
#                     current_url_list = current_url.split('page=')
#                     current_url_list2 = current_url_list[1].split('&')[1]
#                     next_page_url = current_url_list[0] + 'page=%s'%str(one_page)+current_url_list2
#                     driver.get(next_page_url)
#                     time.sleep(2)
#                     print(207)
#==============================================================================








# =============================================================================
#                     try:
#                         input_page = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/div[6]/div[2]/div/kbd[1]/input')
#                     except NoSuchElementException:
#                          input_page = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div[7]/div[2]/kbd/input')
#                          except NoSuchElementException:
# =============================================================================
                    #current_url = driver.current_url
# =============================================================================
#                     page_index = current_url.index('page=')
#                     driver.get(current_url[0:page_index] + str(one_page))
# =============================================================================
                except:
                    print('stop loading')                        
                    driver.execute_script("window.stop();")
                    print('stopped')
                for text_index in range(1,17):
                    finally_text = ''
                    text = ''
                    text2 = ''
                    text3 = ''
                    text4 = ''
                    text5 = ''
                    text6 = ''
                    post_created_time1 = ''
                    post_created_time2 = ''
                    post_created_time3 = ''
                    poster1 = ''
                    poster2 = ''
                    finally_post_created_time = ''
                    finally_poster = ''
                    date_builder = ''
                    try:
                        text = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span'%str(text_index)).text
                    except NoSuchElementException:
                        print('text except',text)
                    try:
                        text2 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span'%str(text_index)).text
                    except NoSuchElementException:
                        print('text2 except',text2)
                    try:
                        text3 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span'%str(text_index)).text
                    except NoSuchElementException:
                        print('text3 except',text3)
                    try:
                        text4 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span'%str(text_index)).text
                    except NoSuchElementException:
                        print('text4 except',text4)
     
                        #text2 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span'%str(text_index)).text
                        #text3 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[3]/table/tbody/tr[1]/td[%s]/div[3]/div[3]/span'%str(text_index)).text
                        #text4 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span').text
                    #print('text try',text)
                    #print('text2 try',text2)
                    #print('text3 try',text3)
                    #print('text4 try',text4)
    # =============================================================================
    #                 except NoSuchElementException:
    #                     print('text except',text)
    #                     print('text2 except',text2)
    #                     pass
    # =============================================================================
                    if text != '':
                       finally_text = text
                    elif text2 != '':
                       finally_text = text2
                    elif text3 != '':
                        finally_text = text3
                    elif text4 != '':
                        finally_text = text4
                    print('finally_text',finally_text)
                    try:
                        poster1 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[%s]/table/tbody/tr[1]/td[1]/cite/a'%str(text_index)).text
                        #print('poster1 name',poster1)
                    except NoSuchElementException:
                        pass
                        #print('poster1 name passed')
                    try:
                        poster2 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[%s]/table/tbody/tr[1]/td[1]/div[2]/div[1]/a'%str(text_index)).text
                        #print('poster2 name',poster2)
                    except NoSuchElementException:
                        pass
                        #print('poster2 name passed')                    
    # =============================================================================
    #                 try:        
    #                     post_created_time1 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[1]'%str(text_index))
    #                     driver.execute_script("arguments[0].scrollIntoView();", post_created_time1)
    #                     date_builder = ActionChains(driver)
    #                     time.sleep(2)
    #                     date_builder.move_to_element(post_created_time1).click().perform()
    #                     time.sleep(2)
    #                     print('post_created_time1',post_created_time1.text)
    #                 except NoSuchElementException or StaleElementReferenceException:
    #                     print('post_created_time1 passed')
    # =============================================================================
                    try:
                        post_created_time2 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[1]/div/div[1]/div[2]'%str(text_index))
                        driver.execute_script("arguments[0].scrollIntoView();", post_created_time2)
                        date_builder = ActionChains(driver)
                        time.sleep(1)
                        date_builder.move_to_element(post_created_time2).click().perform()
                        time.sleep(1)
                        #print('poster created time2',post_created_time2.text)
                    except NoSuchElementException:
# =============================================================================
                        try:
                            post_created_time3 = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[1]'%str(text_index)).text
                        except:
                            pass
# =============================================================================
                        #/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[3]/table/tbody/tr[1]/td[2]/div[1]
                        #print('post_created_time2 passed')
                    except  StaleElementReferenceException:
                        pass
                         #print('post_created_time2 passed StaleElementReferenceException')
                       
                    if poster1 != '':
                        finally_poster = poster1
                    elif poster2 != '':
                        finally_poster = poster2
    # =============================================================================
    #                 elif post_created_time1 != '':
    #                     finally_post_created_time = post_created_time1.text
    #                 elif post_created_time2 != '':
    #                     finally_post_created_time = post_created_time2.text                    
    # =============================================================================
                    if poster1 != '':
                        finally_post_created_time = post_created_time2
                    elif poster2 != '':
                        finally_post_created_time = post_created_time3
                    #finally_post_created_time = post_created_time2
                    print('finally_poster',finally_poster)
                    print('finally_post_created_time',finally_post_created_time)
                        
                    #finally_text_list.append(finally_text)
                    print('writing one row')
                    try:
                        hkdiscuss_writer.writerow([finally_poster,finally_post_created_time,'攬炒',title_url,title_text,viewed,response,finally_text])
    # 攬炒          
                    except LookupError:
                        print('LookupError')
                        pass
                    #time.sleep(2)
            if len(driver.window_handles) == 2:
                driver.switch_to.window(driver.window_handles[1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
# =============================================================================
# except NoSuchElementException:
#      print('end')
#      pass       
# =============================================================================
                    
#==============================================================================
#                     
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
#                 
# date = driver.find_element_by_xpath('//*[@id="table-pid511644990"]/tbody/tr[1]/td[2]/div[1]/div/div[1]/div[2]')
# date_builder = ActionChains(driver)
# date_builder.move_to_element(date).click().perform()
# date.text
# date = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[10]/table/tbody/tr[1]/td[2]/div[1]/div/div[1]/div[2]')
# date_builder = None
# date_builder = ActionChains(driver)
# date_builder.move_to_element(date).click().perform()
# date.text
# 
# 
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[14]/table/tbody/tr[1]/td[2]/div[1]/div/div[1]/div[2]
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[15]/table/tbody/tr[1]/td[2]/div[1]/div/div[1]/div[2]
# 
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[3]/table/tbody/tr[1]/td[2]/div[1]/div/div[1]/div[2]
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[6]/table/tbody/tr[1]/td[2]/div[1]/div/div[1]/div[2]
# 
# driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[3]/table/tbody/tr[1]/td[2]/div[1]/div/div[1]/div[2]')
# driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[4]/table/tbody/tr[1]/td[2]/div[1]/div/div[1]/div[2]/span').text
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[1]/table/tbody/tr[1]/td[1]/div[2]/div[1]/a
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[3]/table/tbody/tr[1]/td[1]/div[2]/div[1]/a
#         #change page
#             
#     
#             #/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[1]
#             
#  //*[@id="table-pid511578441"]/tbody/tr[1]/td[1]/cite/a
# /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[3]/table/tbody/tr[1]/td[1]/cite/a
# /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[4]/table/tbody/tr[1]/td[1]/cite/a
# /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[1]/table/tbody/tr[1]/td[1]/cite/a
# /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[3]/table/tbody/tr[1]/td[1]/cite/a
# /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/div[2]/div[2]/a[6]
# 
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[10]/table/tbody/tr[1]/td[2]/div[3]/div[3]
# 
# 
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[1]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[3]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[4]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[5]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[6]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[7]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[8]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[10]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[11]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[12]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[14]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
# /html/body/table[1]/tbody/tr/td/div/div/table/tbody/tr/td[1]/div[1]/form/div[15]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
# 
# # =============================================================================
# #                     text = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[%s]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span'%str(text_index)).text
# #                     print('5',text)
# #                 except NoSuchElementException:
# #                     print('passed')
# # =============================================================================
# 
#                 
#         print(viewed)
#         print(response)
#         
#         
#         /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[1]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span
#         /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[14]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span
#         /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[15]/table/tbody/tr[1]/td[2]/div[3]/div[3]/span
#         /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[14]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span
#         /html/body/table[1]/tbody/tr/td/div/table/tbody/tr/td[1]/form/div[20]/table/tbody/tr[1]/td[2]/div[3]/div[5]/span
#         
#         print(title)
#     except NoSuchElementException:
#         title = driver.find_element_by_xpath('//*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[%s]/td[2]/span/a/span'%str(i))
#         print(title.text)
#         print('except')
# windows = driver.window_handles
# time.sleep(3)
# 
# 
# 
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[2]/td[2]/span/a/span
# 
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[1]/td[2]/span/a
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[1]/td[2]/span
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[2]/td[2]/span
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[19]/td[2]/span
# 
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[19]/td[2]/span
# 
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[7]/div/div/kbd/input
# 
# https://www.discuss.com.hk/search.php?searchsubmit=true&srchtxt=%E6%94%AC%E7%82%92&orderby=dateline&page=1
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[3]/td[2]/span
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[2]/td[2]/span/a/span
# 
# 
# 
# 
# 
# //*[@id="mainbody"]/tbody/tr/td/div/div/div[5]/table/tbody/tr[19]/td[2]/span/a/span
#==============================================================================


