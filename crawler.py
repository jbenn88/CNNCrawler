import requests
from bs4 import BeautifulSoup


class Spider:
        url = 'http://www.cnn.com/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        # Methods that have worked
        ''' links = soup.find_all('a')
         for link in links:
            print("<a href='%s'>%s</a>" % (link.get("href"), link.text))
        #
        index = 0
        while index <= 10:
            print(soup.find('article', {'class': 'cd cd--card cd--article cd--idx-' + str(index) + ' cd--extra-small '
                                        'cd--has-siblings cd--media__image cd--time-recent'}).find('a').text)
            index += 1
        #
        for item in soup.findAll('a', attrs={'class': None}):
            print("http://www.cnn.com" + item.get('href'))'''

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

        for i in range(0, len(all_links)):
            print(all_links[i])

        # TODO
            # Add to file if title not in file
            # If title not in file, follow link => check paragraph (pref 3rd/4th) against all paragraphs
                #If match, delete headline (already read about it)
                #If link has been in file for more than 3 days, delete(old news)
                    #If no match, add to file of headlines_to_be_read
                    #pull img from page to use as thumbnail for headline?
            # If title in file, toss b/c duplicate
