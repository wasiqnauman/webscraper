from bs4 import BeautifulSoup
import requests


def scrape(url, count):
    """
    @param url of bookstore page and starting index for the count
    scrapes the book title and price
    prints it and continues to next page till it exists
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')  # common class for all books
    for i in items:
        names = i.find('h3')  # title of the book is contained in h3
        name = names.find('a').get('title')  # get name from title attribute
        price = i.find('p', class_='price_color').text.strip('Â')  # clean the string
        print(f'{count}) {name}: {price}')
        count += 1

    next = soup.find('li', class_='next')
    if next is not None:  # check if there is a next page
        nextpage = next.find('a').get('href')  # get url of next page from the href attribute
        newUrl = url[0:36] + nextpage
        scrape(newUrl, count)  # scrape the next page recursively

def main():
    scrape('http://books.toscrape.com/catalogue/page-1.html', 1)


if __name__ == '__main__': main()
