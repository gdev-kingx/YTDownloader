from pytube import Youtube
from sys import argv

try:
  # Get YT url from command
  url = argv[1]

  yt = Youtube(url)

  print("Title: ", yt.title)
  print("Views: ", yt.views)

  # Get the highest resolution stream
  yd = yt.streams.get_highest_resolution()

  # Download the video in the directory you require
  yd.download('Your Directory path') # or you dont have to specify a directory and it will install the video in the same directory as the py file

  print("Download Complete.")
  print("Thanks for using YTDownloader!")
  
except Exception as e:
  print("An error occured!", str(e))
