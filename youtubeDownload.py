from pytube import YouTube

url = input("Enter the Youtube link: ")

video = YouTube(url)

stream = video.streams.first()

print("Downloading....")
stream.download()

print("Video downloaded successfully!")