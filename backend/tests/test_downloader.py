from app.services.downloader import MediaDownloader


def main():

    url = input("Enter YouTube URL: ").strip()

    downloader = MediaDownloader()

    print("\nDownloading...\n")

    result = downloader.download(url)

    print("\nDownload Result\n")

    print(result)


if __name__ == "__main__":
    main()