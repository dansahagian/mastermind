import random

COLORS = ('w', 'b', 'k', 'y', 'r', 'g')


def create_sequence():
    seq = []

    for i in range(0, 4):
        seq.append(random.choice(COLORS))

    return seq


def enter_color():
    color = input('Please enter your color (w, b, k, y, r, g): ')
    if color not in COLORS:
        print('{} is not a valid color!'.format(color))
        return enter_color()
    else:
        return color


def guess_sequence():
    guess = []

    for i in range(0, 4):
        guess.append(enter_color())

    confirm = input('\nPlease confirm guess of {} w/ y or n: '.format(guess))

    if confirm == 'y':
        return guess
    else:
        print('\nPlease reenter your sequence.\n')
        return guess_sequence()


def score_guess(guess, answer):
    ans = list(answer)
    ges = list(guess)

    score = []
    for i, color in enumerate(ges):
        if color == ans[i]:
            score.append('k')
            ans[i] = '*'
            ges[i] = '-'

    for i, color in enumerate(ges):
        if color in ans:
            score.append('w')
            ans[ans.index(color)] = '*'
            ges[i] = '-'

    random.shuffle(score)
    return score


def is_game_over(guess_num, score):
    if score == ['k', 'k', 'k', 'k']:
        print('You won!')
        return True

    if guess_num > 10:
        print('You used all your turns. You lose!')
        return True

    return False


def main():
    # answer = create_sequence()
    answer = ['g', 'b', 'w', 'b']
    print()

    guesses = []
    scores = []

    i = 1
    score = ['', '', '', '']

    while not is_game_over(i, score):
        guess = guess_sequence()
        guesses.append(guess)

        score = score_guess(guess, answer)
        scores.append(score)

        for j, each in enumerate(guesses):
            print('Guess {}: {} - Score: {}'.format(j + 1, each, scores[j]))
        print()

        i += 1

    print('The sequence was {}.'.format(answer))

if __name__ == '__main__':
    main()
