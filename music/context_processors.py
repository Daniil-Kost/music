from .settings import PORTAL_URL

def catalog_proc(request):
	return {'PORTAL_URL': PORTAL_URL}
