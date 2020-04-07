# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:59:52 2019

@author: yunod
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:49:04 2019

@author: alex.yu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:53:24 2019

@author: Yu Ho Kwan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:13:01 2019

@author: Yu Ho Kwan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:58:58 2019

@author: yunod
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:22:38 2019

@author: yunod
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 18:23:28 2019

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
excel = open(base_path+'\lihkg'+'201912192100_all_tag_fried_time.csv', mode='w', errors='ignored',newline='',encoding='utf-8-sig')  # gb18030  utf-8-sig
lihkg_writer = csv.writer(excel, delimiter=',') # , errors='ignored'
lihkg_writer.writerow(['poster','date','tag','page_url','topic_title','topic_like_score','topic_unlike_score','like_no','unlike_no','text'])
# 攬炒 暴力

options = webdriver.ChromeOptions()
#driver.set_page_load_timeout(7)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#options.add_argument("--headless") 
driver = webdriver.Chrome(base_path+'\chromedriver.exe',chrome_options=options)
 # ('炒巴', 0.06778148513543551)
keywords = """
('勇武', 0.013962275752024808)
('戰線', 0.011077556632166644)
('手足', 0.03063759599248665)
('獨立', 0.009542053732658396)
('支那', 0.008982912261999302)
('愛狗', 0.008993659839976879)
('831', 0.008116229611686452)
('TG', 0.008225908390222756)
('文宣', 0.007986756130428081)
('藍絲', 0.007896872054613846)
('經濟攬', 0.007348478161932328)
('經濟圈', 0.006251690376569294)
('裝修', 0.006361369155105598)
('制裁', 0.004876335369589717)
('推爆', 0.0048258662555973495)
('popo', 0.0048258662555973495)
('革命', 0.004824175677342704)
('被捕', 0.004711174885214315)
('缺一不可', 0.004558197391499844)
('抄巴', 0.004387151141452136)
('藍店', 0.004277472362915833)
('台灣', 0.004387151141452136)
('大灣區', 0.004277472362915833)
('敵人', 0.004277472362915833)
('杯葛', 0.004208539262335088)
('毒果', 0.0045845503921116285)
('黑衣', 0.0044836810574459705)
('人權', 0.0037491127453563463)
('失業', 0.0037283994152715045)
('五毛', 0.002960187917348076)
('出聲', 0.0041677935843795295)
('破壞', 0.0041677935843795295)
('condom', 0.0041677935843795295)
('民意', 0.004075215372313621)
('反抗', 0.0036073508088324564)
('左膠', 0.003509720913161709)
('三罷', 0.0034000421346254057)
('襯黃店', 0.003180684577552799)
('黨鐵', 0.003180684577552799)
('自殺', 0.0030710057990164952)
('調查', 0.002961327020480192)
('區選議會', 0.002961327020480192)
('區議會', 0.002961327020480192)
('蘋果', 0.0028516482419438886)
('強姦', 0.0027419694634075852)
('眾籌', 0.0027419694634075852)
('罷買', 0.0027419694634075852)
('星火', 0.00270587250239454)
('大學', 0.002632290684871282)
('高質', 0.002632290684871282)
('港豬', 0.0025226119063349785)
('癱瘓', 0.0024129331277986748)
('焦土', 0.0023041428471017814)
('支那人', 0.002360988015545239)
"""
keywords = keywords.split('\n')
keywords = [x for x in keywords if x!='']
key_word_list = []
for i in keywords:
    code = 'string ='+i
    exec(code)
    key_word_list.append(string)
