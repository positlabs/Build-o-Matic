#!/usr/bin/env python

# http://docs.wand-py.org/en/0.2-maintenance/index.html
import wand
import os


def run(projectPath):

	def scrapeUrls():
		filesToScrape = []
		urls = []
		for root, dirs, files in os.walk(projectPath):
			for f in files:
				# check if it's an image. if it is, don't push it
				ext = os.path.splitext(f)[1];
				if not ext in ['.jpg', ".jpeg", ".gif", ".png"]:
					path = os.path.join(root, f)
					print path
					filesToScrape.append(path)


		imgRegex = "('|\")(.*)(\.png|\.jpg|\.jpeg|\.gif|\.bmp)"
				#read in the files, search for instances of image urls
		for f in filesToScrape:
			text = open(f, "r").read()
			print "\nreading... ", f

		return urls

	urls = scrapeUrls()



run("../test_project")