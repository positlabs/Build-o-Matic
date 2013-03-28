Build-o-Matic
=============

Python build script for HTML 5 sites.

- Compiles JS from script tags
- Compiles LESS into CSS from link tags
- Lossless image optimization of jpgs, pngs, gifs


Instructions
=============
0. install dependencies (see below)
1. open config.py and replace the default values with your own
2. surround script tag groups with build tags

	```
	<!-- build someFile.js -->
	```

	```
	[script tags]
	```

	```
	<!-- /build -->
	```

3. same for css/less, but with a different label

	```
	<!-- styles desktop.css -->
	```

	```
	[css or less link tags]
	```

	```
	<!-- /styles -->
	```

4. on the command line, navigate to the build-o-matic.py dir, and run it

Dependencies
=============

LESS: http://lesscss.org/
-----------
npm install -g less

CleanCSS: http://davidwalsh.name/clean-css
-----------
npm install clean-css

ImageOptim: http://imageoptim.com/
-----------
Must be installed in Applications/ (else you can change where the optimg.py script looks). This will only work on mac.

Trimage: http://trimage.org/
-----------

Alternative to ImageOptim. Added Trimage support to make image optimization cross-platform, but it has an annoying number of dependencies.
- pyqt4 - http://www.riverbankcomputing.com/software/pyqt/download
- - qmake - sudo port install qt4-mac
- - sip - http://www.riverbankcomputing.com/software/sip/download
- optipng - http://optipng.sourceforge.net/
- jpegoptim - http://www.kokkonen.net/tjko/projects.html
- advancecomp - http://advancemame.sourceforge.net/comp-readme.html
- pngcrush - http://pmt.sourceforge.net/pngcrush/
- libjpeg - http://www.ijg.org/files/jpegsrc.v8c.tar.gz


WARNINGS
===========

- Currently, the image optimizer will overwrite the original images. To see image compression in action, replace
imgs/ contents with contents of unoptimized_images/

- the tag scraper doesn't look for comments, so it will compile a script if it's between the build markers