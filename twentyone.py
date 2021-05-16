#NAME: Zeynep Kocacenk
#ID: 101146323
import random

#deal a card from deck
def dealCard():
    card = random.randint(1,13)
    return card

#get the value of card as in the original deck
    #'A','J','Q','K'
def displayHand(list):
    values = ''
    for l in list:
        if l == 1:
            values = values + "A" + ' '
        elif l == 11:
            values = values + "J" + ' '
        elif l == 12:
            values = values + "Q" + ' '
        elif l == 13:
            values = values + "K" + ' '
        else:
            values = values + str(l) + ' '
    return values

#adding all the cards that they have got
    #as in the int version
def sumHand(list):
    sum_cards = 0
    Aces_list = []  #this will keep track how many of aces the hand has
    for l in list:
        if l in [11,12,13]:
            sum_cards += 10
        elif l == 1:
            Aces_list.append("A")
        else:
            sum_cards += l

    #this will control if 'A' will be '1', or '11'
    for a in range(len(Aces_list)):
        if 11 + sum_cards > 21:
            sum_cards += 1
        else:
            sum_cards += 11
    return sum_cards

#this will determine how much will be deduct from the score
    #if x = the sum of hand
    #if x <= 21, the subract will be score - (21-x)
    #if x > 21, then it will be score - 21
def points_determining(x):
    points = 0
    if x > 21:
        points += 21
    else:
        points = (21-x)
    return points

#this will determine which category it will beling depends on the final score
def getRank(S):
    if S >= 95 and S <= 100:
        return "Ace!"
    elif S >= 85 and S <= 94:
        return "King"
    elif S >= 75 and S <= 84:
        return "Queen"
    elif S >= 50 and S <= 74:
        return "Jack"
    elif S >= 25 and S <= 49:
        return "Commoner"
    elif S >= -5 and S <= 24:
        return "Noob"

#this is the play which involves 5 rounds
    #it asks whether they 'hit' or 'stand',etc.
def play():
    score = 100

    for i in range(1,6):
        hands_of_cards = [dealCard(), dealCard()]
        values_with_deck = ''
        sums = sumHand(hands_of_cards)
        print(f"\nRound {i}\nScore: {score}")
        print(f"Your hand: {displayHand(hands_of_cards)} ({sums})")

        while True:
            want = input("Would you like to 'hit' or 'stand': ")
            if want == 'hit':
                get_card = dealCard()
                hands_of_cards.append(get_card)
                get_value = displayHand(hands_of_cards)
                values_with_deck += get_value
                sums = sumHand(hands_of_cards)
                print(f"Your hand: {get_value} ({sums})")
                if sums > 21:
                    print("Bust!")
                    score = score - points_determining(sums)
                    break
                else:
                    continue
            elif want == 'stand':
                score = score - points_determining(sums)
                break

            else:
                continue

    print(f"\nFinal Score: {score}, Your rank: {getRank(score)}")

#this will determine whether they want to play again or not
def main():
    play()
    while True:
        want = input("Would you like to play again? (y/n) ")
        if want == 'y':
            play()
            continue
        elif want == "n":
            print("Goodbye!")
            break
        else:
            print(f"I'm sorry {want} is not a valid option. Please enter 'y' or 'n'. ")
            continue

main()
