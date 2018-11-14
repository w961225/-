# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import bs4 as bs
import requests
import pandas as pd
import os

path = r'D:\C Disk Transfer\Destop\


get = download
put = upload
del
list = show

#Define function to download a list of S&P 500 companies with ticker and company name
def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    #resp.text will show all the source code
    #resp show the information for the page
    soup = bs.BeautifulSoup(resp.text,'lxml')
    #soup can understand the text as a html file
    table = soup.find('table',{'class':'wikitable sortable'})
    tickers = [] #save tickers column here
    securities = [] #save securities column here
    sectors = [] #save sectors column here
    row = table.findAll('tr')[1]
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        # show regular expression and ignore the html code
        security = row.findAll('td')[1].text
        sector = row.findAll('td')[3].text
        tickers.append(ticker)
        securities.append(security)
        sectors.append(sector)
    df = pd.DataFrame('ticker': tickers,)
    df_new