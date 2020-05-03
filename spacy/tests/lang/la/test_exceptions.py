from __future__ import unicode_literals

import pytest

@pytest.mark.parametrize(
    "text,lemma",
    [
        ("Pacem nobiscum pepigistis.", "nos"),
    ],
)
def test_tokenization_lemma_1(la_tokenizer, text, lemma):
    tokens= la_tokenizer(text)
    assert tokens[1].lemma_==lemma



@pytest.mark.parametrize(
    "text,lemma",
    [
        ("Latini, quibuscum Tullo regnante ictum foedus erat, incursionem in agrum Romanum fecerunt", "qui"),
    ],
)
def test_tokenization_lemma_2(la_tokenizer, text, lemma):
    tokens= la_tokenizer(text)
    assert tokens[2].lemma_==lemma



@pytest.mark.parametrize(
    "text,lemma",
    [
        ("Curate haec, sultis, magna diligentia.", "si"),
    ],
)
def test_tokenization_lemma_3(la_tokenizer, text, lemma):
    tokens= la_tokenizer(text)
    assert tokens[3].lemma_==lemma