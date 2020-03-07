from django.http import HttpResponse
from .models import *
from rest_framework import viewsets
from .serializers import InteractionSerializer
from rest_framework import filters, generics
import json
# Create your views here.

def index(request):
    return HttpResponse("Page d'accueil H-DIC")


def searching(request):
    username = "MDAOUPHARS"
    password = "AfT98BjjGIUc"
    connection_hedrine = ConnectionHedrine(username, password)
    interactions = Hedrine.send_intersection(connection_hedrine, 1, 1)
    connection_hedrine.close()
    return HttpResponse(interactions)


def test(request):
    Hedrine.load_drugs()
    Hedrine.load_herbs()
    username = "MDAOUPHARS"
    password = "AfT98BjjGIUc"
    connection_hedrine = ConnectionHedrine(username, password)
    for drug_id in Hedrine.drugs.keys():
        for herb_id in Hedrine.herbs.keys():
            raw_interactions = Hedrine.send_intersection(connection_hedrine, drug_id, herb_id)
            interactions = Hedrine.treat_raw_interactions(raw_interactions)
            for i in range(len(interactions["possibilities"])):
                interaction = Interaction(nom_plante = Hedrine.herbs[str(herb_id)], # revenir ici
                                          effets_plante = interactions["possibilities"][i]["herb_effect"],
                                          intensite_plante = interactions["possibilities"][i]["herb_intensity"],
                                          nom_med = Hedrine.drugs[str(drug_id)], # revenir ici
                                          effets_med = interactions["possibilities"][i]["drug_effect"],
                                          intensite_med= interactions["possibilities"][i]["drug_intensity"],
                                          consequence = interactions["possibilities"][i]["consequence"] )
                interaction.save()
    return HttpResponse("Ensemble des interactions ajoutées")


class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

class InteractionAPIView(generics.ListCreateAPIView):
    search_fields = ['nom_plante','nom_med']
    filter_backends = (filters.SearchFilter,)
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

