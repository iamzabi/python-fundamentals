import string

def display_board(dict) :
    i = 1
    while i < 10:
        if i == 4 or i == 7:
            print('\n-----------')
        print(' ' + dict[i] + ' ', end='')
        if i == 3 or i == 6 or i == 9:
            pass
        else:
            print('|', end='')
        i += 1
    print('\n'*2)

def ask():
    player_1 = input('\nplayer 1, what will you choose : X / O  \n').upper()
    if player_1 == 'X' :
        player_2 = 'O'
    else :
        player_2 = 'X'
    return [player_1, player_2]

def playing(dict):
    i = 0
    temp = False
    list_a = []
    list_b = []
    while i < 9 :
        while True :
            a = int(input("Position Player-1 : \n"))
            if dict[a] != ' ':
                print("Sorry wrong position!!!")
                print("Try Again---")
                continue
            else :
                break

        list_a.append(a)
        list_a.sort()
        dict[a] = value[0]
        display_board(dict)
        temp = check_win(list_a)

        if temp == True :
            print("Player 1 wins")
            break

        while True :
            b = int(input("position player-2 : \n"))
            if dict[b] != ' ':
                print("Sorry Wrong Position!!!!")
                print("Try Again---")
                continue
            else :
                break

        list_b.append(int(b))
        list_b.sort()
        dict[b] = value[1]
        display_board(dict)
        temp = check_win(list_b)

        if temp == True :
            print("Player 2 wins")
            break
        i+=1
    else :
        print("Sorry its Draw :")

def check_win(result):
    a = ''
    for i in result:
        a = a + str(i)
    list = ['123', '456', '789','147', '258' , '369', '159', '357']
    for i in list:
        if i in a:
            return True



print("Do you want to play game : yes / no")

play = input().lower()

if play == 'yes':

    while True :
        dict = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
        display_board(dict)
        value = ask()
        playing(dict)

        flag = input("Do you want to play again : yes/no ").lower()
        if flag == 'no':
            break
        else :
            continue


