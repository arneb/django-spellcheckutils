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
      read/write access. This is a workaround for some problems with mod_python.
      You need it, if you encounter an error like this one::
      
        *** glibc detected *** double free or corruption (out): 0x0000000000a8f790 ***
        
      This may happen, if for some reason aspell thinks it's home-dir setting
      points to /root and the current user cannot read/write this directory.
      
      
Known Problems
--------------

If you get an error about undefined symbols::
    
    AttributeError: python: undefined symbol: new_aspell_config
    
or with mod_python::

    AttributeError: /usr/sbin/apache2: undefined symbol: new_aspell_config
    
Please have a detailed look at the INSTALL document and install the
aspell-python C-Extension for interfacing with aspell. The ctypes binding 
pyaspell seems to have some problems on some systems.
