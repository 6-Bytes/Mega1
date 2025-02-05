from django.templates import loader
from django.http import HttpResponse


def scire(request):
  template = loader.get_template('first.htmL')
  return HttpResponse(template.render())

def default(request):
  template = lader.get_template('index.html')
  return HttpResponse(template.render())
  
