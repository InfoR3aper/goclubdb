from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Layer, Club, Clubtype, Clubstatus, ClubForm, LayerForm, ClubtypeForm, ClubstatusForm

#Static greeting page
def index(request):
    layers = Layer.objects.all()
    return render(request, 'layerlist.html', {'layers': layers})

def layerlist(request):
    layers = Layer.objects.all()
    return render(request, 'layerlist.html', {'layers': layers})

def clublist(request, layername):
    layer = Layer.objects.filter(name=layername)
    if len(layer) != 1: #Must be one and only one layer with this name.
        layers = Layer.objects.all()
        return render(request, 'layerlist.html', {'layers': layers}) #Redirect to layer list
    clubs = Club.objects.filter(layer__name=layername)
    return render(request, 'clublist.html', {'clubs': clubs, 'layer': layer[0]})

def clubdetail(request, clubid):
    club = Club.objects.filter(id=clubid)
    if len(club) != 1: #Must be one and only one club with this name.
        layers = Layer.objects.all()
        return render(request, 'layerlist.html', {'layers': layers}) #Redirect to layer list
    clublayer = Layer.objects.filter(id=club[0].layer_id)
    return render(request, 'clubdetail.html', {'club': club[0], 'layer': clublayer[0]})

class ClubCreate(CreateView):
    model = Club
    form_class = ClubForm

#Create club with layer pre-populated
class ClubCreateLayer(CreateView):
    model = Club
    form_class = ClubForm
    def get_initial(self):
        layer = get_object_or_404(Layer, name=self.kwargs.get('name'))
        return { 'layer':layer }

class ClubUpdate(UpdateView):
    model = Club
    form_class = ClubForm

class ClubDelete(DeleteView):
    model = Club
    form_class = ClubForm

