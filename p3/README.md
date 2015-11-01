Describr
========

The aim of this app is to describe in few words, the 'feel' of a place. There are many reviews publicly available on Google Maps, e.g. [Bombay](https://www.google.co.in/maps/place/Mumbai,+Maharashtra/@19.0826891,72.6016899,10z/)

We use a crawler to gather such reviews and create a small set of words that best describes any given geography. The motivation behind doing so is to graduate one level above a numeric rating, enabling people to understand the exact feel or vibe behind a place. And still saving them the time-taking task of reading a review for only the relevant places.

Data
----

* We use the publicly available reviews on [Google Maps](https://support.google.com/maps/answer/6230175?hl=en) using the [Google Places Web Service API](https://developers.google.com/places/web-service/).
* We also use [nltk](http://www.nltk.org/book/) library in Python to tag Part-of-Speechs in these reviews
* Finally, we use [MPQA Subjectivity Lexicon](http://mpqa.cs.pitt.edu/lexicons/subj_lexicon/) to identify the most polar adjectives in our bag-of-words obtained from the reviews

