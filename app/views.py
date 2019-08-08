import datetime
import os
from app import settings
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'
    file_listing = []
    file_names = os.listdir(settings.FILES_PATH)
    if date != None:
        d = datetime.datetime.strptime(date, "%Y-%m-%d")
        date = datetime.datetime.date(d)
        for name in file_names:
            file_dict = {}
            file_dict['name'] = name
            file_data = os.stat(settings.FILES_PATH + '/' + name)
            file_dict['ctime'] = datetime.datetime.fromtimestamp(file_data.st_ctime)
            file_dict['mtime'] = datetime.datetime.fromtimestamp(file_data.st_mtime)
            if datetime.date.fromtimestamp(file_data.st_ctime) == date:
                file_listing.append(file_dict)
    else:
        for name in file_names:
            file_dict = {}
            file_dict['name'] = name
            file_data = os.stat(settings.FILES_PATH + '/' + name)
            file_dict['ctime'] = datetime.datetime.fromtimestamp(file_data.st_ctime)
            file_dict['mtime'] = datetime.datetime.fromtimestamp(file_data.st_mtime)
            file_listing.append(file_dict)
    context = {
        'files': file_listing,
        'date': date
    }
    return render(request, template_name, context)


def file_content(request, name):
    with open(settings.FILES_PATH + '/' + name, 'r') as file:
        content = file.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )
