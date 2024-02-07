from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Click


@csrf_exempt
def click(request):
    if request.method == 'POST':
        newclick = Click(name='python')
        newclick.save()
        return HttpResponse(
            "click added: " + str(newclick.id) + " with " + newclick.name + ".", status=201)
    elif request.method == 'GET':
        allClicks = Click.objects.all()
        return HttpResponse(allClicks)
