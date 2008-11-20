==========================
A spellchecker for Django
==========================

Django-spellcheckutils aims to provide some useful utils for spellchecking
text in django applications.

Currently it implements the following bits:

  * a simple template filter (named spellcheck) to highlight misspelled words
  
Planned:

  * a form-field which can validate input by checking for spelling errors
  * some utils to update/manipulate the users wordlist
  
  
Settings
---------

There is one **optional** Django Settings variable:

    * ASPELL_HOME_DIR : You may set this to a path where the python code has
      write access. This is a workaround for some problems with mod_python.