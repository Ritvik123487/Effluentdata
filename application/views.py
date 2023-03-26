from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def index (request):
    return render(request, "index.html")


def team (request):
    return render(request, "team.html")

def graph(request):
    # Assuming you have the image source URL stored in a variable called 'img_src'
    img_src = 'path/to/image.png'
    context = {'img_src': img_src}
    return render(request, 'graph.html', context)


from .calculations import generate_plot

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def generate_plot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        input1 = float(data['input1'])
        input2 = float(data['input2'])

        plot_data = generate_plot(input1, input2)

        response_data = {
            'plot_data': plot_data
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
