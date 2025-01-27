# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from .common import _ParserScraper


class ProjectFuture(_ParserScraper):
    imageSearch = '//td[@class="tamid"]/img'
    prevSearch = '//a[./img[@alt="Previous"]]'

    def __init__(self, name, comic, first, last=None):
        super(ProjectFuture, self).__init__('ProjectFuture/' + name)

        self.url = 'http://www.projectfuturecomic.com/' + comic + '.php'
        self.stripUrl = self.url + '?strip=%s'
        self.firstStripUrl = self.stripUrl % first

        if last:
            self.url = self.stripUrl
            self.endOfLife = True

    @classmethod
    def getmodules(cls):
        return (
            cls('AWalkInTheWoods', 'simeon', '1', last='12'),
            cls('BenjaminBuranAndTheArkOfUr', 'ben', '00', last='23'),
            cls('BookOfTenets', 'tenets', '01', last='45'),
            cls('CriticalMass', 'criticalmass', 'cover', last='26'),
            cls('DarkLordRising', 'darklord', '01-00', last='10-10'),
            cls('FishingTrip', 'fishing', '01-00'),
            cls('HeadsYouLose', 'heads', '00-01', last='07-12'),
            cls('NiallsStory', 'niall', '00'),
            cls('ProjectFuture', 'strip', '0'),
            cls('RedValentine', 'redvalentine', '1', last='6'),
            cls('ShortStories', 'shorts', '01-00'),
            cls('StrangeBedfellows', 'bedfellows', '1', last='6'),
            cls('TheAxemanCometh', 'axeman', '01-01', last='02-18'),
            cls('ToCatchADemon', 'daxxon', '01-00', last='03-14'),
            cls('TheDarkAngel', 'darkangel', 'cover', last='54'),
            cls('TheEpsilonProject', 'epsilon', '00-01'),
            cls('TheHarvest', 'harvest', '01-00'),
            cls('TheSierraChronicles', 'sierra', '0', last='29'),
            cls('TheTuppenyMan', 'tuppenny', '00', last='16'),
            cls('TurningANewPage', 'azrael', '1', last='54'),
        )
