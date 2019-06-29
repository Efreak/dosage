# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import requests

from ..helpers import indirectStarter
from ..scraper import _ParserScraper


class Katbox(_ParserScraper):
    imageSearch = ('//div[@class="webcomic-image"]//img',
                   '//div[contains(@class, "webcomic-media")]//img')
    prevSearch = '//a[contains(@class, "previous-webcomic-link")]'
    latestSearch = '//a[contains(@class, "last-webcomic-link")]'
    starter = indirectStarter

    def __init__(self, name, sub, comic, first, last=None, adult=False, fixNames=False):
        super(Katbox, self).__init__('Katbox/' + name)

        baseUrl = 'http://%s.katbox.net/' % sub

        self.stripUrl = baseUrl + 'comics/%s/'
        if sub == 'cervelet':
            # Special case for Addictive Science
            self.stripUrl = baseUrl + 'comic/%s/'
            self.multipleImagesPerStrip = True
        if comic:
            self.stripUrl = self.stripUrl % (comic + '/%s')

        self.firstStripUrl = self.stripUrl % first

        if last:
            self.url = self.stripUrl % last
            self.starter = super().starter
            self.endOfLife = True
        else:
            self.url = self.firstStripUrl

        if adult:
            self.adult = True
            ageGateCookie = requests.cookies.create_cookie(domain='.katbox.net', name='age_gate', value='18')
            self.session.cookies.set_cookie(ageGateCookie)

        if fixNames:
            self.namer = self.dateNamer

    def fetchUrls(self, url, data, urlSearch):
        self.imageUrls = super().fetchUrls(url, data, urlSearch)
        # Special case for broken navigation in Addictive Science
        if url == 'http://cervelet.katbox.net/comic/addictive-science/easter-egg-5/':
            self.imageUrls = ('http://cervelet.katbox.net/wp-content/uploads/sites/11/ad.Science644.jpg',
                              'http://cervelet.katbox.net/wp-content/uploads/sites/11/ad.Science645.jpg',
                              'http://cervelet.katbox.net/wp-content/uploads/sites/11/ad.Science646.jpg',
                              'http://cervelet.katbox.net/wp-content/uploads/sites/11/ad.Science647.jpg',
                              'http://cervelet.katbox.net/wp-content/uploads/sites/11/ad.Science648.jpg')
        return self.imageUrls

    def dateNamer(self, imageUrl, pageUrl):
        page = self.getPage(pageUrl)
        postDateTime = page.xpath('//div[@class="post-details"]//time')[0].get('datetime')
        index = postDateTime.rsplit('-', 1)[0].replace(':', '-')
        title = pageUrl.rsplit('/', 2)[-2]
        if len(self.imageUrls) > 1:
            title = title + '_' + str(self.imageUrls.index(imageUrl))
        ext = imageUrl.rsplit('.', 1)[-1]
        return  "%s_%s.%s" % (index, title, ext)

    def getPrevUrl(self, url, data):
        # Special case for broken navigation in Addictive Science
        if url == 'http://cervelet.katbox.net/comic/addictive-science/easter-egg-5/':
            return 'http://cervelet.katbox.net/comic/addictive-science/school-stuff-13/'
        return super().getPrevUrl(url, data)


    @classmethod
    def getmodules(cls):
        return (
            cls('AddictiveScience', 'cervelet', 'addictive-science', 'page-1', fixNames=True),
            cls('ArtificialIncident', 'sage', 'ai', 'issue-one-life-changing'),
            cls('CaribbeanBlue', 'nekonny', 'cblue', 'caribbean-blue', last='326-the-end'),
            cls('Debunkers', 'nixie', 'debunkers', 'nixie-the-debunker'),
            cls('DesertFox', 'desertfox', None, 'origins-1', adult=True, fixNames=True),
            cls('Draconia', 'razorfox', None, 'chapter-1-page-1', adult=True),
            cls('Eorah', 'hiorou', 'eorah', 'eorah-title'),
            cls('EtherealWorlds', 'sahtori', 'oasis', '1-nightly-wanderings'),
            cls('IMew', 'nekonny', 'imew', 'imew', last='addictive-imew-16'),
            cls('ItsyBitsyAdventures', 'silverblaze', 'iba', 'fight-the-machine'),
            cls('LasLindas', 'chalo', 'las-lindas', 'day-one', adult=True),
            cls('Olivia', 'kadath', 'olivia', 'misplaced-virtues-title-page', adult=True),
            cls('Paprika', 'nekonny', 'paprika', '001-revolution'),
            cls('PeterAndCompany', 'peterverse', 'peter-and-company', 'strip-1'),
            cls('PeterAndWhitney', 'peterverse', 'peter-and-whitney', 'comic-1-graduation-day'),
            cls('PracticeMakesPerfect', 'nekonny', 'pmp', '001-procrastination'),
            cls('Rascals', 'godai', 'rascals', 'rascals-cover', adult=True),
            cls('TheEyeOfRamalach', 'avencri', 'theeye', 'boxes-and-memories'),
            cls('TheSprawl', 'snowdon', 'sprawl', 'the-sprawl-log01-print-edition-available-now', adult=True),
            cls('TruckOff', 'fox-pop', 'truck-off', 'prologue-00'),
            cls('UberQuest', 'kozmiko', 'uberquest', 'uberquest-chapter-i-temporal-adventure'),
            cls('Yosh', 'sage', 'yosh', 'introduction'),
        )