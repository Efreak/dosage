# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import requests
from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import bounceStarter, queryNamer, indirectStarter, xpath_class
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPNavi


class PandyLand(_WordPressScraper):
    url = 'http://pandyland.net/'
    firstStripUrl = 'http://pandyland.net/1/'


class ParadigmShift(_ParserScraper):
    stripUrl = 'http://www.paradigmshiftmanga.com/ps/%s.html'
    firstStripUrl = stripUrl % 'part-one-equilibrium'
    url = firstStripUrl
    imageSearch = '//div[@id="the-comic"]//img'
    prevSearch = '//a[contains(@class, "previous-comic-link")]'
    latestSearch = '//a[contains(@class, "last-comic-link")]'
    starter = indirectStarter
    currentVolume = 4

    def namer(self, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 1)[-1]
        if not filename.startswith('ps' + str(self.currentVolume)):
            filename = 'ps' + str(self.currentVolume) + '-' + filename
        if pageUrl.rsplit('/', 1)[-1].startswith('part-'):
            self.currentVolume = self.currentVolume - 1
        return filename


class ParallelUniversum(_BasicScraper):
    url = 'http://www.paralleluniversum.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '001-der-comic-ist-tot'
    imageSearch = compile(tagre("img", "src",
                                r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+/)' % rurl) +
                         tagre("span", "class", "prev"))
    help = 'Index format: number-stripname'
    lang = 'de'


class PartiallyClips(_WordPressScraper):
    url = 'http://partiallyclips.com/'
    firstStripUrl = url + 'comic/screaming-woman/'


class PastelDefender(_BasicScraper):
    baseUrl = 'http://www.pasteldefender.com/'
    url = baseUrl + 'coverbackcover.html'
    stripUrl = baseUrl + '%s.html'
    firstStripUrl = stripUrl % 'cover'
    imageSearch = compile(r'<IMG SRC="(images/.+?)" WIDTH="742"')
    prevSearch = compile(r'<A HREF="([^"]+)"><IMG SRC="images/back\.gif"')
    help = 'Index format: nnn'


class PeanutBerrySundae(_ParserScraper):
    baseUrl = 'https://foxyverse.com/'
    url = baseUrl + 'comics/'
    stripUrl = baseUrl + 'peanut-berry-sundae-%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = ('//img[contains(@src, "Page")]',
                   '//img[contains(@src, "page")]')
    latestSearch = '//a[contains(@href, "peanut-berry-sundae")]'
    starter = indirectStarter

    def getPrevUrl(self, url, data):
        # Replace missing navigation links
        pageNum = int(url.replace('-70-2', '-71').rstrip('/').rsplit('-', 1)[-1])
        url = self.stripUrl % str(pageNum - 1)
        return url.replace('-71', '-70-2')


class PebbleVersion(_ParserScraper):
    url = 'http://www.pebbleversion.com/'
    stripUrl = url + 'Archives/Strip%s.html'
    imageSearch = "//table/tr[2]//img"
    prevSearch = '//a[text()="Previous Comic"]'
    help = 'Index format: n (unpadded)'


class PennyAndAggie(_BasicScraper):
    url = 'http://pennyandaggie.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.pennyandaggie\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?p\=\d+)", quote="'") +
                         tagre("img", "src", r'%simages/previous_day\.gif' % rurl, quote=""))
    help = 'Index format: n (unpadded)'


class PennyArcade(_ParserScraper):
    url = 'http://www.penny-arcade.com/comic/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1998/11/18'
    imageSearch = '//div[@id="comicFrame"]//img'
    prevSearch = '//a[%s]' % xpath_class('btnPrev')
    nextSearch = '//a[%s]' % xpath_class('btnNext')
    starter = bounceStarter
    help = 'Index format: yyyy/mm/dd'

    def namer(self, image_url, page_url):
        p = page_url.split('/')
        return '%04d%02d%02d' % (int(p[4]), int(p[5]), int(p[6]))


class PeppermintSaga(_WPNavi):
    url = 'http://www.pepsaga.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '3'
    help = 'Index format: number'
    adult = True


class PeppermintSagaBGR(_WPNavi):
    url = 'http://bgr.pepsaga.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '4'
    help = 'Index format: number'
    adult = True


class PeterAndCompany(_ParserScraper):
    url = 'http://peterandcompany.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '20050101'
    imageSearch = ('//div[@id="page"]//img',
                   '//div[@id="strip"]//img[contains(@src, "strips/")]')
    prevSearch = '//a[./img[contains(@src, "nav_previous")]]'


class PeterAndWhitney(_ParserScraper):
    url = 'http://peterandwhitney.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '20160502'
    imageSearch = '//div[@id="page"]//img'
    prevSearch = '//a[./img[contains(@src, "nav_previous")]]'


class PeterIsTheWolf(_ParserScraper):
    stripUrl = 'http://www.peteristhewolf.com/adult/%s.html'
    url = stripUrl % 'home'
    firstStripUrl = stripUrl % '001'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = ('//a[text()="Previous Page"]',
                  '//a[text()="Previous Story Page"]')
    multipleImagesPerStrip = True
    adult = True

    def getPrevUrl(self, url, data):
        # Fix loop in site navigation
        if url == self.stripUrl % '194':
            return self.stripUrl % '193'
        return super().getPrevUrl(url, data)


