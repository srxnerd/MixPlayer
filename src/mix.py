#!/usr/bin/env python3

""" get muisc stream radiojavan """
"""this programm for stream  onlion muisc in terminal """
#import lib
from click import echo , style # display text  Animation
import requests
from bs4 import BeautifulSoup
from sys import exit
from os import  popen , system
from wget import download
from urlextract import URLExtract
from urllib.request import urlopen
from inscriptis import get_text # get text for BeautifulSoup
import argparse # beta get argparse for python Soon
from  vlc import MediaPlayer # for play and stream music mp3 and link
from time import sleep
from memory_profiler import profile
import _thread

#welcome to Mix this mix for play muisc stream in termianl linux

# TODO: autocompalte for name artist

# TODO: add argument to programm optional
parser = argparse.ArgumentParser(description="Mix player is a program to stream & download & play music")
parser.add_argument("-ir","--fa", action="store_true", help=" - select music fa or en")
parser.add_argument("-e","--en", action="store_true", help=" - select music fa or en")
parser.add_argument("-n","--n", type=str, help=" - get name artist")
parser.add_argument("-f","--f", type=str, help=" - get last name artist", default= " ")
parser.add_argument("-t","--track", type=str, help=" - get track name artist", default= " ")
parser.add_argument('-d',"--download" , help=" - download muisc", action="store_true")
parser.add_argument('-g',"--get" , help=" - get artist", action="store_true")
# parser.add_argument('-p',"--playlist" , help=" - get playlist", action="store_true")
parser.add_argument("--ser", type=str, help=" - artist searcher")
args = parser.parse_args()

#choice muisc fa or en
# choise_en_or_fa = args.fa


@profile
def Browser_artist():
    """    serach name artist  """
    browser_artist_char = args.ser
    url_radio_javan = "https://www.radiojavan.com/mp3s/browse/artists/"+browser_artist_char
    url_Browsers = requests.get(url_radio_javan).text
    soup = BeautifulSoup(url_Browsers, "lxml")
    data_Browser = soup.find_all("span", class_="artist")
    for item_browser in data_Browser:
        get_txt = get_text(str(item_browser))
        print(get_txt)

#server download music form radio javan
url_download = "https://host1.rj-mw1.com/media/mp3/mp3-256/" # url stream
url_download_2 = "https://host2.rj-mw1.com/media/mp3/mp3-256/" # url stream
url_download_3 = "https://host1.rj-mw1.com/media/mp3/"


extractor = URLExtract()
#def music irani get muisc radio javan
def music_fa():
    """this def for get music fa"""
    name_artist = args.n
    famle_artist = args.f
    track_name_artist = args.track
    url = "https://www.radiojavan.com/search?query="+name_artist+"+"+famle_artist+"+"+track_name_artist
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
    url_ext_3 = url_download_3+get_txt_name+"-"+get_txt_track+".mp3"
    url_ext_3 = url_ext_3.replace("-&", "")
    url_ext_2 = url_ext_2.replace("-&", "")
    url_ext = url_ext.replace("-&", "")
    

    #show play list track artist




    try:
        #checkd url steram found or not found!
        u = urlopen(url_ext_2).readline()
        if u == b'Not found':
            if args.download:
                print("download done!")
                download(url_ext)
                exit()
            msg_player = "Mix Player\n"
            msg = " start play music "
            rows, columns = popen('stty size', 'r').read().split() # get size terminal
            msg_x = msg.center(int(columns))
            msg_y = msg_player.center(int(columns))
            system("clear")
            echo(style(msg_y, blink=True, bold=True, fg="red"))
            echo(style(msg_x, blink=True, bold=True, fg="red"))
            name = "\n\n\nartist: "+get_txt_name
            track = "\ntrack: "+get_txt_track
            echo(style(name, bold=True,fg="reset",))
            echo(style(track, bold=True,fg="reset"))
            soup_name_track_all = soup.find_all("span", class_="song_name")
            j = 0
            Music5 = " - - -  - - 5 New music - - - - - "
            Music5 = Music5.center(int(columns))
            echo(style(Music5, bold=True,fg="reset"))
            track_5 = soup_name_track_all[0:5]
            for i in track_5:
                global playlist_arti
                global playlist_artist_2
                get_txt_track_all = get_text(str(i))
                get_txt_track_all = get_txt_track_all.replace(" ", "-")
                all_tk = get_txt_track_all.center(int(columns))
                j = j+1
                print("\n\n",j,"-")
                echo(style(all_tk, bold=True,fg="reset"))
            MediaPlay2 = MediaPlayer(url_ext)
            MediaPlay2.play()
            sleep(240) # sleep for play muisc
           
        else:
            if args.download:
                    download(url_ext_2)
                    print("download done!")
                    exit()
            msg_player = "------------Mix Player-----------\n"
            msg = " start play music  \n\n"
            rows, columns = popen('stty size', 'r').read().split()
            
            msg_x = msg.center(int(columns))
            msg_y = msg_player.center(int(columns))
            system("clear")
            echo(style(msg_y, blink=True, bold=True,fg="red"))
            echo(style(msg_x, blink=True, bold=True,fg="red"))
            name  = "\n\n\nartist: "+get_txt_name
            track = "\ntrack: "+get_txt_track
            echo(style(name, bold=True,fg="reset"))
            echo(style(track, bold=True,fg="reset"))
            soup_name_track_all = soup.find_all("span", class_="song_name")
            j = 0
            Music5 = " - - -  - - 5 New music - - - - - "
            Music5 = Music5.center(int(columns))
            echo(style(Music5, bold=True,fg="reset"))
            track_5 = soup_name_track_all[0:5]
            for i in track_5:
                global playlist_arti
                global playlist_artist_2
                get_txt_track_all = get_text(str(i))
                get_txt_track_all = get_txt_track_all.replace(" ", "-")
                all_tk = get_txt_track_all.center(int(columns))
                j = j+1
                print("\n\n",j,"-")
                echo(style(all_tk, bold=True,fg="reset"))
            MediaPlay = MediaPlayer(url_ext_2) # strt stream muisc
            MediaPlay.play()
            sleep(240)
        
    
            # def PlaylistArtist():
                # for track_in_playlist in soup_name_track_all:
                    # playlists = get_text(str(track_in_playlist))
                    # print(playlists)





    except BaseException:
        system("clear")
        print("Exit Mix Player")


#get music en Soon
def music_en():# play muisc en
    """this def for get music en"""
    print("update")
    # name_artist = str(sys.argv[2])
    # url_download = "https://online.freemusicdownloads.world/results?search="+name_artist # add name to link
    # print(url_download)

#run
def main():
    if args.fa:
        music_fa()
    if args.en:
       music_en()
    if args.get:
        Browser_artist()
    # if choise_en_or_fa == "en":
        # print("Sorry This option is being completed!")



if __name__ == "__main__":
   main()