from django.template import Library
from django.conf import settings
from django.utils.safestring import mark_safe
from spellcheckutils.main import get_speller

register = Library()

PUNCTUATION = """.,;:!?()'" """ # stripped from words before checking
HTML_SNIPPET = '<span class="spellingerror">%(word)s</span>' # how to mark misspelled words
HTML_SNIPPET_SUGGEST = '<span class="spellingerror" title="%(suggestions)s">%(word)s</span>'


@register.filter
def spellcheck(value, args='de'):
    """
    Simple template filter which adds a css clas "spellingerror" to mispelled
    words in text to which this filter is applied.
    
    Add something like this to your stylesheet:
    
        span.spellingerror {border-bottom:1px dashed red;}
        
    Currently handles only plain text, not html markup. Returns a safe string,
    so be sure not to run unsafe content through this filter.
    
    Usage:
    
        {{ text|spellcheck }}
        
        or forcing a specific language:
        
        {{ text|spellcheck:"en" }}
    
    """
    try:
        wordlist = value.split()
    except AttributeError:
        wordlist = []
    speller = get_speller(args)
    for i,word in enumerate(wordlist):
        word = word.strip(PUNCTUATION)
        if not speller.check(str(word.encode(settings.DEFAULT_CHARSET))):
            wordlist[i] = wordlist[i].replace(word, HTML_SNIPPET % {'word':word})
    return mark_safe(' '.join(wordlist))


@register.filter
def spellcheck_suggest(value, args='de'):
    """
    The same as ``spellcheck`` (see above) but adds suggestions to wrong words
    in a ``title`` attribute, so that javascript can pick them up.
    
    NOTE: only use one of the templatetags at a time because ``get_speller()``
    will only work correctly on the first call. This problem will be addressed 
    in a later release.
    
    """ 
    try:   
        wordlist = value.split()
    except AttributeError:
        wordlist = []
    speller = get_speller(args)
    for i,word in enumerate(wordlist):
        word = word.strip(PUNCTUATION)
        if not speller.check(str(word.encode(settings.DEFAULT_CHARSET))):
            try:
                s_list = speller.suggest(word)
                suggestions = [unicode(w, 'utf-8') for w in s_list]
                wordlist[i] = wordlist[i].replace(word, HTML_SNIPPET_SUGGEST % {'word':word, 'suggestions': ",".join(suggestions)})
            except:
                wordlist[i] = wordlist[i].replace(word, HTML_SNIPPET_SUGGEST % {'word':word, 'suggestions': ""})
    return mark_safe(' '.join(wordlist))
    
    
    