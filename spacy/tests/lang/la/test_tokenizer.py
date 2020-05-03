from __future__ import unicode_literals

import pytest


tokenize_text=[

#Liber primus[De Vulgari Eloquentia (Dante)]
    #I.I
    (

        "Cum neminem ante nos de vulgaris eloquentie doctrina quicquam inveniamus tractasse,",
        [
            "Cum",
            "neminem",
            "ante",
            "nos",
            "de",
            "vulgaris",
            "eloquentie",
            "doctrina",
            "quicquam",
            "inveniamus",
            "tractasse",
            ","
        ]
    ),

    #II.I
    (
        "Non dico autem «nostra» ut et aliam sit esse locutionem quam hominis: nam eorum que sunt omnium soli homini datum est loqui, cum solum sibi necessarium fuerit.",

        [
            "Non",
            "dico",
            "autem",
            "«",
            "nostra",
            "»",
            "ut",
            "et",
            "aliam",
            "sit",
            "esse",
            "locutionem",
            "quam",
            "hominis",
            ":",
            "nam",
            "eorum",
            "que",
            "sunt",
            "omnium",
            "soli",
            "homini",
            "datum",
            "est",
            "loqui",
            ",",
            "cum",
            "solum",
            "sibi",
            "necessarium",
            "fuerit",
            "."
        ]
    ),

#Catilinarie, 1,3, Cicerone
    (
        "An vero vir amplissimus, P. Scipio, pontefix maximus, Ti. Gracchum mediocriter lebefactantem statum rei publicae, privatus interfecit;",

        [
            "An",
            "vero",
            "vir",
            "amplissimus",
            ",",
            "P.",
            "Scipio",
            ",",
            "pontefix",
            "maximus",
            ",",
            "Ti.",
            "Gracchum",
            "mediocriter",
            "lebefactantem",
            "statum",
            "rei",
            "publicae",
            ",",
            "privatus",
            "interfecit",
            ";"
        ]
    ),
]

@pytest.mark.parametrize("text, expected_token", tokenize_text)
def test_tokenization_with_text(la_tokenizer, text, expected_token):
    tokens= la_tokenizer(text)
    list_token= [token.text for token in tokens]
    assert list_token==expected_token

@pytest.mark.parametrize(
    "text,length",
    [
        ("Quoscumque de te queri audivi, quacumque potui ratione placavi.", 11),
        ("An vero vir amplissimus, P. Scipio, pontefix maximus, Ti. Gracchum mediocriter lebefactantem statum rei publicae, privatus interfecit;", 22),
        ("occicus est cum liberis M. Fulvius consularis.", 8),
    ],
)
def test_tokenization_with_text_length(la_tokenizer, text, length):
    tokens= la_tokenizer(text)
    assert len(tokens)==length