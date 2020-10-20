from django.http.response import JsonResponse
from django.http import HttpResponse

def test(request):
  return HttpResponse("helloworld")