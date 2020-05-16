from random import randint
answer = randint(1, 10)


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You are a genius!!')
            return True
    else:
        print('Hey, I said 1~10')
        return False


if __name__ == '__main__':
    while True:
        try:
            guess = int(input('Guess a number 1~10: '))
            if(run_guess(guess, answer)):
                break
        except ValueError:
            print('Please enter a number')
            continue
