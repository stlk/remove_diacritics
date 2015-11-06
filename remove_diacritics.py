import sys
import itertools

from unidecode import unidecode


def remove_diacritics(text):
  return unidecode(text)


if __name__ == '__main__':
  text = sys.argv[1]
  print("Here it is!:\n{0}".format(remove_diacritics(text)))
