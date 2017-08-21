# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from catalog.models import Singer, Album, Track, Genre
import random

class Command(BaseCommand):

	args = '<model_name model_name ...>'
	help = "Prints to console name of created objects in a database."


	def handle(self, *args, **options):

		self.stdout.write(
			u'Function of automatic filling of the Database.')

		#singer
		if 'singer' in args:
			singer_name = raw_input(
				u'Input the name of Singer: ')

			singer = Singer(singer_name = singer_name,)
			singer.save()
			self.stdout.write(
				u'Objects %s create in database' % singer)

		#album
		if 'album' in args:
			album_title = raw_input(
				u'Input the name of Album: ')

			album = Album(album_title = album_title,)
			album.save()
			self.stdout.write(
				u'Objects %s create in database' % album)

		#track
		if 'track' in args:
			track_name = raw_input(
				u'Input the name of Track: ')

			track = Track(track_name = track_name,)
			track.save()
			self.stdout.write(
				u'Objects %s create in database' % track)

		#genre
		if 'genre' in args:
			genre_name = raw_input(
				u'Input the name of Genre: ')

			genre = Genre(genre_name = genre_name,)
			genre.save()
			self.stdout.write(
				u'Objects %s create in database' % genre)


		