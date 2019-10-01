from django.shortcuts import render
from connexion.models import User
from django.db import connection
from django.contrib import messages



def selection(request):
    joueur = User.objects.filter(estjoueur=1)
    if request.method == "POST":
        messages.success(request, f'Convocations faites')
        journee = request.POST.get("journee", None)
        id = request.POST
        id = request.POST.copy()
        del id["journee"]
        del id["csrfmiddlewaretoken"]
        n = 1
        with connection.cursor() as cursor:
            cursor.execute("replace into match_joueursselect (journee) values (%s)", journee)
        for i in id:
            n = str(n)
            i = str(i)
            journee = str(journee)
            with connection.cursor() as cursor:
                cursor.execute("update match_joueursselect set j"+n+" = %s where journee = %s", (i, journee))
            n = int(n)
            n = n +1

    context = {
        "joueur": joueur
    }
    return render(request, 'match/selection.html', context)


def finmatch(request):
    joueur = User.objects.filter(estjoueur=1)
    if request.method == "POST":
        messages.success(request, f'Données enregistréss')
        for i in joueur:
            id = i.id
            id = str(id)
            selec = request.POST.get(id, None)
            titu = request.POST.get("titu"+id, None)
            but = request.POST.get("but" + id, None)
            jaune = request.POST.get("jaune" + id, None)
            rouge = request.POST.get("rouge" + id, None)

            if selec != None:
                if titu == None:
                    titu = 0
                else:
                    titu = 1

                if rouge == None:
                    rouge = 0
                else:
                    rouge = 1

                jaune = int(jaune)
                if jaune == 2:
                    rouge = 1

                titu = str(titu)
                but = str(but)
                jaune = str(jaune)
                rouge = str(rouge)

                with connection.cursor() as cursor:
                    cursor.execute("update connexion_joueur set matchs = matchs +1, titularisations = titularisations +%s, buts = buts +%s, jaune = jaune +%s, rouge = rouge + %s where user_id = %s", (titu, but, jaune, rouge, id))

    context = {
        "joueur": joueur
    }
    return render(request, 'match/finmatch.html', context)