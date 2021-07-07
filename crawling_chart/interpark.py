from json.decoder import JSONDecodeError
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc
import platform
import matplotlib.pyplot as plt
import json
import re

class EMPinter:
    def craw_data(self, page_num):
        main_url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube" 
        browser = webdriver.Chrome("C:/driver/chromedriver")
        browser.get(main_url)
        browser.implicitly_wait(3)
        try:
            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')
            channel_list = soup.select('form > table > tbody > tr')
            results = []
            for page in range(1,3):
            
                url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page={page}" 
                browser.get(url)
                time.sleep(2)
                html = browser.page_source
                soup = BeautifulSoup(html, 'html.parser')
                channel_list = soup.select('form > table > tbody > tr')
                for channel in channel_list:
                    title = channel.select('h1 > a')[0].text.strip() 
                    category = channel.select('p.category')[0].text.strip()
                    subscriber = channel.select('.subscriber_cnt')[0].text 
                    view = channel.select('.view_cnt')[0].text
                    video = channel.select('.video_cnt')[0].text
                    data = [title, category, subscriber, view, video]
                    results.append(data)
            browser.implicitly_wait(10)
            df = pd.DataFrame(results)
            df.columns = ['title', 'category', 'subscriber', 'view', 'video']
            df.to_excel('C:/202105_lab/08.Crawling/middle_2/files/youtube_rank.xlsx', index = False)
            browser.close()
            asdf = "크롤링완료"
            print(asdf)
        except Exception as e:
            print("페이지 파싱에러", e)
        finally:
            time.sleep(3)

        return asdf

    def excl_data(self, page_num):
        try:
            
        
            df = pd.read_excel('C:/202105_lab/08.Crawling/middle_2/files/youtube_rank.xlsx')
            print(df.head())
            df = df.head() #데이터10개만
            df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
            df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
            pivot_df = df.pivot_table(index = 'category', values = 'replaced_subscriber', aggfunc = ['sum','count'])
            pivot_df.columns = ['subscriber_sum', 'category_count']
            pivot_df = pivot_df.reset_index()
            pivot_df = pivot_df.sort_values(by='subscriber_sum', ascending=False)
            print("asdasd")
            plt.figure(figsize = (30,10))
            plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['category'], autopct='%1.1f%%')
            columns = ['title','category','subscriber', 'view', 'video', 'replaced_subscriber']
            # print(df)
            js = df.to_json(orient = 'records', force_ascii=False) # pandas형식을json으로 한글파일 안깨지게
            # print(js)
            
            
        except Exception as e:
            print("페이지 파싱에러", e)
        finally:
            time.sleep(3)
            
        return js  


    def chart_data(self, chart_num):
        try:
            
            # 저장과 불러오기둘다 절대경로를 사용해서 오류뜨면서 안될거임
            df = pd.read_excel('C:/202105_lab/08.Crawling/middle_2/files/youtube_rank.xlsx')
            # print(chart_num)
            chart_num = int(chart_num) # str타입이라 int타입으로 변경
            # print(type(chart_num))
            df = df[0:chart_num]
            
            df['sub'] = df['subscriber'].str.replace('만', '')
            df['sub'] = df['sub'].astype('int') #int 타입 변경을 위해서 '만' 제거후 변경 

            df = df[['title','sub']]
            print(df) # 그래프작성에 필요한자료 2개만 가져오기
            
            chdf = df.to_json(orient = 'records', force_ascii=False) # pandas형식을json으로 한글파일 안깨지게


            
        except Exception as e:
            print("페이지 파싱에러", e)
        finally:
            time.sleep(3)
            
        return chdf 

    