import random


def play():
    print('****** Jogo da Advinhação ****** \n')
    print('Acerte o número antes de zerar as tentativas \n')

    random_number = random.randrange(1, 100)

    print('Selecione o nivel de dificuldade \n(Facil[1] Medio[2] Difícil[3])')
    nivel = int(input(':'))

    if nivel > 3:
        print('Insira um valor entre 1 e 3')
    elif nivel == 1:
        attemps = 20
    elif nivel == 2:
        attemps = 10
    else:
        attemps = 5

    for round in range(1, attemps + 1):

        print(f'Tentativa {round} de {attemps}')
        guess = int(input('digite um numero entre 1 e 100: '))

        if guess < 1 or guess > 100:
            print('Você deve digitar um número entre 1 e 100!\n')

        win = guess == random_number
        bigger = guess > random_number
        smaller = guess < random_number

        if win:
            print('Você acertou!')
        elif round == attemps:
            print(f'Você perdeu! :( O número secreto era {random_number}')
        else:
            if bigger:
                print('Você errou! Tente um número menor ;)  \n')
            elif smaller:
                print('Você errou! Tente um número maior ;) \n')


play()
