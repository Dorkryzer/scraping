from bs4 import BeautifulSoup
import bs4
import requests



if __name__ == '__main__':
    players_list = [212709014,70388657,84584373]
    heightest = ['',0]

    def kill_comparer(lister):
        global heightest
        for player in lister:
            url ='https://www.dotabuff.com/players/'+ str(player)+'/records'
            header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
            result = requests.get(url,headers=header)
            doc = BeautifulSoup(result.text,"html.parser")
            article = doc.find_all('div',class_='value')
            ans = int(article[1].text)
            name = doc.find('div',class_='header-content-title').text[:-7] 
            print(f'{name} has a record of {ans} kills in one match')
            if int(ans) > heightest[1]:
                heightest = [name,ans]
            
    kill_comparer(players_list)
    print(f'{heightest[0]} has the most above all with {heightest[1]}')
    
    