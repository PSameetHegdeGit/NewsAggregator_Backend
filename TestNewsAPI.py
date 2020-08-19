import unittest
from NewsApiLibrary import *

class TestnewsAPI(unittest.TestCase):

    def test_TestBlockWorking(self):
        self.assertTrue(True)

    def test_AnotherTestBlock(self):
        self.assertTrue(True)


    def test_WorkingWithUnicodeFormattedStrings(self, unicodeFormattedStringList=[u'fox-news', u'nbc-news', u'cnn-news'], string="fox-news, cnn-news, nbc-news"):
        try:
            for source in unicodeFormattedStringList:
                print(source)

            print(string.split(", "))
        except:
            self.assertTrue(False)

    def test_ArticleListProperlyGenerated(self, searchFor='Trump', sources=['fox-news', 'cnn', 'nbc-news'], language='en'):
        newsInstance = NewsAPI()
        with open("tester_AllArticles.html", 'w') as tester:
            articlesFromAllSources = {source:newsInstance.getTopHeadlines(searchFor, source, language)['articles'] for source in sources}
            tester.write(str(articlesFromAllSources))

    def test_sourcesProperlyGenerated(self, sources="[u'fox-news', u'cnn', u'nbc-news']"):
        sources=sources[1:len(sources) - 1]
        print(sources)
        sources=sources.split(", ")
        sources=list(map(lambda source:source[2:len(source)-1], sources))
        print(sources)

    def test_gettingHTMLFromURL(self, url='https://www.cnn.com/2020/06/11/politics/icc-executive-order/index.html'):
        test_article = getHTML(url)
        with open('tester_putHTML.html', 'w') as tester:
            tester.write(test_article.text)

