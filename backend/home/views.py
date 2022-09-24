from django.shortcuts import render, redirect
from .models import Org
from .forms import OrgForm
from .models import Org, OrgForm
from rest_framework import viewsets
from .serializers import OrgSerializer, OrgFormSerializer


class OrgViewSet(viewsets.ModelViewSet):
    queryset = Org.objects.all().order_by('name')
    serializer_class = OrgSerializer

class OrgFormViewSet(viewsets.ModelViewSet):
    queryset = OrgForm.objects.all().order_by('Name')
    serializer_class = OrgFormSerializer

def index(request):
    orgs = Org.objects.all() 
    return render(request, 'index.html', {'orgs': orgs})

def create(request):
    error = ''
    if request.method == 'POST':
        form = OrgForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = OrgForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)

