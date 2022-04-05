import youtube_dl

def func3():
    print ("function 3 starting")
    url=input("enter the url: ")
    info=youtube_dl.YoutubeDL().extract_info(url=url,download=False)
    filename=f"{info['title']}"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        #'noplaylist':False,
        #'outtmpl':filename,
        'outtmpl':"%(title)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        #'writethumbnail': True
    }

    with youtube_dl.YoutubeDL(options) as dl:
        dl.download([url])
        meta = dl.extract_info(url, download=False)
        print("Downloaded {}".format(filename))
        print("------------")
        print ('upload date : %s' %(meta['upload_date']))
        print ('uploader    : %s' %(meta['uploader']))
        print ('views       : %d' %(meta['view_count']))
        print ('likes       : %d' %(meta['like_count']))
        #print ('dislikes    : %d' %(meta['dislike_count']))
        print ('id          : %s' %(meta['id']))
        print ('format      : %s' %(meta['format']))
        print ('duration    : %s' %(meta['duration']))
        print ('title       : %s' %(meta['title']))
        print ('description : %s' %(meta['description']))
        print("---------**--")

    # for result in meta:
    #     print (result)
    #     print (result.format)
    #     print ("{}".format(result.format))
    #     print ('format  : %s' %(meta['format'])) 

def func1():
    print ("function 1 starting")
    url=input("enter the url: ")
    info=youtube_dl.YoutubeDL().extract_info(url=url,download=False)
    filename=f"{info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'noplaylist':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as dl:
        dl.download([url])

    print("Downloaded {}".format(filename))

if __name__=='__main__':
    #func1()
    func3()