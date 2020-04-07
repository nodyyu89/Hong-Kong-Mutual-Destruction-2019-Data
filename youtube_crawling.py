# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 09:32:57 2019

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


#driver.get("https://lihkg.com/profile/216907")
#//*[@id="leftPanel"]/div[2]/div[2]/div[1]/div[2]/div/a[1]
SCROLL_PAUSE_TIME = 0.5

base_path = r'C:\Users\yunod\OneDrive\桌面\old pc 20190908\complex network 2018\2019\complex network modeling\policy network n political computation\hk_research_20191126'
excel = open(base_path+'\youtube'+'20200218攬炒_all_tag_fried_time.csv', mode='w', errors='ignored',newline='',encoding='utf-8-sig')  # gb18030  utf-8-sig
youtube_writer = csv.writer(excel, delimiter=',') # , errors='ignored'
youtube_writer.writerow(['poster','subscriber','date','tag','title','description_text','like_no','dislike_no','view_no','review_test','review like_no','review dislike no'])
# 攬炒 暴力

options = webdriver.ChromeOptions()
#driver.set_page_load_timeout(7)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#options.add_argument("--headless") 
driver = webdriver.Chrome(base_path+'\chromedriver.exe',chrome_options=options)
 # ('炒巴', 0.06778148513543551)
driver.get('https://www.youtube.com/results?search_query=攬炒') 
result_output = []

for video in range(1,100):
    try:
        print('1')
        video_item = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[%s]/div[1]/ytd-thumbnail/a'%str(video))
        video_url = video_item.get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to_window(driver.window_handles[1])
        driver.get(video_url)
        print('video_url',video_url)
    except:
        print('2')
        height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(1)
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(3)
        try:
            print('3')
            video_item = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[%s]/div[1]/ytd-thumbnail/a'%str(video))
            video_url = video_item.get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to_window(driver.window_handles[1])
            driver.get(video_url)
            print('video_url',video_url)
        except:
            print('4')
            pass

    try:
        print('5')
        display_btn = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/paper-button[2]')
        driver.execute_script("arguments[0].click();", display_btn)
        time.sleep(1)
        display_text = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/div/div/yt-formatted-string').text
        like_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-formatted-string').text
        unlike_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-formatted-string').text
        title = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string').text
        date = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[2]/yt-formatted-string').text
        view_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/yt-view-count-renderer/span[1]').text
        poster = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/div[2]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a').text
        subscriber = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/div[2]/ytd-video-owner-renderer/div[1]/yt-formatted-string').text
        print('display_text',display_text)
        print('like_no',like_no)
        print('unlike_no',unlike_no)
        print('title',title)
        print('date',date)
        print('view_no',view_no)
        print('poster',poster)
        print('subscriber',subscriber)
        time.sleep(2)

    except:
        ('missing')
    review_text_list = []
    review_text = ''
    for review in range(1,500):
        print('6')
        try:
            print('7')
            review_text = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%s]/ytd-comment-renderer/div[1]/div[2]/ytd-expander/div/yt-formatted-string[2]'%str(review))
            review_like_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%s]/ytd-comment-renderer/div[1]/div[2]/ytd-comment-action-buttons-renderer/div[1]/span[2]'%str(review))
            #/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[2]/ytd-comment-renderer/div[1]/div[2]/ytd-comment-action-buttons-renderer/div[1]/span[2]
            #/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[3]/ytd-comment-renderer/div[1]/div[2]/ytd-comment-action-buttons-renderer/div[1]/span[2]
            #/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[17]/ytd-comment-renderer/div[2]/div[2]/ytd-comment-action-buttons-renderer/div[1]/div[2]
            review_text = review_text.text
            review_like_no = review_like_no.text
            print(review,review_text,review_like_no)
            try:
                view_reply_btn = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%s]/div/ytd-comment-replies-renderer/div[1]/ytd-button-renderer[1]/a/paper-button/yt-formatted-string'%str(review)).click()
                try:
                    for reply in range(1,15): 
                        print('8.1')
                        #/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[28]/div/ytd-comment-replies-renderer/div[1]/div/div[1]/ytd-comment-renderer[1]/div[2]/div[2]/ytd-expander/div/yt-formatted-string[2]
