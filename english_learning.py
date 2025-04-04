from random import choice, sample, shuffle
from words import *
from consts import *


def get_word() -> str:
    return choice(list(words))


def get_variants(word) -> list[str]:
    correct_meaning = words[word]
    variants = list(words.values())
    variants.remove(correct_meaning)
    wrong_meanings = sample(variants, VARIANT_COUNT - 1)
    variants = [correct_meaning] + wrong_meanings
    shuffle(variants)
    return variants


def check_correct(word, meaning) -> bool:
    return words[word] == meaning
