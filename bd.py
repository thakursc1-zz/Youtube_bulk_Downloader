from pytube import YouTube
from pytube.utils import print_status, FullPaths
from pytube.exceptions import PytubeError
from pprint import pprint



#Read links from done.txt to check if files have already been downloaded
with open('done.txt','r') as f:
	done = f.readlines()

#Read download.txt where you can add links using ubuntu terminal 

#you can add new line to a file like this :
#$echo "https://www.youtube.com/watch?v=vmgu4dRUoSQ" >> /path/download.txt 

with open('download.txt' ,'r') as f:
	download = f.readlines()

#Iterating over the lines and 
for i in download:
	if i in done:
		print(i,"has been already been downloaded")
	else:
		try:
			yt = YouTube(i)
			video = yt.get('mp4', '720p')
			print(yt.filename)
			video.download('/media/thakursc1/SID/Vid/',on_progress=print_status)
			##append done songs to this list 
			done.append(i)
		except:
			print("File format and pixel combination doesnt match. Skipping File",yt.filename)


### Writing the complete list of done downloads 
with open('done.txt','w') as f:
	for i in done:
		f.write(i)

