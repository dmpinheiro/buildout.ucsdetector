#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys


def detect(buildout):
    bout = buildout['buildout']
    find_links = bout['find-links']
    if sys.maxunicode > 65536:
        unicode_specific_links = bout['ucs4-links']
    else:
        unicode_specific_links = bout['ucs2-links']
    bout['find-links'] = "\n".join([unicode_specific_links,find_links])
