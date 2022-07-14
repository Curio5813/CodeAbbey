"""
==============
Bulls and Cows
==============

This is an old game for two players, often played with paper and pen. Modern version is also known as
Mastermind.

First player, let it be Alice - chooses a secret 4-digit code (like 1492), with all digits different.

The second player, let it be Barbara - makes several attempts to guess this code. She can offer any
combinations of 4 digits (without repetitions) - and for each attempt the Alice should answer with a hint.

The hint consists of two values:

first tells how many digits are guessed correctly and are in correct positions;
second tells how many digits are guessed correctly but are in wrong positions.

For example, if the secret value is 1492 and Barbara's guess is 2013 - Alice should answer with 0-2.
And if the guess is 1865, then the hint would be 1-0.

This game could also be played with 4-letter words, but in this case it may require the knowledge of the
language.

Further information could be found in the dedicated wikipedia article.

Problem statement
Your goal is to write a program which calculates the values which should be told as a hint to the given guess.

Input data will contain the secret value and the number of guesses in the first line.
Second line will contain the specified amount of guesses.
Answer should contain hints for these guesses, they should be given in format X-Y and separated with spaces.

Example:

input data:
1492 5
2013 1865 1234 4321 7491

answer:
0-2 1-0 1-2 0-3 2-1
"""
print('')


def bulls_and_cows():
    codigo = '2954'
    advinhacoes = ['5843', '8430', '0842', '0391', '9832', '2308', '5912', '9204', '3024', '3082', '4820',
                   '9412', '2549', '0428']
    n, cont1, cont2, posicao_correta, numero_correto, hint = 0, 0, 0, [], [], []
    for k in range(0, len(advinhacoes)):
        while n < len(advinhacoes[k]):
            if advinhacoes[k][n] == codigo[n]:
                cont1 += 1
            elif advinhacoes[k][n] in codigo:
                cont2 += 1
            n += 1
        posicao_correta.append(cont1)
        numero_correto.append(cont2)
        cont1 = 0
        cont2 = 0
        n = 0
    for k in range(0, len(posicao_correta)):
        print(f'{posicao_correta[k]}-{numero_correto[k]}', end=' ')
    print('')
    return ''


print(bulls_and_cows())