key_word_list = [x[0] for x in key_word_list]
#driver.get("https://lihkg.com/profile/216907")https://lihkg.com/search?q=%E6%94%AC%E7%82%92&type=desc_create_time
for keywords in key_word_list:
    driver.get('https://lihkg.com/search?q=%s&type=desc_create_time'%keywords)# desc_create_time  # score
    windows = driver.window_handles
    time.sleep(3)
    main_window = driver.current_window_handle
    
    for i in range(1,150):
        try:
            #main_window = driver.current_window_handle
            driver.switch_to.window(driver.window_handles[0])
            wait_topic = WebDriverWait(driver, 3)
            time.sleep(2)
            topic = wait_topic.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="leftPanel"]/div[2]/div[%s]/div[1]/div[2]/div'%str(i))))
               #next_page_btn = driver.find_element_by_xpath('//*[@id="page-%s"]/div[3]'%str(page_no))
            topic_url =  wait_topic.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="leftPanel"]/div[2]/div[%s]/div[1]/div[2]/div/a[1]'%str(i)))).get_attribute('href')
            print(topic_url)
            
            # Open a new window
            driver.execute_script("window.open('');")
    # Switch to the new window and open URL B
            driver.switch_to.window(driver.window_handles[1])
            driver.get(topic_url)
    # …Do something here
            print("Current Page Title is : %s" %driver.title)
    
            
            #topic.click()
            #topic = driver.find_element_by_xpath('//*[@id="leftPanel"]/div[2]/div[%s]/div[1]/div[2]/div'%str(i))
           # topic.click()
            time.sleep(3)     
            topic_text = driver.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div[1]/span').text
            topic_like_score = driver.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div[2]/span[3]').get_attribute('data-score')
            topic_unlike_score = driver.find_element_by_xpath('/html/body/div[1]/nav/div[2]/div[2]/span[4]').get_attribute('data-score')
            print(topic_text,topic_like_score,topic_unlike_score)
            time.sleep(1)
            print(1)
            #/html/body/div[1]/nav/div[2]/div[2]/span[3]
        except ElementClickInterceptedException:
                #driver.close()
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    # Switch back to the first tab with URL A
                driver.switch_to_window(driver.window_handles[0])             
                print("Current Page Title is : %s" %driver.title)
                print(2)
    
        except TimeoutException:
                print('1',topic.location)
                driver.execute_script("arguments[0].scrollIntoView();",topic)
                actions = ActionChains(driver)
                actions.move_to_element(topic).perform()
                #driver.execute_script("arguments[0].scrollIntoView(%s);", topic)
                
                 #body = browser.find_element_by_tag_name("body")
                body = driver.find_element_by_css_selector('body')
                body.send_keys(Keys.PAGE_DOWN)
                print(3)
    
    #==============================================================================
    #             topic.click()
    # 
    #             for d in range(0,5):
    #                 topic.send_keys(Keys.PAGE_DOWN)            
    #==============================================================================
                time.sleep(3)
        except NoSuchElementException or StaleElementReferenceException :
    
            print('empty')
            print(4)
            try:
                #topic.location
                driver.execute_script("arguments[0].scrollIntoView();",topic)
                actions = ActionChains(driver)
                actions.move_to_element(topic).perform()
                #driver.execute_script("arguments[0].scrollIntoView(%s);", topic)
                
                 #body = browser.find_element_by_tag_name("body")
                for d in range(0,5):
                    body = driver.find_element_by_css_selector('body')
                    body.send_keys(Keys.PAGE_DOWN)
                    #topic.send_keys(Keys.PAGE_DOWN)            
                time.sleep(3)
                print(4)
            except NoSuchElementException or StaleElementReferenceException:
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')# Switch back to the first tab with URL A
                driver.switch_to_window(driver.window_handles[0])             
                print("Current Page Title is : %s" %driver.title)
                print('finished')
                print(5)
                continue
            except StaleElementReferenceException:
                 time.sleep(2)
                 driver.execute_script("window.close();")
                 time.sleep(2)
                 driver.switch_to_window(driver.window_handles[0])             
                 print("Current Page Title is : %s" %driver.title)
                 continue
                
        
    # =============================================================================
    # //*[@id="leftPanel"]/div[2]/div[1]/div[1]/div[2]/div/a[1]
    # //*[@id="leftPanel"]/div[2]/div[2]/div[1]/div[2]/div/a[1]
    # =============================================================================
        page_no = 1
        while True:
            try:
                #driver.maximize_window()
    # wait for element to appear, then hover it
               wait = WebDriverWait(driver, 5)
               next_page_btn = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="page-%s"]/div[3]'%str(page_no))))
               #next_page_btn = driver.find_element_by_xpath('//*[@id="page-%s"]/div[3]'%str(page_no))
               next_page_btn.click()
               page_no += 1
               time.sleep(2)
               driver.execute_script("arguments[0].scrollIntoView();", next_page_btn)
               print(6)
    
            except NoSuchElementException or StaleElementReferenceException or ElementClickInterceptedException or TimeoutException:
                # Close the tab with URL B
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')# Switch back to the first tab with URL A
    # Switch back to the first tab with URL A
                driver.switch_to_window(driver.window_handles[0])             
                print("Current Page Title is : %s" %driver.title)
                print(7)
                break
            except TimeoutException:
                break
            except ElementClickInterceptedException:
                driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')# Switch back to the first tab with URL A
    # Switch back to the first tab with URL A
                driver.switch_to_window(driver.window_handles[0])             
                print("Current Page Title is : %s" %driver.title)
                print(9)
                break
            if page_no>30:
                print('too much')
                break
    
        for j in range(1,3000):
            #time.sleep(1)
            try:
                print(j)
                user = driver.find_element_by_xpath('//*[@id="%s"]/div/small/span[2]/a'%str(j)).text
                try:
                    like_no = driver.find_element_by_xpath('//*[@id="%s"]/div/div[2]/label[1]'%str(j)).text
                except NoSuchElementException or StaleElementReferenceException or InvalidArgumentException:
                    like_no = ''
                    pass
                try:
                    unlike_no = driver.find_element_by_xpath('//*[@id="%s"]/div/div[2]/label[2]'%str(j)).text
                except NoSuchElementException or StaleElementReferenceException or InvalidArgumentException:
                    unlike_no = ''
                    pass            
                try:
                    date = driver.find_element_by_xpath('//*[@id="%s"]/div/small/span[5]'%str(j)).get_attribute('data-tip')
                except NoSuchElementException or StaleElementReferenceException or InvalidArgumentException:
                    date = ''
                    pass
                user = driver.find_element_by_xpath('//*[@id="%s"]/div/small/span[2]/a'%str(j)).text
                try:
                    content = driver.find_element_by_xpath('//*[@id="%s"]/div/div[1]/div'%str(j)).text
                except NoSuchElementException or StaleElementReferenceException or InvalidArgumentException:
                    content = ''
                #print(user,like_no,unlike_no,date,content)
                #time.sleep(0.5)
                print([str(user),str(date),str(keywords),topic_text,str(like_no),str(unlike_no),str(content)])
                try:
                    lihkg_writer.writerow([str(user),str(date),str(keywords),str(driver.current_url),topic_text,
                                           str(topic_like_score),str(topic_unlike_score),
                                           str(like_no),str(unlike_no),str(content)]) #暴力 攬炒
              
                except LookupError:
                    print('lookuperror')
                    
            except NoSuchElementException or StaleElementReferenceException:
                 print(111)
                 #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')# Switch back to the first tab with URL A
    # Switch back to the first tab with URL A
                 time.sleep(2)
                 driver.execute_script("window.close();")
                 time.sleep(2)
                 driver.switch_to_window(driver.window_handles[0])             
                 print("Current Page Title is : %s" %driver.title)
                 break
 #//*[@id="leftPanel"]/div[2]/div[69]/div[1]/div[2]/div
