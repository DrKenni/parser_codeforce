import requests

site = 'https://codeforces.com/api/problemset.problems?lang=ru'


class Parser:

    @staticmethod
    def get_data(link):
        req = requests.get(link)
        req.encoding = 'utf-8'
        scr = req.text
        return print(scr)

    def star_work(self):
        pass


Parser.get_data(site)