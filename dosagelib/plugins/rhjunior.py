# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class RHJunior(_ParserScraper):
    stripUrl = 'http://www.rhjunior.com/%s/'
    imageSearch = '//div[contains(@class, "entry-content")]//img'
    multipleImagesPerStrip = True

    def __init__(self, name, sub, prev, first, last=None):
        super(RHJunior, self).__init__('RHJunior/' + name)
        self.prevSearch = ('//a[@rel="prev"]', '//a[@title="' + prev + '"]')
        self.url = self.stripUrl % ('comics/' + sub)
        self.firstStripUrl = self.stripUrl % (sub + '-' + first)

        if last:
            self.url = self.stripUrl % (sub + '-' + last)
            self.endOfLife = True

    @classmethod
    def getmodules(cls):
        return (
            cls('GoblinHollow', 'goblin-hollow', '', '0001', last='7'),
            cls('NipAndTuck', 'nip-and-tuck', 'Nip and Tuck', '0000'),
            cls('QuentynQuinnSpaceRanger', 'quentyn-quinn-space-ranger', 'Quentyn Quinn, Space Ranger', '0001'),
            cls('TalesOfTheQuestor', 'tales-of-the-questor', 'Tales of the Questor', 'cover'),
            cls('TheJournalOfEnniasLongscript', 'the-journal-of-ennias-longscript', '', '0001', last='0111'),
            cls('TheProbabilityBomb', 'the-probability-bomb', 'the Probability Bomb', 'kickstarter')
        )
