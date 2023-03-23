import json
import urllib.request
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from .models import AutoSys
from .serializers import AsSerializer
from .forms import AutoSysForm
import requests
import concurrent.futures
from .forms import ASN_IP

from celery import shared_task

class AsViewSet(viewsets.ModelViewSet):
    queryset = AutoSys.objects.all()
    serializer_class = AsSerializer

def home(request):
    all_asn = AutoSys.objects.all()
    return render(request, 'ausys/home.html', context={'data': all_asn})

def add_autosys(request):
    submitted = False
    if request.method == 'POST':
        form = AutoSysForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add?submitted=True')
    else:
        form = AutoSysForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'ausys/add_autosys.html', {'form': form, 'submitted': submitted})

@shared_task
def show_names(request):
    asns = AutoSys.objects.all()
    all_asn = AutoSys.objects.values_list('autosys', flat=True)

    url = "https://stat.ripe.net/data/as-names/data.json?resource="

    with concurrent.futures.ThreadPoolExecutor() as executor:
        responses = list(executor.map(requests.get, [url + str(asn) for asn in all_asn]))

    json_data = [response.json()['data']['names'][str(asn)] for response, asn in zip(responses, all_asn)]

    return render(request, 'ausys/names.html', {'data1': asns, 'data2': json_data})

def list_neighbours(request):
    all_asn = AutoSys.objects.all()

    return render(request, 'ausys/neighbours_list.html', {'asns': all_asn})

def show_neighbours(request, asn_id):
    asn_cur = AutoSys.objects.get(pk= asn_id)

    url = "https://stat.ripe.net/data/asn-neighbours/data.json?data_overload_limit=ignore&resource=" + str(asn_cur.autosys)

    response = urllib.request.urlopen(url)
    data = response.read().decode()

    parsed_data = json.loads(data)

    left_count = parsed_data['data']['neighbour_counts']['left']
    right_count = parsed_data['data']['neighbour_counts']['right']
    uncertain_count = parsed_data['data']['neighbour_counts']['uncertain']
    unique_count = parsed_data['data']['neighbour_counts']['unique']
    count = left_count + right_count + uncertain_count

    json_time = datetime.strptime(parsed_data['time'], '%Y-%m-%dT%H:%M:%S.%f')
    new_time = json_time + timedelta(hours=6)
    time = new_time.strftime("%d.%m.%Y %H:%M:%S")

    neigh = []

    for i in range(count):
        neigh.append(parsed_data['data']['neighbours'][i]['asn'])

    return render(request, 'ausys/neighbours.html', {'asn_cur': asn_cur, 'neighbours': neigh, 'time': time,
                                                     'left': left_count, 'right': right_count,
                                                     'uncertain': uncertain_count, 'unique': unique_count})


def whois(request):
    if request.method == 'POST':
        asn_ip = request.POST.get('asn_ip')
        url = f'https://stat.ripe.net/data/whois/data.json?data_overload_limit=ignore&resource={asn_ip}'
        return redirect(url)
    else:
        form = ASN_IP()
    return render(request, 'ausys/whois.html', {'form_search': form})

@shared_task
def whois_list(request):
    all_asn = AutoSys.objects.all()

    return render(request, 'ausys/whois_list.html', {'asns': all_asn})

def show_whois(request, asn_id):
    asn_cur = AutoSys.objects.get(pk=asn_id)

    url = "https://stat.ripe.net/data/whois/data.json?data_overload_limit=ignore&resource=" + str(
        asn_cur.autosys)

    return redirect(url)

