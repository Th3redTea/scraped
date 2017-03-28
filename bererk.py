#!/usr/bin/python3

#
# So this is a simple example of web sraping using requests and BeautifulSoup
#
##############################################################################
from urllib import parse
from  bs4 import BeautifulSoup
import requests

link_of_pages = []  # array of pages that conaitns  movies


# This function is creat a list of pages in the range of 1 to 10
def ajnabi_list():
    global url
    global i

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        i += 0
        url = "http://www.online.dramacafe.in/browse-NonArabicFilms-videos-" + str(i) + "-date.html"
        link_of_pages.append(url)  # Add the urls to the array
    for _ in link_of_pages:
        get_movies_links(_)


# This function is to  parse movie's links + its titles and store them in a array
def get_movies_links(site):
    global link_of_movies

    for site in link_of_pages:
        r = requests.get(site) # request the link
        soup = BeautifulSoup(r.content, "lxml") # make a soup of it
        title = soup.find_all("div", {'class': 'pm-li-video'})
        link_of_movies = []  # array to store movies
        for link in title:
            parse.unquote(parse.unquote(link))
            get_it = (link.a.get("href"))  # link of movies
            decod_it = parse.unquote(parse.unquote(get_it))
            link_of_movies.append(decod_it)


# Here we generate a text file to store our results
def creat_save_file():
    f = open('list_of_movie.txt','w+')
    for lien in link_of_movies:
            f.write(str(lien)+ "\n")



ajnabi_list()
creat_save_file()


