from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import InteractionSerializer

# Create your views here.

def index(request):
    return HttpResponse("Page d'accueil H-DIC")


def searching(request):
    username = "MDAOUPHARS"
    password = "AfT98BjjGIUc"
    connection_hedrine = ConnectionHedrine(username, password)
    interactions = Hedrine.send_intersection(connection_hedrine, 1, 1)
    return HttpResponse(interactions)
    #connection_hedrine.close()


def test(request):
    interaction_1 = Interaction(nom_plante = "une plante",
                                effets_plante = "effet de la plante",
                                intensite_plante = "intensite de la plante",
                                nom_med = "un medicament",
                                effets_med = " effet du médicament",
                                intensite_med = " intensite du medicament",
                                consequence = "consequence de l'interaction")
    interaction_1.save()
    return HttpResponse("Interaction ajouté")

def init_db(request):

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
