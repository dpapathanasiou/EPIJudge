from test_framework import generic_test, test_utils


def find_anagrams(dictionary):
    d = {} # k = sorted word, v = [word(s)]
    h = {} # k = word, v = sorted string
    for word in dictionary:
        w = ''.join(sorted(word))
        h[word] = w
        words = d.get(w, [])
        words.append(word)
        d[w] = words

    return list(filter(lambda x: len(x) > 1, d.values()))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
