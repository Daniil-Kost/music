from .util import get_genre


def genres_processor(request):
    return {'GENRES': get_genre(request)}






