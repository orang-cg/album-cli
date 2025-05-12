#!/usr/bin/env python

#TODO:Find Python tool to utilise Spotify API
#TODO:Find a suitable low-weight Music Player for local playing
#TODO:Add Config
#TODO:Add TUI/CLI Interface

#NOTE:This will work by allowing the user to select Album through terminal commands
#NOTE:e.g. 'album tpab' or 'album kendrick tpab'. The code names will be configurable
#NOTE:'album status' will allow the visibility of the length of the song/what the song is

#NOTE:Potential API's/Libraries = Spotipy

import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import argparse
import re

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

parser = argparse.ArgumentParser(
                    prog='album',
                    description='A CLI tool to select albums locally and through Spotify',
                    epilog='Text at bottom of help')

parser.add_argument('artist')
parser.add_argument('album')
parser.add_argument('-s', '--spotify')#sys.argv[3]
parser.add_argument('-l', '--local')#sys.argv[3]

args : str = parser.parse_args()

def mode():
    if args.spotify == "-s" or args.spotify == "--spotify":
        spotify()
    elif args.local == "-l" or args.local == "--local":
        local()
    # Default Option Below
    else:
        spotify()

def artist():
    artist : str = args.artist

    return

def album():
    listMode : bool = False
    album : str = args.album

    #HACK: MAKE SURE TO USE THIS
    pattern = fr"{args.album}=([^\s]+)"

    if album == "":
        listMode = True

    albumListFile : str = open('albums.config','r')
    for line in albumListFile:
        if album in line:
            match = re.search(pattern, line)
            if match:
                global albumID
                albumID = match.group(1)  # This is the value after the '='
    return

def check():
    artistListFile : str = open('artists.config','r')
    
    #FIX:Find a way to make a new variable per line of code in config (e.g. artistList1, artistList2 etc.)
    artistList : str = artistListFile.read()
    return

#def options():
    #FIX: MAKE THIS A ARGPARSE
    #if artist == "status":
    #    sys.exit()#UI HERE

def help():
    print("album (artist) (album) (-s/--spotify or -l/--local)")
    print("To view status of album, 'album status'")
    sys.exit()

def local():
    artist()
    album()
    check()
    #FIX:See previous message
    #if artist != artistList:
    #   options() 

    #NOW PLAY WITH PLAYER
    sys.exit()

def spotify():
    artist()
    album()
    check()

    sp.start_playback(context_uri=albumID)
    sys.exit()

mode()
