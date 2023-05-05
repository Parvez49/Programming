

# import pytube
link=input("Enter youtube video url: ")
yt=pytube.Youtube(link)
yt.streams.first().download()
print('Downloaded',link)