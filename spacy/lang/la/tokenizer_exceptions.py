# coding: utf8
from __future__ import unicode_literals

# import symbols – if you need to use more, add them here
from ...symbols import ORTH, LEMMA, TAG, NORM
from ...symbols import ADP, ADJ, PART, PRON, PRON_LEMMA, SCONJ, VERB

_exc = {
    "mecum": [
        {ORTH: "me", LEMMA: "ego", TAG: PRON_LEMMA},
        {ORTH: "cum", TAG: ADP}
    ],
    "tecum": [
        {ORTH: "te", LEMMA: "tu", TAG: PRON_LEMMA},
        {ORTH: "cum", TAG: ADP}
    ],
    "secum": [
        {ORTH: "se", LEMMA: "sui", TAG: PRON_LEMMA},
        {ORTH: "cum", TAG: ADP}
    ],
    "nobiscum": [
        {ORTH: "nobis", LEMMA: "nos", TAG: PRON_LEMMA},
        {ORTH: "cum", TAG: ADP}
    ],
    "vobiscum": [
        {ORTH: "vobis", LEMMA: "vos", TAG: PRON_LEMMA},
        {ORTH: "cum", TAG: ADP}
    ],
    "uobiscum": [
        {ORTH: "uobis", LEMMA: "vos", TAG: PRON_LEMMA},
        {ORTH: "cum", TAG: ADP}
    ],
    "quocum": [
        {ORTH: "quo", LEMMA: "qui", TAG: PRON},
        {ORTH: "cum", TAG: ADP}
    ],
    "quacum": [
        {ORTH: "qua", LEMMA: "qui", TAG: PRON},
        {ORTH: "cum", TAG: ADP}
    ],
    "quicum": [
        {ORTH: "qui", LEMMA: "qui", TAG: PRON},
        {ORTH: "cum", TAG: ADP}
    ],
    "quibuscum": [
        {ORTH: "quibus", LEMMA: "qui", TAG: PRON},
        {ORTH: "cum", TAG: ADP}
    ],
    "sodes": [
        {ORTH: "s", NORM: "si", LEMMA: "si", TAG: SCONJ},
        {ORTH: "odes", NORM: "audes", LEMMA: "audeo", TAG: VERB}
    ],
    "satin": [
        {ORTH: "sati", NORM: "satis", LEMMA: "satis", TAG: ADJ},
        {ORTH: "n", NORM: "ne", LEMMA: "ne", TAG: PART}
    ],
    "scin": [
        {ORTH: "sci", NORM: "scis", LEMMA: "scio", TAG: VERB},
        {ORTH: "n", NORM: "ne", LEMMA: "ne", TAG: PART}
    ],
    "sultis": [
        {ORTH: "s", NORM: "si", LEMMA: "si", TAG: SCONJ},
        {ORTH: "ultis", NORM: "vultis", LEMMA: "volo", TAG: VERB}
    ],
    "similst": [
        {ORTH: "simil", NORM: "similis", LEMMA: "similis", TAG: ADJ},
        {ORTH: "st", NORM: "est", LEMMA: "sum", TAG: VERB}
    ],
    "qualist": [
        {ORTH: "quali", NORM: "qualis", LEMMA: "qualis", TAG: ADJ},
        {ORTH: "st", NORM: "est", LEMMA: "sum", TAG: VERB}
    ],
    "verumst": [
        {ORTH: "verum", LEMMA: "verum", TAG: ADJ},
        {ORTH: "st", NORM: "est", LEMMA: "sum", TAG: VERB}
        ],
    "uerumst": [
        {ORTH: "uerum", LEMMA: "verum", TAG: ADJ},
        {ORTH: "st", NORM: "est", LEMMA: "sum", TAG: VERB}
        ]
}


"""
for exc_data in [
        {ORTH: "A.", LEMMA: "Aulus"},
        {ORTH: "Agr.", LEMMA: "Agrippa"},
        {ORTH: "Ap.", LEMMA: "Appius"},
        {ORTH: "C.", LEMMA: "Gaius"},
        {ORTH: "Cn.", LEMMA: "Gnaeus"},
        {ORTH: "D.", LEMMA: "Decimus"},
        {ORTH: "F.", LEMMA: "Faustus"},
        {ORTH: "K.", LEMMA: "Caeso"},
        {ORTH: "L.", LEMMA: "Lucius"},
        {ORTH: "M'.", LEMMA: "Manius"},
        {ORTH: "M.", LEMMA: "Marcus"},
        {ORTH: "Mam.", LEMMA: "Mamercus"},
        {ORTH: "N", LEMMA: "Numerius"},
        {ORTH: "Oct.", LEMMA: "Octavius"},
        {ORTH: "Opet.", LEMMA: "Opiter"},
        {ORTH: "P.", LEMMA: "Publius"},
        {ORTH: "Post.", LEMMA: "Postumus"},
        {ORTH: "Pro.", LEMMA: "Proculus"},
        {ORTH: "Q.", LEMMA: "Quintus"},
        {ORTH: "S.", LEMMA: "Spurius"},
        {ORTH: "Ser.", LEMMA: "Servius"},
        {ORTH: "Sert.", LEMMA: "Sertor"},
        {ORTH: "Sex.", LEMMA: "Sextus"},
        {ORTH: "St.", LEMMA: "Statius"},
        {ORTH: "T.", LEMMA: "Titus"},
        {ORTH: "Ti.", LEMMA: "Tiberius"},
        {ORTH: "V.", LEMMA: "Vibius"},
        {ORTH: "Vol.", LEMMA: "Volesus"},
        {ORTH: "Vop.", LEMMA: "Vopiscus"},
    ]:
    _exc[exc_data[ORTH]] = [exc_data]
"""
for orth in [
    "P.",
    "Ti.",
    "M.",
]:
    _exc[orth] = [{ORTH: orth}]

TOKENIZER_EXCEPTIONS = _exc
