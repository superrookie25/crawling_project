from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

driver = webdriver.Chrome('/Users/jaemin/PycharmProjects/crawling_project/chromedriver')
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

a=['워너원 강다니엘', '엑소 백현', '박보검', '송중기', '워너원 황민현', '엑소 시우민', '강동원', '이종석', '이준기', '마동석', '조진웅', '조세호', '안재홍', '윤두준', '이민기', '김우빈', '육성재', '공유', '방탄소년단 정국', '아이콘 바비', '워너원 박지훈', '엑소 수호']

for i in a:
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
    elem = driver.find_element_by_name("q")
    keyword=elem.send_keys(i)
    elem.send_keys(Keys.RETURN)
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    count = 1

    folder='./'+i
    if not os.path.isdir(folder) :
        os.mkdir(folder)

    for image in images:
        try:
            image.click()
            time.sleep(1)
            imgUrl=(driver.find_element_by_css_selector('.n3VNCb').get_attribute("src"))
            urllib.request.urlretrieve(imgUrl,f''+folder+'/'+ str(count)+".jpg")
            count += 1
            if count == 5:
                break;
        except:
            break

driver.close()

