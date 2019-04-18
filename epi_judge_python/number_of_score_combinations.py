from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    c = [0] * (final_score + 1)
    c[0] = 1
    for score in individual_play_scores:
        for i in range(score, final_score+1):
            c[i] += c[i-score]
    return c[final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
