from newsapi import NewsApiClient
import requests
from Secrets import api_key



def getHTML(url):
    return requests.get(url)


class NewsAPI():

    newsapi = NewsApiClient(api_key=api_key)


    def getTopHeadlines(self, q, sources, language):
        return self.newsapi.get_top_headlines(q=q, sources=sources, language=language)

    def getEverything(self, q, sources, language):
        return self.newsapi.get_everything(q=q, sources=sources, language=language)











"""

Fxn logic we can use in the future?

   def find_Trump(self, term, iterated):
        tally = 0
        if isinstance(iterated, list):
            for value in iterated:
                tally = tally + self.find_Trump(term, value)
        elif isinstance(iterated, dict):
            for value in iterated.values():
                tally = tally + self.find_Trump(term, value)
        elif isinstance(iterated, str):
            tally = tally + self.stringIteration(term, iterated)

        return tally

    # Could use findall in re module instead (re: regular expressions module)
    def stringIteration(self, term, string):
        tally = 0
        nextHop = len(term) + 1

        try:
            index = string.find(term)
            if index > -1:
                tally += 1
                string = string[nextHop:]
                tally = tally + self.stringIteration(term, string)
        except:
            print('Passed Array Bounds')
            return 0

        return tally




"""













