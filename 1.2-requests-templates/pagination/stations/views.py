from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


with open(BUS_STATION_CSV, newline='', encoding='utf-8') as stations_csv:
    reader = csv.DictReader(stations_csv)
    bus_station = Paginator([dict(i) for i in reader], 10)


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get('page', 1))
    context = {
        'bus_stations': bus_station.get_page(page_number),
        'page': bus_station.get_page(page_number),
    }
    return render(request, 'stations/index.html', context)
