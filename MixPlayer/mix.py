#!/usr/bin/env python3

#import lib
import click # display text  Animation
import requests
from bs4 import BeautifulSoup
import sys
import os
import wget
from urlextract import URLExtract
import json
from urllib.request import urlopen
from inscriptis import get_text # get text for BeautifulSoup
import argparse # beta get argparse for python Soon
import vlc # for play and stream music mp3 and link
from time import sleep


#welcome to Mix this mix for play muisc stream in termianl linux


#server download music form radio javan
url_download = "https://host1.rj-mw1.com/media/mp3/mp3-256/" # url stream
url_download_2 = "https://host2.rj-mw1.com/media/mp3/mp3-256/" # url stream
extractor = URLExtract()



# TODO: add argument to programm optional
parser = argparse.ArgumentParser(description="Mix player is a program to stream & download & play music")
parser.add_argument("fa_or_en", type=str, help=" - select music fa or en")
parser.add_argument("name", type=str, help=" - get name artist")
parser.add_argument("famle", type=str, help=" - get last name artist")
parser.add_argument('-d',"--download" , help=" - download muisc", action="store_true")
args = parser.parse_args()



#choice muisc fa or en
choise_en_or_fa = args.fa_or_en

#def music irani get muisc radio javan
def music_fa():
    name_artist = args.name
    famle_artist = args.famle
    url = "https://www.radiojavan.com/search?query="+name_artist+"+"+famle_artist
    url_req = requests.get(url).text
    soup = BeautifulSoup(url_req, "lxml")
    soup_name_artist = soup.find("span", class_="artist_name")
    soup_name_track = soup.find("span", class_="song_name")
    soup_img = soup.find("img")

    get_txt_name = get_text(str(soup_name_artist))
    get_txt_track = get_text(str(soup_name_track))
    get_txt_name = get_txt_name.replace(" ", "-")
    get_txt_track = get_txt_track.replace(" ", "-")
    url_ext = url_download+get_txt_name+"-"+get_txt_track+".mp3"
    url_ext_2 = url_download_2+get_txt_name+"-"+get_txt_track+".mp3"
    url_ext_2 = url_ext_2.replace("-&", "")
    url_ext = url_ext.replace("-&", "")


    #show play list track artist




    try:
        #checkd url steram found or not found!
        u = urlopen(url_ext_2).readline()
        if u == b'Not found':
            if args.download:
                print("download done!")
                wget.download(url_ext)
                sys.exit()
            msg_player = "Mix Player\n"
            msg = " start play music "
            rows, columns = os.popen('stty size', 'r').read().split() # get size terminal
            x = msg.center(int(columns))
            y = msg_player.center(int(columns))
            os.system("clear")
            click.echo(click.style(y, blink=True, bold=True, fg="red"))
            click.echo(click.style(x, blink=True, bold=True, fg="red"))
            name  = "\n\n\nartist: "+get_txt_name
            track = "\ntrack: "+get_txt_track
            click.echo(click.style(name, bold=True,fg="reset",))
            click.echo(click.style(track, bold=True,fg="reset"))
            p_2 = vlc.MediaPlayer(url_ext)
            p_2.play()
            sleep(240) # sleep for play muisc
           


        else:
            if args.download:
                    wget.download(url_ext_2)
                    print("download done!")
                    sys.exit()
            img_url = extractor.find_urls(str(soup_img))
            for img in img_url:
                global img_show
                img_show = img
            msg_player = "------------Mix Player-----------\n"
            msg = " start play music  \n\n"
            rows, columns = os.popen('stty size', 'r').read().split()
            x = msg.center(int(columns))
            y = msg_player.center(int(columns))
            os.system("clear")
            click.echo(click.style(y, blink=True, bold=True,fg="red"))
            click.echo(click.style(x, blink=True, bold=True,fg="red"))
            name  = "\n\n\nartist: "+get_txt_name
            track = "\ntrack: "+get_txt_track
            # os.system("tiv -h 50 -w 50 "+ img_show)
            click.echo(click.style(name, bold=True,fg="reset"))
            click.echo(click.style(track, bold=True,fg="reset"))
            soup_name_track_all = soup.find_all("span", class_="song_name")
            j = 0
            for i in soup_name_track_all:
                global playlist_arti
                global playlist_artist_2
                get_txt_track_all = get_text(str(i))
                get_txt_track_all = get_txt_track_all.replace(" ", "-")
                all_tk = get_txt_track_all.center(int(columns))
                j = j+1
                print("\n\n",j,"-")
                click.echo(click.style(all_tk, bold=True,fg="reset"))
                

                #play list
                # playlist_all_1 = url_ext = url_download+get_txt_name+"-"+get_txt_track_all+".mp3"
                # playlist_all = url_ext_2 = url_download_2+get_txt_name+"-"+get_txt_track_all+".mp3"
                # playlist_artist = playlist_all
                # playlist_artist_2 = playlist_all_1
                # playlist = []
                # playlist = playlist.append(playlist_artist_2,playlist_artist)
                # vlc.MediaPlayer(playlist[])

                
            p = vlc.MediaPlayer(url_ext_2) # strt stream muisc
            p.play()
            sleep(240)





    except BaseException:
        os.system("clear")
        print("Exit Mix Player")


#get music en Soon
def music_en():# play muisc en
    name_artist = str(sys.argv[2])
    url_download = "https://online.freemusicdownloads.world/results?search="+name_artist # add name to link
    print(url_download)

#run
def main():
    if choise_en_or_fa == "fa":
            music_fa()
    if choise_en_or_fa == "en":
        print("Sorry This option is being completed!")


if __name__ == "__main__":
   main()