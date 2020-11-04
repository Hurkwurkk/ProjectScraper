from bs4 import BeautifulSoup as bs
import requests

#For this webscrap, we will use BBC for a news source
r1 = requests.get('https://www.bbc.com/news/world/us_and_canada'); #insert a URL we want to use
page = r1.content

SOUP_1 = bs(page, 'html.parser')

#The Whole HTML element
ARTICLE_HIGHLIGHT = SOUP_1.find_all('li' , class_='lx-stream__post-container placeholder-animation-finished') #This only applies to the very first Article!
ARTICLE_OTHER = SOUP_1.find_all('li' , class_='lx-stream__post-container')

#Parts of the HTML (REFERENCES)
#ARTICLE_TITLE = SOUP_1.find_all('span' , class_='lx-stream-post__header-text gs-u-align-middle')
#ARTICLE_SUMMARY = SOUP_1.find_all('p' , class_='lx-media-asset-summary qa-map-summary gel-pica')
#ARTICLE_LINK = SOUP_1.find_all('a' , class_='qa-heading-link lx-stream-post__header-link')

for post in ARTICLE_HIGHLIGHT :
    ARTICLE_TITLE = SOUP_1.find('span' , class_='lx-stream-post__header-text gs-u-align-middle')
    ARTICLE_TITLE_SUMMARY = SOUP_1.find('p' , class_='lx-stream-related-story--summary qa-story-summary')
    ARTICLE_LINK = SOUP_1.find('a' , class_='qa-heading-link lx-stream-post__header-link')['href']
    print(ARTICLE_TITLE.text)
    print(f"SUMMARY : {ARTICLE_TITLE_SUMMARY.text}")
    print(f"bbc.com{ARTICLE_LINK}")
print() #Spaces out the other Articles

for post2 in ARTICLE_OTHER :
    #ARTICLE_TITLE_2 = SOUP_1.find_all('span' , class_='lx-stream-post__header-text gs-u-align-middle')
    post2.extend(SOUP_1.find_all('span' , class_='lx-stream-post__header-text gs-u-align-middle'))
    print(post2.text)
