#!/usr/bin/env python

import Wand
import os




def run(projectPath):

	def scrapeUrls():
		filesToScrape = []
		urls = []
		for root, dirs, files in os.walk(projectPath):
			for f in files:
				# TODO  -check if it's an image. if it is, don't push it
				ext = os.path.splitext(f)[1];
				print ext
				if not ext in ['.jpg', ".jpeg", ".gif", ".png"]:
					arr.push(os.path.join(root, f))

		#read in the files, search for instances of image urls
		for f in filesToScrape:
			text = open(f)

		return urls

	urls = scrapeUrls()



run("test_project")