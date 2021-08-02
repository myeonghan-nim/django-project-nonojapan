from django.shortcuts import render, redirect

from .models import ProhibitedGood


def index(request):
    context = {
        'goods': ProhibitedGood.objects.all()
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    good = ProhibitedGood(
        product=request.GET.get('product'),
        replace=request.GET.get('replace'),
        info=request.GET.get('info')
    )
    good.save()
    return redirect('/nonojapan/')


def detail(request, pk):
    context = {
        'good': ProhibitedGood.objects.get(pk=pk)
    }
    return render(request, 'detail.html', context)


def edit(request, pk):
    context = {
        'good': ProhibitedGood.objects.get(pk=pk)
    }
    return render(request, 'edit.html', context)


def update(request, pk):
    good = ProhibitedGood.objects.get(pk=pk)
    good.product = request.GET.get('product')
    good.replace = request.GET.get('replace')
    good.info = request.GET.get('info')
    good.save()
    return redirect('/nonojapan/')


def delete(request, pk):
    ProhibitedGood.objects.get(pk=pk).delete()
    return redirect('/nonojapan/')
