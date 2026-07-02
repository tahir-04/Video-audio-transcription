from app.services.downloader import MediaDownloader

url = input("Enter URL: ")

downloader = MediaDownloader()

result = downloader.download(url)

print()

print(result)