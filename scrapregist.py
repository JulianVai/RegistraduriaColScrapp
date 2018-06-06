# Script that will download all the E14 Files from.
#URL : https://visor.e14digitalizacion.com/

from urllib.request import urlretrieve

url = 'https://visor.e14digitalizacion.com/e14_divulgacion/01/001/001/PRE/3028012_E14_PRE_X_01_001_001_XX_01_030_X_XXX.pdf'
#url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'


def urlget(url):

    urlretrieve(url, '3028012_E14_PRE_X_01_001_001_XX_01_030_X_XXX.pdf')

def main():
    urlget(url)

if __name__ == '__main__':
    main()
