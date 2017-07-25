from django.shortcuts import render
from django.views import generic

class Home(generic.ArchiveIndexView):
    template_name = "home/index.html"


