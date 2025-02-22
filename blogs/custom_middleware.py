import time

class TiempoDeProcesmientoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tiempo_inicio = time.time()
        response =self.get_response(request)
        tiempo_fin = time.time()
        tiempo_total = tiempo_fin - tiempo_inicio
        response['X-Tiempo-De-Procesamiento'] = str(tiempo_total) + 'seg'

        return response
