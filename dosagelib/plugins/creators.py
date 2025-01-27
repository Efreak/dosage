# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper
from ..helpers import indirectStarter


class Creators(_ParserScraper):
    imageSearch = '//a[contains(@class,"fancybox")]/img'
    prevSearch = '//a[@id="nav_prev"]'
    latestSearch = '//div[contains(@class,"caption")]/a'
    starter = indirectStarter

    def __init__(self, name, path, lang=None):
        super(Creators, self).__init__('Creators/' + name)
        self.url = 'https://www.creators.com/features/' + path
        if lang:
            self.lang = lang

    @classmethod
    def getmodules(cls):
        return (
            # Some comics are not listed on the "all" page (too old?)
            cls('CafeconLeche', 'cafe-con-leche'),
            cls('DonaldDuck', 'donald-duck'),
            cls('Flare', 'flare'),
            cls('FlightDeck', 'flight-deck'),
            cls('GirlsAndSports', 'girls-and-sports'),
            cls('HomeOffice', 'stay-at-home-dad'),
            cls('HopeAndDeath', 'hope-and-death'),
            cls('MickeyMouse', 'mickey-mouse'),
            cls('NaturalSelection', 'natural-selection'),
            cls('OffCenter', 'off-center'),
            cls('Recess', 'recess'),
            cls('Rugrats', 'rugrats'),
            cls('TheQuigmans', 'the-quigmans'),
            cls('WinnieThePooh', 'winnie-the-pooh'),
            # do not edit anything below since these entries are generated from
            # scripts/creators.py
            # START AUTOUPDATE
            cls('AFBranco', 'a.f.-branco'),
            # Agnes has a duplicate in GoComics/Agnes
            # AndyCapp has a duplicate in GoComics/AndyCapp
            cls('AndyMarlette', 'andy-marlette'),
            cls('Archie', 'archie'),
            cls('ArchieSpanish', 'archie-spanish', 'es'),
            # AskShagg has a duplicate in GoComics/AskShagg
            # BC has a duplicate in GoComics/BC
            # BobGorrell has a duplicate in GoComics/BobGorrell
            # ChipBok has a duplicate in GoComics/ChipBok
            # ChrisBritt has a duplicate in GoComics/ChrisBritt
            # DaddysHome has a duplicate in GoComics/DaddysHome
            # DiamondLil has a duplicate in GoComics/DiamondLil
            # DogEatDoug has a duplicate in GoComics/DogEatDoug
            # DogsOfCKennel has a duplicate in GoComics/DogsOfCKennel
            # FloAndFriends has a duplicate in GoComics/FloAndFriends
            # ForHeavensSake has a duplicate in GoComics/ForHeavensSake
            # FreeRange has a duplicate in GoComics/FreeRange
            # GaryMarkstein has a duplicate in GoComics/GaryMarkstein
            # GaryVarvel has a duplicate in GoComics/GaryVarvel
            # Heathcliff has a duplicate in GoComics/Heathcliff
            cls('HeathcliffSpanish', 'heathcliff-spanish', 'es'),
            # HerbAndJamaal has a duplicate in GoComics/HerbAndJamaal
            # JohnDeering has a duplicate in GoComics/JohnDeering
            # KenCatalino has a duplicate in GoComics/KenCatalino
            # LibertyMeadows has a duplicate in GoComics/LibertyMeadows
            cls('LongStoryShort', 'long-story-short'),
            # MarshallRamsey has a duplicate in GoComics/MarshallRamsey
            # MichaelRamirez has a duplicate in GoComics/MichaelRamirez
            # MikeLuckovich has a duplicate in GoComics/MikeLuckovich
            # Momma has a duplicate in GoComics/Momma
            # NestHeads has a duplicate in GoComics/NestHeads
            # OneBigHappy has a duplicate in GoComics/OneBigHappy
            # PaulSzep has a duplicate in GoComics/PaulSzep
            # Rubes has a duplicate in GoComics/Rubes
            #cls('Rugrats', 'rugrats'),
            # ScaryGary has a duplicate in GoComics/ScaryGary
            cls('Spectickles', 'spectickles'),
            # SpeedBump has a duplicate in GoComics/SpeedBump
            # SteveBenson has a duplicate in GoComics/SteveBenson
            # SteveBreen has a duplicate in GoComics/SteveBreen
            # SteveKelley has a duplicate in GoComics/SteveKelley
            # StrangeBrew has a duplicate in GoComics/StrangeBrew
            # TheBarn has a duplicate in GoComics/TheBarn
            # TheMeaningOfLila has a duplicate in GoComics/TheMeaningOfLila
            # TheOtherCoast has a duplicate in GoComics/TheOtherCoast
            cls('TomStiglich', 'tom-stiglich'),
            # WeePals has a duplicate in GoComics/WeePals
            # WizardOfId has a duplicate in GoComics/WizardOfId
            cls('WizardOfIdSpanish', 'wizard-of-id-spanish', 'es'),
            # WorkingItOut has a duplicate in GoComics/WorkingItOut
            # ZackHill has a duplicate in GoComics/ZackHill
            # END AUTOUPDATE
        )
