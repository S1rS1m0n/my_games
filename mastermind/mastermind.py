from random import randint


# Keep creating games as long as the user wants to play
while True:
    print('\n' + '-' * 62 + '\n')
    answer = input('Do you want to play mastermind? (yes/no) ').lower()
    if answer == 'no':
        print('Bye.')
        break
    elif answer not in ['yes', 'no']:
        print('You must enter "yes" or "no", please retry.')
        continue

    # Generate a random 4-digit code
    code = ''
    for i in range(4):
        code += str(randint(0, 9))

    print('''\nS (Strike) = correct digit at the right place
B (Ball) = correct digit at the wrong place''')

    # Allow the user up to 9 attempts to guess the code
    attempt = 0
    while attempt < 9:
        guess = input('\nEnter a 4-digit code. ')
        if not guess.isdigit() or len(guess) != 4:
            print('Invalid guess, please retry.')
            continue
        attempt += 1
        strikes, balls = 0, 0

        # Convert strings to lists to allow in-place modifications
        code_digits = [digit for digit in code]
        guess_digits = [digit for digit in guess]

        if guess == code:
            print('You win.')
            break

        # Count the strikes
        for i in range(4):
            if code_digits[i] == guess_digits[i]:
                strikes += 1
                # Mark matched digits to prevent re-counting them as balls
                code_digits[i] = guess_digits[i] = None

        # Count the balls and mark matched digits to avoid re-counting them
        for i in range(4):
            if guess_digits[i] is not None and guess_digits[i] in code_digits:
                balls += 1
                code_digits[code_digits.index(guess_digits[i])] = None

        print(f'Attempt {attempt}/9: \n{strikes}S\n{balls}B')

    if guess != code:
        print(f'You lose. The code was {code}.')