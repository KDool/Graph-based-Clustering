import datetime
from selenium import webdriver
from multiprocessing import Process
import time
import re
import pandas as pd
import os
import csv
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
import multiprocessing
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

URL = "https://www.youtube.com/c/DomainofScience"
DRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service('/usr/local/bin/chromedriver')


def crawlSingleUrl(url_profile=None,channel_id=None):
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.set_page_load_timeout(20)
    url = url_profile + '/channels?view=56'
    driver.get(url)
    list_result=[]
    #Scroll down scrollbar
    while True:
        scroll_height = 2000
        document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
        time.sleep(1.5)
        document_height_after = driver.execute_script("return document.documentElement.scrollHeight")
        if document_height_after == document_height_before:
            break
            
    elems = driver.find_elements_by_css_selector(".style-scope ytd-grid-channel-renderer [href]")
    links = [elem.get_attribute('href') for elem in elems]
    # list_channels = driver.find_elements_by_xpath('//div[@id="channel-info"]/a')
    list_channels = driver.find_elements_by_xpath('//span[@id="title"]')
    list_subscribers = driver.find_elements_by_xpath('//span[@id="thumbnail-attribution"]')
    number_of_channels = len(links)
    print('Length: ',number_of_channels)
    if number_of_channels < 1:
        temp={}
        temp['channel_id'] = channel_id
        temp['related_channel'] = ''
        temp ['subscriber'] = ''
        temp['link'] = ''
        list_result.append(temp)
    for i in range(number_of_channels):
        # print(links[i])
        # print(list_channels[i].text)
        # print(list_subscribers[i].text)
        if list_subscribers[i].text != '':
            sub = list_subscribers[i].text[:-12]
        else:
            sub = list_subscribers[i].text
        id_cut = links[i].split('/')[-1]
        temp={}
        temp['channel_id'] = channel_id
        temp['related_channel'] = list_channels[i].text
        temp ['subscriber'] = sub
        temp['user-channelid'] = id_cut
        list_result.append(temp)
    driver.close()
    return list_result

def readUrlProfileCSV(path_csv=None,row_start=None,row_end=None):
    df = pd.read_csv(path_csv,usecols={'channel_id','profile_url'},index_col=False)
    # print(df)
    df_result = df[row_start:row_end]
    # print(df_result)
    return df_result

def countNumberOfProfile(path_csv=None):
    df = pd.read_csv(path_csv,usecols={'channel_id','profile_url'},index_col=False)
    number_profiles = len(df)
    return number_profiles
def crawlMultipleUrls(path_csv=None,start=None,end=None,path_result=None):
    df_start = readUrlProfileCSV(path_csv,start,end)
    # list_temp = [] 
    result=[]
    for index, row in df_start.iterrows():
        # print(index,row['channel_id'], row['profile_url'])    
        result= result + crawlSingleUrl(row['profile_url'],row['channel_id'])
        # print("Get Url error: ",row['profile_url'])
    df_result = pd.DataFrame(result)
    df_result.to_csv(path_result, mode="a", header=False, index=False)

def writeFieldNameToFile(file):
    field_name = []
    field_name.append({'channel_id':'channel_id','related_channel':'related_channel','subscriber':'subscriber','user-channelid':'user-channelid'})
    df = pd.DataFrame(field_name)
    df.to_csv(file, mode="a", header=False, index=False, na_rep="NaN",quoting=csv.QUOTE_ALL)



if __name__ == '__main__':
    numProcess = 1  # number process
    path_dataset = '/Users/vankhaido/HUST/GR2/YoutubeDataset/channels.csv'
    path_result = '/Users/vankhaido/HUST/GR2/YoutubeDataset/result.csv'
    writeFieldNameToFile(path_result)
    # final = countNumberOfProfile(path_dataset)
    final =10
    ### Multiprocessing with Process
    processes = [Process(target=crawlMultipleUrls, args=(path_dataset,i, i + int(final / numProcess),path_result)) for i in
                 range(0, final, int(final / numProcess))]  # init numProcess process
    # Run processes
    for p in processes: p.start()
    # Exit the completed processes
    for p in processes: p.join()
    
# print(countNumberOfProfile('/Users/vankhaido/HUST/GR2/YoutubeDataset/channels.csv'))
# readUrlProfileCSV('/Users/vankhaido/HUST/GR2/YoutubeDataset/channels.csv',0,3)
# crawlMultipleUrls(path_csv='/Users/vankhaido/HUST/GR2/YoutubeDataset/channels.csv',start=1,end=5,path_result='./result.csv')
# x = crawlSingleUrl('http://www.youtube.com/channel/UC2xskkQVFEpLcGFnNSLQY0A')
# print(x)