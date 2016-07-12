import requests
from bs4 import BeautifulSoup
from datetime import date
import calendar
from lxml import html
import re
import urllib.request
import json


class Spider:

        url = "http://www.cnn.com"
        user_agent = {'User-agent': 'Chrome/51.0.2704.103'}
        source_code = requests.get(url, headers=user_agent)
        tree = html.fromstring(source_code.content)


        date_today = date.today()
        print()
        print("Headlines for " + calendar.day_name[date_today.weekday()] + " {:%B %d, %Y}".format(date_today) + ":\n")


        # Non-working (does not print out headlines or links) as of 7/8/16 - Soup is pulling in articles in what looks to be json object
        # format - commenting out until sure of issue

        url = 'http://www.cnn.com/'
        user_agent = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        source_code = requests.get(url, headers=user_agent)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        # Arrays for headline links, titles, and another all-inclusive array for the remaining links on the page
        link = []
        title = []
        all_links = []
        time_stamps = []
        for item in soup.findAll(attrs={'data-vr-contentbox': True}):
            link.append("http://www.cnn.com" + item.get('data-vr-contentbox'))

        for item in soup.findAll('span', {'class': 'cd__headline-text'}):

            title.append(item.text)

        for item in soup.findAll('a'):
            all_links.append("http://www.cnn.com" + item.get('href'))

        # Find a way to match up timestamps
        '''for item in soup.findAll('div', {'class': 'cd__timestamp'}):
            time_stamps.append(item.text)

            for i in range(0, len(time_stamps)):
                print(time_stamps[i])'''

        for i in range(0, len(title)):
            print(title[i] + " | Link: " + link[i])

        #for i in range(0, len(all_links)):
         #   print(all_links[i])

        # TODO
            # Add to file if title not in file
            # If title not in file, follow link => check paragraph (pref 3rd/4th) against all paragraphs
                #If match, delete headline (already read about it)
                #If link has been in file for more than 3 days, delete(old news)
                    #If no match, add to file of headlines_to_be_read
                    #pull img from page to use as thumbnail for headline?
            # If title in file, toss b/c duplicate
            """"""
