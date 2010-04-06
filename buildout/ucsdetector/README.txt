buildout.ucsdetector
********************

The buildout.ucsdetector is a buildout extension that allows define diferent
links according to the UCS (Unicode Character Set) used by the python executable
associated with the buildout process. It's a workaround to provide a way to
install a project with that uses C/Python Unicode API internally and have to
provide support for diferent Python Unicode installations.
At the moment, Python 2.x versions have two python unicode support: UCS2 and
UCS4.
More details about the problem can be found at the `Python Documentation
       <http://docs.python.org/c-api/unicode.html>`_.


Available Options
*****************

- ucs2-links
            Define which dependency links will be added at the find-links option if
            the python process if UCS2 enabled.
        

- ucs4-links
            Define which dependency links will be added at the find-links
            option if the python have UCS4 support.
