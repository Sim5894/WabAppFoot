from django.shortcuts import render
from django.contrib import messages
from .form import CreateCovoitForm, PlaceForm
from connexion.models import User
from .models import Voiture
from django.db import connection


def covoit(request):
    data = Voiture.objects.all()
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            addresse = form.cleaned_data["addresse"]
            id = request.POST.get('id', None)
            uid = request.POST.get('uid', None)
            uid = str(uid)
            for p in Voiture.objects.raw("select * from covoit_voiture where id = "+id):
                placebase = p.placedispo
                placelibre = p.placelibre
                diff = (placebase - placelibre)+1
                diff = str(diff)

            if placelibre > 0:
                with connection.cursor() as cursor:
                    cursor.execute("update covoit_voiture set p"+diff+" = %s, addr"+diff+" = %s where id = %s", (uid, addresse, id))
                    cursor.execute("update covoit_voiture set placelibre = placelibre -1 where id = %s", id)
                    messages.success(request, f'Places enregistrés')
            else:
                messages.warning(request, f'Plus de places')
    else:
        form = PlaceForm()

    context = {
        "form": form,
        "voiture": data
    }
    return render(request, 'covoit/covoiturage.html', context)


def addcovoit(request):
    user = request.user.id
    user1 = User.objects.get(id=user)

    if request.method == "POST":
        form = CreateCovoitForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Covoiturage enregistré')
            obj = form.save(commit=False)
            dispo = form.cleaned_data["placedispo"]
            obj.placelibre = dispo
            obj.conduct = user1
            obj.save()
    else:
        form = CreateCovoitForm()

    context = {
        "form": form
    }
    return render(request, 'covoit/addCovoit.html', context)

