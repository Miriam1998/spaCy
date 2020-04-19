# encoding: utf8
from __future__ import unicode_literals

# Initial stopword list taken from Perseus Hopper
# http://www.perseus.tufts.edu/hopper/stopwords
#
# This should be replaced by recent work

STOP_WORDS = set(("ab ac ad adhic aliqui aliquis an ante apud at atque aut "
"autem cum cur de deinde dum ego enim ergo es est et etiam etsi ex fio haud "
"hic iam idem igitur ille in infra inter interim ipse is ita magis modo mox "
"nam ne nec necque neque nisi non nos o ob per possum post pro quae quam quare "
"qui quia quicumque quidem quilibet quis quisnam quisquam quisque quisquis quo "
"quoniam sed si sic sive sub sui sum super suus tam tamen trans tu tum ubi uel "
"uero unus ut".split()))
