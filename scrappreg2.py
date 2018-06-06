# Ahora intentamos con el módulo requests únicamente.

# Import package
import requests
from bs4 import BeautifulSoup

# Specify the url: url
url = ("https://visor.e14digitalizacion.com/")

def main(url):
    # Packages the request, send the request and catch the response: r
    r = requests.get(url)

    # Extract the response: text
    html_doc = r.text

    # Create a BeautifulSoup object from the HTML: soup
    soup = BeautifulSoup(html_doc)

    # Prettify the BeautifulSoup object: pretty_soup
    pretty_soup = soup.prettify()

    # Print the html
    print(pretty_soup)

if __name__ == '__main__':
    main(url)