# =============================================================================
                except:
                    print('no reply')
            except:
                pass
# =============================================================================
#/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[30]/div/ytd-comment-replies-renderer/div[1]/ytd-button-renderer[1]/a/paper-button/yt-formatted-string
#/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[28]/div/ytd-comment-replies-renderer/div[1]/ytd-button-renderer[1]/a/paper-button

                    #/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[26]/div/ytd-comment-replies-renderer/div[1]/ytd-button-renderer[1]/a/paper-button/yt-formatted-string
            try:
                print('8')
                youtube_writer.writerow([poster,subscriber,date,'攬炒',title,display_text,like_no,unlike_no,view_no,review_text,review_like_no,'review dislike no'])
                result_output.append([poster,subscriber,date,'攬炒',title,display_text,like_no,unlike_no,view_no,review_text,review_like_no,'review dislike no'])
                print('result_output',result_output)
            except:
                print('9')
                pass
        except:
            print('10')
            height = driver.execute_script("return document.body.scrollHeight")
            time.sleep(3)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            print('scrolling',review)
            review_text_list.append(review_text)
            print('review_text_list',review_text_list)
        if len(review_text_list) > 5:
            print('11')
            if review_text_list[-1] == review_text_list[-2]:
                break
    #driver.back()
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(2)






# =============================================================================
# 
# 
# 
# display_btn = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/paper-button[2]/yt-formatted-string')
# display_btn.click()
# display_text = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/div/div/yt-formatted-string').text
# like_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-formatted-string').text
# unlike_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-formatted-string').text
# title = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string').text
# date = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[2]/yt-formatted-string').text
# view_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/yt-view-count-renderer/span[1]').text
# 
# for review in range(1,1000):
#     try:
#         display_btn = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/paper-button[2]/yt-formatted-string')
#         display_btn.click()
#         display_text = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[9]/div[3]/ytd-video-secondary-info-renderer/div/ytd-expander/div/div/yt-formatted-string').text
#         like_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-formatted-string').text
#         unlike_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-formatted-string').text
#         title = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string').text
#         date = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[2]/yt-formatted-string').text
#         view_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[1]/div[1]/yt-view-count-renderer/span[1]').text
#     except:
#         ('missing')
#     try:
#         review_text = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%s]/ytd-comment-renderer/div[2]/div[2]/ytd-expander/div/yt-formatted-string[2]'%str(review))
#         review_like_no = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%s]/ytd-comment-renderer/div[2]/div[2]/ytd-comment-action-buttons-renderer/div[1]/span[2]'%str(review))
#         review_text = review_text.text
#         review_like_no = review_like_no.text
#         print(review_text,review_like_no)
#     except:
#         height = driver.execute_script("return document.body.scrollHeight")
#         time.sleep(1)
#         driver.find_element_by_tag_name('body').send_keys(Keys.END)
#     driver.back()
# # =============================================================================
# #     driver.execute_script("window.scrollTo(0, 1200);")
# #         new_height = driver.execute_script("return document.body.scrollHeight")
# #         if new_height == last_height:
# #             break
# #         last_height = new_height
# # =============================================================================
# 
# /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[1]/ytd-comment-renderer/div[2]/div[2]/ytd-expander/div/yt-formatted-string[2]
# /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[2]/ytd-comment-renderer/div[2]/div[2]/ytd-expander/div/yt-formatted-string[2]
# /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[3]/ytd-comment-renderer/div[2]/div[2]/ytd-expander/div/yt-formatted-string[2]
# 
# /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[3]/ytd-comment-renderer/div[2]/div[2]/ytd-comment-action-buttons-renderer/div[1]/span[2]
# 
# 
# =============================================================================


