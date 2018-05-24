"""
Century HB
https://www.showtimes.com/movie-theaters/century-huntington-beach-and-xd-10452/

UA Long Beach
https://www.showtimes.com/movie-theaters/ua-long-beach-6-5799/

Regal Garden Grove Stadium 16
https://www.showtimes.com/movie-theaters/regal-garden-grove-stadium-16-12127/

Edwards Westpark 8
https://www.showtimes.com/movie-theaters/edwards-westpark-8-5789/

AMC Orange 30
https://www.showtimes.com/movie-theaters/amc-orange-30-amc-block-30-8723/

RT Top Box Office
https://www.rottentomatoes.com/browse/in-theaters/

"""

theaters=["https://www.showtimes.com/movie-theaters/century-huntington-beach-and-xd-10452/",
          "https://www.showtimes.com/movie-theaters/ua-long-beach-6-5799/",
          "https://www.showtimes.com/movie-theaters/regal-garden-grove-stadium-16-12127/",
          "https://www.showtimes.com/movie-theaters/edwards-westpark-8-5789/",
          "https://www.showtimes.com/movie-theaters/amc-orange-30-amc-block-30-8723/",          
        ]



import requests, bs4

RT="https://www.rottentomatoes.com/browse/in-theaters/"


headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
res=requests.get(RT,headers=headers)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"lxml")

#Doesn't work - data in json file
movieTitles=soup.select(".middle_col a")
rtRatings=soup.select(".tMeterScore")

TT=[]
for k in range(len(theaters)):
    res2=requests.get(theaters[k],headers=headers)
    res2.raise_for_status()
    soup2=bs4.BeautifulSoup(res2.text,"lxml")
    
    
    times=soup2.select(".buttonticket")
    titles=soup2.select(".media-heading")
    
    media=[]
    for x in range(len(titles)):
        media.append(titles[x].select("a"))
        
    theaterTitles=[]
    for x in range(0,len(media),2):
        try:
            theaterTitles.append(media[x][0].text[50:-46])
        except IndexError:
            pass
    TT.append(theaterTitles)