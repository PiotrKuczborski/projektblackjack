import random 
from termcolor import colored


def main():
    printIntro()
    player_win = 0
    dealer_win = 0
    while True:
        player_hand = player()
        dealer_hand = dealer()
        player_win, dealer_win = compare_between(player_hand, dealer_hand, player_win, dealer_win)
        printResult(player_hand, dealer_hand, player_win, dealer_win)
        if (player_win == 5):
            print(colored('YOU WIN!','green'))
            ans1=input("Play again? ")
            if (ans1 =="y" or ans1 == "Y"):
                main()
            else:
                print('THANKS FOR PLAYING!')
                return False

        elif (dealer_win == 5):
            print(colored('YOU LOST!','red'))
            ans2=input("Play again?")
            if (ans2 =="y" or ans2 == "Y"):
                main()
            else:
                print('THANKS FOR PLAYING!')
                return False
     

def printIntro():
    print (colored('\nBlackjack jest kasynową wersją gry w oczko. Zadaniem gracza jest uzyskać jak najbliżej (ale nie więcej niż) 21 punktów.','blue'))
    print (colored('W grze używa się kilku talii złożonych z 52 kart. ','blue'))
    print (colored('Karty od dwójki do dziesiątki mają wartość równą numerowi karty.','blue'))
    print (colored('Walet, Dama i Król mają wartość równą 10 punktów.','blue'))
    print (colored('As ma wartość równą 1 lub 11, w zależności co jest lepsze dla gracza.','blue'))
    print (colored('\nTwoja kolej:'))


def player():
    hand = []
    ans  ="h"
    hand.append(card())
    while ans[0] == "h" or ans[0] == "H":
        hand.append(card())
        hand = eval_ace(hand)
        print(colored("\nYour hand: {0} total = {1}".format(hand, sum(hand)),'green'))
        if bust(hand):
            break
        if blackjack(hand):
            break
        ans = input(colored("Do you want to Hit or Stand (H or S)? "))
        
    return hand


def card():
    talia=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    shuffle=random.randrange(len(talia))
    shuffle_card = talia[shuffle]
    return shuffle_card


def eval_ace(hand):
    
    total = sum(hand)
    for ace in hand:
        if ace == 11 and total > 21:
            position_ace = hand.index(11)
            hand[position_ace] = 1
    return hand


def bust(hand):
    total = sum(hand)
    if total > 21:
        return True


def blackjack(hand):
    total = sum(hand)
    if total == 21:
        return True


def dealer():
    hand = []
    hand.append(card())
    while sum(hand) <= 16:
        hand.append(card())
        hand = eval_ace(hand)
        if sum(hand) == 17:
            return hand
    
    return hand


def compare_between(player, dealer,player_win,dealer_win):
    total_player = sum(player)
    total_dealer = sum(dealer)
    player_bust = bust(player)
    dealer_bust = bust(dealer)
    player_blackjack = blackjack(player)
    dealer_blackjack = blackjack(dealer)
   
   
    if player_bust:
        if not dealer_blackjack and total_dealer < 21:
            dealer_win += 1
    if dealer_bust:
        if not player_blackjack and total_player < 21:
            player_win += 1
    if player_bust and dealer_bust:
        if total_player > total_dealer:
            player_win += 1
        elif total_dealer > total_player:
            dealer_win += 1
        else:
            return player_win, dealer_win

    if player_blackjack:
        print(colored('\nYou have BLACKJACK!','yellow'))
        player_win += 1
    if dealer_blackjack:
        dealer_win += 1
        print(colored('\nDealer has blackjack :(','red'))
    if player_blackjack and dealer_blackjack:
        # player_win == dealer_win
        return player_win, dealer_win
    if total_player < 21 and total_dealer < 21:
        if total_player > total_dealer:
            player_win += 1
        elif total_dealer > total_player:
            dealer_win += 1
        else:
            # player_win == dealer_win
            return player_win, dealer_win
    return player_win, dealer_win


def printResult(player_hand, dealer_hand, player_win, dealer_win):
    print(colored("\nResults: ",'red'))
    print("Player has: {0} total = {1}".format(player_hand, sum(player_hand)))    
    print("Dealer has: {0} total = {1}".format(dealer_hand, sum(dealer_hand)))
    print(colored("player: {} | dealer: {}".format(player_win, dealer_win),'blue'))


if __name__ == "__main__": main()


    
