#!/usr/bin/env python2
#mapper2.py
import sys

set_ids = {} #dict with id_film:decade
ratings = {} #dict with id_fils:rating
ratings_decades = {} #dict with decade:list[ratings]

NUM_FILMS = 0
MAX_FILMS = 100

def printFilms():
    for decades in ratings_decades:
        avarage = 0.0
        for rating in ratings_decades[decades]:
            avarage += float(rating)
        print(str(decades)+ "\t" + str(avarage/len(ratings_decades[decades])) + "\t" +str(len(ratings_decades[decades])) +"\t")
    ratings_decades.clear()
    NUM_FILMS = 0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 2: #reducer OUTPUT_FILE
        ids = parts[1].split(',')
        for film in ids:
            set_ids[film] = parts[0]
    else:   #avarage file
        ratings[parts[0]] = parts[1]

for id, rating in ratings.items():
    if id in set_ids:
        decade = set_ids[id]
        if decade not in ratings_decades:
            ratings_decades[decade] = []
        ratings_decades[decade].append(rating)
        NUM_FILMS += 1
        if NUM_FILMS >= MAX_FILMS:
            printFilms()
if NUM_FILMS < MAX_FILMS:
    printFilms()
