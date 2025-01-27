# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper

# Comicgenesis has a lot of comics, but most of them are disallowed by
# robots.txt


class ComicGenesis(_ParserScraper):
    multipleImagesPerStrip = True
    imageSearch = '//img[contains(@src, "/comics/")]'
    prevSearch = (
        '//a[img/@alt="Previous comic"]',
        '//a[text()="Previous comic"]',
    )
    help = 'Index format: yyyymmdd'

    def __init__(self, name, sub=None, last=None, baseUrl=None, lang=None, ignoreRobotsTxt=False):
        super(ComicGenesis, self).__init__('ComicGenesis/' + name)

        if sub:
            baseUrl = 'http://%s.comicgenesis.com/' % sub

        self.stripUrl = baseUrl + 'd/%s.html'
        if last:
            self.url = self.stripUrl % last
            self.endOfLife = True
        else:
            self.url = baseUrl

        if lang:
            self.lang = lang

        if ignoreRobotsTxt:
            self.ignoreRobotsTxt = True

    @classmethod
    def getmodules(cls):
        return (
            cls('AAAAA', 'aaaaa'),
            cls('AdventuresofKiltman', 'kiltman'),
            cls('AmorModerno', 'amormoderno'),
            cls('AnythingButRealLife', 'anythingbutreallife'),
            cls('Ardra', 'ardra'),
            cls('Artwork', 'artwork'),
            cls('BabeintheWoods', 'babeinthewoods'),
            cls('BackwaterPlanet', 'bobthespirit'),
            cls('BendyStrawVampires', 'bsvampires'),
            cls('BlindSight', 'blindsight'),
            cls('BreakingtheDoldrum', 'breakingthedoldrum'),
            cls('BrotherSwan', 'warlordofnoodles'),
            cls('Candi', baseUrl='http://candicomics.com/'),
            cls('Cerintha', 'cerintha'),
            cls('CorporateLife', 'corporatelife'),
            cls('CrimsonFury', 'crimsonfury', ignoreRobotsTxt=True),
            cls('DarkWelkin', 'darkwelkin'),
            cls('DeepBlue', 'gjbivin', last='20131109'),
            cls('DemonEater', 'demoneater'),
            cls('Dissonance', 'dissonance'),
            cls('DoodleDiaries', 'doodlediaries'),
            cls('DormSweetDorm', 'dormsweetdorm'),
            cls('DoubleyouTeeEff', 'doubleyouteeeff'),
            cls('DragonsBane', 'jasonwhitewaterz'),
            cls('Dreamaniac', 'dreamaniaccomic'),
            cls('ElnifiChronicles', 'elnifichronicles'),
            cls('EvesApple', 'evesapple'),
            cls('FancyThat', 'fancythat'),
            cls('FantasyQwest', 'creatorauthorman'),
            cls('Fantazine', 'fantazin'),
            cls('FaultyLogic', 'faultylogic', ignoreRobotsTxt=True),
            cls('FightCastOrEvade', 'fightcastorevade', ignoreRobotsTxt=True),
            cls('Flounderville', 'flounderville'),
            cls('GEM', 'keltzy'),
            cls('Gonefor300days', 'g4300d'),
            cls('ImpendingDoom', 'impending'),
            cls('InANutshell', 'nutshellcomics'),
            cls('KernyMantisComics', 'kernymantis'),
            cls('KitsuneJewel', 'kitsunejewel'),
            cls('KittyCattyGames', 'kittycattygames'),
            cls('KiwiDayN', 'kiwidayn'),
            cls('KungFounded', 'kungfounded'),
            cls('LabBratz', 'labbratz'),
            cls('Laserwing', 'laserwing'),
            cls('LumiasKingdom', 'lumia'),
            cls('Majestic7', 'majestic7'),
            cls('MaximumWhimsy', 'maximumwhimsy'),
            cls('MenschUnsererZeitGerman', 'muz', lang='de', last='20090630'),
            cls('MenschUnsererZeit', 'rabe', last='20090630'),
            cls('MoonCrest24', 'mooncrest', last='20121117'),
            cls('Mushian', 'tentoumushi'),
            cls('NightwolfCentral', 'nightwolfcentral'),
            cls('NoneMoreComic', 'nonemore'),
            cls('NoTimeForLife', 'randyraven', last='20100510'),
            cls('OcculTango', 'occultango'),
            cls('ODCKS', 'odcks'),
            cls('OfDoom', 'ofdoom'),
            cls('OpportunityofaLifetime', 'carpathia'),
            cls('Orbz', 'orbz'),
            cls('OwMySanity', 'owmysanity'),
            cls('PhantomThesis', 'phantomthesis'),
            cls('ProfessorSaltinesAstrodynamicDirigible', 'drsaltine'),
            cls('PsychicDyslexiaInstitute', 'pdi'),
            cls('PublicidadeEnganosa', 'publicidadeenganosa'),
            cls('RandomAxeOfKindness', 'randomaxe'),
            cls('SalemUncommons', 'salemuncommons'),
            cls('SamandElisAdventures', 'sameliadv'),
            cls('Sandusky', 'sandusky', ignoreRobotsTxt=True),
            cls('SarahZero', 'plughead'),
            cls('SixByNineCollege', 'sixbyninecollege'),
            cls('SpoononHighandFireontheMountian', 'spoon'),
            cls('SuicideForHire', 'suicideforhire', ignoreRobotsTxt=True),
            cls('SynapticMisfires', 'synapticmisfires'),
            cls('TakingStock', 'mapaghimagsik'),
            cls('TemplarArizona', 'templaraz'),
            cls('TheAdventuresofKaniraBaxter', 'kanirabaxter'),
            cls('TheAdventuresofVindibuddSuperheroInTraining', 'vindibudd', last='20070720'),
            cls('TheEasyBreather', 'easybreather'),
            cls('TheFoxfireChronicles', 'foxfire', ignoreRobotsTxt=True),
            cls('TheMisadventuresofOkk', 'okk'),
            cls('ThePath', 'thepath', '20081226'),
            cls('TheTalesofKalduras', 'kalduras'),
            cls('UmlautHouse', 'umlauthouse', ignoreRobotsTxt=True),
            cls('Unconventional', 'unconventional'),
            cls('WarMageNC17', 'warmage'),
            cls('WebcomicTheWebcomicWebcomicWebcomicWebcomic', 'dannormnsanidey'),
            cls('Wereworld', 'wereworld', ignoreRobotsTxt=True),
            cls('WhatYouDontSee', 'phantomlady4'),
            cls('Wierdman', 'asa'),
        )
