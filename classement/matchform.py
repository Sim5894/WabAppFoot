from django import forms
from classement.models import Classement, Calendrier
from django.db import connection


class CalendrierForm(forms.Form):
    nombre_jour = Calendrier.objects.raw('SELECT * FROM tfe.classement_calendrier GROUP BY journee')
    nbjournee = ()
    i = 1
    for j in nombre_jour:
        i = str(i)
        x = (i, "Journée numéro " + i)
        nbjournee = nbjournee + (x,)
        i = int(i)
        i = i + 1

    nbJour = forms.ChoiceField(choices=nbjournee, label="")


class PrograJourForm(forms.Form):
    nombre_jour = Calendrier.objects.raw('SELECT * FROM tfe.classement_calendrier GROUP BY journee')
    nbjournee = ()
    i = 1
    for j in nombre_jour:
        i = str(i)
        x = (i, "Journée numéro " + i)
        nbjournee = nbjournee + (x,)
        i = int(i)
        i = i + 1

    nbJour = forms.ChoiceField(choices=nbjournee, label="")


class MatchForm(forms.Form):

    but_a1 = forms.IntegerField(label="", required=False)
    but_b1 = forms.IntegerField(label="", required=False)
    but_a2 = forms.IntegerField(label="", required=False)
    but_b2 = forms.IntegerField(label="", required=False)
    but_a3 = forms.IntegerField(label="", required=False)
    but_b3 = forms.IntegerField(label="", required=False)
    but_a4 = forms.IntegerField(label="", required=False)
    but_b4 = forms.IntegerField(label="", required=False)
    but_a5 = forms.IntegerField(label="", required=False)
    but_b5 = forms.IntegerField(label="", required=False)
    but_a6 = forms.IntegerField(label="", required=False)
    but_b6 = forms.IntegerField(label="", required=False)
    but_a7 = forms.IntegerField(label="", required=False)
    but_b7 = forms.IntegerField(label="", required=False)
    but_a8 = forms.IntegerField(label="", required=False)
    but_b8 = forms.IntegerField(label="", required=False)


class PrograMatch(forms.Form):
    data = Classement.objects.values_list("equipe", flat=True)

    Journee = ()
    first = ("", "")
    Journee = (first,) + Journee

    for equipe in data:
        x = (equipe, equipe)
        Journee = (x,) + Journee

    journee = forms.IntegerField(label="Journée numéro:")
    equipe_11 = forms.ChoiceField(choices=Journee, label="")
    equipe_12 = forms.ChoiceField(choices=Journee, label="")
    equipe_21 = forms.ChoiceField(choices=Journee, label="")
    equipe_22 = forms.ChoiceField(choices=Journee, label="")
    equipe_31 = forms.ChoiceField(choices=Journee, label="")
    equipe_32 = forms.ChoiceField(choices=Journee, label="")
    equipe_41 = forms.ChoiceField(choices=Journee, label="")
    equipe_42 = forms.ChoiceField(choices=Journee, label="")
    equipe_51 = forms.ChoiceField(choices=Journee, label="")
    equipe_52 = forms.ChoiceField(choices=Journee, label="")
    equipe_61 = forms.ChoiceField(choices=Journee, label="")
    equipe_62 = forms.ChoiceField(choices=Journee, label="")
    equipe_71 = forms.ChoiceField(choices=Journee, label="")
    equipe_72 = forms.ChoiceField(choices=Journee, label="")
    equipe_81 = forms.ChoiceField(choices=Journee, label="")
    equipe_82 = forms.ChoiceField(choices=Journee, label="")


def sqlclass(equipe, goala, goalb):
    points = 0
    if goala > goalb:
        result = "gagner"
        points = 3
    elif goala == goalb:
        result = "nul"
        points = 1
    elif goalb > goala:
        result = "perdu"
        points = 0
    points = str(points)

    with connection.cursor() as cursor:
        cursor.execute("UPDATE classement_classement SET "+result+" = "+result+" +1 WHERE equipe = %s", (equipe))
        cursor.execute("UPDATE classement_classement SET points = points +"+ points + " WHERE equipe = %s", (equipe))
        cursor.execute("UPDATE classement_classement SET jouer = jouer +1 WHERE equipe = %s" , (equipe))
        row = cursor.fetchone()

        return row


def sqlprogra(journee, equipea, equipeb):
    journee = str(journee)
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO classement_calendrier (journee, equipeA, equipeB) VALUES (%s, %s, %s)", (journee, equipea, equipeb))
        if equipea == 'Ronvau Chaumont' or equipeb == 'Ronvau Chaumont':
            cursor.execute("insert into  tfe.match_matchsronvau(id, journee, equipeA, equipeB) select id, journee, equipeA, equipeB from tfe.classement_calendrier where (equipeA ='Ronvau Chaumont' or equipeB = 'Ronvau Chaumont') and journee = %s", (journee))
        row = cursor.fetchone()

        return row


def sqlencodea(equipe, goal):
    goal = str(goal)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE classement_calendrier SET goalA = %s WHERE equipeA = %s", (goal, equipe))
        row = cursor.fetchone()

        return row


def sqlencodeb(equipe, goal):
    goal = str(goal)
    with connection.cursor() as cursor:
        cursor.execute("UPDATE classement_calendrier SET goalB = %s WHERE equipeB = %s", (goal, equipe))
        row = cursor.fetchone()

        return row
