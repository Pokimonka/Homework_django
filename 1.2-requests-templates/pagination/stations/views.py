import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))

def create_stations_list():
    bus_stations_list = []
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            stations = {
                'Name': r['Name'],
                'Street':r['Street'],
                'District': r['District']
            }
            bus_stations_list.append(stations)
    return bus_stations_list

def bus_stations(request):
    bus_stations_list = create_stations_list()

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)
    print(page_number)
    context = {
         #'bus_stations': bus_stations_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
