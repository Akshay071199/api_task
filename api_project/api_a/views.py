from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def sum_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            num1 = data.get('num1', 0)
            num2 = data.get('num2', 0)
            result = num1 + num2
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
