from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver

result = {}


class Scraper:
    def scrape_google(search_term):
        """
        This calss will perform a search for provided term on Google
        and then provide the links for the first 5 results from Google search.
        :return: List of links of first 5 results.
        :rtype: list
        """
        driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        google_url = "https://www.google.com/search?q={}".format(search_term) + \
                     "&num=" + str(5)
        driver.get(google_url)
        # time.sleep(3)
        driver.implicitly_wait(100)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        result_div = soup.find_all('div', attrs={'class': 'g'})

        links = []
        titles = []
        descriptions = []
        for r in result_div:
            # Checks if each element is present, else, raise exception
            try:
                link = r.find('a', href=True)
                title = None
                title = r.find('h3')

                if isinstance(title, Tag):
                    title = title.get_text()

                description = None
                description = r.find('span', attrs={'class': 'st'})

                if isinstance(description, Tag):
                    description = description.get_text()

                # Check to make sure everything is present before appending
                if link != '' and title != '' and description != '':
                    links.append(link['href'])
                    titles.append(title)
                    descriptions.append(description)
            # Next loop if one element is not present
            except Exception as e:
                print(e)
                continue

        resp = " ".join(str(x) for x in links)
        return resp
