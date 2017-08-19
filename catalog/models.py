from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Singer(models.Model):
	"""Singer Model"""

	class Meta(object):
		"""docstring for Meta"""
		verbose_name =u"Singer"
		verbose_name_plural =u"Singers"
			
	singer_name = models.CharField(
		max_length =256,
		blank =False,
		verbose_name =u"Name")

	singer_photo = models.ImageField(
		blank =True,
		verbose_name =u"Photo",
		null =True)

	singer_albums = models.ManyToManyField('Album',
		verbose_name =u"Albums", 
		blank =True,)

	def __unicode__(self):
		return u"%s %s" % (self.singer_name)

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

	track_album = models.ForeignKey('Album',
		verbose_name =u"Album",
		blank =True,
		null =True,
		on_delete =models.CASCADE)

	track_song = models.FileField(upload_to='uploads', 
		max_length =100)

	def __unicode__(self):
		return u"%s (%s)" % (self.track_name)

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

	genre_albums = models.ManyToManyField('Album',
		verbose_name =u"Albums", 
		blank =True,)

	def __unicode__(self):
		return u"%s %s" % (self.genre_name)