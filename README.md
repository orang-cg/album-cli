# album-cli
A CLI tool which allows you to select music albums (currently heavily in progress)

## Issues ##
Currently I have only got this working on VENV. This is because Spotipy needs to be installed and there is not a package with brew on macOS. Once I get my Linux PC set back up I will fix this.

## Installation ##
Right now there is no package or anything so just download the script and the example configs from the source code. [Spotipy](https://spotipy.readthedocs.io/en/2.25.1/) is required for this script.

Make sure to open the [Spotify Developer Dashboard](https://developer.spotify.com) and create a new app. In here use the Web API and Web Playback API. The Redirect URL can be set to any valid URL/URI (Use 'http://127.0.0.1:9090/' if you are unsure).

Once this is done, in terminal type this:

### macOS or Linux ###

  > export SPOTIPY_CLIENT_ID='your-spotify-client-id'  
  > export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'  
  > export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

Replace the contents of the apostrophes with the Client ID, Client Secret, and Redirect URI respectively
 
## Usage ##
Run the Python Script with Python3.

Commands:
  > -s or --spotify to load through spotify (default)  
  > -l or --local to load through media player (currently unfunctional)

  > artistName (defined in artist.config)

  > albumName (defined in album.config)

I have plans to add other commands which can provide functionality such as wallpaper changes.

