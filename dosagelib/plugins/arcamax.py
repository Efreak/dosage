# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class Arcamax(_ParserScraper):
    imageSearch = '//img[@id="comic-zoom"]'
    prevSearch = '//a[@class="prev"]'

    def __init__(self, name, path):
        super(Arcamax, self).__init__('Arcamax/' + name)
        self.url = 'http://www.arcamax.com/thefunnies/' + path + '/'

    @classmethod
    def getmodules(cls):
        return (
            # do not edit anything below since these entries are generated from
            # scripts/arcamax.py
            # START AUTOUPDATE
            # 1AndDone has a duplicate in GoComics/1AndDone
            # 9ChickweedLane has a duplicate in GoComics/9ChickweedLane
            cls('AFBranco', 'afbranco'),
            # Agnes has a duplicate in GoComics/Agnes
            cls('AlGoodwyn', 'algoodwyn'),
            # AndyCapp has a duplicate in GoComics/AndyCapp
            # AndyMarlette has a duplicate in Creators/AndyMarlette
            # Archie has a duplicate in Creators/Archie
            cls('ArcticCircle', 'arcticcircle'),
            # AskShagg has a duplicate in GoComics/AskShagg
            # AuntyAcid has a duplicate in GoComics/AuntyAcid
            cls('BabyBlues', 'babyblues'),
            # BallardStreet has a duplicate in GoComics/BallardStreet
            # BarneyAndClyde has a duplicate in GoComics/BarneyAndClyde
            cls('BarneyGoogleAndSnuffySmith', 'barneygoogle'),
            # BC has a duplicate in GoComics/BC
            cls('BeetleBailey', 'beetlebailey'),
            cls('Bizarro', 'bizarro'),
            cls('Blondie', 'blondie'),
            # BobGorrell has a duplicate in GoComics/BobGorrell
            cls('Boondocks', 'boondocks'),
            # BreakingCatNews has a duplicate in GoComics/BreakingCatNews
            cls('BrianDuffy', 'brianduffy'),
            cls('BrilliantMindOfEdisonLee', 'brilliantmindofedisonlee'),
            # Candorville has a duplicate in GoComics/Candorville
            cls('CarpeDiem', 'carpediem'),
            # Cathy has a duplicate in GoComics/Cathy
            # ChipBok has a duplicate in GoComics/ChipBok
            # ChrisBritt has a duplicate in GoComics/ChrisBritt
            # ClayBennett has a duplicate in GoComics/ClayBennett
            cls('Crankshaft', 'crankshaft'),
            # CulDeSac has a duplicate in GoComics/CulDeSac
            cls('Curtis', 'curtis'),
            cls('DaddyDaze', 'daddydaze'),
            # DaddysHome has a duplicate in GoComics/DaddysHome
            # DarrinBell has a duplicate in GoComics/DarrinBell
            cls('DavidMHitch', 'davidmhitch'),
            cls('DennisTheMenace', 'dennisthemenace'),
            # DiamondLil has a duplicate in GoComics/DiamondLil
            cls('DinetteSet', 'thedinetteset'),
            # DogEatDoug has a duplicate in GoComics/DogEatDoug
            # DogsOfCKennel has a duplicate in GoComics/DogsOfCKennel
            # Doonesbury has a duplicate in GoComics/Doonesbury
            cls('Dustin', 'dustin'),
            cls('EdGamble', 'edgamble'),
            cls('FamilyCircus', 'familycircus'),
            # FloAndFriends has a duplicate in GoComics/FloAndFriends
            # ForBetterOrForWorse has a duplicate in GoComics/ForBetterOrForWorse
            # ForHeavensSake has a duplicate in GoComics/ForHeavensSake
            # FortKnox has a duplicate in GoComics/FortKnox
            # FreeRange has a duplicate in GoComics/FreeRange
            # Garfield has a duplicate in GoComics/Garfield
            # GaryMarkstein has a duplicate in GoComics/GaryMarkstein
            # GaryVarvel has a duplicate in GoComics/GaryVarvel
            # GetFuzzy has a duplicate in GoComics/GetFuzzy
            # GingerMeggs has a duplicate in GoComics/GingerMeggs
            # Heathcliff has a duplicate in GoComics/Heathcliff
            # HerbAndJamaal has a duplicate in GoComics/HerbAndJamaal
            cls('HiAndLois', 'hiandlois'),
            # JeffDanziger has a duplicate in GoComics/JeffDanziger
            cls('JerryKingCartoons', 'humorcartoon'),
            cls('JimmyMargulies', 'jimmymargulies'),
            cls('JohnBranch', 'johnbranch'),
            # JohnDeering has a duplicate in GoComics/JohnDeering
            # KenCatalino has a duplicate in GoComics/KenCatalino
            cls('KirkWalters', 'kirkwalters'),
            cls('LeeJudge', 'leejudge'),
            # LisaBenson has a duplicate in GoComics/LisaBenson
            # LittleDogLost has a duplicate in GoComics/LittleDogLost
            # LongStoryShort has a duplicate in Creators/LongStoryShort
            # LooseParts has a duplicate in GoComics/LooseParts
            # Luann has a duplicate in GoComics/Luann
            cls('MallardFillmore', 'mallardfillmore'),
            # MarshallRamsey has a duplicate in GoComics/MarshallRamsey
            cls('Marvin', 'marvin'),
            cls('MasterStrokesGolfTips', 'masterstrokes'),
            cls('MeaningOfLila', 'meaningoflila'),
            # MichaelRamirez has a duplicate in GoComics/MichaelRamirez
            # MikeDuJour has a duplicate in GoComics/MikeDuJour
            # MikeLester has a duplicate in GoComics/MikeLester
            # MikeLuckovich has a duplicate in GoComics/MikeLuckovich
            cls('MikePeters', 'mikepeters'),
            cls('MikeShelton', 'mikeshelton'),
            cls('MikeSmith', 'mikesmith'),
            # Momma has a duplicate in GoComics/Momma
            cls('MotherGooseAndGrimm', 'mothergooseandgrimm'),
            cls('Mutts', 'mutts'),
            # NestHeads has a duplicate in GoComics/NestHeads
            # NickAnderson has a duplicate in GoComics/NickAnderson
            # NonSequitur has a duplicate in GoComics/NonSequitur
            # OneBigHappy has a duplicate in GoComics/OneBigHappy
            # PaulSzep has a duplicate in GoComics/PaulSzep
            # Peanuts has a duplicate in GoComics/Peanuts
            # PearlsBeforeSwine has a duplicate in GoComics/PearlsBeforeSwine
            # Pickles has a duplicate in GoComics/Pickles
            # PoorlyDrawnLines has a duplicate in GoComics/PoorlyDrawnLines
            # RedAndRover has a duplicate in GoComics/RedAndRover
            # ReplyAll has a duplicate in GoComics/ReplyAll
            cls('RhymesWithOrange', 'rhymeswithorange'),
            # RoseIsRose has a duplicate in GoComics/RoseIsRose
            # Rubes has a duplicate in GoComics/Rubes
            # RudyPark has a duplicate in GoComics/RudyPark
            # Rugrats has a duplicate in Creators/Rugrats
            # SarahsScribbles has a duplicate in GoComics/SarahsScribbles
            # ScaryGary has a duplicate in GoComics/ScaryGary
            # Shoe has a duplicate in GoComics/Shoe
            # SigneWilkinson has a duplicate in GoComics/SigneWilkinson
            cls('Spectickles', 'spectickles'),
            # SpeedBump has a duplicate in GoComics/SpeedBump
            # SteveBenson has a duplicate in GoComics/SteveBenson
            # SteveBreen has a duplicate in GoComics/SteveBreen
            # SteveKelley has a duplicate in GoComics/SteveKelley
            # StrangeBrew has a duplicate in GoComics/StrangeBrew
            cls('TakeItFromTheTinkersons', 'takeitfromthetinkersons'),
            # TheBarn has a duplicate in GoComics/TheBarn
            cls('TheLockhorns', 'thelockhorns'),
            # TheOtherCoast has a duplicate in GoComics/TheOtherCoast
            cls('ThePajamaDiaries', 'thepajamadiaries'),
            cls('TimCampbell', 'timcampbell'),
            # TomStiglich has a duplicate in Creators/TomStiglich
            # WallaceTheBrave has a duplicate in GoComics/WallaceTheBrave
            # WeePals has a duplicate in GoComics/WeePals
            # WizardOfId has a duplicate in GoComics/WizardOfId
            # WorkingItOut has a duplicate in GoComics/WorkingItOut
            # Wumo has a duplicate in GoComics/WuMo
            # ZackHill has a duplicate in GoComics/ZackHill
            cls('Zits', 'zits'),
            # END AUTOUPDATE
        )
