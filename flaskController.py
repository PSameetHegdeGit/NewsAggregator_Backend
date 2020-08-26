from flask import Flask, render_template, request, redirect, url_for, abort
from flask_cors import CORS

import pprint

import utilities

from pymongo import *

app = Flask(__name__)
CORS(app)

from NewsApiLibrary import *

sourcesAndArticles = {}
client = MongoClient('mongodb+srv://admin:<newsaggregatoradministrator>@newsaggregatordb.tsujr.mongodb.net/<NewsAggregatorDB>?retryWrites=true&w=majority')

@app.route("/", methods=["GET", "POST"])
def landing():
    print("in Landing")
    if request.method == "POST":
        test = request.form['test']
        todo = request.form['todo']

        if todo == 'insert':
            print("in todo")
            post = {'info': test}
            try:
                client.list_database_names()
                print('Successfully inserted?')
            except:
                print('ERROR')
        elif todo == 'get':
            try:
                pass
            except:
                print('ERROR')


        return redirect(url_for('landing'))

    else:
        return render_template("landing.html")

@app.route("/display_content/<searchFor>&<sources>&<language>&<method>", methods=["GET", "POST"])
def display_content(searchFor, sources, language, method):
    newsInstance = NewsAPI()

    global sourcesAndArticles

    sources = utilities.generateListOfSources(sources)


    sourcesAndArticles.clear()

    try:
        if method == "getTopHeadlines":

            sourcesAndArticles = {source:newsInstance.getTopHeadlines(searchFor, source, language)['articles'] for source in sources}
            return sourcesAndArticles

        elif method == "getEverything":


            sourcesAndArticles = {source:newsInstance.getEverything(searchFor, source, language)['articles'] for source in sources}
            return sourcesAndArticles

    except:
        abort(404)

if __name__ == '__main__':
    app.run()




  # May use below code when posting to db
  # if request.method == "POST":
    #     sourceSelection = request.form.get("ChooseNewsSource")
    #     sources = sourcesAndArticles.keys()
    #     index = sources.index(sourceSelection)
    #     sources[0], sources[index] = sources[index], sources[0]
    #
    #     return render_template('displayedContent.html', sources=sources, articlesFromAllSources=[sourcesAndArticles[sourceSelection]])






"""
Filtering:

# Be able to choose between Get Everything or Get Top Headlines (cannot choose both!!)

(1) By news Source (If we select more than 1 news source)
(2) By Country
(3) By language(If we choose more than one language)
(4) Part of spectrum


Choose between Getting top headlines and everything

"""





