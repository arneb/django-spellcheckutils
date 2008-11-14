"""
Main file of django-spellcheckutils, provides a factory function for Speller
objects. Be sure to only use one Speller at a time!

If available uses the C-extension to interface with aspell.
If the C-extension is not available, a system-wide installation of
pyaspell (ctypes port of the C-extension) is used.
If that also fails the bundled version of pyaspell is used.

"""

from django.conf import settings


try:
    from aspell import Speller
    c_aspell = True # see get_speller docstring for why this is needed
except ImportError:
    c_aspell = False
    try:
        from pyaspell import Aspell as Speller
    except ImportError:
        from spellcheckutils.lib.pyaspell import Aspell as Speller
            


def get_speller(lang=settings.LANGUAGE_CODE, encoding=settings.DEFAULT_CHARSET):
    """
    Returns a Speller object ready for checking words.
    
    Note: aspell and pyaspell seem to have a different configkeys format in
    the constructor. Depending on the c_aspell variable the args are adjuseted
    slightly.
    
    """
    args = [('encoding', encoding), ('lang', lang)]
    if not c_aspell:
        args = [args,]
    return Speller(*args)

