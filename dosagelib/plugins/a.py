# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2018 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape, MULTILINE

from ..util import tagre
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import regexNamer, bounceStarter, indirectStarter
from .common import _WordPressScraper, _WPNavi, _WPNaviIn


class AbbysAgency(_WordPressScraper):
    url = 'https://abbysagency.us/'
    stripUrl = url + 'blog/comic/%s/'
    firstStripUrl = stripUrl % 'a'


class AbstruseGoose(_BasicScraper):
    url = 'http://abstrusegoose.com/'
    rurl = escape(url)
    starter = bounceStarter
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre('img', 'src',
                                r'(http://abstrusegoose\.com/strips/[^<>"]+)'))
    prevSearch = compile(tagre('a', 'href', r'(%s\d+)' % rurl) +
                         r'&laquo; Previous')
    nextSearch = compile(tagre('a', 'href', r'(%s\d+)' % rurl) +
                         r'Next &raquo;')
    help = 'Index format: n (unpadded)'
    textSearch = compile(tagre("img", "title", r'([^"]+)'))

    def namer(self, image_url, page_url):
        index = int(page_url.rstrip('/').split('/')[-1])
        name = image_url.split('/')[-1].split('.')[0]
        return 'c%03d-%s' % (index, name)


class AbsurdNotions(_BasicScraper):
    baseUrl = 'http://www.absurdnotions.org/'
    url = baseUrl + 'page129.html'
    stripUrl = baseUrl + 'page%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre('img', 'src', r'(an[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre('a', 'href', r'([^"]+)') +
                         tagre('img', 'src', r'nprev\.gif'))
    help = 'Index format: n (unpadded)'


class AcademyVale(_BasicScraper):
    url = 'http://www.imagerie.com/vale/'
    stripUrl = url + 'avarch.cgi?%s'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(tagre('img', 'src', r'(avale\d{4}-\d{2}\.gif)'))
    prevSearch = compile(tagre('a', 'href', r'(avarch[^">]+)', quote="") +
                         tagre('img', 'src', r'AVNavBack\.gif'))
    help = 'Index format: nnn'


class Achewood(_BasicScraper):
    url = 'http://www.achewood.com/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '00000000'
    imageSearch = compile(tagre("img", "src", r'(/comic\.php\?date=\d+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)',
                               after="Previous"))
    help = 'Index format: mmddyyyy'
    namer = regexNamer(compile(r'date=(\d+)'))


class ADoemainOfOurOwn(_ParserScraper):
    # Retrieve comic from the Internet Archive
    url = 'https://web.archive.org/web/20170914100348/http://www.doemain.com/index.cgi/2008-11-14'
    firstStripUrl = 'https://web.archive.org/web/20170914104142/http://www.doemain.com/index.cgi/1999-04-24'
    imageSearch = '//img[contains(@src, "strips/")]'
    prevSearch = '//a[./img[@alt="Previous Strip"]]'
    endOfLife = True

    def namer(self, imageUrl, pageUrl):
        # Fix date formatting
        filename = imageUrl.rsplit('/', 1)[-1]
        if len(filename) > 6 and filename[0:6].isdigit():
            month = filename[0:2]
            day = filename[2:4]
            year = ('19' if filename[4] == '9' else '20') + filename[4:6]
            filename = '%s-%s-%s%s' % (year, month, day, filename[6:])
        return filename


class AdventuresOfFifne(_ParserScraper):
    stripUrl = 'http://fifine.purrsia.com/%s.html'
    url = stripUrl % 'COMICS'
    firstStripUrl = stripUrl % 'Fifine01'
    imageSearch = '//img[contains(@src, "jpg")]'
    prevSearch = '//a[text()="PREVIOUS"]'
    multipleImagesPerStrip = True
    endOfLife = True

    def namer(self, imageUrl, pageUrl):
        # Prepend chapter number to image filename
        filename = imageUrl.rsplit('/', 1)[-1]
        if filename[0] == 'p':
            filename = filename.replace('p', '1_p')
        filename = filename.replace('TIL', '2_TIL')
        filename = filename.replace('NS', '3_NS')
        filename = filename.replace('LG', '4_LG')
        filename = filename.replace('WM', '5_WM')
        return filename

    def getPrevUrl(self, url, data):
        # Fix broken navigation links
        if url == self.stripUrl % 'lg06':
            return self.stripUrl % 'lg05'
        return super().getPrevUrl(url, data)


class AfterStrife(_WPNavi):
    baseUrl = 'http://afterstrife.com/'
    stripUrl = baseUrl + '?p=%s'
    url = stripUrl % '262'
    firstStripUrl = stripUrl % '1'
    help = 'Index format: nnn'
    endOfLife = True


class AGirlAndHerFed(_ParserScraper):
    url = 'https://agirlandherfed.com/'
    stripUrl = url + '1.%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic-image"]/img'
    prevSearch = '//div[@id="comic-nav"]/a[.//img[contains(@src, "back")]]'
    help = 'Index format: nnn'


class AHClub(_WPNaviIn):
    baseUrl = 'http://rickgriffinstudios.com/'
    url = baseUrl + 'ah-club/'
    stripUrl = baseUrl + 'comic-post/%s/'
    firstStripUrl = stripUrl % 'cover'
    latestSearch = '//a[contains(@title, "Permanent Link")]'
    starter = indirectStarter
    nav = {
        'ah-club-2-cover': 'ah-club-1-page-24',
        'ah-club-3-cover': 'ah-club-2-page-28',
        'ah-club-4-cover': 'ah-club-3-page-22'
    }

    def getPrevUrl(self, url, data):
        # Links between chapters
        url = url.rstrip('/').rsplit('/', 1)[-1]
        if self.nav and url in self.nav:
            return self.stripUrl % self.nav[url]
        return super().getPrevUrl(url, data)


class AhoiPolloi(_ParserScraper):
    url = 'https://ahoipolloi.blogger.de/'
    stripUrl = url + '?day=%s'
    firstStripUrl = stripUrl % '20060306'
    multipleImagesPerStrip = True
    lang = 'de'
    imageSearch = '//img[contains(@src, "/static/antville/ahoipolloi/")]'
    prevSearch = '//a[contains(@href, "/?day=")]'
    help = 'Index format: yyyymmdd'


class AhoyEarth(_WPNavi):
    url = 'http://www.ahoyearth.com/'


class AirForceBlues(_WordPressScraper):
    url = 'http://farvatoons.com/'
    firstStripUrl = url + 'comic/in-texas-there-are-texans/'


class ALessonIsLearned(_BasicScraper):
    url = 'http://www.alessonislearned.com/'
    prevSearch = compile(tagre("a", "href", r"(index\.php\?comic=\d+)",
                               quote="'") + r"[^>]+previous")
    stripUrl = url + 'index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(cmx/lesson\d+\.[a-z]+)"))
    help = 'Index format: nnn'


class Alice(_WordPressScraper):
    url = 'http://www.alicecomics.com/'
    latestSearch = '//a[text()="Latest Alice!"]'
    starter = indirectStarter


class AlienDice(_WordPressScraper):
    url = 'http://aliendice.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '05162001'

    def getPrevUrl(self, url, data):
        # Fix broken navigation
        if url == self.stripUrl % 'day-29-part-2-page-3-4':
            return self.stripUrl % 'day-29-part-2-page-3-2'
        return super().getPrevUrl(url, data)

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filename
        return imageUrl.rsplit('/', 1)[-1].replace('20010831', '2001-08-31')


class AlienDiceLegacy(_WordPressScraper):
    name = 'AlienDice/Legacy'
    stripUrl = 'http://aliendice.com/comic/%s/'
    url = stripUrl % 'legacy-2-15'
    firstStripUrl = stripUrl % 'legacy-1'


class AlienLovesPredator(_BasicScraper):
    url = 'http://alienlovespredator.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2004/10/12/unavoidable-delay'
    imageSearch = compile(tagre("img", "src", r'([^"]+)',
                                after='border="1" alt="" width="750"'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class AlienShores(_WordPressScraper):
    url = 'http://alienshores.com/alienshores_band/'
    firstStripUrl = url + 'AScomic/updated-cover/'


class AllTheGrowingThings(_BasicScraper):
    url = 'http://growingthings.typodmary.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/04/21/all-the-growing-things'
    imageSearch = compile(tagre("img", "src", r'(%sfiles/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name'


class AlphaLuna(_ParserScraper):
    url = 'https://alphaluna.net/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'issue-1-cover'
    imageSearch = '//main[@id="comic"]//img'
    prevSearch = '//a[@rel="prev"]'


class AlphaLunaSpanish(_ParserScraper):
    name = 'AlphaLuna/Spanish'
    lang = 'es'
    url = 'https://alphaluna.net/spanish/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'issue-1-cover'
    imageSearch = '//main[@id="comic"]//img'
    prevSearch = '//a[@rel="prev"]'


class Altermeta(_ParserScraper):
    url = 'http://altermeta.net/'
    stripUrl = url + 'archive.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[./img[contains(@src, "back")]]'
    nextSearch = '//a[./img[contains(@src, "forward")]]'
    starter = bounceStarter
    help = 'Index format: n (unpadded)'

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rsplit('=', 1)[-1] + '_' + imageUrl.rsplit('/', 1)[-1]


class AltermetaOld(Altermeta):
    url = Altermeta.url + 'oldarchive/index.php'
    stripUrl = Altermeta.url + 'oldarchive/archive.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    prevSearch = compile(r'<a href="([^"]+)">Back')


class AmazingSuperPowers(_BasicScraper):
    url = 'http://www.amazingsuperpowers.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/09/heredity'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/name'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            # video
            self.stripUrl % '2013/05/orbital-deathray-kickstarter',
        )


class AmbersNoBrainers(_ParserScraper):
    baseUrl = 'https://foxyverse.com/'
    url = baseUrl + 'comics/'
    stripUrl = baseUrl + 'ambers-no-brainers-%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "Page")]'
    latestSearch = '//a[contains(@href, "ambers-no-brainers")]'
    starter = indirectStarter

    def getPrevUrl(self, url, data):
        # Replace missing navigation links
        pageNum = int(url.rstrip('/').rsplit('-', 1)[-1])
        return self.stripUrl % str(pageNum - 1)


class Amya(_WordPressScraper):
    url = 'http://www.amyachronicles.com/'


class Anaria(_ParserScraper):
    url = 'https://www.leahbriere.com/anaria-the-witchs-dream/'
    firstStripUrl = url
    imageSearch = '//div[contains(@class, "gallery")]//a'
    multipleImagesPerStrip = True
    endOfLife = True

    def namer(self, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 1)[-1]
        return filename.replace('00.jpg', 'new00.jpg').replace('new', '1')


class Angband(_BasicScraper):
    url = 'http://angband.calamarain.net/'
    stripUrl = url + 'view.php?date=%s'
    firstStripUrl = stripUrl % '2005-12-30'
    imageSearch = compile(tagre("img", "src", r'(comics/Scroll[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?date\=[^"]+)') +
                         "Previous")
    help = 'Index format: yyyy-mm-dd'


class Angels2200(_BasicScraper):
    url = 'http://www.janahoffmann.com/angels/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.janahoffmann\.com/angels/comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "&laquo; Previous")
    help = 'Index format: yyyy/mm/dd/part-<n>-comic-<n>'


class Annyseed(_ParserScraper):
    baseUrl = 'http://www.mirrorwoodcomics.com/'
    url = baseUrl + 'AnnyseedLatest.htm'
    stripUrl = baseUrl + 'Annyseed%s.htm'
    imageSearch = '//div/img[contains(@src, "Annyseed")]'
    prevSearch = '//a[img[@name="Previousbtn"]]'
    help = 'Index format: nnn'
    FIX_RE = compile(r'Annyseed/Finished%20For%20Print/')

    def imageUrlModifier(self, image_url, data):
        return self.FIX_RE.sub('', image_url)

    def link_modifier(self, fromurl, tourl):
        """Fix circular link."""
        if 'Annyseed150' in fromurl and 'Annyseed150' in tourl:
            return self.stripUrl % '149'
        return tourl


class AntiheroForHire(_ParserScraper):
    stripUrl = 'http://www.giantrobot.club/antihero-for-hire/%s'
    firstStripUrl = stripUrl % '2016/6/8/entrance-vigil'
    url = firstStripUrl
    imageSearch = '//div[@class="image-wrapper"]//img[not(@class="thumb-image")]'
    multipleImagesPerStrip = True
    endOfLife = True
    archive = []

    def starter(self):
        # Build list of chapters for navigation
        page = self.getPage(self.url)
        archiveLinks = page.xpath('//ul[@class="archive-group-list"]//a[contains(@class, "archive-item-link")]')
        for link in archiveLinks:
            self.archive.append(link.get('href'))
        return self.archive[0]

    def getPrevUrl(self, url, data):
        # Retrieve previous chapter from list
        index = self.archive.index(url) + 1
        return self.archive[index] if index < len(self.archive) else None


class AppleGeeks(_BasicScraper):
    url = 'http://www.applegeeks.com/'
    stripUrl = url + 'comics/viewcomic.php?issue=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'((?:/comics/)?issue\d+\.jpg)'))
    prevSearch = compile(r'<div class="caption">Previous Comic</div>\s*<p><a href="([^"]+)">', MULTILINE)
    allow_errors = (404,)
    help = 'Index format: n (unpadded)'


class ARedTailsDream(_BasicScraper):
    baseUrl = 'http://www.minnasundberg.fi/'
    stripUrl = baseUrl + 'comic/page%s.php'
    firstStripUrl = stripUrl % '00'
    url = baseUrl + 'comic/recent.php'
    imageSearch = compile(tagre('img', 'src', r'(chapter.+?/eng[^"]*)'))
    prevSearch = compile(tagre('a', 'href', r'(page\d+\.php)') +
                         tagre("img", "src", r'.*?aprev.*?'))
    help = 'Index format: nn'


class ArtificialIncident(_ParserScraper):
    url = 'https://www.artificialincident.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'issue-one-life-changing'
    imageSearch = '//div[@class="webcomic-image"]//img'
    prevSearch = '//a[contains(@class, "previous-webcomic-link")]'


class Ashes(_WordPressScraper):
    url = 'http://www.flowerlarkstudios.com/comicpage/prologue/10232009/'
    firstStripUrl = url
    starter = indirectStarter


class AstronomyPOTD(_ParserScraper):
    baseUrl = 'http://apod.nasa.gov/apod/'
    url = baseUrl + 'astropix.html'
    starter = bounceStarter
    stripUrl = baseUrl + 'ap%s.html'
    firstStripUrl = stripUrl % '061012'
    imageSearch = '//a/img'
    multipleImagesPerStrip = True
    prevSearch = '//a[text()="<"]'
    nextSearch = '//a[text()=">"]'
    help = 'Index format: yymmdd'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return data.xpath('//iframe')  # videos

    def namer(self, image_url, page_url):
        return '%s-%s' % (page_url.split('/')[-1].split('.')[0][2:],
                          image_url.split('/')[-1].split('.')[0])


class ATaleOfTails(_WordPressScraper):
    url = 'http://www.feretta.net/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'a-tale-of-tails-1-0'
    adult = True


class AxeCop(_WordPressScraper):
    url = 'http://axecop.com/comic/season-two/'
