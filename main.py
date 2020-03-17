import rumps
import os
import sys
from urllib.request import Request, urlopen
from decimal import Decimal

import rumps
import requests

#pulling coinbase data
API_URL = 'https://corona.lmao.ninja/all'

EXEC_TIMER = 60  # refresh every 60 seconds


class Corona_Counter(rumps.App):
    def __init__(self, _):
        super(Corona_Counter, self).__init__("Corona_Counter")
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
        self.icon = None
        self.menu = ["About", ["Country",("World Wide", "China","Italy","Iran","Spain","S. Korea","Germany","France","USA","Switzerland","UK","Netherlands","Norway","Sweden","Belgium","Austria","Denmark","Japan","Diamond Princess","Malaysia","Canada","Qatar","Australia","Greece","Czechia","Portugal","Israel","Finland","Slovenia","Singapore","Brazil","Bahrain","Ireland","Estonia","Iceland","Pakistan","Poland","Romania","Egypt","Chile","Hong Kong","Thailand","Philippines","Indonesia","Iraq","Saudi Arabia","India","Kuwait","San Marino","Lebanon","UAE","Russia","Peru","Luxembourg","Slovakia","Taiwan","Argentina","South Africa","Bulgaria","Vietnam","Algeria","Ecuador","Croatia","Serbia","Panama","Brunei","Colombia","Mexico","Armenia","Albania","Turkey","Cyprus","Costa Rica","Hungary","Palestine","Morocco","Belarus","Latvia","Georgia","Malta","Jordan","Moldova","Uruguay","Sri Lanka","Azerbaijan","Bosnia and Herzegovina","Senegal","Oman","Afghanistan","Dominican Republic","Tunisia","North Macedonia","Lithuania","Faeroe Islands","Venezuela","Burkina Faso","Jamaica","Martinique","Andorra","Maldives","Cambodia","Macao","Bolivia","French Guiana","Kazakhstan","Réunion","Guatemala","New Zealand","Bangladesh","Paraguay","Uzbekistan","Guyana","Ukraine","Liechtenstein","Rwanda","Monaco","Channel Islands","Ghana","Guadeloupe","Honduras","Cameroon","Ethiopia","Puerto Rico","Ivory Coast","Cuba","Mongolia","Trinidad and Tobago","French Polynesia","Gibraltar","Guam","Kenya","St. Barth","Seychelles","Nigeria","Aruba","Curaçao","DRC","Namibia","Saint Lucia","Saint Martin","Cayman Islands","Sudan","Nepal","Antigua and Barbuda","Bahamas","Benin","Bhutan","CAR","Congo","Equatorial Guinea","Gabon","Greenland","Guinea","Vatican City","Liberia","Mauritania","Mayotte","St. Vincent Grenadines","Somalia","Suriname","Eswatini","Tanzania","Togo","U.S. Virgin Islands")]]
    @rumps.clicked("About")
    def prefs(self, _):
        rumps.notification("Awesome title", "Made by Roxiun", "Credit: Idea - u/ImAColdhart API - corona.lmao.ninja ")

    @rumps.clicked("Country", "World Wide")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('all')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"

    @rumps.clicked("Country", "China")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('china')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"

    @rumps.clicked("Country", "Italy")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('italy')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"

    @rumps.clicked("Country", "Australia")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('australia')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"

    @rumps.clicked("Country", "India")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('india')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Italy")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('italy')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Iran")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('iran')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Spain")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('spain')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Germany")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('germany')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "France")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('france')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "USA")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('usa')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Switzerland")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('switzerland')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "UK")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('uk')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Netherlands")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('netherlands')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Norway")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('norway')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}" 
    @rumps.clicked("Country", "Sweeden")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('sweeden')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Belgium")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('belgium')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Austria")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('austria')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Denmark")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('denmark')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Japan")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('japan')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Malaysia")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('malaysia')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Canada")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('canada')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Singapore")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('singapore')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Hong Kong")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('hong kong')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Thailand")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('thailand')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"
    @rumps.clicked("Country", "Taiwan")
    def prefs(self, _):
        f = open("country.txt", "w")
        f.write('taiwan')
        f.close()
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"

    @rumps.timer(EXEC_TIMER)
    def pull_data(self, _):
        g = open("country.txt", "r")
        f = g.readlines()[0]
        g.close()
        if f == 'all':
            country_link = f
        else:
            country_link = f"countries/{f}"
        req = Request(f'https://corona.lmao.ninja/{country_link}', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        webpage = webpage.decode("utf-8")
        num_cases = eval(webpage)
        cases = num_cases['cases']
        self.title = f"Cases: {str(cases)}"

if __name__ == "__main__":
    Corona_Counter("Loading...").run() #debug=True