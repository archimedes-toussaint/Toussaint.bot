import requests 
from bs4 import BeautifulSoup
import youtube_dl

class MusicDownloaderBot:

  def __init__(self):
    self.base_url = 'https://www.youtube.com'

  def search_song(self, song_name):
    search_url = self.base_url + '/results?search_query=' + song_name
    response = requests.get(search_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    video_ids = [link.get('href') for link in soup.select('a.yt-uix-tile-link')]
    return video_ids[0] # return first video id

  def download_song(self, video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([video_url])

if __name__ == "__main__":
  bot = MusicDownloaderBot()
  song_name = input('Enter the name of the artirst and song title:')
  video_url = bot.base_url + bot.search_song(song_name)
  bot.download_song(video_url)
  print("Song downloaded successfully!")