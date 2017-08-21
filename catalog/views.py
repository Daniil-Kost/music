# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView
from django.forms import ModelForm
from django import forms
from django.views.generic import CreateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout
from crispy_forms.bootstrap import FormActions
from models import Singer, Album, Track, Genre
from util import paginate, get_current_genre

# Create your views here.

#Singers
def singers_list(request):

	singers = Singer.objects.all()

	#apply pagination, 3 singers per page
	context = paginate(singers, 3, request, {}, var_name = 'singers')

	return render(request, 'catalog/singers_list.html', context)

#Albums
def albums_list(request):

	albums = Album.objects.all()

	tracks =Track.objects.all()

	#apply pagination, 3 albums per page
	context = paginate(albums, 3, request, {'tracks':tracks}, var_name = 'albums')

	return render(request, 'catalog/albums_list.html', context)

#Ganres
def genres_list(request):

	#check if we need to show only one genre of genres
	current_genre = get_current_genre(request)
	if current_genre:
		genres = Genre.objects.filter(
			genre_name = current_genre)
	else:
		#otherwise show all genres
		genres = Genre.objects.all()

	#apply pagination, 3 genres per page
	context = paginate(genres, 3, request, {}, var_name = 'genres')

	return render(request, 'catalog/genres_list.html', context)

#Track list
class TrackForm(ModelForm):
	"""docstring for TrackForm"""

	class Meta:
		model = Track

		exclude = ("",)
		#fields ="__all__"
		
	def __init__(self, *args, **kwargs):
		super(TrackForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		#set from tag attributes
		self.helper.form_action = reverse('track', 
			kwargs = {'pk': kwargs['instance'].id})
		self.helper.form_method = 'POST'
		self.helper.form_class = 'form-horizontal'


class TrackView(UpdateView):
	"""docstring for TrackView"""

	model = Track
	template_name = 'catalog/track.html'

	exclude = ("",)

	form_class = TrackForm

	success_url = 'albums/'
	
	def post(self, request, *args, **kwargs):
		if request.POST.get('home_button'):
			return HttpResponseRedirect(reverse('albums'))
		else:
			return super(
				TrackView, self).post(request, *args, **kwargs)
