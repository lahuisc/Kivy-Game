from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
import shelve
import math
import random
from kivy.core.audio import SoundLoader
from kivy.storage.jsonstore import JsonStore
 

# with shelve.open('Data') as data:
# # #     print(dict(data))

store = JsonStore('data.json')


class ImageButton(ButtonBehavior, Image):
    pass

class ImageToggleButton(ToggleButtonBehavior, Image):
    pass

class Manager(ScreenManager):
    pass

class LoadScreen(Screen):
    def set(self):
        with shelve.open('Data') as data:
            store.put('loops', loops = False)

class HomeScreen(Screen):
    
    def playMusic(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('music')['music'] == True:
                app.oneSong.stop()
                app.twoSong.stop()
                app.homeSong.play()
        
    def loadCurrency(self):
        with shelve.open('Data') as data:
            self.ids.coins.text = str(store.get('coins')['coins'])
            self.ids.rubies.text = str(store.get('rubies')['rubies'])
            self.ids.sapphires.text = str(store.get('sapphires')['sapphires'])
            self.ids.emeralds.text = str(store.get('emeralds')['emeralds'])

class StoreScreen(Screen):
    def loadCurrency(self):
        with shelve.open('Data') as data:
            self.ids.coins.text = str(store.get('coins')['coins'])
            self.ids.rubies.text = str(store.get('rubies')['rubies'])
            self.ids.sapphires.text = str(store.get('sapphires')['sapphires'])
            self.ids.emeralds.text = str(store.get('emeralds')['emeralds'])
    
    def basePack(self):
        with shelve.open('Data') as data:
            if store.get('coins')['coins'] >= 100: 
                store.put('coins', coins = store.get('coins')['coins'] - 100)
                self.parent.current = 'basepackscrn'
    
    def elitePack(self):
        with shelve.open('Data') as data:
            if store.get('coins')['coins'] >= 100: 
                store.put('coins', coins = store.get('coins')['coins'] - 500)
                self.parent.current = 'elitepackscrn'
    
    def sapphirePack(self):
        with shelve.open('Data') as data:
            if store.get('coins')['coins'] >= 100: 
                store.put('sapphires', sapphires = store.get('sapphires')['sapphires'] - 1)
                self.parent.current = 'sapphirepackscrn'
    
    def emeraldPack(self):
        with shelve.open('Data') as data:
            if store.get('coins')['coins'] >= 100: 
                store.put('emeralds', emeralds = store.get('emeralds')['emeralds'] - 1)
                self.parent.current = 'emeraldpackscrn'
    
    def rubyPack(self):
        with shelve.open('Data') as data:
            if store.get('coins')['coins'] >= 100: 
                store.put('rubies', rubies = store.get('rubies')['rubies'] - 1)
                self.parent.current = 'rubypackscrn'
              
class ArmyScreen(Screen):
    def loadCurrency(self):
        with shelve.open('Data') as data:
            self.ids.coins.text = str(store.get('coins')['coins'])
            self.ids.rubies.text = str(store.get('rubies')['rubies'])
            self.ids.sapphires.text = str(store.get('sapphires')['sapphires'])
            self.ids.emeralds.text = str(store.get('emeralds')['emeralds'])
    def loadCards(self):
        with shelve.open('Data') as data:
            if store.get('minerUnlocked')['minerUnlocked'] == True:
                self.ids.miner.source = "Images/minercard.png"
            if store.get('swordsmanUnlocked')['swordsmanUnlocked'] == True:
                self.ids.swordsman.source = "Images/swordsmancard.png"
            if store.get('archerUnlocked')['archerUnlocked'] == True:
                self.ids.archer.source = "Images/archercard.png"
            if store.get('pikemanUnlocked')['pikemanUnlocked'] == True:
                self.ids.pikeman.source = "Images/pikemancard.png"
            if store.get('bardUnlocked')['bardUnlocked'] == True:
                self.ids.bard.source = "Images/bardcard.png"
            if store.get('gnomeUnlocked')['gnomeUnlocked'] == True:
                self.ids.gnome.source = "Images/gnomecard.png"
            if data['gnomeminerUnlocked'] == True:
                self.ids.gnomeminer.source = "Images/gnomeminercard.png"
            if data['mageUnlocked'] == True:
                self.ids.mage.source = "Images/magecard.png"
            if data['priestUnlocked'] == True:
                self.ids.priest.source = "Images/priestcard.png"
            if data['crusaderUnlocked'] == True:
                self.ids.crusader.source = "Images/crusadercard.png"
    
    def peasant(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'peasant')
    def miner(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'miner')
            if store.get('minerUnlocked')['minerUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def swordsman(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'swordsman')
            if store.get('swordsmanUnlocked')['swordsmanUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def archer(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'archer')
            if store.get('archerUnlocked')['archerUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def pikeman(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'pikeman')
            if store.get('pikemanUnlocked')['pikemanUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def bard(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'bard')
            if store.get('bardUnlocked')['bardUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def gnome(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'gnome')
            if store.get('gnomeUnlocked')['gnomeUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def gnomeminer(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'gnomeminer')
            if data['gnomeminerUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def mage(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'mage')
            if data['mageUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def priest(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'priest')
            if data['priestUnlocked'] == True:
                self.parent.current = 'upgradescrn'
    def crusader(self):
        with shelve.open('Data') as data:
            store.put('current', current = 'crusader')
            if data['crusaderUnlocked'] == True:
                self.parent.current = 'upgradescrn'

class SettingsScreen(Screen):
    def musictoggle(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('music')['music'] == True:
                store.put('music', music = False)
                app.homeSong.stop()
            else:
                store.put('music', music = True)
                app.homeSong.play()

class StatsScreen(Screen):
    pass

class World1Screen(Screen):
    def playMusic(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('music')['music'] == True:
                app.homeSong.play()

    def loadLevel1(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 1:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 1)

    def loadLevel2(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 2:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 2)
    
    def loadLevel3(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 3:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 3)

    def loadLevel4(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 4:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 4)
        
    def loadLevel5(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 5:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 5)
    
    def loadLevel6(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 6:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 6)

    def loadLevel7(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 7:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 7)

    def loadLevel8(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 8:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 8)

    def loadLevel9(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 9:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 9)

    def loadLevel10(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 10:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 10)
    
    def loadLevel11(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 11:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 11)
    
    def loadLevel12(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 12:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 12)

    def loadLevel13(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 13:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 13)
    
    def loadLevel14(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 14:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 14)
    
    def loadLevel15(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 15:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=True)
                store.put('endless', endlessjson=0)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 15)

    def endless(self):
        with shelve.open('Data') as data:   
            if store.get('unlockedlevel')['unlockedlevel'] >= 15:
                self.parent.current = 'deckscrn'
                store.put('bosslevel', bossleveljson=False)
                store.put('endless', endlessjson=1)
                store.put('endmove', endmovejson=0)
                store.put('level', level = 16)

class World2Screen(Screen):
    pass

class ResetSureScreen(Screen):
    def max(self):  
        store.put('endmove', endmovejson=0)
        store.put('endless', endlessjson=0)
        store.put('bosslevel', bossleveljson=False)
        store.put('bosshealth', bosshealthjson=0)
        store.put('screen', screenjson='none')
        store.put('gamestate', gamestatejson='none')
        store.put('aimg', aimgjson='none')
        store.put('bimg', bimgjson='none')
        store.put('cimg', cimgjson='none')
        store.put('yesdraw1', yesdraw1json=True)
        store.put('yesdraw2', yesdraw2json=True)
        store.put('yesdraw3', yesdraw3json=True)
        store.put('lane', lanejson='top')
        store.put('iron', ironjson=0)
        store.put('readydrop', drop = 'none')
        store.put('selectedcards', cards = 0)
        store.put('level', level = 0)
        store.put('unlockedlevel', unlockedlevel = 150)
        store.put('coins', coins = 10000)
        store.put('rubies', rubies = 10)
        store.put('emeralds', emeralds = 10)
        store.put('sapphires', sapphires = 10)
        store.put('music', music = True)
        store.put('current', current ='Peasant')
        store.put('pack', pack ='none')
        store.put('peasantUnlocked', peasantUnlocked =True)
        store.put('peasantCards', Cards = 0)
        store.put('peasantHealth', Health = 50)
        store.put('peasantHealthLvl', HealthLvl = 1)
        store.put('peasantDamage', Damage = 10)
        store.put('peasantDamageLvl', DamageLvl = 1)
        store.put('peasantSpeed', Speed = 10)
        store.put('peasantSpeedLvl', SpeedLvl = 1)
        store.put('peasantDefense', Defense = 20)
        store.put('peasantDefenseLvl', DefenseLvl = 1)
        store.put('peasantRange', Range = 0)
        store.put('peasantRangeLvl', RangeLvl = 1)
        store.put('peasantCost', Cost = 10)
        store.put('peasantSpecial', Special = 0)
        store.put('peasantSpecialLvl', SpecialLvl = 1)
        store.put('swordsmanUnlocked', swordsmanUnlocked =True)
        store.put('swordsmanCards', Cards = 0)
        store.put('swordsmanHealth', Health = 100)
        store.put('swordsmanHealthLvl', HealthLvl = 1)
        store.put('swordsmanDamage', Damage = 15)
        store.put('swordsmanDamageLvl', DamageLvl = 1)
        store.put('swordsmanSpeed', Speed = 10)
        store.put('swordsmanSpeedLvl', SpeedLvl = 1)
        store.put('swordsmanDefense', Defense = 25)
        store.put('swordsmanDefenseLvl', DefenseLvl = 1)
        store.put('swordsmanRange', Range = 0)
        store.put('swordsmanRangeLvl', RangeLvl = 1)
        store.put('swordsmanCost', Cost = 30)
        store.put('swordsmanSpecial', Special = 0)
        store.put('swordsmanSpecialLvl', SpecialLvl = 1)
        store.put('minerUnlocked', minerUnlocked = True)
        store.put('minerCards', Cards = 0)
        store.put('minerHealth', Health = 70)
        store.put('minerHealthLvl', HealthLvl = 1)
        store.put('minerDamage', Damage = 0)
        store.put('minerDamageLvl', DamageLvl = 1)
        store.put('minerSpeed', Speed = 10)
        store.put('minerSpeedLvl', SpeedLvl = 1)
        store.put('minerDefense', Defense = 25)
        store.put('minerDefenseLvl', DefenseLvl = 1)
        store.put('minerRange', Range = 0)
        store.put('minerRangeLvl', RangeLvl = 1)
        store.put('minerCost', Cost = 20)
        store.put('minerSpecial', Special = 12)
        store.put('minerSpecialLvl', SpecialLvl = 1)
        store.put('archerUnlocked', archerUnlocked = True)
        store.put('archerCards', Cards = 0)
        store.put('archerHealth', Health = 50)
        store.put('archerHealthLvl', HealthLvl = 1)
        store.put('archerDamage', Damage = 6)
        store.put('archerDamageLvl', DamageLvl = 1)
        store.put('archerSpeed', Speed = 10)
        store.put('archerSpeedLvl', SpeedLvl = 1)
        store.put('archerDefense', Defense = 10)
        store.put('archerDefenseLvl', DefenseLvl = 1)
        store.put('archerRange', Range = 6)
        store.put('archerRangeLvl', RangeLvl = 1)
        store.put('archerCost', Cost = 20)
        store.put('archerSpecial', Special = 0)
        store.put('archerSpecialLvl', SpecialLvl = 1)
        store.put('pikemanUnlocked', pikemanUnlocked = True)
        store.put('pikemanCards', Cards = 0)
        store.put('pikemanHealth', Health = 60)
        store.put('pikemanHealthLvl', HealthLvl = 1)
        store.put('pikemanDamage', Damage = 20)
        store.put('pikemanDamageLvl', DamageLvl = 1)
        store.put('pikemanSpeed', Speed = 10)
        store.put('pikemanSpeedLvl', SpeedLvl = 1)
        store.put('pikemanDefense', Defense = 20)
        store.put('pikemanDefenseLvl', DefenseLvl = 1)
        store.put('pikemanRange', Range = 0)
        store.put('pikemanRangeLvl', RangeLvl = 1)
        store.put('pikemanCost', Cost = 30)
        store.put('pikemanSpecial', Special = 0)
        store.put('pikemanSpecialLvl', SpecialLvl = 1)
        store.put('bardUnlocked', bardUnlocked = True)
        store.put('bardCards', Cards = 0)
        store.put('bardHealth', Health = 40)
        store.put('bardHealthLvl', HealthLvl = 1)
        store.put('bardDamage', Damage = 0)
        store.put('bardDamageLvl', DamageLvl = 1)
        store.put('bardSpeed', Speed = 10)
        store.put('bardSpeedLvl', SpeedLvl = 1)
        store.put('bardDefense', Defense = 10)
        store.put('bardDefenseLvl', DefenseLvl = 1)
        store.put('bardRange', Range = 0)
        store.put('bardRangeLvl', RangeLvl = 1)
        store.put('bardCost', Cost = 30)
        store.put('bardSpecial', Special = 5)
        store.put('bardSpecialLvl', SpecialLvl = 1)
        store.put('gnomeUnlocked', gnomeUnlocked = True)
        store.put('gnomeCards', Cards = 0)
        store.put('gnomeHealth', Health = 30)
        store.put('gnomeHealthLvl', HealthLvl = 1)
        store.put('gnomeDamage', Damage = 20)
        store.put('gnomeDamageLvl', DamageLvl = 1)
        store.put('gnomeSpeed', Speed = 10)
        store.put('gnomeSpeedLvl', SpeedLvl = 1)
        store.put('gnomeDefense', Defense = 20)
        store.put('gnomeDefenseLvl', DefenseLvl = 1)
        store.put('gnomeRange', Range = 0)
        store.put('gnomeRangeLvl', RangeLvl = 1)
        store.put('gnomeCost', Cost = 25)
        store.put('gnomeSpecial', Special = 0)
        store.put('gnomeSpecialLvl', SpecialLvl = 1)
        with shelve.open('Data') as data:
            data['gnomeminerUnlocked'] = True
            data['gnomeminerCards'] = 0
            data['gnomeminerHealth'] = 50
            data['gnomeminerHealthLvl'] = 1
            data['gnomeminerDamage'] = 0
            data['gnomeminerDamageLvl'] = 1
            data['gnomeminerSpeed'] = 10
            data['gnomeminerSpeedLvl'] = 1
            data['gnomeminerDefense'] = 50
            data['gnomeminerDefenseLvl'] = 1
            data['gnomeminerRange'] = 0
            data['gnomeminerRangeLvl'] = 1
            data['gnomeminerCost'] = 40
            data['gnomeminerSpecial'] = 24
            data['gnomeminerSpecialLvl'] = 1
            data['mageUnlocked'] = True
            data['mageCards'] = 0
            data['mageHealth'] = 70
            data['mageHealthLvl'] = 1
            data['mageDamage'] = 10
            data['mageDamageLvl'] = 1
            data['mageSpeed'] = 10
            data['mageSpeedLvl'] = 1
            data['mageDefense'] = 25
            data['mageDefenseLvl'] = 1
            data['mageRange'] = 4
            data['mageRangeLvl'] = 1
            data['mageCost'] = 45
            data['mageSpecial'] = 0
            data['mageSpecialLvl'] = 1
            data['priestUnlocked'] = True
            data['priestCards'] = 0
            data['priestHealth'] = 40
            data['priestHealthLvl'] = 1
            data['priestDamage'] = 0
            data['priestDamageLvl'] = 1
            data['priestSpeed'] = 10
            data['priestSpeedLvl'] = 1
            data['priestDefense'] = 25
            data['priestDefenseLvl'] = 1
            data['priestRange'] = 4
            data['priestRangeLvl'] = 1
            data['priestCost'] = 50
            data['priestSpecial'] = 5
            data['priestSpecialLvl'] = 1
            data['crusaderUnlocked'] = True
            data['crusaderCards'] = 0
            data['crusaderHealth'] = 200
            data['crusaderHealthLvl'] = 1
            data['crusaderDamage'] = 20
            data['crusaderDamageLvl'] = 1
            data['crusaderSpeed'] = 10
            data['crusaderSpeedLvl'] = 1
            data['crusaderDefense'] = 25
            data['crusaderDefenseLvl'] = 1
            data['crusaderRange'] = 0
            data['crusaderRangeLvl'] = 1
            data['crusaderCost'] = 70
            data['crusaderSpecial'] = 0
            data['crusaderSpecialLvl'] = 1

    def reset(self):
        store.put('endmove', endmovejson=0)
        store.put('endless', endlessjson=0)
        store.put('bosslevel', bossleveljson=False)
        store.put('bosshealth', bosshealthjson=0)
        store.put('screen', screenjson='none')
        store.put('gamestate', gamestatejson='none')
        store.put('aimg', aimgjson='none')
        store.put('bimg', bimgjson='none')
        store.put('cimg', cimgjson='none')
        store.put('yesdraw1', yesdraw1json=True)
        store.put('yesdraw2', yesdraw2json=True)
        store.put('yesdraw3', yesdraw3json=True)
        store.put('lane', lanejson='top')
        store.put('iron', ironjson=0)
        store.put('readydrop', drop = 'none')
        store.put('selectedcards', cards = 0)
        store.put('level', level = 0)
        store.put('unlockedlevel', unlockedlevel = 1)
        store.put('coins', coins = 0)
        store.put('rubies', rubies = 0)
        store.put('emeralds', emeralds = 0)
        store.put('sapphires', sapphires = 0)
        store.put('music', music = True)
        store.put('current', current ='Peasant')
        store.put('pack', pack ='none')
        store.put('peasantUnlocked', peasantUnlocked =True)
        store.put('peasantCards', Cards = 0)
        store.put('peasantHealth', Health = 50)
        store.put('peasantHealthLvl', HealthLvl = 1)
        store.put('peasantDamage', Damage = 10)
        store.put('peasantDamageLvl', DamageLvl = 1)
        store.put('peasantSpeed', Speed = 10)
        store.put('peasantSpeedLvl', SpeedLvl = 1)
        store.put('peasantDefense', Defense = 20)
        store.put('peasantDefenseLvl', DefenseLvl = 1)
        store.put('peasantRange', Range = 0)
        store.put('peasantRangeLvl', RangeLvl = 1)
        store.put('peasantCost', Cost = 10)
        store.put('peasantSpecial', Special = 0)
        store.put('peasantSpecialLvl', SpecialLvl = 1)
        store.put('swordsmanUnlocked', swordsmanUnlocked = False)
        store.put('swordsmanCards', Cards = 0)
        store.put('swordsmanHealth', Health = 100)
        store.put('swordsmanHealthLvl', HealthLvl = 1)
        store.put('swordsmanDamage', Damage = 15)
        store.put('swordsmanDamageLvl', DamageLvl = 1)
        store.put('swordsmanSpeed', Speed = 10)
        store.put('swordsmanSpeedLvl', SpeedLvl = 1)
        store.put('swordsmanDefense', Defense = 25)
        store.put('swordsmanDefenseLvl', DefenseLvl = 1)
        store.put('swordsmanRange', Range = 0)
        store.put('swordsmanRangeLvl', RangeLvl = 1)
        store.put('swordsmanCost', Cost = 30)
        store.put('swordsmanSpecial', Special = 0)
        store.put('swordsmanSpecialLvl', SpecialLvl = 1)
        store.put('minerUnlocked', minerUnlocked = False)
        store.put('minerCards', Cards = 0)
        store.put('minerHealth', Health = 70)
        store.put('minerHealthLvl', HealthLvl = 1)
        store.put('minerDamage', Damage = 0)
        store.put('minerDamageLvl', DamageLvl = 1)
        store.put('minerSpeed', Speed = 10)
        store.put('minerSpeedLvl', SpeedLvl = 1)
        store.put('minerDefense', Defense = 25)
        store.put('minerDefenseLvl', DefenseLvl = 1)
        store.put('minerRange', Range = 0)
        store.put('minerRangeLvl', RangeLvl = 1)
        store.put('minerCost', Cost = 20)
        store.put('minerSpecial', Special = 12)
        store.put('minerSpecialLvl', SpecialLvl = 1)
        store.put('archerUnlocked', archerUnlocked = False)
        store.put('archerCards', Cards = 0)
        store.put('archerHealth', Health = 50)
        store.put('archerHealthLvl', HealthLvl = 1)
        store.put('archerDamage', Damage = 6)
        store.put('archerDamageLvl', DamageLvl = 1)
        store.put('archerSpeed', Speed = 10)
        store.put('archerSpeedLvl', SpeedLvl = 1)
        store.put('archerDefense', Defense = 10)
        store.put('archerDefenseLvl', DefenseLvl = 1)
        store.put('archerRange', Range = 6)
        store.put('archerRangeLvl', RangeLvl = 1)
        store.put('archerCost', Cost = 20)
        store.put('archerSpecial', Special = 0)
        store.put('archerSpecialLvl', SpecialLvl = 1)
        store.put('pikemanUnlocked', pikemanUnlocked = False)
        store.put('pikemanCards', Cards = 0)
        store.put('pikemanHealth', Health = 60)
        store.put('pikemanHealthLvl', HealthLvl = 1)
        store.put('pikemanDamage', Damage = 20)
        store.put('pikemanDamageLvl', DamageLvl = 1)
        store.put('pikemanSpeed', Speed = 10)
        store.put('pikemanSpeedLvl', SpeedLvl = 1)
        store.put('pikemanDefense', Defense = 20)
        store.put('pikemanDefenseLvl', DefenseLvl = 1)
        store.put('pikemanRange', Range = 0)
        store.put('pikemanRangeLvl', RangeLvl = 1)
        store.put('pikemanCost', Cost = 30)
        store.put('pikemanSpecial', Special = 0)
        store.put('pikemanSpecialLvl', SpecialLvl = 1)
        store.put('bardUnlocked', bardUnlocked = False)
        store.put('bardCards', Cards = 0)
        store.put('bardHealth', Health = 40)
        store.put('bardHealthLvl', HealthLvl = 1)
        store.put('bardDamage', Damage = 0)
        store.put('bardDamageLvl', DamageLvl = 1)
        store.put('bardSpeed', Speed = 10)
        store.put('bardSpeedLvl', SpeedLvl = 1)
        store.put('bardDefense', Defense = 10)
        store.put('bardDefenseLvl', DefenseLvl = 1)
        store.put('bardRange', Range = 0)
        store.put('bardRangeLvl', RangeLvl = 1)
        store.put('bardCost', Cost = 30)
        store.put('bardSpecial', Special = 5)
        store.put('bardSpecialLvl', SpecialLvl = 1)
        store.put('gnomeUnlocked', gnomeUnlocked = False)
        store.put('gnomeCards', Cards = 0)
        store.put('gnomeHealth', Health = 30)
        store.put('gnomeHealthLvl', HealthLvl = 1)
        store.put('gnomeDamage', Damage = 20)
        store.put('gnomeDamageLvl', DamageLvl = 1)
        store.put('gnomeSpeed', Speed = 10)
        store.put('gnomeSpeedLvl', SpeedLvl = 1)
        store.put('gnomeDefense', Defense = 20)
        store.put('gnomeDefenseLvl', DefenseLvl = 1)
        store.put('gnomeRange', Range = 0)
        store.put('gnomeRangeLvl', RangeLvl = 1)
        store.put('gnomeCost', Cost = 25)
        store.put('gnomeSpecial', Special = 0)
        store.put('gnomeSpecialLvl', SpecialLvl = 1)
        with shelve.open('Data') as data:
            data['gnomeminerUnlocked'] = False
            data['gnomeminerCards'] = 0
            data['gnomeminerHealth'] = 50
            data['gnomeminerHealthLvl'] = 1
            data['gnomeminerDamage'] = 0
            data['gnomeminerDamageLvl'] = 1
            data['gnomeminerSpeed'] = 10
            data['gnomeminerSpeedLvl'] = 1
            data['gnomeminerDefense'] = 50
            data['gnomeminerDefenseLvl'] = 1
            data['gnomeminerRange'] = 0
            data['gnomeminerRangeLvl'] = 1
            data['gnomeminerCost'] = 40
            data['gnomeminerSpecial'] = 24
            data['gnomeminerSpecialLvl'] = 1
            data['mageUnlocked'] = False
            data['mageCards'] = 0
            data['mageHealth'] = 70
            data['mageHealthLvl'] = 1
            data['mageDamage'] = 10
            data['mageDamageLvl'] = 1
            data['mageSpeed'] = 10
            data['mageSpeedLvl'] = 1
            data['mageDefense'] = 25
            data['mageDefenseLvl'] = 1
            data['mageRange'] = 4
            data['mageRangeLvl'] = 1
            data['mageCost'] = 45
            data['mageSpecial'] = 0
            data['mageSpecialLvl'] = 1
            data['priestUnlocked'] = False
            data['priestCards'] = 0
            data['priestHealth'] = 40
            data['priestHealthLvl'] = 1
            data['priestDamage'] = 0
            data['priestDamageLvl'] = 1
            data['priestSpeed'] = 10
            data['priestSpeedLvl'] = 1
            data['priestDefense'] = 25
            data['priestDefenseLvl'] = 1
            data['priestRange'] = 4
            data['priestRangeLvl'] = 1
            data['priestCost'] = 50
            data['priestSpecial'] = 5
            data['priestSpecialLvl'] = 1
            data['crusaderUnlocked'] = False
            data['crusaderCards'] = 0
            data['crusaderHealth'] = 200
            data['crusaderHealthLvl'] = 1
            data['crusaderDamage'] = 20
            data['crusaderDamageLvl'] = 1
            data['crusaderSpeed'] = 10
            data['crusaderSpeedLvl'] = 1
            data['crusaderDefense'] = 25
            data['crusaderDefenseLvl'] = 1
            data['crusaderRange'] = 0
            data['crusaderRangeLvl'] = 1
            data['crusaderCost'] = 70
            data['crusaderSpecial'] = 0
            data['crusaderSpecialLvl'] = 1
        self.ids.sure.text = "RESET"

class UpgradeScreen(Screen):
    def select(self):
        with shelve.open('Data') as data:
            self.ids.card.source = "Images/" + str(store.get('current')['current']) + "Card.png"
            self.ids.health.text = str(store.get(str(store.get('current')['current']) + "Health")  ['Health'])
            self.ids.damage.text = str(store.get(str(store.get('current')['current']) + "Damage")  ['Damage'])
            self.ids.defense.text = str(store.get(str(store.get('current')['current']) + "Defense")  ['Defense'])
            self.ids.range.text = str(store.get(str(store.get('current')['current']) + "Range")  ['Range'])
            self.ids.special.text = str(store.get(str(store.get('current')['current']) + "Special")  ['Special'])
            self.ids.cards.text = str(store.get(str(store.get('current')['current']) + "Cards")  ['Cards'])
            self.ids.healthbar.source = "Images/lvl" + str(store.get(str(store.get('current')['current']) + "HealthLvl")  ["HealthLvl"]) + "health.png"
            self.ids.damagebar.source = "Images/lvl" + str(store.get(str(store.get('current')['current']) + "DamageLvl")  ["DamageLvl"]) + "damage.png"
            self.ids.defensebar.source = "Images/lvl" + str(store.get(str(store.get('current')['current']) + "DefenseLvl")  ["DefenseLvl"]) + "defense.png"
            self.ids.rangebar.source = "Images/lvl" + str(store.get(str(store.get('current')['current']) + "RangeLvl")  ["RangeLvl"]) + "range.png"
            self.ids.specialbar.source = "Images/lvl" + str(store.get(str(store.get('current')['current']) + "SpecialLvl")  ["SpecialLvl"]) + "special.png"

    def upgradeHealth(self):
        if (store.get(str(store.get('current')['current']) + "Unlocked")  [str(store.get('current')['current']) + "Unlocked"]) == True:
            if  (store.get(str(store.get('current')['current']) + "Cards")  ["Cards"]) >= (store.get(str(store.get('current')['current']) + "HealthLvl")["HealthLvl"] + 1):
                store.put(str(store.get('current')['current']) + "HealthLvl", HealthLvl = (store.get(str(store.get('current')['current']) + "HealthLvl")["HealthLvl"] + 1))
                store.put(str(store.get('current')['current']) + "Cards", Cards = (store.get(str(store.get('current')['current']) + "Cards") ['Cards'] - (store.get(str(store.get('current')['current']) + "HealthLvl") ['HealthLvl'])))
                store.put(str(store.get('current')['current']) + "Health" , Health = math.ceil(store.get(str(store.get('current')['current']) + "Health")['Health'] * 1.15))
                self.select()
    def upgradeDamage(self):
        if (store.get(str(store.get('current')['current']) + "Unlocked")  [str(store.get('current')['current']) + "Unlocked"]) == True:
            if  (store.get(str(store.get('current')['current']) + "Cards")  ["Cards"]) >= (store.get(str(store.get('current')['current']) + "DamageLvl")["DamageLvl"] + 1):
                store.put(str(store.get('current')['current']) + "DamageLvl", DamageLvl = (store.get(str(store.get('current')['current']) + "DamageLvl")["DamageLvl"] + 1))
                store.put(str(store.get('current')['current']) + "Cards", Cards = (store.get(str(store.get('current')['current']) + "Cards") ['Cards'] - (store.get(str(store.get('current')['current']) + "DamageLvl") ['DamageLvl'])))
                store.put(str(store.get('current')['current']) + "Damage" , Damage = math.ceil(store.get(str(store.get('current')['current']) + "Damage")['Damage'] * 1.15))
                self.select()
    def upgradeDefense(self):
        if (store.get(str(store.get('current')['current']) + "Unlocked")  [str(store.get('current')['current']) + "Unlocked"]) == True:
            if  (store.get(str(store.get('current')['current']) + "Cards")  ["Cards"]) >= (store.get(str(store.get('current')['current']) + "DefenseLvl")["DefenseLvl"] + 1):
                store.put(str(store.get('current')['current']) + "DefenseLvl", DefenseLvl = (store.get(str(store.get('current')['current']) + "DefenseLvl")["DefenseLvl"] + 1))
                store.put(str(store.get('current')['current']) + "Cards", Cards = (store.get(str(store.get('current')['current']) + "Cards") ['Cards'] - (store.get(str(store.get('current')['current']) + "DefenseLvl") ['DefenseLvl'])))
                store.put(str(store.get('current')['current']) + "Defense" , Defense = math.ceil(store.get(str(store.get('current')['current']) + "Defense")['Defense'] * 1.15))
                self.select()
    def upgradeRange(self):
        if (store.get(str(store.get('current')['current']) + "Unlocked")  [str(store.get('current')['current']) + "Unlocked"]) == True:
            if  (store.get(str(store.get('current')['current']) + "Cards")  ["Cards"]) >= (store.get(str(store.get('current')['current']) + "RangeLvl")["RangeLvl"] + 1):
                store.put(str(store.get('current')['current']) + "RangeLvl", RangeLvl = (store.get(str(store.get('current')['current']) + "RangeLvl")["RangeLvl"] + 1))
                store.put(str(store.get('current')['current']) + "Cards", Cards = (store.get(str(store.get('current')['current']) + "Cards") ['Cards'] - (store.get(str(store.get('current')['current']) + "RangeLvl") ['RangeLvl'])))
                store.put(str(store.get('current')['current']) + "Range" , Range = math.ceil(store.get(str(store.get('current')['current']) + "Range")['Range'] * 1.15))
                self.select()
    def upgradeSpecial(self):
        if (store.get(str(store.get('current')['current']) + "Unlocked")  [str(store.get('current')['current']) + "Unlocked"]) == True:
            if  (store.get(str(store.get('current')['current']) + "Cards")  ["Cards"]) >= (store.get(str(store.get('current')['current']) + "SpecialLvl")["SpecialLvl"] + 1):
                store.put(str(store.get('current')['current']) + "SpecialLvl", SpecialLvl = (store.get(str(store.get('current')['current']) + "SpecialLvl")["SpecialLvl"] + 1))
                store.put(str(store.get('current')['current']) + "Cards", Cards = (store.get(str(store.get('current')['current']) + "Cards") ['Cards'] - (store.get(str(store.get('current')['current']) + "SpecialLvl") ['SpecialLvl'])))
                store.put(str(store.get('current')['current']) + "Special" , Special = math.ceil(store.get(str(store.get('current')['current']) + "Special")['Special'] * 1.15))
                self.select()

class BasePackScreen(Screen):
    rng = 0
    def flipCard(self):   
        with shelve.open('Data') as data: 
            if self.ids.card1.source == "Images/cardback.png":
                self.rng = random.randint(0,7)
                if self.rng == 0 or self.rng == 1:
                    self.ids.card1.source = "Images/peasantcard.png"
                    store.put('peasantCards', Cards = store.get('peasantCards')['Cards'] + 1)
                elif self.rng == 2 or self.rng == 3:
                    if store.get('minerUnlocked')['minerUnlocked'] == True:
                        self.ids.card1.source = "Images/minercard.png"
                        store.put('minerCards', Cards = store.get('minerCards')['Cards']  + 1)
                    else:
                        self.flipCard()
                elif self.rng == 4 or self.rng == 5:
                    if store.get('swordsmanUnlocked')['swordsmanUnlocked'] == True:
                        self.ids.card1.source = "Images/swordsmancard.png"
                        store.put('swordsmanCards', Cards = store.get('swordsmanCards')['Cards'] + 1)
                    else:
                        self.flipCard()
                elif self.rng == 6 or self.rng == 7:
                    if store.get('archerUnlocked')['archerUnlocked'] == True:
                        self.ids.card1.source = "Images/archercard.png"
                        store.put('archerCards', Cards = store.get('archerCards')['Cards'] + 1)
                    else:
                        self.flipCard()
              
    def flipCard2(self):
        with shelve.open('Data') as data:   
            if self.ids.card2.source == "Images/cardback.png":
                self.rng = random.randint(0,14)
                if self.rng == 0 or self.rng == 1:
                    self.ids.card2.source = "Images/peasantcard.png"
                    store.put('peasantCards', Cards = store.get('peasantCards')['Cards'] + 1)
                elif self.rng == 2 or self.rng == 3:
                    if store.get('minerUnlocked')['minerUnlocked'] == True:
                        self.ids.card2.source = "Images/minercard.png"
                        store.put('minerCards', Cards = store.get('minerCards')['Cards']  + 1)
                    else:
                        self.flipCard2()
                elif self.rng == 4 or self.rng == 5:
                    if store.get('swordsmanUnlocked')['swordsmanUnlocked'] == True:
                        self.ids.card2.source = "Images/swordsmancard.png"
                        store.put('swordsmanCards', Cards = store.get('swordsmanCards')['Cards'] + 1)
                    else:
                        self.flipCard2()
                elif self.rng == 6 or self.rng == 7:
                    if store.get('archerUnlocked')['archerUnlocked'] == True:
                        self.ids.card2.source = "Images/archercard.png"
                        store.put('archerCards', Cards = store.get('archerCards')['Cards'] + 1)
                    else:
                        self.flipCard2()
                elif self.rng == 8:
                    if store.get('pikemanUnlocked')['pikemanUnlocked'] == True:
                        self.ids.card2.source = "Images/pikemancard.png"
                        store.put('pikemanCards', Cards = store.get('pikemanCards')['Cards'] + 1)
                    else:
                        self.flipCard2()
                elif self.rng == 9:
                    if store.get('bardUnlocked')['bardUnlocked'] == True:
                        self.ids.card2.source = "Images/bardcard.png"
                        store.put('bardCards', Cards = store.get('bardCards')['Cards'] + 1)
                    else:
                        self.flipCard2()
                elif self.rng == 10:
                    if store.get('gnomeUnlocked')['gnomeUnlocked'] == True:
                        self.ids.card2.source = "Images/gnomecard.png"
                        store.put('gnomeCards', Cards = store.get('gnomeCards')['Cards'] + 1)
                    else:
                        self.flipCard2()
                elif self.rng == 11:
                    if data['gnomeminerUnlocked'] == True:
                        self.ids.card2.source = "Images/gnomeminercard.png"
                        data['gnomeminerCards'] = data['gnomeminerCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 12:
                    if data['mageUnlocked'] == True:
                        self.ids.card2.source = "Images/magecard.png"
                        data['mageCards'] = data['mageCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 13:
                    if data['priestUnlocked'] == True:
                        self.ids.card2.source = "Images/priestcard.png"
                        data['priestCards'] = data['priestCards'] + 1
                    else:
                        self.flipCard2()
                elif self.rng == 14:
                    if data['crusaderUnlocked'] == True:
                        self.ids.card2.source = "Images/crusadercard.png"
                        data['crusaderCards'] = data['crusaderCards'] + 1
                    else:
                        self.flipCard2()

    def reset(self):
        self.ids.card2.source = "Images/cardback.png"
        self.ids.card1.source = "Images/cardback.png"

class ElitePackScreen(Screen):
    def reset(self):
        self.ids.card1.source = "Images/cardback.png"
        self.ids.card2.source = "Images/cardback.png"
        self.ids.card3.source = "Images/cardback.png"

class SapphirePackScreen(Screen):
    def reset(self):
        self.ids.card1.source = "Images/cardback.png"

class EmeraldPackScreen(Screen):
    def reset(self):
        self.ids.card1.source = "Images/cardback.png"

class RubyPackScreen(Screen):
    def reset(self):
        self.ids.card1.source = "Images/cardback.png"

class DeckScreen(Screen):
    def start(self):
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] == 8:
                self.ids.chosen.clear_widgets()
                self.parent.current = 'gamescrn'
                

    def loadCards(self):
        with shelve.open('Data') as data:
            if store.get('minerUnlocked')['minerUnlocked'] == True:
                self.ids.miner.source = "Images/minercard.png"
            if store.get('swordsmanUnlocked')['swordsmanUnlocked'] == True:
                self.ids.swordsman.source = "Images/swordsmancard.png"
            if store.get('archerUnlocked')['archerUnlocked'] == True:
                self.ids.archer.source = "Images/archercard.png"
            if store.get('pikemanUnlocked')['pikemanUnlocked'] == True:
                self.ids.pikeman.source = "Images/pikemancard.png"
            if store.get('bardUnlocked')['bardUnlocked'] == True:
                self.ids.bard.source = "Images/bardcard.png"
            if store.get('gnomeUnlocked')['gnomeUnlocked'] == True:
                self.ids.gnome.source = "Images/gnomecard.png"
            if data['gnomeminerUnlocked'] == True:
                self.ids.gnomeminer.source = "Images/gnomeminercard.png"
            if data['mageUnlocked'] == True:
                self.ids.mage.source = "Images/magecard.png"
            if data['priestUnlocked'] == True:
                self.ids.priest.source = "Images/priestcard.png"
            if data['crusaderUnlocked'] == True:
                self.ids.crusader.source = "Images/crusadercard.png"

    def clearCards(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            self.ids.chosen.clear_widgets()
            store.put('selectedcards', cards = 0)
            app.army.clear()

    def addPeasant(self):
        self.peas = Image(source='Images/peasantcard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                self.ids.chosen.add_widget(self.peas)
                store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                app.army.append('peasant')

    def addMiner(self):
        self.peas = Image(source='Images/minercard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if store.get('minerUnlocked')['minerUnlocked'] == True:
                    self.ids.chosen.add_widget(self.peas)
                    store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                    app.army.append('miner')
    
    def addSwordsman(self):
        self.peas = Image(source='Images/swordsmancard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if store.get('swordsmanUnlocked')['swordsmanUnlocked'] == True:
                    self.ids.chosen.add_widget(self.peas)
                    store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                    app.army.append('swordsman')
    
    def addArcher(self):
        self.peas = Image(source='Images/archercard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if store.get('archerUnlocked')['archerUnlocked'] == True:
                    self.ids.chosen.add_widget(self.peas)
                    store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                    app.army.append('archer')
    
    def addPikeman(self):
        self.peas = Image(source='Images/pikemancard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if store.get('pikemanUnlocked')['pikemanUnlocked'] == True:
                    if self.ids.pikeman.source == "Images/pikemancard.png":
                        self.ids.chosen.add_widget(self.peas)
                        store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                        app.army.append('pikeman')
                        self.ids.pikeman.source = "Images/emptycard.png"

    def addBard(self):
        self.peas = Image(source='Images/bardcard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if store.get('bardUnlocked')['bardUnlocked'] == True:
                    if self.ids.bard.source == "Images/bardcard.png":
                        self.ids.chosen.add_widget(self.peas)
                        store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                        app.army.append('bard')
                        self.ids.bard.source = "Images/emptycard.png"
    
    def addGnome(self):
        self.peas = Image(source='Images/gnomecard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if store.get('gnomeUnlocked')['gnomeUnlocked'] == True:
                    if self.ids.gnome.source == "Images/gnomecard.png":
                        self.ids.chosen.add_widget(self.peas)
                        store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                        app.army.append('gnome')
                        self.ids.gnome.source = "Images/emptycard.png"
                    
    def addGnomeminer(self):
        self.peas = Image(source='Images/gnomeminercard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if data['gnomeminerUnlocked'] == True:
                    if self.ids.gnomeminer.source == "Images/gnomeminercard.png":
                        self.ids.chosen.add_widget(self.peas)
                        store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                        app.army.append('gnomeminer')
                        self.ids.gnomeminer.source = "Images/emptycard.png"
    
    def addMage(self):
        self.peas = Image(source='Images/magecard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if data['mageUnlocked'] == True:
                    if self.ids.mage.source == "Images/magecard.png":
                        self.ids.chosen.add_widget(self.peas)
                        store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                        app.army.append('mage')
                        self.ids.mage.source = "Images/emptycard.png"

    def addPriest(self):
        self.peas = Image(source='Images/priestcard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if data['priestUnlocked'] == True:
                    if self.ids.priest.source == "Images/priestcard.png":
                        self.ids.chosen.add_widget(self.peas)
                        store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                        app.army.append('priest')
                        self.ids.priest.source = "Images/emptycard.png"

    def addCrusader(self):
        self.peas = Image(source='Images/crusadercard.png')
        self.peas.size_hint= 0.12,4
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('selectedcards') ['cards'] <= 7:
                if data['crusaderUnlocked'] == True:
                    if self.ids.crusader.source == "Images/crusadercard.png":
                        self.ids.chosen.add_widget(self.peas)
                        store.put('selectedcards', cards = store.get('selectedcards') ['cards'] + 1)
                        app.army.append('crusader')
                        self.ids.crusader.source = "Images/emptycard.png"

class GameScreen(Screen):


    top = []
    middle = []
    bottom = []

    def loadCurrency(self):
        with shelve.open('Data') as data:
            self.ids.coins.text = str(store.get('coins')['coins'])

    class entity():
        def __init__(self, imgstr, health, damage, speed, range, defense, defensetype, special, specialtype, attacktype, alive, x, row, side, tile, sprite, animate, direction, ore):
            self.imgstr = imgstr
            self.health = health
            self.damage = damage
            self.speed = speed
            self.range = range
            self.defense = defense
            self.defensetype = defensetype
            self.special = special
            self.specialtype = specialtype
            self.attacktype = attacktype
            self.alive = alive
            self.x = x
            self.row = row
            self.side = side
            self.tile = tile
            self.sprite = sprite
            self.animate = animate
            self.direction = direction
            self.ore = ore

    def updateIron(self):
        with shelve.open('Data') as data:
            self.ids.ironcount.text = str(store.get('iron')['ironjson'])
            self.ids.coins.text = str(store.get('coins')['coins'])
        
    def updateIron2(self, dt):
        with shelve.open('Data') as data:
            self.ids.ironcount.text = str(store.get('iron')['ironjson'])

    def addIron(self, *args):
        store.put('iron', ironjson = (store.get('iron')['ironjson'])+ 1)

    def black1(self):
        self.ids.a.source = 'Images/blackcard.png'

    def black2(self):
        self.ids.b.source = 'Images/blackcard.png'
    
    def black3(self):
        self.ids.c.source = 'Images/blackcard.png'

    def holeLoop(self, dt):
        for i in self.top:
                if i.side == 'hole':
                    char = Image(source = "Images/" + i.imgstr + ".png")
                    char.size_hint = 0.013, 0.43
                    xlocation = (i.tile * 0.005) 
                    char.pos_hint = {'x':xlocation, 'top':1.11}
                    char.fit_mode = "fill"
                    self.ids.troop.add_widget(char)
        for i in self.middle:
                if i.side == 'hole':
                    char = Image(source = "Images/" + i.imgstr + ".png")
                    char.size_hint = 0.013, 0.43
                    xlocation = (i.tile * 0.005) 
                    char.pos_hint = {'x':xlocation, 'top':0.805}
                    char.fit_mode = "fill"
                    self.ids.troop.add_widget(char)
        for i in self.bottom:
                if i.side == 'hole':
                    char = Image(source = "Images/" + i.imgstr + ".png")
                    char.size_hint = 0.013, 0.43
                    xlocation = (i.tile * 0.005) 
                    char.pos_hint = {'x':xlocation, 'top':0.5}
                    char.fit_mode = "fill"
                    self.ids.troop.add_widget(char)

    def loop(self, dt):
        
        with shelve.open('Data') as data:
            self.ids.troop.clear_widgets()
            store.put('gamestate', gamestatejson='none')
            for i in self.top:
                if i.alive == False:
                    self.top.remove(i)
                if i.alive == True and i.side == 'good':
                    if i.tile == 63:
                        self.top.remove(i)
                    else:
                        if i.attacktype == "meele":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for hit in self.top:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1):
                                            i.animate = 10
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'right':
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + '1' + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                            elif any(b.side == 'hole' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for b in self.top:
                                        if b.imgstr == 'regularore':
                                            i.direction = 'left'
                                            i.ore = 'regular'
                                        if b.imgstr == 'packedore':
                                            i.direction = 'left'
                                            i.ore = 'packed'
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile >= 1:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.14}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.ore == 'regular':
                                if i.animate >= 24:
                                    i.animate = 17
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                            if i.ore == 'packed':
                                if i.animate >= 32 or i.animate <=23:
                                    i.animate = 25
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile <= 0:
                            if i.ore == 'regular':
                                i.direction = 'right'
                                store.put('iron', ironjson = (store.get('iron')['ironjson']) + (i.special))
                            if i.ore == 'packed':
                                i.direction = 'right'
                                store.put(('iron'), ironjson = ((store.get('iron')['ironjson']) + (i.special)) * 1.5)
                        elif i.attacktype == "spear":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.top:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1 or hit.tile == i.tile + 2):
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000072)
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "range":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.top:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'range':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "bard":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                i.animate = 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.14}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                    rng = random.randint(0, store.get('bardSpecial')['Special'])
                                    if rng >= 3:
                                        store.put('iron', ironjson = (store.get('iron')['ironjson']) + 1)
                                    if rng == 2:
                                        store.put('coins', coins = store.get('coins')['coins'] + 1)
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "magic":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.top:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'magic':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "healer":
                            if any(b.side == 'good' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.top):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.top:
                                        if hit.side == 'good' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):    
                                            hit.health = hit.health + i.special
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':1.11}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
            for i in self.middle:
                if i.alive == False:
                    self.middle.remove(i)
                if i.alive == True and i.side == 'good':
                    if i.tile == 63:
                        self.middle.remove(i)
                    else:
                        if i.attacktype == "meele":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for hit in self.middle:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1):
                                            i.animate = 10
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'right':
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + '1' + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                            elif any(b.side == 'hole' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for b in self.middle:
                                        if b.imgstr == 'regularore':
                                            i.direction = 'left'
                                            i.ore = 'regular'
                                        if b.imgstr == 'packedore':
                                            i.direction = 'left'
                                            i.ore = 'packed'
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile >= 1:      
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.ore == 'regular':
                                if i.animate >= 24:
                                    i.animate = 17
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                            if i.ore == 'packed':
                                if i.animate >= 32 or i.animate <=23:
                                    i.animate = 25
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile <= 0:
                            if i.ore == 'regular':
                                i.direction = 'right'
                                store.put('iron', ironjson = (store.get('iron')['ironjson']) + (i.special))
                            if i.ore == 'packed':
                                i.direction = 'right'
                                store.put('iron', ironjson = math.ceil((store.get('iron')['ironjson']) +((i.special) * 1.5)))
                        elif i.attacktype == "spear":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.middle:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1 or hit.tile == i.tile + 2):
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000072)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "range":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.middle:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'range':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "bard":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                i.animate = 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                    rng = random.randint(0, store.get('bardSpecial')['Special'])
                                    if rng >= 3:
                                        store.put('iron', ironjson = (store.get('iron')['ironjson']) + 1)
                                    if rng == 2:
                                        store.put('coins', coins = store.get('coins')['coins'] + 1)
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "magic":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.middle:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'magic':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "healer":
                            if any(b.side == 'good' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.middle):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.middle:
                                        if hit.side == 'good' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):    
                                            hit.health = hit.health + i.special
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.805}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
            for i in self.bottom:
                if i.alive == False:
                    self.bottom.remove(i)
                if i.alive == True and i.side == 'good':
                    if i.tile == 63:
                        self.bottom.remove(i)
                    else:
                        if i.attacktype == "meele":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for hit in self.bottom:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1):
                                            i.animate = 10
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'right':
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + '1' + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                            elif any(b.side == 'hole' and (b.tile == i.tile or b.tile == i.tile + 1) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    for b in self.bottom:
                                        if b.imgstr == 'regularore':
                                            i.direction = 'left'
                                            i.ore = 'regular'
                                        if b.imgstr == 'packedore':
                                            i.direction = 'left'
                                            i.ore = 'packed'
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile >= 1:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.ore == 'regular':
                                if i.animate >= 24:
                                    i.animate = 17
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                            if i.ore == 'packed':
                                if i.animate >= 32 or i.animate <=23:
                                    i.animate = 25
                                    i.tile = i.tile - 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "mine" and i.direction == 'left' and i.tile <= 0:
                            if i.ore == 'regular':
                                i.direction = 'right'
                                store.put('iron', ironjson = (store.get('iron')['ironjson']) + (i.special))
                            if i.ore == 'packed':
                                i.direction = 'right'
                                store.put('iron', ironjson = math.ceil((store.get('iron')['ironjson']) +((i.special) * 1.5)))
                        elif i.attacktype == "spear":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.bottom:
                                        if hit.side == 'bad' and (hit.tile == i.tile or hit.tile == i.tile + 1 or hit.tile == i.tile + 2):
                                            if hit.defensetype == 'meele':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.016, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000072)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "range":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.bottom:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'range':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.specialtype == "bard":
                            if any(b.side == 'bad' and (b.tile == i.tile or b.tile == i.tile + 1 or b.tile == i.tile + 2) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                i.animate = 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                    rng = random.randint(0, store.get('bardSpecial')['Special'])
                                    if rng >= 3:
                                        store.put('iron', ironjson = (store.get('iron')['ironjson']) + 1)
                                    if rng == 2:
                                        store.put('coins', coins = store.get('coins')['coins'] + 1)
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "magic":
                            if any(b.side == 'bad' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.bottom:
                                        if hit.side == 'bad' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):
                                            if hit.defensetype == 'magic':
                                                fac = (100 - hit.defense)/100
                                                hit.health = hit.health - (i.damage * fac)
                                            if hit.attacktype == 'boss':
                                                store.put('bosshealth', bosshealthjson = store.get('bosshealth')['bosshealthjson'] - i.damage)
                                                hit.health = hit.health - i.damage 
                                            else:
                                                hit.health = hit.health - i.damage
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1
                        elif i.attacktype == "healer":
                            if any(b.side == 'good' and (b.tile >= i.tile and b.tile <= i.tile + i.range) for b in self.bottom):
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) 
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 16:
                                    i.animate = 10
                                    for hit in self.bottom:
                                        if hit.side == 'good' and (hit.tile >= i.tile and hit.tile <= i.tile + i.range):    
                                            hit.health = hit.health + i.special
                                            if hit.health <= 0:
                                                hit.alive = False
                                else: 
                                    i.animate = i.animate + 1
                            else:
                                char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                                char.size_hint = 0.013, 0.43
                                xlocation = (i.tile * 0.005) + ((i.animate - 2) * 0.000062)
                                char.pos_hint = {'x':xlocation, 'top':0.5}
                                char.fit_mode = "fill"
                                self.ids.troop.add_widget(char)
                                if i.animate >= 9:
                                    i.animate = 2
                                    i.tile = i.tile + 1
                                else: 
                                    i.animate = i.animate + 1

    def loopBad(self, dt):
        with shelve.open('Data') as data:
            for i in self.top:
                if i.alive == False:
                    if i.side == 'bad':
                        store.put('coins', coins = store.get('coins')['coins'] + 1)
                    self.top.remove(i)
                if i.alive == True and i.side == 'bad':
                    if i.attacktype == "meele":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1) for b in self.top):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "spear":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1 or b.tile == i.tile - 2) for b in self.top):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1 or hit.tile == i.tile - 2):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000072)
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "range":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.top):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'range':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "magic":

                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.top):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'magic':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.11}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "boss":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.top) or any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.middle) or any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.025, 1
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':1.05}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'boss':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                                for hit in self.middle:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'boss':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                                for hit in self.bottom:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'boss':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.025, 1
                            xlocation = (i.tile * 0.005) - (0.000062)
                            char.pos_hint = {'x':xlocation, 'top':1.05}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile
                            else: 
                                i.animate = i.animate + 1
            for i in self.middle:
                if i.alive == False:
                    if i.side == 'bad':
                        store.put('coins', coins = store.get('coins')['coins'] + 1)
                    self.middle.remove(i)
                if i.alive == True and i.side == 'bad':
                    if i.attacktype == "meele":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.middle:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "spear":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1 or b.tile == i.tile - 2) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1 or hit.tile == i.tile - 2):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000072)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "range":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.middle:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'range':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "magic":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.middle:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'magic':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "boss":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.middle):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.805}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile
                            else: 
                                i.animate = i.animate + 1
            for i in self.bottom:
                if i.alive == False:
                    if i.side == 'bad':
                        store.put('coins', coins = store.get('coins')['coins'] + 1)
                    self.bottom.remove(i)
                if i.alive == True and i.side == 'bad':
                    if i.attacktype == "meele":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.bottom:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "spear":
                        if any(b.side == 'good' and (b.tile == i.tile or b.tile == i.tile - 1 or b.tile == i.tile - 2) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.48
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.top:
                                    if hit.side == 'good' and (hit.tile == i.tile or hit.tile == i.tile - 1 or hit.tile == i.tile - 2):
                                        if hit.defensetype == 'meele':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.016, 0.48
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000072)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "range":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.bottom:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'range':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "magic":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                                for hit in self.bottom:
                                    if hit.side == 'good' and (hit.tile <= i.tile and hit.tile >= i.tile - i.range):
                                        if hit.defensetype == 'magic':
                                            fac = (100 - hit.defense)/100
                                            hit.health = hit.health - (i.damage * fac)
                                        else:
                                            hit.health = hit.health - i.damage
                                        if hit.health <= 0:
                                            hit.alive = False
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile - 1
                            else: 
                                i.animate = i.animate + 1
                    elif i.attacktype == "boss":
                        if any(b.side == 'good' and (b.tile <= i.tile and b.tile >= i.tile - i.range) for b in self.bottom):
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) 
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 16:
                                i.animate = 10
                            else: 
                                i.animate = i.animate + 1
                        else:
                            char = Image(source = "Images/" + i.imgstr + str(i.animate) + ".png")
                            char.size_hint = 0.013, 0.43
                            xlocation = (i.tile * 0.005) - ((i.animate - 2) * 0.000062)
                            char.pos_hint = {'x':xlocation, 'top':0.5}
                            char.fit_mode = "fill"
                            self.ids.troop.add_widget(char)
                            if i.animate >= 9:
                                i.animate = 2
                                i.tile = i.tile
                            else: 
                                i.animate = i.animate + 1

    def gameStateTest(self, dt):
        with shelve.open('Data') as data:
            if store.get('endless') ['endlessjson'] >= 1:
                if store.get('screen') ['screenjson'] == 'game':
                    if any (i.side == 'bad' and i.tile <= 0 for i in self.top):
                        store.put('gamestate', gamestatejson='lose')
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.middle):
                        store.put('gamestate', gamestatejson='lose')
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.bottom):
                        store.put('gamestate', gamestatejson='lose')
                    elif any (i.side == 'bad' and i.alive == True for i in self.top):
                        store.put('gamestate', gamestatejson='none')
                    elif any (i.side == 'bad' and i.alive == True for i in self.middle):
                        store.put('gamestate', gamestatejson='none')
                    elif any (i.side == 'bad' and i.alive == True for i in self.bottom):
                        store.put('gamestate', gamestatejson='none')
                    else:
                        store.put('gamestate', gamestatejson='win')
            if store.get('bosslevel') ['bossleveljson'] == False:
                if store.get('screen') ['screenjson'] == 'game':
                    if any (i.side == 'bad' and i.tile <= 0 for i in self.top):
                        store.put('gamestate', gamestatejson='lose')
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.middle):
                        store.put('gamestate', gamestatejson='lose')
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.bottom):
                        store.put('gamestate', gamestatejson='lose')
                    elif any (i.side == 'bad' and i.alive == True for i in self.top):
                        store.put('gamestate', gamestatejson='none')
                    elif any (i.side == 'bad' and i.alive == True for i in self.middle):
                        store.put('gamestate', gamestatejson='none')
                    elif any (i.side == 'bad' and i.alive == True for i in self.bottom):
                        store.put('gamestate', gamestatejson='none')
                    else:
                        store.put('gamestate', gamestatejson='win')
            if store.get('bosslevel') ['bossleveljson'] == True:
                if store.get('screen') ['screenjson'] == 'game':
                    if any (i.side == 'bad' and i.tile <= 0 for i in self.top):
                        store.put('gamestate', gamestatejson='lose')
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.middle):
                        store.put('gamestate', gamestatejson='lose')
                    elif any (i.side == 'bad' and i.tile <= 0 for i in self.bottom):
                        store.put('gamestate', gamestatejson='lose')
                    elif store.get('bosshealth')['bosshealthjson'] <= 0:
                        store.put('gamestate', gamestatejson='win')
            if store.get('screen') ['screenjson'] == 'game':   
                if store.get('gamestate') ['gamestatejson'] == 'win':
                    if store.get('endless') ['endlessjson'] >= 1:
                        self.parent.current = 'deckscrn'
                        store.put('endless', endlessjson= store.get('endless') ['endlessjson'] + 2)
                        store.put('endmove', endmovejson=0)
                        self.clearCards
                        store.put('screen', screenjson='none')
                        self.ids.endless.text = str(math.ceil(((store.get('endless') ['endlessjson'])/2)))
                    else: 
                        self.clearCards
                        self.parent.current = 'winscrn'
                        store.put('screen', screenjson='none')
                if store.get('gamestate') ['gamestatejson'] == 'lose':
                    self.clearCards
                    self.parent.current = 'losescrn'
                    store.put('screen', screenjson='none')

    def randomAdd(self, dt):
        with shelve.open('Data') as data:
            print (str(data['endmove']))
            rng = random.randint(0,7)
            if rng == 0:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('skeleton', 50 + store.get('endless') ['endlessjson'], 10, 10, 0, 20 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('skeleton', 50 + store.get('endless') ['endlessjson'], 10, 10, 0, 20 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('skeleton', 50 + store.get('endless') ['endlessjson'], 10, 10, 0, 20 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 1:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b5 = self.entity('spearskeleton', 50 + store.get('endless') ['endlessjson'], 20, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b5)
                if rnr == 1:
                    b5 = self.entity('spearskeleton', 50 + store.get('endless') ['endlessjson'], 20, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b5)
                if rnr == 2:
                    b5 = self.entity('spearskeleton', 50 + store.get('endless') ['endlessjson'], 20, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b5)
            if rng == 2:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('axeskeleton', 100 + store.get('endless') ['endlessjson'], 15, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('axeskeleton', 100 + store.get('endless') ['endlessjson'], 15, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('axeskeleton', 100 + store.get('endless') ['endlessjson'], 15, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 3:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b6 = self.entity('crossbowskeleton', 50 + store.get('endless') ['endlessjson'], 6, 10, 6, 10 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b6)
                if rnr == 1:
                    b6 = self.entity('crossbowskeleton', 50 + store.get('endless') ['endlessjson'], 6, 10, 6, 10 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b6)
                if rnr == 2:
                    b6 = self.entity('crossbowskeleton', 50 + store.get('endless') ['endlessjson'], 6, 10, 6, 10 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b6)
            if rng == 4:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b8 = self.entity('brokengnome', 25 + store.get('endless') ['endlessjson'], 30, 10, 0, 50 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b8)
                if rnr == 1:
                    b8 = self.entity('brokengnome', 25 + store.get('endless') ['endlessjson'], 30, 10, 0, 50 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b8)
                if rnr == 2:
                    b8 = self.entity('brokengnome', 25 + store.get('endless') ['endlessjson'], 30, 10, 0, 50 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b8)
            if rng == 5:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('darkartsgnome', 60 + store.get('endless') ['endlessjson'], 10, 10, 4, 25 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('darkartsgnome', 60 + store.get('endless') ['endlessjson'], 10, 10, 4, 25 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('darkartsgnome', 60 + store.get('endless') ['endlessjson'], 10, 10, 4, 25 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 6:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b2 = self.entity('demon', 120 + store.get('endless') ['endlessjson'], 8, 10, 0, 75 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b2)
                if rnr == 1:
                    b2 = self.entity('demon', 120 + store.get('endless') ['endlessjson'], 8, 10, 0, 75 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b2)
                if rnr == 2:
                    b2 = self.entity('demon', 120 + store.get('endless') ['endlessjson'], 8, 10, 0, 75 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b2)
            if rng == 7:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b3 = self.entity('torchskeleton', 20 + store.get('endless') ['endlessjson'], 50, 10, 3, 5 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b3)
                if rnr == 1:
                    b3 = self.entity('torchskeleton', 20 + store.get('endless') ['endlessjson'], 50, 10, 3, 5 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b3)
                if rnr == 2:
                    b3 = self.entity('torchskeleton', 20 + store.get('endless') ['endlessjson'], 50, 10, 3, 5 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b3)

    def randomAddEnd(self):
        with shelve.open('Data') as data:
            store.put('endmove', endmovejson = store.get('endmove') ['endmovejson'] + 10)
            rng = random.randint(0,7)
            if rng == 0:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('skeleton', 50 + store.get('endless') ['endlessjson'], 10, 10, 0, 20 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('skeleton', 50 + store.get('endless') ['endlessjson'], 10, 10, 0, 20 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('skeleton', 50 + store.get('endless') ['endlessjson'], 10, 10, 0, 20 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 1:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b5 = self.entity('spearskeleton', 50 + store.get('endless') ['endlessjson'], 20, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b5)
                if rnr == 1:
                    b5 = self.entity('spearskeleton', 50 + store.get('endless') ['endlessjson'], 20, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b5)
                if rnr == 2:
                    b5 = self.entity('spearskeleton', 50 + store.get('endless') ['endlessjson'], 20, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b5)
            if rng == 2:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('axeskeleton', 100 + store.get('endless') ['endlessjson'], 15, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('axeskeleton', 100 + store.get('endless') ['endlessjson'], 15, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('axeskeleton', 100 + store.get('endless') ['endlessjson'], 15, 10, 0, 25 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 3:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b6 = self.entity('crossbowskeleton', 50 + store.get('endless') ['endlessjson'], 6, 10, 6, 10 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b6)
                if rnr == 1:
                    b6 = self.entity('crossbowskeleton', 50 + store.get('endless') ['endlessjson'], 6, 10, 6, 10 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b6)
                if rnr == 2:
                    b6 = self.entity('crossbowskeleton', 50 + store.get('endless') ['endlessjson'], 6, 10, 6, 10 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b6)
            if rng == 4:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b8 = self.entity('brokengnome', 25 + store.get('endless') ['endlessjson'], 30, 10, 0, 50 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b8)
                if rnr == 1:
                    b8 = self.entity('brokengnome', 25 + store.get('endless') ['endlessjson'], 30, 10, 0, 50 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b8)
                if rnr == 2:
                    b8 = self.entity('brokengnome', 25 + store.get('endless') ['endlessjson'], 30, 10, 0, 50 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b8)
            if rng == 5:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b4 = self.entity('darkartsgnome', 60 + store.get('endless') ['endlessjson'], 10, 10, 4, 25 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b4)
                if rnr == 1:
                    b4 = self.entity('darkartsgnome', 60 + store.get('endless') ['endlessjson'], 10, 10, 4, 25 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b4)
                if rnr == 2:
                    b4 = self.entity('darkartsgnome', 60 + store.get('endless') ['endlessjson'], 10, 10, 4, 25 + store.get('endless') ['endlessjson'], 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b4)
            if rng == 6:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b2 = self.entity('demon', 120 + store.get('endless') ['endlessjson'], 8, 10, 0, 75 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b2)
                if rnr == 1:
                    b2 = self.entity('demon', 120 + store.get('endless') ['endlessjson'], 8, 10, 0, 75 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b2)
                if rnr == 2:
                    b2 = self.entity('demon', 120 + store.get('endless') ['endlessjson'], 8, 10, 0, 75 + store.get('endless') ['endlessjson'], 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b2)
            if rng == 7:
                rnr = random.randint(0,2)
                if rnr == 0:
                    b3 = self.entity('torchskeleton', 20 + store.get('endless') ['endlessjson'], 50, 10, 3, 5 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.top.append(b3)
                if rnr == 1:
                    b3 = self.entity('torchskeleton', 20 + store.get('endless') ['endlessjson'], 50, 10, 3, 5 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.middle.append(b3)
                if rnr == 2:
                    b3 = self.entity('torchskeleton', 20 + store.get('endless') ['endlessjson'], 50, 10, 3, 5 + store.get('endless') ['endlessjson'], 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 75 + store.get('endmove') ['endmovejson'], 1, 2, 'left', 'none')
                    self.bottom.append(b3)

    irong = Clock.schedule_interval(addIron, 0.6)

    def action(self):
        self.ids.b.source = "Images/emptyCard.png"
        self.ids.c.source = "Images/emptyCard.png"
        self.ids.a.source = "Images/emptyCard.png"
        store.put('screen', screenjson='game')
        store.put('gamestate', gamestatejson='none')
        store.put('bosshealth', bosshealthjson  = 0)
        store.put('iron', ironjson  = 0)
        if store.get('loops')['loops'] == False:
            Clock.schedule_interval(self.loop, 0.125)
            Clock.schedule_interval(self.loopBad, 0.125)
            Clock.schedule_interval(self.holeLoop, 0.125)
            Clock.schedule_interval(self.gameStateTest, 2)
            store.put('loops', loops = True)
        if store.get('level')['level'] == 15:
            Clock.schedule_once(self.randomAdd, 10)
            Clock.schedule_once(self.randomAdd, 20)
            Clock.schedule_once(self.randomAdd, 30)
            Clock.schedule_once(self.randomAdd, 40)
            Clock.schedule_once(self.randomAdd, 50)
            Clock.schedule_once(self.randomAdd, 60)
            Clock.schedule_once(self.randomAdd, 70)
            Clock.schedule_once(self.randomAdd, 80)
            Clock.schedule_once(self.randomAdd, 90)
            Clock.schedule_once(self.randomAdd, 100)
            Clock.schedule_once(self.randomAdd, 110)
            Clock.schedule_once(self.randomAdd, 120)
            Clock.schedule_once(self.randomAdd, 130)
            Clock.schedule_once(self.randomAdd, 140)
            Clock.schedule_once(self.randomAdd, 150)
            Clock.schedule_once(self.randomAdd, 160)
            Clock.schedule_once(self.randomAdd, 170)
            Clock.schedule_once(self.randomAdd, 180)
            Clock.schedule_once(self.randomAdd, 190)
            Clock.schedule_once(self.randomAdd, 200)
            Clock.schedule_once(self.randomAdd, 210)
            Clock.schedule_once(self.randomAdd, 220)
            Clock.schedule_once(self.randomAdd, 230)
            Clock.schedule_once(self.randomAdd, 240)
            Clock.schedule_once(self.randomAdd, 250)
        if store.get('endless') ['endlessjson'] >= 1:
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            self.randomAddEnd()
            store.put('yesdraw1', yesdraw1json=True)
            store.put('yesdraw2', yesdraw2json=True)
            store.put('yesdraw3', yesdraw3json=True)
        app = App.get_running_app()
        if store.get('level')['level'] <=7 :
            if store.get('music')['music'] == True:
                app.homeSong.stop()
                app.twoSong.stop()
                app.oneSong.play()
            self.ids.endless.text = ""
            self.ids.background.source = "Images/background1.png"  
            self.ids.top.source = "Images/row1.png"   
            self.ids.middle.source = "Images/row1.png"   
            self.ids.bottom.source = "Images/row1.png"   
        if store.get('level')['level'] >= 8 and store.get('level')['level'] <= 11:
            self.ids.background.source = "Images/background2.png" 
            self.ids.top.source = "Images/row1.png"   
            self.ids.middle.source = "Images/row1.png"   
            self.ids.bottom.source = "Images/row1.png"   
            if store.get('music')['music'] == True:
                app.homeSong.stop()
                app.oneSong.stop()
                app.twoSong.play()
            self.ids.endless.text = ""
        if store.get('level')['level'] >= 12 and store.get('level')['level'] <= 15:
            self.ids.background.source = "Images/background3.png" 
            self.ids.top.source = "Images/row2.png"   
            self.ids.middle.source = "Images/row2.png"   
            self.ids.bottom.source = "Images/row2.png" 
            self.ids.endless.text = ""  
            if store.get('music')['music'] == True:
                app.homeSong.stop()
                app.oneSong.play()
                app.twoSong.stop()
        if store.get('level')['level'] ==16:
            self.ids.endless.text = str(math.ceil((store.get('endless') ['endlessjson']/2)))
            rrng = random.randint(0,2)
            if rrng == 0:
                if store.get('music')['music'] == True:
                    app.homeSong.stop()
                    app.twoSong.stop()
                    app.oneSong.play()
                self.ids.background.source = "Images/background1.png"  
                self.ids.top.source = "Images/row1.png"   
                self.ids.middle.source = "Images/row1.png"   
                self.ids.bottom.source = "Images/row1.png"   
            if rrng == 1:
                self.ids.background.source = "Images/background2.png" 
                self.ids.top.source = "Images/row1.png"   
                self.ids.middle.source = "Images/row1.png"   
                self.ids.bottom.source = "Images/row1.png"   
                if store.get('music')['music'] == True:
                    app.homeSong.stop()
                    app.oneSong.stop()
                    app.twoSong.play()
            if rrng == 2:
                self.ids.background.source = "Images/background3.png" 
                self.ids.top.source = "Images/row2.png"   
                self.ids.middle.source = "Images/row2.png"   
                self.ids.bottom.source = "Images/row2.png"   
                if store.get('music')['music'] == True:
                    app.homeSong.stop()
                    app.oneSong.play()
                    app.twoSong.stop()
                        
    def iron(self):
        self.irong()
        Clock.schedule_interval(self.updateIron2, 1)
        app = App.get_running_app()
        print (app.army)
        with shelve.open('Data') as data:
            self.ids.ironcount.text = str(store.get('iron')['ironjson'])
            self.ids.coins.text = str(store.get('coins')['coins'])

    def loadCards(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            aaa = app.army[0]
            self.ids.a.source = "Images/" + str(aaa) + "card.png"
            bbb = app.army[1]
            self.ids.b.source = "Images/" + str(bbb) + "card.png"
            ccc = app.army[2]
            self.ids.c.source = "Images/" + str(ccc) + "card.png"

    def drawCard1(self):
        rng = random.randint(0,7)
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('yesdraw1')['yesdraw1json'] == True:
                curr = app.army[rng]
                if curr == 'peasant':
                    self.ids.a.source = "Images/PeasantCard.png"
                    store.put('aimg', aimgjson="Images/PeasantCard.png")
                if curr == 'miner':
                    self.ids.a.source = "Images/MinerCard.png"
                    store.put('aimg', aimgjson="Images/MinerCard.png")
                if curr == 'swordsman':
                    self.ids.a.source = "Images/SwordsmanCard.png"
                    store.put('aimg', aimgjson="Images/SwordsmanCard.png")
                if curr == 'archer':
                    self.ids.a.source = "Images/ArcherCard.png"
                    store.put('aimg', aimgjson="Images/ArcherCard.png")
                if curr == 'pikeman':
                    self.ids.a.source = "Images/PikemanCard.png"
                    store.put('aimg', aimgjson="Images/PikemanCard.png")
                if curr == 'bard':
                    self.ids.a.source = "Images/BardCard.png"
                    store.put('aimg', aimgjson="Images/BardCard.png")
                if curr == 'gnome':
                    self.ids.a.source = "Images/GnomeCard.png"
                    store.put('aimg', aimgjson="Images/GnomeCard.png")
                if curr == 'gnomeminer':
                    self.ids.a.source = "Images/GnomeminerCard.png"
                    store.put('aimg', aimgjson="Images/GnomeminerCard.png")
                if curr == 'mage':
                    self.ids.a.source = "Images/MageCard.png"
                    store.put('aimg', aimgjson="Images/MageCard.png")
                if curr == 'priest':
                    self.ids.a.source = "Images/PriestCard.png"
                    store.put('aimg', aimgjson="Images/PriestCard.png")
                if curr == 'crusader':
                    self.ids.a.source = "Images/CrusaderCard.png"
                    store.put('aimg', aimgjson="Images/CrusaderCard.png")
            else:
                self.ids.a.source = str(store.get('aimg') ['aimgjson'])
            store.put('yesdraw1', yesdraw1json=False)
    def drawCard2(self):
        rng2 = random.randint(0,7)
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('yesdraw2')['yesdraw2json'] == True:
                curr = app.army[rng2]
                if curr == 'peasant':
                    self.ids.b.source = "Images/PeasantCard.png"
                    store.put('bimg', bimgjson="Images/PeasantCard.png")
                if curr == 'miner':
                    self.ids.b.source = "Images/MinerCard.png"
                    store.put('bimg', bimgjson="Images/MinerCard.png")
                if curr == 'swordsman':
                    self.ids.b.source = "Images/SwordsmanCard.png"
                    store.put('bimg', bimgjson="Images/SwordsmanCard.png")
                if curr == 'archer':
                    self.ids.b.source = "Images/ArcherCard.png"
                    store.put('bimg', bimgjson="Images/ArcherCard.png")
                if curr == 'pikeman':
                    self.ids.b.source = "Images/PikemanCard.png"
                    store.put('bimg', bimgjson="Images/PikemanCard.png")
                if curr == 'bard':
                    self.ids.b.source = "Images/BardCard.png"
                    store.put('bimg', bimgjson="Images/BardCard.png")
                if curr == 'gnome':
                    self.ids.b.source = "Images/GnomeCard.png"
                    store.put('bimg', bimgjson="Images/GnomeCard.png")
                if curr == 'gnomeminer':
                    self.ids.b.source = "Images/GnomeminerCard.png"
                    store.put('bimg', bimgjson="Images/GnomeminerCard.png")
                if curr == 'mage':
                    self.ids.b.source = "Images/MageCard.png"
                    store.put('bimg', bimgjson="Images/MageCard.png")
                if curr == 'priest':
                    self.ids.b.source = "Images/PriestCard.png"
                    store.put('bimg', bimgjson="Images/PriestCard.png")
                if curr == 'crusader':
                    self.ids.b.source = "Images/CrusaderCard.png"
                    store.put('bimg', bimgjson="Images/CrusaderCard.png")
            else:
                self.ids.b.source = str(store.get('bimg') ['bimgjson'])
            store.put('yesdraw2', yesdraw2json=False)
    def drawCard3(self):
        rng3 = random.randint(0,7)
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if store.get('yesdraw3')['yesdraw3json'] == True:
                curr = app.army[rng3]
                if curr == 'peasant':
                    self.ids.c.source = "Images/PeasantCard.png"
                    store.put('cimg', cimgjson="Images/PeasantCard.png")
                if curr == 'miner':
                    self.ids.c.source = "Images/MinerCard.png"
                    store.put('cimg', cimgjson="Images/MinerCard.png")
                if curr == 'swordsman':
                    self.ids.c.source = "Images/SwordsmanCard.png"
                    store.put('cimg', cimgjson="Images/SwordsmanCard.png")
                if curr == 'archer':
                    self.ids.c.source = "Images/ArcherCard.png"
                    store.put('cimg', cimgjson="Images/ArcherCard.png")
                if curr == 'pikeman':
                    self.ids.c.source = "Images/PikemanCard.png"
                    store.put('cimg', cimgjson="Images/PikemanCard.png")
                if curr == 'bard':
                    self.ids.c.source = "Images/BardCard.png"
                    store.put('cimg', cimgjson="Images/BardCard.png")
                if curr == 'gnome':
                    self.ids.c.source = "Images/GnomeCard.png"
                    store.put('cimg', cimgjson="Images/GnomeCard.png")
                if curr == 'gnomeminer':
                    self.ids.c.source = "Images/GnomeminerCard.png"
                    store.put('cimg', cimgjson="Images/GnomeminerCard.png")
                if curr == 'mage':
                    self.ids.c.source = "Images/MageCard.png"
                    store.put('cimg', cimgjson="Images/MageCard.png")
                if curr == 'priest':
                    self.ids.c.source = "Images/PriestCard.png"
                    store.put('cimg', cimgjson="Images/PriestCard.png")
                if curr == 'crusader':
                    self.ids.c.source = "Images/CrusaderCard.png"
                    store.put('cimg', cimgjson="Images/CrusaderCard.png")
            else:
                self.ids.c.source = str(store.get('cimg') ['cimgjson'])
            store.put('yesdraw3', yesdraw3json=False)

    def clearCards(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            self.ids.b.source = "Images/emptyCard.png"
            self.ids.c.source = "Images/emptyCard.png"
            self.ids.a.source = "Images/emptyCard.png"
            store.put('selectedcards', cards = 0)
            app.army.clear()
            self.top.clear()
            store.put('gamestate', gamestatejson='none')
            store.put('screen', screenjson='none')
            self.middle.clear()
            self.bottom.clear()
            self.irong.cancel()
            store.put('iron', ironjson=0)
            store.put('yesdraw1', yesdraw1json=True)
            store.put('yesdraw2', yesdraw2json=True)
            store.put('yesdraw3', yesdraw3json=True)

    def select1(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if self.ids.a.source == "Images/PeasantCard.png":
                if store.get('iron')['ironjson'] >= 10:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('peasant', store.get('peasantHealth')['Health'], store.get('peasantDamage')['Damage'], 0, 0, store.get('peasantDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 10)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('peasant', store.get('peasantHealth')['Health'], store.get('peasantDamage')['Damage'], 0, 0, store.get('peasantDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 10)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('peasant', store.get('peasantHealth')['Health'], store.get('peasantDamage')['Damage'], 0, 0, store.get('peasantDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 10)
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/PeasantCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/MinerCard.png":
                if store.get('iron')['ironjson'] >= 20:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('miner', store.get('minerHealth')['Health'], 0, 0, 0, store.get('minerDefense')['Defense'], 'meele', store.get('minerSpecial')['Special'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('miner', store.get('minerHealth')['Health'], 0, 0, 0, store.get('minerDefense')['Defense'], 'meele', store.get('minerSpecial')['Special'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('miner', store.get('minerHealth')['Health'], 0, 0, 0, store.get('minerDefense')['Defense'], 'meele', store.get('minerSpecial')['Special'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/MinerCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/SwordsmanCard.png":
                if store.get('iron')['ironjson'] >= 30:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('swordsman', store.get('swordsmanHealth')['Health'], store.get('swordsmanDamage')['Damage'], 0, 0, store.get('swordsmanDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('swordsman', store.get('swordsmanHealth')['Health'], store.get('swordsmanDamage')['Damage'], 0, 0, store.get('swordsmanDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('swordsman', store.get('swordsmanHealth')['Health'], store.get('swordsmanDamage')['Damage'], 0, 0, store.get('swordsmanDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/SwordsmanCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/ArcherCard.png":
                if store.get('iron')['ironjson'] >= 20:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('archer', store.get('archerHealth')['Health'], store.get('archerDamage')['Damage'], 0, store.get('archerRange')['Range'], store.get('archerDefense')['Defense'], 'range', 0, 'none', 'range', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('archer', store.get('archerHealth')['Health'], store.get('archerDamage')['Damage'], 0, store.get('archerRange')['Range'], store.get('archerDefense')['Defense'], 'range', 0, 'none', 'range', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('archer', store.get('archerHealth')['Health'], store.get('archerDamage')['Damage'], 0, store.get('archerRange')['Range'], store.get('archerDefense')['Defense'], 'range', 0, 'none', 'range', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/ArcherCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/PikemanCard.png":
                if store.get('iron')['ironjson'] >= 30:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('pikeman', store.get('pikemanHealth')['Health'], store.get('pikemanDamage')['Damage'], 0, 0, store.get('pikemanDefense')['Defense'], 'meele', 0, 'none', 'spear', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('pikeman', store.get('pikemanHealth')['Health'], store.get('pikemanDamage')['Damage'], 0, 0, store.get('pikemanDefense')['Defense'], 'meele', 0, 'none', 'spear', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('pikeman', store.get('pikemanHealth')['Health'], store.get('pikemanDamage')['Damage'], 0, 0, store.get('pikemanDefense')['Defense'], 'meele', 0, 'none', 'spear', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/PikemanCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/BardCard.png":
                if store.get('iron')['ironjson'] >= 30:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('bard', store.get('bardHealth')['Health'], 0, 0, 0, store.get('bardDefense')['Defense'], 'range', store.get('bardSpecial')['Special'], 'bard', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('bard', store.get('bardHealth')['Health'], 0, 0, 0, store.get('bardDefense')['Defense'], 'range', store.get('bardSpecial')['Special'], 'bard', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('bard', store.get('bardHealth')['Health'], 0, 0, 0, store.get('bardDefense')['Defense'], 'range', store.get('bardSpecial')['Special'], 'bard', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.b
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/BardCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/GnomeCard.png":
                if store.get('iron')['ironjson'] >= 25:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('gnome', store.get('gnomeHealth')['Health'], store.get('gnomeDamage')['Damage'], 0, 0, store.get('gnomeDefense')['Defense'], 'magic', 0, 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 25)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('gnome', store.get('gnomeHealth')['Health'], store.get('gnomeDamage')['Damage'], 0, 0, store.get('gnomeDefense')['Defense'], 'magic', 0, 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 25)
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('gnome', store.get('gnomeHealth')['Health'], store.get('gnomeDamage')['Damage'], 0, 0, store.get('gnomeDefense')['Defense'], 'magic', 0, 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 25)
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/GnomeCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/GnomeminerCard.png":
                if store.get('iron')['ironjson'] >= data['gnomeminerCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['gnomeminerCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['gnomeminerCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['gnomeminerCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/GnomeminerCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/MageCard.png":
                if store.get('iron')['ironjson'] >= data['mageCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['mageCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['mageCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['mageCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/MageCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/PriestCard.png":
                if store.get('iron')['ironjson'] >= data['priestCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['priestCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['priestCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['priestCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/PriestCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
            if self.ids.a.source == "Images/CrusaderCard.png":
                if store.get('iron')['ironjson'] >= data['crusaderCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['crusaderCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['crusaderCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['crusaderCost'])
                        store.put('yesdraw1', yesdraw1json=True)
                    store.put('aimg', aimgjson="Images/CrusaderCard.png")
                else:
                    store.put('yesdraw1', yesdraw1json=False)
    def select2(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if self.ids.b.source == "Images/PeasantCard.png":
                if store.get('iron')['ironjson'] >= 10:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('peasant', store.get('peasantHealth')['Health'], store.get('peasantDamage')['Damage'], 0, 0, store.get('peasantDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 10)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('peasant', store.get('peasantHealth')['Health'], store.get('peasantDamage')['Damage'], 0, 0, store.get('peasantDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 10)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('peasant', store.get('peasantHealth')['peasantHealth'], store.get('peasantDamage')['peasantDamage'], 0, 0, store.get('peasantDefense')['peasantDefense'], 'meele', 0, 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 10)
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('bimg', bimgjson="Images/PeasantCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/MinerCard.png":
                if store.get('iron')['ironjson'] >= 20:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('miner', store.get('minerHealth')['Health'], 0, 0, 0, store.get('minerDefense')['Defense'], 'meele', store.get('minerSpecial')['Special'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('miner', store.get('minerHealth')['Health'], 0, 0, 0, store.get('minerDefense')['Defense'], 'meele', store.get('minerSpecial')['Special'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('miner', store.get('minerHealth')['Health'], 0, 0, 0, store.get('minerDefense')['Defense'], 'meele', store.get('minerSpecial')['Special'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('aimg', aimgjson="Images/MinerCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/SwordsmanCard.png":
                if store.get('iron')['ironjson'] >= 30:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('swordsman', store.get('swordsmanHealth')['Health'], store.get('swordsmanDamage')['Damage'], 0, 0, store.get('swordsmanDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('swordsman', store.get('swordsmanHealth')['Health'], store.get('swordsmanDamage')['Damage'], 0, 0, store.get('swordsmanDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('swordsman', store.get('swordsmanHealth')['Health'], store.get('swordsmanDamage')['Damage'], 0, 0, store.get('swordsmanDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('aimg', aimgjson="Images/SwordsmanCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/ArcherCard.png":
                if store.get('iron')['ironjson'] >= 20:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('archer', store.get('archerHealth')['Health'], store.get('archerDamage')['Damage'], 0, store.get('archerRange')['Range'], store.get('archerDefense')['Defense'], 'range', 0, 'none', 'range', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('archer', store.get('archerHealth')['Health'], store.get('archerDamage')['Damage'], 0, store.get('archerRange')['Range'], store.get('archerDefense')['Defense'], 'range', 0, 'none', 'range', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('archer', store.get('archerHealth')['Health'], store.get('archerDamage')['Damage'], 0, store.get('archerRange')['Range'], store.get('archerDefense')['Defense'], 'range', 0, 'none', 'range', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('aimg', aimgjson="Images/ArcherCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/PikemanCard.png":
                if store.get('iron')['ironjson'] >= 30:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('pikeman', store.get('pikemanHealth')['Health'], store.get('pikemanDamage')['Damage'], 0, 0, store.get('pikemanDefense')['Defense'], 'meele', 0, 'none', 'spear', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('pikeman', store.get('pikemanHealth')['Health'], store.get('pikemanDamage')['Damage'], 0, 0, store.get('pikemanDefense')['Defense'], 'meele', 0, 'none', 'spear', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('pikeman', store.get('pikemanHealth')['Health'], store.get('pikemanDamage')['Damage'], 0, 0, store.get('pikemanDefense')['Defense'], 'meele', 0, 'none', 'spear', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('aimg', aimgjson="Images/PikemanCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/BardCard.png":
                if store.get('iron')['ironjson'] >= 30:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('bard', store.get('bardHealth')['Health'], 0, 0, 0, store.get('bardDefense')['Defense'], 'range', store.get('bardSpecial')['Special'], 'bard', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('bard', store.get('bardHealth')['Health'], 0, 0, 0, store.get('bardDefense')['Defense'], 'range', store.get('bardSpecial')['Special'], 'bard', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('bard', store.get('bardHealth')['Health'], 0, 0, 0, store.get('bardDefense')['Defense'], 'range', store.get('bardSpecial')['Special'], 'bard', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.b
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('aimg', aimgjson="Images/BardCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/GnomeCard.png":
                if store.get('iron')['ironjson'] >= 25:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('gnome', store.get('gnomeHealth')['Health'], store.get('gnomeDamage')['Damage'], 0, 0, store.get('gnomeDefense')['Defense'], 'magic', 0, 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 25)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('gnome', store.get('gnomeHealth')['Health'], store.get('gnomeDamage')['Damage'], 0, 0, store.get('gnomeDefense')['Defense'], 'magic', 0, 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 25)
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('gnome', store.get('gnomeHealth')['Health'], store.get('gnomeDamage')['Damage'], 0, 0, store.get('gnomeDefense')['Defense'], 'magic', 0, 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 25)
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('aimg', aimgjson="Images/GnomeCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/GnomeminerCard.png":
                if store.get('iron')['ironjson'] >= data['gnomeminerCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['gnomeminerCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['gnomeminerCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['gnomeminerCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('bimg', bimgjson="Images/GnomeminerCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/MageCard.png":
                if store.get('iron')['ironjson'] >= data['mageCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['mageCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['mageCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['mageCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('bimg', bimgjson="Images/MageCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/PriestCard.png":
                if store.get('iron')['ironjson'] >= data['priestCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['priestCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['priestCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['priestCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('bimg', bimgjson="Images/PriestCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
            if self.ids.b.source == "Images/CrusaderCard.png":
                if store.get('iron')['ironjson'] >= data['crusaderCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['crusaderCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['crusaderCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['crusaderCost'])
                        store.put('yesdraw2', yesdraw2json=True)
                    store.put('bimg', bimgjson="Images/CrusaderCard.png")
                else:
                    store.put('yesdraw2', yesdraw2json=False)
    def select3(self):
        app = App.get_running_app()
        with shelve.open('Data') as data:
            if self.ids.c.source == "Images/PeasantCard.png":
                if store.get('iron')['ironjson'] >= 10:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('peasant', store.get('peasantHealth')['Health'], store.get('peasantDamage')['Damage'], 0, 0, store.get('peasantDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 10)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('peasant', store.get('peasantHealth')['Health'], store.get('peasantDamage')['Damage'], 0, 0, store.get('peasantDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 10)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('peasant', store.get('peasantHealth')['Health'], store.get('peasantDamage')['Damage'], 0, 0, store.get('peasantDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 10)
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('cimg', cimgjson="Images/PeasantCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/MinerCard.png":
                if store.get('iron')['ironjson'] >= 20:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('miner', store.get('minerHealth')['Health'], 0, 0, 0, store.get('minerDefense')['Defense'], 'meele', store.get('minerSpecial')['Special'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('miner', store.get('minerHealth')['Health'], 0, 0, 0, store.get('minerDefense')['Defense'], 'meele', store.get('minerSpecial')['Special'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('miner', store.get('minerHealth')['Health'], 0, 0, 0, store.get('minerDefense')['Defense'], 'meele', store.get('minerSpecial')['Special'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('aimg', aimgjson="Images/MinerCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/SwordsmanCard.png":
                if store.get('iron')['ironjson'] >= 30:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('swordsman', store.get('swordsmanHealth')['Health'], store.get('swordsmanDamage')['Damage'], 0, 0, store.get('swordsmanDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('swordsman', store.get('swordsmanHealth')['Health'], store.get('swordsmanDamage')['Damage'], 0, 0, store.get('swordsmanDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('swordsman', store.get('swordsmanHealth')['Health'], store.get('swordsmanDamage')['Damage'], 0, 0, store.get('swordsmanDefense')['Defense'], 'meele', 0, 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('aimg', aimgjson="Images/SwordsmanCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/ArcherCard.png":
                if store.get('iron')['ironjson'] >= 20:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('archer', store.get('archerHealth')['Health'], store.get('archerDamage')['Damage'], 0, store.get('archerRange')['Range'], store.get('archerDefense')['Defense'], 'range', 0, 'none', 'range', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('archer', store.get('archerHealth')['Health'], store.get('archerDamage')['Damage'], 0, store.get('archerRange')['Range'], store.get('archerDefense')['Defense'], 'range', 0, 'none', 'range', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('archer', store.get('archerHealth')['Health'], store.get('archerDamage')['Damage'], 0, store.get('archerRange')['Range'], store.get('archerDefense')['Defense'], 'range', 0, 'none', 'range', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 20)
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('aimg', aimgjson="Images/ArcherCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/PikemanCard.png":
                if store.get('iron')['ironjson'] >= 30:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('pikeman', store.get('pikemanHealth')['Health'], store.get('pikemanDamage')['Damage'], 0, 0, store.get('pikemanDefense')['Defense'], 'meele', 0, 'none', 'spear', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('pikeman', store.get('pikemanHealth')['Health'], store.get('pikemanDamage')['Damage'], 0, 0, store.get('pikemanDefense')['Defense'], 'meele', 0, 'none', 'spear', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('pikeman', store.get('pikemanHealth')['Health'], store.get('pikemanDamage')['Damage'], 0, 0, store.get('pikemanDefense')['Defense'], 'meele', 0, 'none', 'spear', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('aimg', aimgjson="Images/PikemanCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/BardCard.png":
                if store.get('iron')['ironjson'] >= 30:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('bard', store.get('bardHealth')['Health'], 0, 0, 0, store.get('bardDefense')['Defense'], 'range', store.get('bardSpecial')['Special'], 'bard', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('bard', store.get('bardHealth')['Health'], 0, 0, 0, store.get('bardDefense')['Defense'], 'range', store.get('bardSpecial')['Special'], 'bard', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('bard', store.get('bardHealth')['Health'], 0, 0, 0, store.get('bardDefense')['Defense'], 'range', store.get('bardSpecial')['Special'], 'bard', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.b
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 30)
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('aimg', aimgjson="Images/BardCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/GnomeCard.png":
                if store.get('iron')['ironjson'] >= 25:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('gnome', store.get('gnomeHealth')['Health'], store.get('gnomeDamage')['Damage'], 0, 0, store.get('gnomeDefense')['Defense'], 'magic', 0, 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 25)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('gnome', store.get('gnomeHealth')['Health'], store.get('gnomeDamage')['Damage'], 0, 0, store.get('gnomeDefense')['Defense'], 'magic', 0, 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 25)
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('gnome', store.get('gnomeHealth')['Health'], store.get('gnomeDamage')['Damage'], 0, 0, store.get('gnomeDefense')['Defense'], 'magic', 0, 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - 25)
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('aimg', aimgjson="Images/GnomeCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/GnomeminerCard.png":
                if store.get('iron')['ironjson'] >= data['gnomeminerCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['gnomeminerCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['gnomeminerCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('gnomeminer', data['gnomeminerHealth'], data['gnomeminerDamage'], data['gnomeminerSpeed'], data['gnomeminerRange'], data['gnomeminerDefense'], 'magic', data['gnomeminerSpecial'], 'mine', 'none', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['gnomeminerCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('cimg', cimgjson="Images/GnomeminerCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/MageCard.png":
                if store.get('iron')['ironjson'] >= data['mageCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['mageCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['mageCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('mage', data['mageHealth'], data['mageDamage'], data['mageSpeed'], data['mageRange'], data['mageDefense'], 'magic', data['mageSpecial'], 'none', 'magic', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['mageCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('cimg', cimgjson="Images/MageCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/PriestCard.png":
                if store.get('iron')['ironjson'] >= data['priestCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['priestCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['priestCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('priest', data['priestHealth'], data['priestDamage'], data['priestSpeed'], data['priestRange'], data['priestDefense'], 'magic', data['priestSpecial'], 'none', 'healer', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['priestCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('cimg', cimgjson="Images/PriestCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)
            if self.ids.c.source == "Images/CrusaderCard.png":
                if store.get('iron')['ironjson'] >= data['crusaderCost']:
                    if store.get('lane')['lanejson'] == 'top':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 1, 'good', 0, 1, 2, 'right', 'none')
                        self.top.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['crusaderCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'middle':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 2, 'good', 0, 1, 2, 'right', 'none')
                        self.middle.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['crusaderCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    if store.get('lane')['lanejson'] == 'bottom':
                        add = self.entity('crusader', data['crusaderHealth'], data['crusaderDamage'], data['crusaderSpeed'], data['crusaderRange'], data['crusaderDefense'], 'meele', data['crusaderSpecial'], 'none', 'meele', True, 0, 3, 'good', 0, 1, 2, 'right', 'none')
                        self.bottom.append(add)
                        store.put('iron', ironjson = store.get('iron')['ironjson'] - data['crusaderCost'])
                        store.put('yesdraw3', yesdraw3json=True)
                    store.put('cimg', cimgjson="Images/CrusaderCard.png")
                else:
                    store.put('yesdraw3', yesdraw3json=False)

    def rowTop(self):
        with shelve.open('Data') as data:
            if store.get('level')['level'] <=11 or store.get('level')['level'] == 16:
                store.put('lane', lanejson="top")
                self.ids.top.source = 'Images/row1selected.png'
                self.ids.middle.source = 'Images/row1.png'
                self.ids.bottom.source = 'Images/row1.png'
                print(self.top)
            elif store.get('level')['level'] >=12 :
                store.put('lane', lanejson="top")
                self.ids.top.source = 'Images/row2selected.png'
                self.ids.middle.source = 'Images/row2.png'
                self.ids.bottom.source = 'Images/row2.png'
                print(self.top)
    def rowMiddle(self):
        with shelve.open('Data') as data:
            if store.get('level')['level'] <=11 or store.get('level')['level'] == 16:
                store.put('lane', lanejson="middle")
                self.ids.middle.source = 'Images/row1selected.png'
                self.ids.bottom.source = 'Images/row1.png'
                self.ids.top.source = 'Images/row1.png'
                print(self.top)
            elif store.get('level')['level'] >=12 :
                store.put('lane', lanejson="middle")
                self.ids.middle.source = 'Images/row2selected.png'
                self.ids.top.source = 'Images/row2.png'
                self.ids.bottom.source = 'Images/row2.png'
                print(self.top)
    def rowBottom(self):
        with shelve.open('Data') as data:
            if store.get('level')['level'] <=11 or store.get('level')['level'] == 16:
                store.put('lane', lanejson="bottom")
                self.ids.bottom.source = 'Images/row1selected.png'
                self.ids.middle.source = 'Images/row1.png'
                self.ids.top.source = 'Images/row1.png'
                print(self.top)
            elif store.get('level')['level'] >=12 :
                store.put('lane', lanejson="bottom")
                self.ids.bottom.source = 'Images/row2selected.png'
                self.ids.top.source = 'Images/row2.png'
                self.ids.middle.source = 'Images/row2.png'
                print(self.top)
          
    def summonBadGuys(self):
        with shelve.open('Data') as data:
            self.top.clear()
            self.middle.clear()
            self.bottom.clear()
            if store.get('level')['level'] ==1:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 35, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 71, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 91, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 116, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 126, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 136, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 136, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 141, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 151, 1, 2, 'left', 'none')
                self.bottom.append(b9)
            elif store.get('level')['level'] ==2:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 35, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 86, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 96, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 106, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 111, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 121, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 131, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 141, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 146, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 156, 1, 2, 'left', 'none')
                self.bottom.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 161, 1, 2, 'left', 'none')
                self.top.append(b10)
                b11 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 161, 1, 2, 'left', 'none')
                self.middle.append(b11)   
            elif store.get('level')['level'] ==3:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 35, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 86, 1, 2, 'left', 'none')
                self.bottom.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 96, 1, 2, 'left', 'none')
                self.top.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 101, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 111, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 111, 1, 2, 'left', 'none')
                self.bottom.append(b5)
                b6 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 126, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 131, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 136, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 148, 1, 2, 'left', 'none')
                self.bottom.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 155, 1, 2, 'left', 'none')
                self.top.append(b10)
                b11 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.middle.append(b11)      
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 168, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 174, 1, 2, 'left', 'none')
                self.bottom.append(b13)
                b14 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 175, 1, 2, 'left', 'none')
                self.middle.append(b14)   
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 182, 1, 2, 'left', 'none')
                self.bottom.append(b15)         
            elif store.get('level')['level'] ==4:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.bottom.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 91, 1, 2, 'left', 'none')
                self.top.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 98, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 112, 1, 2, 'left', 'none')
                self.bottom.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 123, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('spearskeleton', 60, 10, 10, 0, 10, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 136, 1, 2, 'left', 'none')
                self.top.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 143, 1, 2, 'left', 'none')
                self.middle.append(b7)
                b8 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 152, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 160, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('spearskeleton', 60, 10, 10, 0, 10, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 171, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 176, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 187, 1, 2, 'left', 'none')
                self.middle.append(b12)
                b13 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 195, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('spearskeleton', 60, 10, 10, 0, 10, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.bottom.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 206, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 212, 1, 2, 'left', 'none')
                self.top.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 224, 1, 2, 'left', 'none')
                self.bottom.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 226, 1, 2, 'left', 'none')
                self.middle.append(b18)
            elif store.get('level')['level'] ==5:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.middle.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.middle.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 103, 1, 2, 'left', 'none')
                self.top.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 113, 1, 2, 'left', 'none')
                self.bottom.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 122, 1, 2, 'left', 'none')
                self.top.append(b5)
                b6 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 132, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 139, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 147, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 150, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.top.append(b10)
                b11 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 166, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 169, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 175, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 181, 1, 2, 'left', 'none')
                self.middle.append(b14)
                b15 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 190, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 192, 1, 2, 'left', 'none')
                self.top.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 197, 1, 2, 'left', 'none')
                self.middle.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 204, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 213, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 216, 1, 2, 'left', 'none')
                self.bottom.append(b20)
            elif store.get('level')['level'] ==6:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.bottom.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.middle.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 105, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 115, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 123, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 131, 1, 2, 'left', 'none')
                self.bottom.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 145, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 150, 1, 2, 'left', 'none')
                self.top.append(b8)
                b9 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 155, 1, 2, 'left', 'none')
                self.bottom.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 160, 1, 2, 'left', 'none')
                self.middle.append(b10)
                b11 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 163, 1, 2, 'left', 'none')
                self.bottom.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 176, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 186, 1, 2, 'left', 'none')
                self.middle.append(b13)
                b14 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 194, 1, 2, 'left', 'none')
                self.top.append(b14)
                b15 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 208, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 214, 1, 2, 'left', 'none')
                self.middle.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 216, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 224, 1, 2, 'left', 'none')
                self.bottom.append(b19)
            elif store.get('level')['level'] ==7:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 27, 1, 2, 'left', 'none')
                self.middle.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.middle.append(b1)
                b2 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 104, 1, 2, 'left', 'none')
                self.bottom.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 116, 1, 2, 'left', 'none')
                self.middle.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 126, 1, 2, 'left', 'none')
                self.top.append(b5)
                b6 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 138, 1, 2, 'left', 'none')
                self.top.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 142, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 152, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 168, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 180, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 188, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 207, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 212, 1, 2, 'left', 'none')
                self.bottom.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 218, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 222, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 231, 1, 2, 'left', 'none')
                self.middle.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 233, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 243, 1, 2, 'left', 'none')
                self.bottom.append(b19)
                b20 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 249, 1, 2, 'left', 'none')
                self.middle.append(b20)
            elif store.get('level')['level'] ==8:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.bottom.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 27, 1, 2, 'left', 'none')
                self.middle.append(h2)
                h3 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 24, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.bottom.append(b1)
                b2 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 99, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 108, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 116, 1, 2, 'left', 'none')
                self.bottom.append(b5)
                b6 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 127, 1, 2, 'left', 'none')
                self.top.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 137, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 148, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 155, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 170, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 172, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 186, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 193, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.middle.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 214, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 227, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 229, 1, 2, 'left', 'none')
                self.top.append(b17)
                b18 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 238, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 247, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 255, 1, 2, 'left', 'none')
                self.bottom.append(b20)
            elif store.get('level')['level'] ==9:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 27, 1, 2, 'left', 'none')
                self.bottom.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 24, 1, 2, 'left', 'none')
                self.middle.append(h2)
                h3 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 101, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 111, 1, 2, 'left', 'none')
                self.bottom.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 123, 1, 2, 'left', 'none')
                self.bottom.append(b5)
                b6 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 133, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 143, 1, 2, 'left', 'none')
                self.top.append(b7)
                b8 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 150, 1, 2, 'left', 'none')
                self.top.append(b8)
                b9 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.bottom.append(b9)
                b10 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 169, 1, 2, 'left', 'none')
                self.middle.append(b10)
                b11 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 177, 1, 2, 'left', 'none')
                self.bottom.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 186, 1, 2, 'left', 'none')
                self.middle.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 193, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.middle.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 217, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 225, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 231, 1, 2, 'left', 'none')
                self.top.append(b17)
                b18 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 239, 1, 2, 'left', 'none')
                self.middle.append(b18)
                b19 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 246, 1, 2, 'left', 'none')
                self.top.append(b19)
                b20 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 253, 1, 2, 'left', 'none')
                self.bottom.append(b20)
                b21 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.middle.append(b21)
            elif store.get('level')['level'] ==10:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 27, 1, 2, 'left', 'none')
                self.middle.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 24, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 30, 1, 2, 'left', 'none')
                self.top.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.bottom.append(b1)
                b2 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 92, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 99, 1, 2, 'left', 'none')
                self.top.append(b3)
                b4 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 110, 1, 2, 'left', 'none')
                self.bottom.append(b4)
                b5 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 118, 1, 2, 'left', 'none')
                self.top.append(b5)
                b6 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 127, 1, 2, 'left', 'none')
                self.middle.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 137, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 148, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 159, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 170, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 175, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 183, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 190, 1, 2, 'left', 'none')
                self.middle.append(b13)
                b14 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 198, 1, 2, 'left', 'none')
                self.top.append(b14)
                b15 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 214, 1, 2, 'left', 'none')
                self.bottom.append(b15)
                b16 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 227, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 229, 1, 2, 'left', 'none')
                self.top.append(b17)
                b18 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 238, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 250, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 255, 1, 2, 'left', 'none')
                self.bottom.append(b20)
                b21 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.top.append(b21)
                b22 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 266, 1, 2, 'left', 'none')
                self.middle.append(b22)
            elif store.get('level')['level'] ==11:
                h1 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 25, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 22, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 28, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 91, 1, 2, 'left', 'none')
                self.bottom.append(b2)
                b3 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 105, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 114, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 122, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 131, 1, 2, 'left', 'none')
                self.bottom.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 137, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 148, 1, 2, 'left', 'none')
                self.middle.append(b8)
                b9 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 157, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 170, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 174, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 180, 1, 2, 'left', 'none')
                self.bottom.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 192, 1, 2, 'left', 'none')
                self.top.append(b13)
                b14 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 200, 1, 2, 'left', 'none')
                self.top.append(b14)
                b15 = self.entity('spearskeleton', 50, 20, 10, 0, 30, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 208, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 216, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 233, 1, 2, 'left', 'none')
                self.middle.append(b17)
                b18 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 238, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 247, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 254, 1, 2, 'left', 'none')
                self.bottom.append(b20)
                b21 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.top.append(b21)
                b22 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 267, 1, 2, 'left', 'none')
                self.middle.append(b22)
            elif store.get('level')['level'] ==12:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 26, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 23, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.middle.append(b1)
                b2 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 89, 1, 2, 'left', 'none')
                self.top.append(b2)
                b3 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 96, 1, 2, 'left', 'none')
                self.middle.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 105, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 114, 1, 2, 'left', 'none')
                self.bottom.append(b5)
                b6 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 124, 1, 2, 'left', 'none')
                self.top.append(b6)
                b7 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 138, 1, 2, 'left', 'none')
                self.middle.append(b7)
                b8 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 146, 1, 2, 'left', 'none')
                self.bottom.append(b8)
                b9 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 157, 1, 2, 'left', 'none')
                self.top.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 160, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 168, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 183, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 189, 1, 2, 'left', 'none')
                self.middle.append(b13)
                b14 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 196, 1, 2, 'left', 'none')
                self.bottom.append(b14)
                b15 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 202, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 220, 1, 2, 'left', 'none')
                self.middle.append(b16)
                b17 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 226, 1, 2, 'left', 'none')
                self.top.append(b17)
                b18 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 232, 1, 2, 'left', 'none')
                self.bottom.append(b18)
            elif store.get('level')['level'] ==13:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 26, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 23, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 88, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 95, 1, 2, 'left', 'none')
                self.bottom.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 102, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 122, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 129, 1, 2, 'left', 'none')
                self.bottom.append(b6)
                b7 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 137, 1, 2, 'left', 'none')
                self.bottom.append(b7)
                b8 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 151, 1, 2, 'left', 'none')
                self.top.append(b8)
                b9 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 157, 1, 2, 'left', 'none')
                self.middle.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 164, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 170, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 182, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 192, 1, 2, 'left', 'none')
                self.bottom.append(b13)
                b14 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 201, 1, 2, 'left', 'none')
                self.middle.append(b14)
                b15 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 209, 1, 2, 'left', 'none')
                self.top.append(b15)
                b16 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 220, 1, 2, 'left', 'none')
                self.middle.append(b16)
                b17 = self.entity('crossbowskeleton', 50, 6, 10, 6, 10, 'range', 0, 'none', 'range', True, 0, 1, 'bad', 232, 1, 2, 'left', 'none')
                self.bottom.append(b17)
                b18 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 239, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 244, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 250, 1, 2, 'left', 'none')
                self.top.append(b20)
                b21 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.bottom.append(b21)
                b22 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 267, 1, 2, 'left', 'none')
                self.middle.append(b22)
                b23 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 273, 1, 2, 'left', 'none')
                self.top.append(b23)
            elif store.get('level')['level'] ==14:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 26, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 23, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 81, 1, 2, 'left', 'none')
                self.top.append(b1)
                b2 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 88, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 100, 1, 2, 'left', 'none')
                self.bottom.append(b3)
                b4 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 102, 1, 2, 'left', 'none')
                self.top.append(b4)
                b5 = self.entity('axeskeleton', 100, 15, 10, 0, 25, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 122, 1, 2, 'left', 'none')
                self.middle.append(b5)
                b6 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 129, 1, 2, 'left', 'none')
                self.bottom.append(b6)
                b7 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 132, 1, 2, 'left', 'none')
                self.middle.append(b7)
                b8 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 141, 1, 2, 'left', 'none')
                self.top.append(b8)
                b9 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 150, 1, 2, 'left', 'none')
                self.middle.append(b9)
                b10 = self.entity('skeleton', 50, 10, 10, 0, 20, 'meele', 0, 'none', 'meele', True, 0, 1, 'bad', 160, 1, 2, 'left', 'none')
                self.bottom.append(b10)
                b11 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 168, 1, 2, 'left', 'none')
                self.middle.append(b11)
                b12 = self.entity('darkartsgnome', 60, 10, 10, 4, 25, 'magic', 0, 'none', 'magic', True, 0, 1, 'bad', 183, 1, 2, 'left', 'none')
                self.top.append(b12)
                b13 = self.entity('brokengnome', 25, 30, 10, 0, 50, 'magic', 0, 'none', 'meele', True, 0, 1, 'bad', 189, 1, 2, 'left', 'none')
                self.middle.append(b13)
                b14 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 200, 1, 2, 'left', 'none')
                self.top.append(b14)
                b15 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 210, 1, 2, 'left', 'none')
                self.middle.append(b15)
                b16 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 215, 1, 2, 'left', 'none')
                self.bottom.append(b16)
                b17 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 223, 1, 2, 'left', 'none')
                self.bottom.append(b17)
                b18 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 231, 1, 2, 'left', 'none')
                self.top.append(b18)
                b19 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 244, 1, 2, 'left', 'none')
                self.middle.append(b19)
                b20 = self.entity('spearskeleton', 50, 20, 10, 0, 25, 'meele', 0, 'none', 'spear', True, 0, 1, 'bad', 250, 1, 2, 'left', 'none')
                self.top.append(b20)
                b21 = self.entity('demon', 120, 8, 10, 0, 75, 'range', 0, 'none', 'meele', True, 0, 1, 'bad', 261, 1, 2, 'left', 'none')
                self.bottom.append(b21)
                b22 = self.entity('torchskeleton', 20, 50, 10, 3, 5, 'meele', 0, 'none', 'range', True, 0, 1, 'bad', 266, 1, 2, 'left', 'none')
                self.middle.append(b22)
            elif store.get('level')['level'] ==15:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 26, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 23, 1, 2, 'left', 'none')
                self.middle.append(h3)
                b1 = self.entity('dragon', 600, 4, 10, 8, 0, 'none', 0, 'none', 'boss', True, 0, 1, 'bad', 60, 1, 2, 'left', 'none')
                store.put('bosshealth', bosshealthjson = 500)
                self.top.append(b1)
                b2 = self.entity('nothing', 600, 4, 10, 8, 0, 'none', 0, 'none', 'boss', True, 0, 1, 'bad', 60, 1, 2, 'left', 'none')
                self.middle.append(b2)
                b3 = self.entity('nothing', 600, 4, 10, 8, 0, 'none', 0, 'none', 'boss', True, 0, 1, 'bad', 60, 1, 2, 'left', 'none')
                self.bottom.append(b3)
            elif store.get('level')['level'] ==16:
                h1 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 20, 1, 2, 'left', 'none')
                self.top.append(h1)
                h2 = self.entity('packedore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 26, 1, 2, 'left', 'none')
                self.bottom.append(h2)
                h3 = self.entity('regularore', 50, 5, 10, 0, 10, 'none', 0, 'none', 'none', True, 0, 1, 'hole', 23, 1, 2, 'left', 'none')
                self.middle.append(h3)

class LoseScreen(Screen):
    pass

class WinScreen(Screen):
    def set(self):
        self.ids.card1.source = "Images/cardback.png"
    def flipCard(self):
        with shelve.open('Data') as data:   
            if store.get('level')['level'] ==1 and store.get('unlockedlevel')['unlockedlevel'] == 1:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/minercard.png"
                    store.put('minerUnlocked', minerUnlocked = True)
                    store.put('unlockedlevel', unlockedlevel = 2)
            if store.get('level')['level'] ==2 and store.get('unlockedlevel')['unlockedlevel'] == 2:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/swordsmancard.png"
                    store.put('swordsmanUnlocked', swordsmanUnlocked = True)
                    store.put('unlockedlevel', unlockedlevel = 3)
            if store.get('level')['level'] ==3 and store.get('unlockedlevel')['unlockedlevel'] == 3:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/goldcard50.png"
                    store.put('coins', coins = store.get('coins')['coins'] + 50)
                    store.put('unlockedlevel', unlockedlevel = 4)
            if store.get('level')['level'] == 4 and store.get('unlockedlevel')['unlockedlevel'] == 4:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/archercard.png"
                    store.put('archerUnlocked', archerUnlocked = True)
                    store.put('unlockedlevel', unlockedlevel = 5)
            if store.get('level')['level'] == 5 and store.get('unlockedlevel')['unlockedlevel'] == 5:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/goldcard50.png"
                    store.put('coins', coins = store.get('coins')['coins'] + 50)
                    store.put('unlockedlevel', unlockedlevel = 6)
            if store.get('level')['level'] == 6 and store.get('unlockedlevel')['unlockedlevel'] == 6:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/pikemancard.png"
                    store.put('pikemanUnlocked', pikemanUnlocked = True)
                    store.put('unlockedlevel', unlockedlevel = 7)
            if store.get('level')['level'] ==7 and store.get('unlockedlevel')['unlockedlevel'] == 7:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/bardcard.png"
                    store.put('bardUnlocked', bardUnlocked = True)
                    store.put('unlockedlevel', unlockedlevel = 8)
            if store.get('level')['level'] ==8 and store.get('unlockedlevel')['unlockedlevel'] == 8:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/goldcard50.png"
                    store.put('coins', coins = store.get('coins')['coins'] + 50)
                    store.put('unlockedlevel', unlockedlevel = 9)
            if store.get('level')['level'] == 9 and store.get('unlockedlevel')['unlockedlevel'] == 9:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/gnomecard.png"
                    data['gnomeCards'] = data['gnomeCards'] + 1
                    data['gnomeUnlocked'] = True
                    store.put('unlockedlevel', unlockedlevel = 10)
            if store.get('level')['level'] ==10 and store.get('unlockedlevel')['unlockedlevel'] == 10:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/gnomeminercard.png"
                    store.put('gnomeUnlocked', gnomeUnlocked = True)
                    store.put('unlockedlevel', unlockedlevel = 11)
            if store.get('level')['level'] == 11 and store.get('unlockedlevel')['unlockedlevel'] == 11:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/magecard.png"
                    data['mageCards'] = data['mageCards'] + 1
                    data['mageUnlocked'] = True
                    store.put('unlockedlevel', unlockedlevel = 12)
            if store.get('level')['level'] == 12 and store.get('unlockedlevel')['unlockedlevel'] == 12:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/sapphirecard.png"
                    store.put('sapphires', sapphires = store.get('sapphires')['sapphires'] + 1)
                    store.put('unlockedlevel', unlockedlevel = 13)
            if store.get('level')['level'] == 13 and store.get('unlockedlevel')['unlockedlevel'] == 13:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/priestcard.png"
                    data['priestCards'] = data['priestCards'] + 1
                    data['priestUnlocked'] = True
                    store.put('unlockedlevel', unlockedlevel = 14)
            if store.get('level')['level'] == 14 and store.get('unlockedlevel')['unlockedlevel'] == 14:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/crusadercard.png"
                    data['crusaderCards'] = data['crusaderCards'] + 1
                    data['crusaderUnlocked'] = True
                    store.put('unlockedlevel', unlockedlevel = 15)
            if store.get('level')['level'] ==15 and store.get('unlockedlevel')['unlockedlevel'] == 15:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/emeraldcard.png"
                    store.put('emeralds', emeralds = store.get('emeralds')['emeralds'] + 10)
                    store.put('unlockedlevel', unlockedlevel = 16)
            else:
                if self.ids.card1.source == "Images/cardback.png":
                    self.ids.card1.source = "Images/goldcard10.png"
                    store.put('coins', coins = store.get('coins')['coins'] + 10)

kv = Builder.load_file('medieval.kv')

class MedievalApp(App):
    homeSong = SoundLoader.load('Home_1.mp3')
    oneSong = SoundLoader.load('world1.mp3')
    twoSong = SoundLoader.load('world1.2.mp3')
    music = True
    army=[]
    def build(self):
        return kv

MedievalApp().run()