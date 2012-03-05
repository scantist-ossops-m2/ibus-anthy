# -*- coding: utf-8 -*-
from gi.repository import GObject
from gi.repository import Anthy

anthy = Anthy.GContext()
anthy.set_encoding(Anthy.UTF8_ENCODING)
anthy.init_personality()
anthy.do_set_personality('ibus__ibus_symbol')
anthy.set_string('てすと')
anthy.resize_segment(0, -1)
print anthy.get_nr_segments()
print anthy.get_nr_candidates(0)
print anthy.get_segment(0, 0)
print anthy.commit_segment(0, 0)
anthy.set_prediction_string('てすと')
print anthy.get_nr_predictions()
print anthy.get_prediction(0)
print anthy.commit_prediction(0)
