#!/usr/bin/python3

#
# So this is a simple example of web sraping using requests and BeautifulSoup
#
##############################################################################

from  bs4 import BeautifulSoup
import requests

link_of_pages = [] #array of pages that conaitns  movies


#This function is creat a list of pages in the range of 1 to 10
def ajnabi_list():
    global url

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        i += 0
        url = "http://www.online.dramacafe.in/browse-NonArabicFilms-videos-" + str(i) + "-date.html"
        link_of_pages.append(url) #Add the urls to the array

#This function is to  parse movie's links + its titles and store them in a array
def get_movies_links(page):
    r = requests.get(page)
    soup = BeautifulSoup(r.content, "lxml")
    title = soup.find_all("div", {'class': 'pm-li-video'})
    link_of_movies = [] # array to store movies
    try:
        for link in title:
            link_of_movies.append(str(link.a.get("href") + link.a.string)) #link of movies + its title

    except:
        pass

#Here we generate a text file to store our results
def creat_save_file():
    for lien in link_of_pages:
        movies = []
        update_list = movies.append(get_movies_links(str(lien)))
        print(update_list)
        with open("link_of_movies.txt", 'w+') as f:
            f.write(str(update_list))


ajnabi_list()
creat_save_file()
