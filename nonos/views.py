from django.shortcuts import render, redirect
from .models import Nojapan

# Create your views here.


def index(request):

    nos = Nojapan.objects.all()

    context = {
        'nos': nos
    }

    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):

    product = request.GET.get('product')
    replace = request.GET.get('replace')
    info = request.GET.get('info')

    nos = Nojapan(product=product, replace=replace, info=info)
    nos.save()

    return redirect('/nonos/')


def detail(request, no_id):

    no = Nojapan.objects.get(id=no_id)

    context = {
        'no': no
    }

    return render(request, 'detail.html', context)


def edit(request, no_id):

    no = Nojapan.objects.get(id=no_id)

    context = {
        'no': no
    }

    return render(request, 'edit.html', context)


def update(request, no_id):

    no = Nojapan.objects.get(id=no_id)

    no.product = request.GET.get('product')
    no.replace = request.GET.get('replace')
    no.info = request.GET.get('info')
    no.save()

    return redirect('/nonos/')


def delete(request, no_id):

    no = Nojapan.objects.get(id=no_id)

    no.delete()

    return redirect('/nonos/')