class PHDComics(_ParserScraper):
    BROKEN_COMMENT_END = compile(r'--!>')

    baseUrl = 'http://phdcomics.com/'
    url = baseUrl + 'comics.php'
    stripUrl = baseUrl + 'comics/archive.php?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@id="comic2"]'
    prevSearch = '//a[img[contains(@src, "prev_button")]]'
    nextSearch = '//a[img[contains(@src, "next_button")]]'
    help = 'Index format: n (unpadded)'

    # Ugly hack :(
    def _parse_page(self, data):
        data = self.BROKEN_COMMENT_END.sub('-->', data)
        return super(PHDComics, self)._parse_page(data)

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            # video
            self.stripUrl % '1880',
            self.stripUrl % '1669',
        )


class Picklewhistle(_ComicControlScraper):
    url = 'http://www.picklewhistle.com/'


class PicPakDog(_WordPressScraper):
    url = 'http://www.picpak.net/'
    firstStripUrl = url + 'comic/dogs-cant-spell/'


# Keep, because naming is different to PHDComics...
class PiledHigherAndDeeper(PHDComics):
    starter = bounceStarter
    namer = queryNamer('comicid', use_page_url=True)


class Pixel(_BasicScraper):
    url = 'http://pixelcomic.net/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '000.shtml'
    imageSearch = compile(tagre("img", "src", r'(\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(%s\d+\.(?:php|shtml))' % rurl,
                               before="prev"))
    help = 'Index format: nnn'


class PlanescapeSurvival(_BasicScraper):
    url = 'http://planescapecomic.com/'
    stripUrl = url + '%s.html'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img alt="Previous" ')
    help = 'Index format: nnn'


class PlushAndBlood(_ParserScraper):
    url = 'http://www.plushandblood.com/Comic.php'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[./img[contains(@src, "Nav/Prev")]]'


class PokeyThePenguin(_ParserScraper):
    url = 'http://www.yellow5.com/pokey/archive/'
    stripUrl = url + 'index%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//p/img'
    latestSearch = '(//a)[last()]'
    multipleImagesPerStrip = True
    starter = indirectStarter
    help = 'Index format: number'

    def getPrevUrl(self, url, data):
        """Decrease index.html number."""
        mo = compile(r"index(\d+)\.html").search(url)
        num = int(mo.group(1)) - 1
        prefix = url.rsplit('/', 1)[0]
        return "%s/index%d.html" % (prefix, num)


class PoorlyDrawnLines(_ParserScraper):
    url = 'http://poorlydrawnlines.com/comic/'
    firstStripUrl = url + 'campus-characters/'
    imageSearch = '//div[%s]//img' % xpath_class('comic')
    prevSearch = '//a[@rel="prev"]'


class PoppyOPossum(_WordPressScraper):
    baseUrl = 'https://www.poppy-opossum.com/'
    url = baseUrl + '?latest'
    stripUrl = baseUrl + 'comic/%s'
    firstStripUrl = stripUrl % 'a-story'


class PowerNap(_ParserScraper):
    url = 'http://www.powernapcomic.com/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20110617'
    imageSearch = '//img[contains(@src, "/pnap")]'
    prevSearch = '//a[./img[contains(@src, "previous")]]'

    def imageUrlModifier(self, url, data):
        return url.replace('\n', '').strip()

    def getPrevUrl(self, url, data):
        return super().getPrevUrl(url, data).replace('\n', '').strip()


class Precocious(_ParserScraper):
    url = 'http://www.precociouscomic.com/'
    stripUrl = url + 'archive/comic/%s'
    firstStripUrl = stripUrl % '2009/03/09'
    imageSearch = '//img[contains(@src, "/comics/")]'
    prevSearch = '//a[img[contains(@src, "/back_arrow")]]'
    help = 'Index format: yyyy/mm/dd'


class PrinceOfSartar(_WPNavi):
    url = 'http://www.princeofsartar.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'introduction-chapter-1'
    nextSearch = '//a[%s]' % xpath_class('navi-next')
    starter = bounceStarter
    help = 'Index format: name'

    def namer(self, image_url, page_url):
        """Use page URL to contruct a unique name."""
        title = page_url.rsplit('/', 2)[1]
        image_ext = image_url.rsplit('.', 1)[1]
        return '%s.%s' % (title, image_ext)


class PS238(_ParserScraper):
    url = 'http://ps238.nodwick.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '12072006'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@class="comic-nav-base comic-nav-previous"]'
    help = 'Index format: yyyy-mm-dd'


class PvPOnline(_ParserScraper):
    url = 'http://pvponline.com/comic/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'mon-may-04'
    imageSearch = '//section[@class="comic-art"]/img'
    prevSearch = '//div[contains(@class, "comic-nav")]/a[contains(text(), "Prev")]'
