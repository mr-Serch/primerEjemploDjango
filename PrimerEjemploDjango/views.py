from django.http import HttpResponse

def inicio(request):
	contenido = """
	<html>
	    <body>
	        <h1>Hola Mundo</h1>
	    </body>
	</html>
	"""
	return HttpResponse(contenido)
