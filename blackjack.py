import random
import os

def clear ():
    # clear = lambda: os.system('clear') 
    os.system("cls")

def betting():
  user_cash = 1000
  computer_cash = 1000
  pot = 0

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

def compare(user_score, computer_score,user_cash, computer_cash, pot):

  user_cash = 900
  computer_cash = 900
  pot = 200

  if user_score > 21 and computer_score > 21:
    computer_cash += 200
    pot -= 200
    return "You busted. You lose"

  if user_score == computer_score:
    user_cash += 100
    computer_cash += 100
    pot -= 200
    return "Draw"

  elif computer_score == 0:
    computer_cash += 200
    pot -= 200
    return "Lose, opponent has Blackjack"

  elif user_score == 0:
    user_cash += 200
    pot -= 200
    return "Win with a Blackjack"

  elif user_score > 21:
    computer_cash += 200
    pot -= 200
    return "You busted. You lose"

  elif computer_score > 21:
    user_cash += 200
    pot -= 200
    return "Dealer busted. You win"
    

  elif user_score > computer_score:
    user_cash += 200
    pot -= 200
    return "You win"

  else:
    computer_cash += 200
    pot -= 200
    return "Dealer wins"

def play_game():

  user_cards = []
  computer_cards = []
  game = False
      
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game:
    global user_cash
    global computer_cash
    global pot

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Player cash = ${new_user_cash}")
    print("\n")
    
    print(f"Dealer's cards: {computer_cards[0]}, X")
    print(f"Dealer cash = ${new_computer_cash}")
    print("\n")

    print(f"Pot = ${new_pot}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game = True
    else:
      user_should_deal = input("Type '1' to Hit, type '2' to Stay: ")
      if user_should_deal == "1":
        user_cards.append(deal_card())
        clear()
      else:
        clear()
        game = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")

  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score,user_cash, computer_cash, pot))

play_game()

while input("Play again? Type 'y' or 'n': ") == "y":
  global user_cash 
  user_cash = user_cash - 100
  global computer_cash 
  computer_cash = computer_cash - 100
  global pot
  pot = pot + 200
  clear()
  play_game()
  
  #needs a betting system
  #needs to play with more than 1 persoan 