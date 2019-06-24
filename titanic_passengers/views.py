import json

from django.db.models import Count, Q
from django.shortcuts import render
from django.http import JsonResponse

from .models import TitanicPassenger
# Create your views here.

def index(request):
    return render(request, 'index.html')

def sex_view(request):
    dataset = TitanicPassenger.objects \
        .values('sex') \
        .annotate(survived_count=Count('sex', filter=Q(survived=True)),
                  not_survived_count=Count('sex', filter=Q(survived=False))) \
        .order_by('sex')

    return render(request, 'sex.html', {'dataset': dataset})

def sex_view_2(request):
    dataset = TitanicPassenger.objects \
        .values('sex') \
        .annotate(survived_count=Count('sex', filter=Q(survived=True)),
                  not_survived_count=Count('sex', filter=Q(survived=False))) \
        .order_by('sex')

    categories = list()
    survived_series = list()
    not_survived_series = list()

    for entry in dataset:
        categories.append('%s Class' % entry['sex'])
        survived_series.append(entry['survived_count'])
        not_survived_series.append(entry['not_survived_count'])

    return render(request, 'sex_2.html', {
        'categories': json.dumps(categories),
        'survived_series': json.dumps(survived_series),
        'not_survived_series': json.dumps(not_survived_series)
    })

def sex_view_3(request):
    dataset = TitanicPassenger.objects \
        .values('sex') \
        .annotate(survived_count=Count('sex', filter=Q(survived=True)),
                  not_survived_count=Count('sex', filter=Q(survived=False))) \
        .order_by('sex')

    categories = list()
    survived_series_data = list()
    not_survived_series_data = list()

    for entry in dataset:
        categories.append('%s Class' % entry['sex'])
        survived_series_data.append(entry['survived_count'])
        not_survived_series_data.append(entry['not_survived_count'])

    survived_series = {
        'name': '生存',
        'data': survived_series_data,
        'color': 'green'
    }

    not_survived_series = {
        'name': '死亡',
        'data': not_survived_series_data,
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': '男女別の生存者数'},
        'xAxis': {'categories': categories},
        'series': [survived_series, not_survived_series]
    }

    dump = json.dumps(chart)

    return render(request, 'sex_3.html', {'chart': dump})

def ajax(request):
    return render(request, 'ajax.html')


def chart_data(request):
    dataset = TitanicPassenger.objects \
        .values('embarked') \
        .exclude(embarked='') \
        .annotate(total=Count('embarked')) \
        .order_by('embarked')

    port_display_name = dict()
    for port_tuple in TitanicPassenger.PORT_CHOICES:
        port_display_name[port_tuple[0]] = port_tuple[1]

    chart = {
        'chart': {'type': 'pie'},
        'title': {'text': '港別乗船員数'},
        'series': [{
            'name': '人数',
            'data': list(map(lambda row: {'name': port_display_name[row['embarked']], 'y': row['total']}, dataset))
        }]
    }

    return JsonResponse(chart)