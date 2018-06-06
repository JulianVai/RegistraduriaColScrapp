# Intentandolo con el paquete request.

# Import the packages.
from urllib.request import urlopen, Request

# Assign the url.
#url = 'https://visor.e14digitalizacion.com/e14_divulgacion/01/001/001/PRE/8371010_E14_PRE_X_01_001_001_XX_01_001_X_XXX.pdf'
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

def main(url):
    # Package the request.
    request = Request(url)

    # Send The request and catches the response 
    response = urlopen(request)

    # Print the datatype of response
    print(type(response))

if __name__ == '__main__':
    main(url)
