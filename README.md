## News_Aggregator Backend

---

This news aggregator backend receives a JSON message from the Angular frontend, parses the message, and calls NewsAPI. Based on the request given by the frontend, NewsAPI will scrape news sites for specific articles by keywords. The backend then parses the output of NewsAPI and relays the message back to the Angular Frontend.

The backend is built with Flask.
