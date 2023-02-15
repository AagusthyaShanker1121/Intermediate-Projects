# python program to download youtube videos using pytube library

from pytube import YouTube

def Download(link) :
    try :
        # instantiating youtube object and acquiring highest resolution video
        video = YouTube(link)
        video = video.streams.get_highest_resolution()

    
        # download the video 
        video.download(output_path = r"C:\Users\AGASTYA SHANKER\Python Files\Youtube")

    except :
        print('An error occurred. Please try next time.')
        return
    
    print("Your video is downloaded. Check your destination folder for video(s).")



  
link = input("Enter the URL of the youtube video.\t") 
Download(link)



