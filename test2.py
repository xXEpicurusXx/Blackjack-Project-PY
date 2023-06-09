import random
import os

def clear ():
    clear = lambda: os.system('clear') 
    clear()

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

  
def compare(user_score, computer_score, new_user_money, new_computer_money, pot):

  if user_score > 21 and computer_score > 21:
    new_computer_money += pot
    print(new_user_money)
    print(new_computer_money)
    return "You busted. You lose"

  if user_score == computer_score:
    return "Draw"

  elif computer_score == 0:
    new_computer_money += pot
    print(new_user_money)
    print(new_computer_money)
    return "Lose, opponent has Blackjack"

  elif user_score == 0:
    new_user_money += pot
    print(new_user_money)
    print(new_computer_money)
    return "Win with a Blackjack"

  elif user_score > 21:
    new_computer_money += pot
    print(new_user_money)
    print(new_computer_money)
    return "You busted. You lose"

  elif computer_score > 21:
    new_user_money += pot
    print(new_user_money)
    print(new_computer_money)
    return "Dealer busted. You win"

  elif user_score > computer_score:
    new_user_money += pot
    print(new_user_money)
    print(new_computer_money)
    return "You win"

  else:
    new_computer_money += pot
    print(new_user_money)
    print(new_computer_money)
    return "Dealer wins"

user_money = 1000
computer_money = 1000
pot = 0

def play_game():

  user_cards = []
  computer_cards = []

  game = False
  
  place_bet = int(input("Place your bet: "))
  new_user_money = user_money - place_bet
  new_computer_money = computer_money - place_bet
  new_pot = pot + (place_bet * 2)
    
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not game:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Your pile = ${new_user_money}")

    print("\n")
    
    print(f"Dealer's cards: {computer_cards[0]}, X")
    print(f"Dealer pile = ${new_computer_money}")
    
    print("\n")
    
    print(f"Current pot = ${new_pot}")


    if user_score == 0 or computer_score == 0 or user_score > 21:
        game = True
    else:
        user_should_deal = input("Type '1' to Hit, type '2' to Stay: ")
        if user_should_deal == "1":
            user_cards.append(deal_card())
        else:
            game = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score, user_money, computer_money, pot))

play_game()

while input("Play again? Type 'y' or 'n': ") == "y":
    clear()
    play_game()