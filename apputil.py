from collections import defaultdict
import random
import numpy as np


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):

        # your code here ...

        words = self.corpus.split()

        term_dict = defaultdict(list)

        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            term_dict[current_word].append(next_word)

        self.term_dict = dict(term_dict)

        return self.term_dict


    

    def generate(self, seed_term=None, term_count=15):

        if self.term_dict is None:
            self.get_term_dict()

        if not self.term_dict:
            return ""

        # Handle seed term
        if seed_term is not None:
            if seed_term not in self.corpus.split():
                raise ValueError("Seed term not found in corpus.")
            current_word = seed_term
        else:
            current_word = np.random.choice(list(self.term_dict.keys()))

        output = [current_word]

        for _ in range(term_count - 1):

            next_words = self.term_dict.get(current_word)

            # Handle edge case (last word or dead end)
            if not next_words:
                break

            current_word = np.random.choice(next_words)
            output.append(current_word)

        return " ".join(output)