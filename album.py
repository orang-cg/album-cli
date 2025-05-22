#!/Users/charlie/Documents/Programming/Python/album-cli/bin/python3

#TODO: Find a suitable low-weight Music Player for local playing
#TODO: Find a suitable library for local playing
#TODO: Add TUI/CLI Interface
#TODO: Add commented part in config to specify Spotify ClientID, Secret, and URI
#TODO: Add list function, to list Artists from artist.config and if you type and artist, list their available albums

#NOTE: 'album status' will allow the visibility of the length of the song/what the song is

#=======================================================================================================

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
parser.add_argument('-s', '--spotify')
parser.add_argument('-l', '--local')
args : str = parser.parse_args()

global artist
global current

def mode():
    if args.spotify == "-s" or args.spotify == "--spotify":
        spotify()
    elif args.local == "-l" or args.local == "--local":
        local()
    # Default Option Below
    else:
        spotify()

#=======================================================================================================

def artist():
    artist : str = args.artist

    with open('artists.config','r') as artistList:
        for line in artistList:
            if artist in line:
                with open('current.song','r') as current:
                    if artist == current.read():
                        status()
                    else:
                        with open('current.song','w') as current:
                            current.write(artist)
                        return
            #else:
                #FIX: Count the amount of lines in the artist list and for line in artist list in range
            #    sys.exit()

            
    return

def album():
    listMode : bool = False
    album : str = args.album
    searchTerm = fr"{args.album}=([^\s]+)"

    if album == "":
        list()

    with open('albums.config','r') as albumList:
        for line in albumList:
            if album in line:
                match = re.search(searchTerm, line)
                if match:
                    global albumID
                    albumID = match.group(1)  # This is the value after the '='
    return

def status():
    #FIX: This should open TUI in finished product. Temporarily exits to stop errors
    album : str = args.album
    if album == "status":
        sys.exit()
    else:
        return

def list():
    print("Available " + artist + "albums:")
    
    searchTerm = fr"{args.artist}="#FIX: Need to figure out how to search for everything between , and ,

    with open('albums.config','r') as albumList:
        for line in albumList:
            if artist in line:
                match = re.search()

#=======================================================================================================

def local():
    artist()
    album()
    #FIX: See previous message
    #if artist != artistList:
    #   options() 

    #NOW PLAY WITH PLAYER
    sys.exit()

def spotify():
    #HACK: Temporarily hiding artist just so it works
    #artist()
    album()

    sp.start_playback(context_uri=albumID)
    sys.exit()

if __name__ == '__main__':
    mode()
