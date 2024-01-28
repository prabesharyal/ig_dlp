from insta_dlp import Instagram_Downloader

url = input("Input Instagram Link : ")
check, caption, filelist = Instagram_Downloader(url)
if check != False:
    print("Identified Media Type: " + check)
    print("Post Caption : " + str(caption))
    print("Path of Downloaded Files: ", end ='')
    print(filelist)
else:
    print("Couldn't Download Instagram Post")
