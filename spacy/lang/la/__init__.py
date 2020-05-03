# coding: utf8
from __future__ import unicode_literals

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .tag_map import TAG_MAP
from .stop_words import STOP_WORDS
from .lemmatizer import LOOKUP
from ...lemmatizer import Lemmatizer
from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ...language import Language
from ...lookups import Lookups
from ...attrs import LANG, NORM
from ...util import update_exc, add_lookups

def _return_la(_):
    return "la"

class LatinDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters[LANG] = _return_la
    lex_attr_getters[NORM] = add_lookups(Language.Defaults.lex_attr_getters[NORM], BASE_NORMS)
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS
    tag_map = TAG_MAP

"""    @classmethod
    def create_lemmatizer(cls, nlp=None, lookups=None):
        if lookups is None:
            lookups = Lookups()
            lookups.add_table("la_lemma_lookup", LOOKUP)
        return Lemmatizer(lookups)
"""

class Latin(Language):
    lang = "la"
    Defaults = LatinDefaults

__all__ = ['Latin']