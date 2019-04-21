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

    anagrams = []
    for word in dictionary:
        words = d[h[word]]
        if len(words) > 1:
            if words not in anagrams:
                anagrams.append(words)
    return anagrams


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
