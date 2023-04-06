from pytube import YouTube

# link = "https://www.youtube.com/watch?v=4jgED1hfgeA"
# youtube_1 = YouTube(link)

# # print(youtube_1.title)
# print(youtube_1.thumbnail_url)
# videos = youtube_1.streams.all()   #All Format streaming
# videos = youtube_1.streams.filter(only_audio=True)   #Only audio format
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
# print()
# strm = int(input("enter: "))
# videos[strm].download()
# print("successfully")

# **** Playlist *****link = "https://www.youtube.com/watch?v=4jgED1hfgeA"
# youtube_1 = YouTube(link)

# # print(youtube_1.title)
# print(youtube_1.thumbnail_url)
# videos = youtube_1.streams.all()   #All Format streaming
# videos = youtube_1.streams.filter(only_audio=True)   #Only audio format
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
# print()
# strm = int(input("enter: "))
# videos[strm].download()
# print("successfully")

from pytube import Playlist
py = Playlist("https://www.youtube.com/playlist?list=PLjVLYmrlmjGdqdwNZvre2yPI6n5LyQ5M9")
print(f'downloading : {py.title}')
for video in py.videos:
    video .streams.first().download()
    
