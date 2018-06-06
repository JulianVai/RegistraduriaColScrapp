# Ahora intentamos con el módulo requests únicamente.
# Y vamos a imprimir los 'href' que encontremos dentro de la página.

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

    # Find the 'a' tags (hyperlinks) : a_tags
    a_tags = soup.find_all('a')

    # Print the URLs to the shell
    for link in a_tags:
        print(link.get('href'))

if __name__ == '__main__':
    main(url)