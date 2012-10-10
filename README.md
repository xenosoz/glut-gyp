# gyp-glut

**gyp-glut** is a [gyp](http://code.google.com/p/gyp/)-enabled [OpenGL Utility Toolkit](http://www.opengl.org/resources/libraries/glut/).
Currently using GLUT 3.7 beta from [the official source code distribution](http://www.opengl.org/resources/libraries/glut/glut_downloads.php#2).

It generates both of

* static library (archive)
* shared library w/ import library.

## Portability
Works with *windows only* for now.

## Missing symbols
Note that it has some missing symbols (versus the binary distribution):

    ___glutGetFCB@4
    ___glutSetFCB@8
    __glutCreateMenuWithExit
    __glutCreateWindowWithExit
    __glutInitWithExit

## NOTICE
**gyp-glut** contains original work of Mark J. Kilgard (the GLUT original author, copyright holder) and Nate Robins (win32 port w/ permission of the original author).
As the original project is not open-sourced but freely distributable, any modification under *src* directory *SHOULD NOT* be carried on.
These programs are provided without guarantee or warrantee expressed or implied.
See src/NOTICE, src/README\* also.
