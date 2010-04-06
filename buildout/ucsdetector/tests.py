#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import doctest
import zc.buildout.testing


def test_suite():
    OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
                            doctest.ELLIPSIS |
                            doctest.NORMALIZE_WHITESPACE)

    suite = doctest.DocFileSuite("README.txt",
             setUp=zc.buildout.testing.buildoutSetUp,
             tearDown=zc.buildout.testing.buildoutTearDown,
             optionflags=OPTIONFLAGS)
           
    return suite
