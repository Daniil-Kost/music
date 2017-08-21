# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Singer(models.Model):
	"""Singer Model"""

	class Meta(object):
		"""docstring for Meta"""
		verbose_name ="Singer"
		verbose_name_plural ="Singers"
			
	singer_name = models.CharField(
		max_length =256,
		blank =False,
		verbose_name ="Name")

	singer_photo = models.ImageField(
		blank =True,
		verbose_name ="Photo",
		null =True)

	singer_albums = models.ManyToManyField('Album',
		verbose_name ="Albums", 
		blank =True,)

	def __unicode__(self):
		return "%s" % (self.singer_name)

#--------------------------------------------------------------
class Album(models.Model):
	"""Album Model"""

	class Meta(object):
		"""docstring for Meta"""
		verbose_name =u"Album"
		verbose_name_plural =u"Albums"
			
	album_title = models.CharField(
		max_length =256,
		blank =False,
		verbose_name =u"Name")

	album_photo = models.ImageField(
		blank =True,
		verbose_name ="Photo",
		null =True)

	album_tracks = models.ManyToManyField('Track',
		verbose_name =u"Tracks", 
		blank =True,)

	album_singers = models.ManyToManyField('Singer',
		verbose_name =u"Singers", 
		blank =True,)

	album_genres = models.ManyToManyField('Genre',
		verbose_name =u"Genres", 
		blank =True,)

	def __unicode__(self):
			return u"%s" % (self.album_title)

#------------------------------------------------
class Track(models.Model):
	"""Track Model"""

	class Meta(object):
		"""docstring for Meta"""
		verbose_name =u"Track"
		verbose_name_plural =u"Tracks"
			
	track_name = models.CharField(
		max_length =256,
		blank =False,
		verbose_name =u"Name")

	track_photo = models.ImageField(
		blank =True,
		verbose_name ="Photo",
		null =True)

	track_singers =  models.ManyToManyField('Singer',
		verbose_name =u"Singers", 
		blank =True,)

	track_album = models.ForeignKey('Album',
		verbose_name =u"Album",
		blank =True,
		null =True,
		on_delete =models.CASCADE)

	track_genre = models.ForeignKey('Genre',
		verbose_name =u"Genre",
		blank =True,
		null =True,
		on_delete =models.SET_NULL)

	track_song = models.FileField(upload_to='uploads', 
		max_length =100)

	def __unicode__(self):
		return u"%s" % (self.track_name)

#-----------------------------------------------------------
class Genre(models.Model):
	"""Genre Model"""

	class Meta(object):
		"""docstring for Meta"""
		verbose_name =u"Genre"
		verbose_name_plural =u"Genres"
			
	genre_name = models.CharField(
		max_length =256,
		blank =False,
		verbose_name =u"Name")

	genre_photo = models.ImageField(
		blank =True,
		verbose_name ="Photo",
		null =True)

	genre_albums = models.ManyToManyField('Album',
		verbose_name =u"Albums", 
		blank =True,)

	def __unicode__(self):
		return u"%s" % (self.genre_name)
