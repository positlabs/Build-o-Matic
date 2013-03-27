Build-o-Matic
=============

Python build script for HTML 5 sites.

- Compiles JS from script tags in index.html
- Compiles LESS into CSS
- Optimizes jpgs, pngs, gifs

Note: Currently, the image optimizer will overwrite the original images. To see image compression in action, replace
imgs/ contents with contents of unoptimized_images/


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

3. same for less, but with a different label

	```
	<!-- less desktop.css -->
	```

	```
	[link tags]
	```

	```
	<!-- /less -->
	```

4. in Terminal, navigate to the build-o-matic.py dir, and run it

Dependencies
=============

ImageOptim: http://imageoptim.com/

Must be installed in Applications/ (else you can change where the optimg.py script looks)

LESS: http://lesscss.org/

npm install -g less

CleanCSS: http://davidwalsh.name/clean-css

npm install clean-css




