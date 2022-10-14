import csv
import random


class WordsDB:
    def __init__(self):
        # TODO: add verbs
        self.nouns: list = []
        self.adverbs: list = []
        self.adjectives: list = []
        self.adparticiples: list = []
        self.participles: list = []

    def parse(self) -> None:
        with open("./db/nouns.csv", "r", encoding="utf8") as nouns, \
                open("./db/adverbs.csv", "r", encoding="utf8") as adverbs, \
                open("./db/adjectives.csv", "r", encoding="utf8") as adjectives, \
                open("./db/adparticiples.csv", "r", encoding="utf8") as adparticiples, \
                open("./db/participles.csv", "r", encoding="utf8") as participles:
            noun_reader = csv.reader(nouns, delimiter=",")
            adverb_reader = csv.reader(adverbs, delimiter=",")
            adjective_reader = csv.reader(adjectives, delimiter=",")
            adparticiple_reader = csv.reader(adparticiples, delimiter=",")
            participle_reader = csv.reader(participles, delimiter=",")
            for noun in noun_reader:
                self.nouns = noun
            for adverb in adverb_reader:
                self.adverbs = adverb
            for adjective in adjective_reader:
                self.adjectives = adjective
            for adparticiple in adparticiple_reader:
                self.adparticiples = adparticiple
            for participle in participle_reader:
                self.participles = participle

    def get_random(self) -> str:
        all_words: list = self.nouns + self.adverbs + self.adjectives + self.participles + self.adparticiples
        random_word: str = random.choice(all_words)
        return random_word

    def get_random_noun(self):
        random_noun: str = random.choice(self.nouns)
        return random_noun

    def get_random_adverb(self):
        random_adverb: str = random.choice(self.adverbs)
        return random_adverb

    def get_random_adjective(self):
        random_adjective: str = random.choice(self.adjectives)
        return random_adjective

    def get_random_adparticiple(self):
        random_adparticiple: str = random.choice(self.adparticiples)
        return random_adparticiple

    def get_random_participle(self):
        random_participle: str = random.choice(self.participles)
        return random_participle
