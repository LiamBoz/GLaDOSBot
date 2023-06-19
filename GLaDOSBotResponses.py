import random, re, requests
from  bs4 import BeautifulSoup

cat_pics = []

def getdata(url):
    r = requests.get(url)
    return r.text

cathtmldata = getdata("https://www.google.com/search?rlz=1C1CHBF_enUS918US918&sxsrf=APwXEdck3FTAWb3DAumXX-Y1KN-CGQODCg:1686717665928&q=cats&tbm=isch&sa=X&ved=2ahUKEwjPlcH6-MH_AhXDEVkFHYUiCuYQ0pQJegQICBAB&biw=1920&bih=1007&dpr=1")

CatSoup = BeautifulSoup(cathtmldata, 'html.parser')

for item in CatSoup.find_all('img'):
    cat_pics.append(item['src'])

def handle_response(message):

    if message == '/cat':
        return random.choice(cat_pics)
