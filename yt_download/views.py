from django.shortcuts import render
from pytube import YouTube
from .settings import BASE_DIR


def home_page(request):
    if request.method == 'POST':
        x = request.POST['youtube_url']
        if request.POST['youtube_url'] == '':
            return render(request, 'home_page.html', context={'vid_download': ''})
        yt = YouTube(x)
        stream = yt.streams.first()
        x_download = stream.download(BASE_DIR + '\downloads')
        vid_download = BASE_DIR + '\downloads\\' + stream.default_filename
        contex = {
            'vid_download': vid_download
        }
        return render(request, 'home_page.html', contex)

    return render(request, 'home_page.html')
