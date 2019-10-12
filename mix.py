#!/usr/bin/env python3

#import lib
import click # display text  Animation
import requests 
from bs4 import BeautifulSoup
import sys
import os
import json 
from urllib.request import urlopen
from inscriptis import get_text # get text for BeautifulSoup 
import argparse # beta get argparse for python Soon
import vlc # for play and stream music mp3 and link
from time import sleep 

#welcome to Mix this mix for play muisc stream in termianl linux 


#server download music form radio javan 
url_download = "https://host1.rj-mw1.com/media/mp3/mp3-256/"
url_download_2 = "https://host2.rj-mw1.com/media/mp3/mp3-256/"


#choice muisc fa or en 
choise_en_or_fa = str(sys.argv[1])

#def music irani get muisc radio javan 
def music_fa():
    name_artist = str(sys.argv[2])
    famle_artist = str(sys.argv[3])
    url = "https://www.radiojavan.com/search?query="+name_artist+"+"+famle_artist
    url_req = requests.get(url).text
    soup = BeautifulSoup(url_req, "lxml")
    soup_name_artist = soup.find("span", class_="artist_name")
    soup_name_track = soup.find("span", class_="song_name")
    get_txt_name = get_text(str(soup_name_artist))
    get_txt_track = get_text(str(soup_name_track))
    get_txt_name = get_txt_name.replace(" ", "-")
    get_txt_track = get_txt_track.replace(" ", "-")
    url_ext = url_download+get_txt_name+"-"+get_txt_track+".mp3"
    url_ext_2 = url_download_2+get_txt_name+"-"+get_txt_track+".mp3"
    url_ext_2 = url_ext_2.replace("-&", "")
    url_ext = url_ext.replace("-&", "")


    #show play list track artist 
    # soup_name_track_all = soup.find_all("span", class_="song_name")
    # for i in soup_name_track_all:
    #     global playlist_arti
    #     global playlist_artist_2
    #     get_txt_track_all = get_text(str(i))
        # print(get_txt_track_all)

    #     get_txt_track_all = get_txt_track_all.replace(" ", "-")
    #     playlist_all_1 = url_ext = url_download+get_txt_name+"-"+get_txt_track_all+".mp3"
    #     playlist_all = url_ext_2 = url_download_2+get_txt_name+"-"+get_txt_track_all+".mp3"
    #     print(playlist_all)
    #     playlist_artist = playlist_all
    #     playlist_artist_2 = playlist_all_1
    
    
    
    try:
        #checkd url steram found or not found!
        u = urlopen(url_ext_2).readline()
        if u == b'Not found':
            msg_player = "Mix Player\n"
            msg = " start play music "
            rows, columns = os.popen('stty size', 'r').read().split() # get size terminal
            x = msg.center(int(columns))
            y = msg_player.center(int(columns))
            os.system("clear")
            click.echo(click.style(y, blink=True, bold=True, fg="red"))
            click.echo(click.style(x, blink=True, bold=True, fg="red"))
            print("artist: ",get_txt_name,"\n", "track: ",get_txt_track)
            p_2 = vlc.MediaPlayer(url_ext)
            p_2.play()
            sleep(240) # sleep for play muisc 

        else: 
            msg_player = "Mix Player\n"
            msg = " start play music "
            rows, columns = os.popen('stty size', 'r').read().split()
            x = msg.center(int(columns))
            y = msg_player.center(int(columns))
            os.system("clear")
            click.echo(click.style(y, blink=True, bold=True,fg="red"))
            click.echo(click.style(x, blink=True, bold=True,fg="red"))
            print("\n\nartist: ",get_txt_name,"\ntrack: ",get_txt_track)
            p = vlc.MediaPlayer(url_ext_2)
            p.play() 
            sleep(240)
        


       

    except BaseException:
        os.system("clear")
        print("Exit Mix")

        
#get music en Soon
def music_en():# play muisc en 
    name_artist = str(sys.argv[2])
    url_download = "https://online.freemusicdownloads.world/results?search="+name_artist # add name to link 
    print(url_download)

#run 
if __name__ == "__main__":
    if choise_en_or_fa == "fa":
        music_fa()
    if choise_en_or_fa == "en":
        music_en()
