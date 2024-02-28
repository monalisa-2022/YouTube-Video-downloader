from pytube import YouTube

link = "https://www.youtube.com/watch?v=KToqhOxaFcw&list=RDMMKToqhOxaFcw&start_radio=1"
yt=YouTube(link)

print(yt.title)                            #for getting title of youtube video
print(yt.thumbnail_url)                    #for getting thumbnail

#downloading yt videos

videos=yt.streams.all()
#videos=yt.streams.filter(only_audio=True)  #to get just audio
vid=list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("enter:"))
videos[strm].download()
print("downloaded successfully")
