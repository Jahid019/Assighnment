#We Have to make a list of dictionaries

from bs4 import BeautifulSoup
import requests

#create a header
headers={'user-agent':'Google Chrome/107.0.5304.89 '}

#request the webpage

request=requests.get('http://www.bbc.com/news', headers=headers )
html=request.content

#create some soup
soup= BeautifulSoup(html,'html.parser')
#Used to easily read html file
#print(soup.prettify())
def bbc_news_scrapper(keyword):
    news_list=[]

    for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
        news_title=h.contents[0].lower()

        if news_title not in news_list:
            if 'bbc' not in news_title:
                news_list.append(news_title)

            
    no_of_news=0
    keyword_list=[]
    #goes through the list and search for the keyword
    for i,title in enumerate(news_list):
        text=''
        if keyword.lower() in title:
            text='--------KEYWORD'
            no_of_news+=1
            keyword_list.append(title)
        print(i+1,':' ,title ) 
    
  
      


bbc_news_scrapper("digital")






