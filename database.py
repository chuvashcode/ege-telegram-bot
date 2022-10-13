import csv
import random


class WordsDB:
    def __init__(self):
        # TODO: add verbs
        self.nouns = []
        self.adverbs = []
        self.adjectives = []
        self.adparticiples = []
        self.participles = []

    def parse(self):
        with open("./db/nouns.csv", "r", encoding="utf8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                self.nouns = row
        with open("./db/adverbs.csv", "r", encoding="utf8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                self.adverbs = row
        with open("./db/adjectives.csv", "r", encoding="utf8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                self.adjectives = row
        with open("./db/adparticiples.csv", "r", encoding="utf8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                self.adparticiples = row
        with open("./db/participles.csv", "r", encoding="utf8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                self.participles = row

    # TODO: implement get with specific category
    def get_random(self) -> str:
        all_words: dict = self.nouns + self.adverbs + self.adjectives + self.participles + self.adparticiples
        random_word: str = random.choice(all_words)
        return random_word
