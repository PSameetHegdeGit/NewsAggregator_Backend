from werkzeug.routing import BaseConverter



def generateListOfSources(sources):
    sources = sources.split(",")

    # sources = list(map(lambda source: source[2:len(source) - 1], sources))
    return sources



