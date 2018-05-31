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

""" OMDB API
apikey=removed
i=imdb ID
t=movie title
type=movie,series,episode
y=year of release
plot=short, full
r=json,xml
callback=jsonp callback name
v=

s=search movie title

http://www.omdbapi.com/?apikey=[yourkey]&t=[title]
http://img.omdbapi.com/?apikey=[yourkey]&
"""




import requests, bs4
import json




headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

#############################
#RT="https://www.rottentomatoes.com/browse/in-theaters/"
#res=requests.get(RT,headers=headers)
#res.raise_for_status()
#soup=bs4.BeautifulSoup(res.text,"lxml")
#
##Doesn't work - data in json file
#movieTitles=soup.select(".middle_col a")
#rtRatings=soup.select(".tMeterScore")
#
#############################
#TT=[]
#for k in range(len(theaters)):
#    res2=requests.get(theaters[k],headers=headers)
#    res2.raise_for_status()
#    soup2=bs4.BeautifulSoup(res2.text,"lxml")
#    
#    
#    times=soup2.select(".buttonticket")
#    titles=soup2.select(".media-heading")
#    
#    media=[]
#    for x in range(len(titles)):
#        media.append(titles[x].select("a"))
#        
#    theaterTitles=[]
#    for x in range(0,len(media),2):
#        try:
#            theaterTitles.append(media[x][0].text[50:-46])
#        except IndexError:
#            pass
#    TT.append(theaterTitles)
#
#uniqueTitles=list(set([item for sublist in TT for item in sublist]))

#######################
apikey="removed"

def getRatings(movieData):
    try:
        ratingsData=movieData["Ratings"]
        ratings=[]
        #for x in range(len(ratings)):
        for x in range(len(ratingsData)):
            if ratingsData[x]["Source"]=='Internet Movie Database':
                ratings.append(float(ratingsData[x]["Value"][0:-3])*10)
            elif ratingsData[x]["Source"]=='Rotten Tomatoes':
                ratings.append(float(ratingsData[x]["Value"][0:-1]))
            elif ratingsData[x]["Source"]=='Metacritic':
                ratings.append(float(ratingsData[x]["Value"][0:-4]))
        averageRating=round(sum(ratings)/len(ratings),1)
        print(movieTitle,averageRating)
    except:
        print(movieTitle,"N/A")


for k in uniqueTitles:
    movieTitle=k
    res=requests.get("http://www.omdbapi.com/?apikey=%s&t=%s" % (apikey, movieTitle))
    res.raise_for_status()
    movieData=json.loads(res.text)
    
    getRatings(movieData)
