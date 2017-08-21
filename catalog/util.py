# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(objects, size, request, context, var_name='object_list'):
	"""Paginate objects provided by view"""

	#apply pagination
	paginator =Paginator(objects, size)

	#try to get page number from request
	page =request.GET.get('page', '1')
	try:
		object_list =paginator.page(page)

	except PageNotAnInteger:
		#if page is not at integer, deliver first page
		object_list =paginator.page(1)

	except EmptyPage:
		#if page is out of range
		#deliver last page of results
		object_list =paginator.page(paginator.num_pages)

	#set variables into context
	context[var_name] =object_list
	context['is_paginated'] =object_list.has_other_pages()
	context['page_obj'] =object_list
	context['paginator'] =paginator

	return context

def get_genre(request):
	"""Returns list of existing groups"""
	#deferred import of Genre model to avoid cycled imports
	from .models import Genre

	#get currently selected group
	cur_genre =get_current_genre(request)

	genres =[]
	for genre in Genre.objects.all().order_by('genre_name'):
		genres.append({
			'id': genre.id,
			'genre_name': genre.genre_name,
			'selected': cur_genre and cur_genre.id ==genre.id and True or False
			})

	return genres


def get_current_genre(request):
	"""Returns currently selected genre or None"""

	#we remember selected genre in a cookie
	pk =request.COOKIES.get('current_genre')

	if pk:
		from .models import Genre
		try:
			genre =Genre.objects.get(pk =int(pk))
		except Genre.DoesNotExist:
			return None
		else:
			return genre
	else:
		return None