# =============================================================================
# 【面对挑衅，#怼港示威者内地姑娘说不害怕#】这两天，一个在德国的深圳女孩班雅伦火了：她思路清晰，流利切换三种语言摆事实、讲道理，霸气对峙香港示威者。8日，雅伦在接受采访时表示，尽管面对各种挑衅和侮辱，她在整个过程中“没有感到一点害怕”。 O3种语言怼示威者的内地姑娘雅伦：面对挑衅没感到害怕
# #香港反对派议员朱凯迪被捕# 该来的终归要来！多名香港“煽暴派”议员被拘捕或预约拘捕！
# #香港# 添马公园现场，今晚又不知闹到几点 L无心简影的微博视频
# 【香港实况播报】颜武周，倒计时一下，这货应该快了……
# 
# #黄媒不报我来报##王思聪还能坐私人飞机吗#
# #青岛爆料#【注意！今晚青岛浮山湾畔将上演消防主题灯光秀】今天是全国第29个“119”消防宣传日，青岛市消防救援支队将在11月9日当晚，利用香港中路青岛中心AB楼座和山东路华润中心主楼座的城市灯光秀，播放2019年119消防安全宣传月活动主题：防范火灾风险建设美好家园；以及祝福标语：青岛消防 展开全文c
# 转：这是默克尔接受《明镜周刊》采访时被问到东西德现状比较时的回答。
# #黄之锋申请赴欧被拒##我也支持香港警察#
# 歡迎光臨❤️兩位美女！ @郑希怡 #梁浸浸##金玡居香港店#
# =============================================================================
#//*[@id="pl_feedlist_index"]/div[2]/div/a
# =============================================================================
# //*[@id="pl_feedlist_index"]/div[1]/div[3]/div[2]/div[1]/div[2]/p[2]/a[1]
# //*[@id="pl_feedlist_index"]/div[1]/div[5]/div/div[1]/div[2]/p[2]/a[1]
# //*[@id="pl_feedlist_index"]/div[1]/div[8]/div/div[1]/div[2]/p[2]/a[1]
# =============================================================================



