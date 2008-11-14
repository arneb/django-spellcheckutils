from django.template import Library
from django.conf import settings
from django.utils.safestring import mark_safe
from spellcheckutils.main import get_speller

register = Library()

PUNCTUATION = """.,;:!?()'" """ # stripped from words before checking
HTML_SNIPPET = '<span class="spellingerror">%(word)s</span>' # how to mark misspelled words


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
    wordlist = value.split()
    speller = get_speller(args)
    for i,word in enumerate(wordlist):
        word = word.strip(PUNCTUATION)
        if not speller.check(str(word.encode(settings.DEFAULT_CHARSET))):
            wordlist[i] = wordlist[i].replace(word, HTML_SNIPPET % {'word':word})
    return mark_safe(' '.join(wordlist))

    
    