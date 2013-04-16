Build-o-Matic
=============

Python build script for HTML 5 sites.

- Compiles and minifies JS from script tags
- Generates CSS from LESS files
- Cleans and compiles CSS 
- Lossless image optimization of jpgs, pngs, gifs


Instructions
=============
0. Install dependencies manually, or run install_mac.py if you're on a mac.
1. Open config-example.json and replace the default values with your own
2. Surround script tag groups with build tags

	```
	<!-- build-o-matic someFile.js -->
	```

	```
	[script tags]
	```

	```
	<!-- /build-o-matic -->
	```

3. Same for css/less, but with a css file name

	```
	<!-- build-o-matic desktop.css -->
	```

	```
	[css or less link tags]
	```

	```
	<!-- /build-o-matic -->
	```

4. On the command line, cd to the build-o-matic.py dir, and run it like so
```python
python build-o-matic.py <path/to/config.json>
```

Arguments
-----------
- `-d` `--deploy`: builds, then uploads contents of config.root to config.ftpRoot
- `-D`: just uploads files
- `-o` `--optimg`: builds, then runs image optimizer on all images in config.images
- `-O`: just runs image processor

Dependencies
=============

Python 2.7: http://python.org/download/

LESS: http://lesscss.org/
-----------
npm install -g less

CleanCSS: http://davidwalsh.name/clean-css
-----------
npm install clean-css

Uglify-js: https://github.com/mishoo/UglifyJS
-----------
npm install uglify-js

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
- Currently, the image optimizer will overwrite the original images. Compression is lossless, though.


Future
===========
- Cross-platform compatibility


License
===========
Copyright (c) 2013 Posit Labs

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.