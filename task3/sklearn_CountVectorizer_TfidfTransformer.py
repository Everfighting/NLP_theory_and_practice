#!/usr/bin/env python3
# -*- coding:utf-8 _*-
# CountVectorizer TfidfTransformer

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

corpus = ['This is the first document.',
          'This is the second second document.',
          'And the third one.',
          'Is this the first document?',
          ]

vectorizer = CountVectorizer()

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
print(tfidf)