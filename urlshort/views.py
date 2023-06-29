from django.shortcuts import render
from .models import UrlShort
from .forms import CreateNewShortURL
from datetime import datetime
import random, string


def home(request):
    return render(request, 'index.html')


def redirect(request, url):
    current_obj = UrlShort.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, '404.html')
    context = {'obj': current_obj[0]}
    return render(request, 'redirect.html', context)


def createShortUrl(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(UrlShort.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            d = datetime.now()
            s = UrlShort(original_url=original_website, short_url=random_chars, created_at=d)
            s.save()
            return render(request, 'created.html', {'chars': random_chars})

    else:
        form = CreateNewShortURL()
        context = {'form': form}
        return render(request, 'create.html', context)
