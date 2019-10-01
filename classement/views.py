from django.shortcuts import render
from .models import Classement, Calendrier
from .matchform import MatchForm, sqlclass, PrograMatch, sqlprogra, sqlencodea, sqlencodeb, CalendrierForm, PrograJourForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required


dataCalendrierj1a = Calendrier.objects.values_list("equipeA", flat=True).filter(journee=1)
dataCalendrierj1b = Calendrier.objects.values_list("equipeB", flat=True).filter(journee=1)

dataClassement = Classement.objects.all().order_by('-points')

dataCalendrier = Calendrier.objects.all()

nombre_jour = Calendrier.objects.raw('SELECT * FROM tfe.classement_calendrier GROUP BY journee')
jour = 0
for j in nombre_jour:
    jour = jour +1

jour_num = Calendrier.objects.filter(journee=1)

context = {
    "dataClassement": dataClassement,
    "dataCalendrier": dataCalendrier,
    "nombre_journee": jour,
    "jour_num": jour_num
}


def calendrier(request):
    if request.method == "POST":
        form = CalendrierForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data["nbJour"]
            jour_num = Calendrier.objects.filter(journee=num)
            context['jour_num'] = jour_num
    else:
        form = CalendrierForm()
    context['form'] = form

    return render(request, 'classement/calendrier-base.html', context)


def classement(request):
    return render(request, 'classement/classement.html', context)



@staff_member_required
def encode(request):
    if request.method =="POST":
        form1 = CalendrierForm(request.POST)
        form2 = MatchForm(request.POST)
        if form1.is_valid():
            num = form1.cleaned_data["nbJour"]
            jour_num = Calendrier.objects.filter(journee=num)
            context['jour_num'] = jour_num
        else:
            form1 = CalendrierForm()

        if form2.is_valid():
            messages.success(request, f'Scores enregistrés')
            i = 0
            for team in dataCalendrierj1a:
                i = int(i)
                i = i+1
                i = str(i)
                goala = form2.cleaned_data["but_a"+i]
                goala = str(goala)
                goalb = form2.cleaned_data["but_b" + i]
                goalb = str(goalb)
                sqlencodea(team, goala)
                sqlclass(team, goala, goalb)

            j=0
            for team in dataCalendrierj1b:
                j = int(j)
                j = j+1
                j = str(j)
                goala = form2.cleaned_data["but_a" + j]
                goala = str(goala)
                goalb = form2.cleaned_data["but_b" + j]
                goalb = str(goalb)
                sqlencodeb(team, goalb)
                sqlclass(team, goalb, goala)
    else:
        form1 = CalendrierForm()
        form2 = MatchForm()
    context['form1']= form1
    context['form2'] = form2
    return render(request, 'classement/encode.html', context)


@staff_member_required
def progra(request):
    if request.method == "POST":
        form = PrograMatch(request.POST)
        if form.is_valid():
            messages.success(request, f'Matchs enregistrés')
            sqlprogra(form.cleaned_data["journee"], form.cleaned_data["equipe_11"], form.cleaned_data["equipe_12"])
            sqlprogra(form.cleaned_data["journee"], form.cleaned_data["equipe_21"], form.cleaned_data["equipe_22"])
            sqlprogra(form.cleaned_data["journee"], form.cleaned_data["equipe_31"], form.cleaned_data["equipe_32"])
            sqlprogra(form.cleaned_data["journee"], form.cleaned_data["equipe_41"], form.cleaned_data["equipe_42"])
            sqlprogra(form.cleaned_data["journee"], form.cleaned_data["equipe_51"], form.cleaned_data["equipe_52"])
            sqlprogra(form.cleaned_data["journee"], form.cleaned_data["equipe_61"], form.cleaned_data["equipe_62"])
            sqlprogra(form.cleaned_data["journee"], form.cleaned_data["equipe_71"], form.cleaned_data["equipe_72"])
            sqlprogra(form.cleaned_data["journee"], form.cleaned_data["equipe_81"], form.cleaned_data["equipe_82"])
    else:
        form = PrograMatch()

    context['form'] = form

    return render(request, 'classement/progra.html', context)


