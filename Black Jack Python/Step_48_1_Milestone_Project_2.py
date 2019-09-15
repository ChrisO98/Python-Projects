# We've learned enough to start a second milestone project!
# You can treat this project a few ways:
#   Code along project with the solutions.
#   Attempt the project on your own. ( DID THIS ONE )
#   Use the workbook as a guid for the project on your own.

# Will be creating a Black Jack game
# For this project you will use OOP to create a BlackJack Game with Python.
# Let's quickly go over the main idea of the game and discuss how OOP should be used for this project.

# For our version of the game we will only have a computer dealer and a human player.
# We start with a normal deck of cards, you will create a representation of a deck with Python.

# SO we have a Computer Dealer, a Human Player, a Deck of Cards (52 Cards), the Player has a Bank Roll(amount of funds,
# Player will place a bet with the amount of funds they have, Dealer passes the Player a card face up then the Dealer
# gets a card face up then another card to the Player face up and then the Dealer gets a card face down, SO the Player
# starts with 2 cards face up, the Player goes first, SO the Player must get 21 to win or closer to it than the Dealer,
# Player may only Hit or Stay, after the Player's turn it is the Dealers turn and if the player is under 21 the Dealer
# will hit and this will go back and forth until they beat the Player get close/to 21 or the Dealer busts or if the
# Player Busts or the Player Wins

# Special Rules:
#   Face Cards (Jack, Queen, King) count as a value of 10
#   Aces can count as either 1 or 11 whichever value is preferable to the player
#   If a player holds an ace valued as 11, the hand is called "soft", meaning that the player cannot go bust
#   by taking an additional card; the value of the ace will become 1 to prevent the hand from exceeding 21.

# If a dealer has less than 17, they must continue drawing cards until they reach 17 or above, without going over 21.
# Once the dealer reaches a score of 17 or more, he/she will then stand
########################################################################################################################

# After completion of this black jack game I evaluated the coding.
# This works but do not code like this ever again. It is bad coding there are too many if and else statements and the
# readability is not good. This works but in terms of good coding this is VERY bad!


class DeckOfCards:

    def __init__(self, deck=52, clubs=None, diamonds=None, spades=None, hearts=None):
        self.deck = deck
        self.clubs = clubs
        self.diamonds = diamonds
        self.spades = spades
        self.hearts = hearts

    def hit(self):
        import random
        while True:

            rng = random.randint(0, 3)
            if rng == 0:
                rng = self.clubs
            elif rng == 1:
                rng = self.diamonds
            elif rng == 2:
                rng = self.spades
            else:
                rng = self.hearts

            if rng == self.clubs:
                get = str(random.randint(0, 12))
                dkey = [
                    'King of Clubs',
                    'Queen of Clubs',
                    'Jack of Clubs',
                    'Ace of Clubs',
                    'Two of Clubs',
                    'Three of Clubs',
                    'Four of Clubs',
                    'Five of Clubs',
                    'Six of Clubs',
                    'Seven of Clubs',
                    'Eight of Clubs',
                    'Nine of Clubs',
                    'Ten of Clubs'
                ]

                while True:
                    for i in dkey:
                        try:
                            grab = self.clubs[get][i]
                        except KeyError:
                            del i
                            continue
                        else:
                            self.deck -= 1
                            name = i
                            del self.clubs[get]
                            return grab, get, name  # grab added to player's sum
                        # going to need to add if statement for 'ace' since its a special case probably in 'Player'class
            elif rng == self.diamonds:
                get = str(random.randint(0, 12))
                dkey = [
                    'King of Diamonds',
                    'Queen of Diamonds',
                    'Jack of Diamonds',
                    'Ace of Diamonds',
                    'Two of Diamonds',
                    'Three of Diamonds',
                    'Four of Diamonds',
                    'Five of Diamonds',
                    'Six of Diamonds',
                    'Seven of Diamonds',
                    'Eight of Diamonds',
                    'Nine of Diamonds',
                    'Ten of Diamonds'
                ]

                while True:
                    for i in dkey:
                        try:
                            grab = self.diamonds[get][i]
                        except KeyError:
                            del i
                            continue
                        else:
                            self.deck -= 1
                            name = i
                            del self.diamonds[get]
                            return grab, get, name  # grab added to player's sum
            elif rng == self.spades:
                get = str(random.randint(0, 12))
                dkey = [
                    'King of Spades',
                    'Queen of Spades',
                    'Jack of Spades',
                    'Ace of Spades',
                    'Two of Spades',
                    'Three of Spades',
                    'Four of Spades',
                    'Five of Spades',
                    'Six of Spades',
                    'Seven of Spades',
                    'Eight of Spades',
                    'Nine of Spades',
                    'Ten of Spades'
                ]

                while True:
                    for i in dkey:
                        try:
                            grab = self.spades[get][i]
                        except KeyError:
                            del i
                            continue
                        else:
                            self.deck -= 1
                            name = i
                            del self.spades[get]
                            return grab, get, name  # grab added to player's sum
            elif rng == self.hearts:
                get = str(random.randint(0, 12))
                dkey = [
                    'King of Hearts',
                    'Queen of Hearts',
                    'Jack of Hearts',
                    'Ace of Hearts',
                    'Two of Hearts',
                    'Three of Hearts',
                    'Four of Hearts',
                    'Five of Hearts',
                    'Six of Hearts',
                    'Seven of Hearts',
                    'Eight of Hearts',
                    'Nine of Hearts',
                    'Ten of Hearts'
                ]

                while True:
                    for i in dkey:
                        try:
                            grab = self.hearts[get][i]
                        except KeyError:
                            del i
                            continue
                        else:
                            self.deck -= 1
                            name = i
                            del self.hearts[get]
                            return grab, get, name  # grab added to player's sum

            break


class Chips:

    def __init__(self, balance, give=20):
        self.balance = balance
        self.give = give

    def __str__(self):
        return f"Your bank: ${self.balance}\nIf you do not enter any bet, it will default to $20\nBets must be $20 or more"

    def bet(self):
        while True:
            try:
                if self.give >= 20:
                    self.balance -= self.give
                    print(f'New Balance: ${self.balance}')
                    break
            except:
                print("Exceeded Bank Amount!")
                print(self.give)
                continue
            else:
                self.balance += self.give
                while self.give < 20:
                    print('Bet must be greater than or equal to $20')
                    self.give = int(input('Place your bet: '))
                self.balance -= self.give


# Create a class for aces #
class Aces:

    def __init__(self, num1, num2, num3, num4, num5=None, num6=None, num7=None, num8=None, num9=None, num10=None):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
        self.num8 = num8
        self.num9 = num9
        self.num10 = num10

    def aces(self):
        if self.num1 == (1, 11):
            self.num1 = 11
        if self.num2 == (1, 11):
            self.num2 = 11
        if self.num3 == (1, 11):
            self.num3 = 11
        if self.num4 == (1, 11):
            self.num4 = 11
        if self.num5 == (1, 11):
            self.num5 = 11
        if self.num6 == (1, 11):
            self.num6 = 11
        if self.num7 == (1, 11):
            self.num7 = 11
        if self.num8 == (1, 11):
            self.num8 = 11
        if self.num9 == (1, 11):
            self.num9 = 11
        if self.num10 == (1, 11):
            self.num10 = 11
        if self.num1 == 11 and self.num3 == 11:
            self.num1 = 1
        if self.num2 == 11 and self.num4 == 11:
            self.num2 = 1
        return self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10

    def over21_ace(self, player_sum=None, dealer_sum=None):
        # Will need the player_sum and dealer_sum and check for aces and convert to them to 1 #
        if player_sum > 21:
            if self.num1 == 11:
                self.num1 = 1
            if self.num3 == 11:
                self.num3 = 1
            if self.num5 == 11:
                self.num5 = 1
            if self.num7 == 11:
                self.num7 = 1
            if self.num9 == 11:
                self.num9 = 1
        elif player_sum <= 21:
            return self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10
        if dealer_sum > 21:
            if self.num2 == 11:
                self.num2 = 1
            if self.num4 == 11:
                self.num4 = 1
            if self.num6 == 11:
                self.num6 = 1
            if self.num8 == 11:
                self.num8 = 1
            if self.num10 == 11:
                self.num10 = 1
        return self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7, self.num8, self.num9, self.num10


class Hand:

    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

    def human(self, fifth=None, seventh=None, ninth=None):

        # display human hand
        print("\nPlayer's Hand:")
        print(f'    {self.first}')
        print(f'    {self.third}')
        if fifth is not None:
            print(f'    {fifth}')
            if seventh is not None:
                print(f'    {seventh}')
                if ninth is not None:
                    print(f'    {seventh}')
                else:
                    pass
            else:
                pass
        else:
            pass

    def computer(self, sixth=None, eighth=None, tenth=None):
        # display computer hand
        print("\nDealer's hand:")
        print(f'    {self.second}')
        # Can create a hidden card #
        # If Player stays reveal hidden card and check to see who wins! #
        if self.fourth == 0:
            print('    Hidden')
        elif self.fourth != 0:
            print(f'    {self.fourth}')
            if sixth is not None:
                print(f'    {sixth}')
                if eighth is not None:
                    print(f'    {eighth}')
                    if tenth is not None:
                        print(f'    {tenth}')
                else:
                    pass
            else:
                pass
    # Maybe do a __name__=='__main__' for doing the def in a specific order


def play_game(balances):
    clubs = {
        '0': {'King of Clubs': 10},
        '1': {'Queen of Clubs': 10},
        '2': {'Jack of Clubs': 10},
        '3': {'Ace of Clubs': (1, 11)},
        '4': {'Two of Clubs': 2},
        '5': {'Three of Clubs': 3},
        '6': {'Four of Clubs': 4},
        '7': {'Five of Clubs': 5},
        '8': {'Six of Clubs': 6},
        '9': {'Seven of Clubs': 7},
        '10': {'Eight of Clubs': 8},
        '11': {'Nine of Clubs': 9},
        '12': {'Ten of Clubs': 10},
    }

    diamonds = {
        '0': {'King of Diamonds': 10},
        '1': {'Queen of Diamonds': 10},
        '2': {'Jack of Diamonds': 10},
        '3': {'Ace of Diamonds': (1, 11)},
        '4': {'Two of Diamonds': 2},
        '5': {'Three of Diamonds': 3},
        '6': {'Four of Diamonds': 4},
        '7': {'Five of Diamonds': 5},
        '8': {'Six of Diamonds': 6},
        '9': {'Seven of Diamonds': 7},
        '10': {'Eight of Diamonds': 8},
        '11': {'Nine of Diamonds': 9},
        '12': {'Ten of Diamonds': 10},
    }

    spades = {
        '0': {'King of Spades': 10},
        '1': {'Queen of Spades': 10},
        '2': {'Jack of Spades': 10},
        '3': {'Ace of Spades': (1, 11)},
        '4': {'Two of Spades': 2},
        '5': {'Three of Spades': 3},
        '6': {'Four of Spades': 4},
        '7': {'Five of Spades': 5},
        '8': {'Six of Spades': 6},
        '9': {'Seven of Spades': 7},
        '10': {'Eight of Spades': 8},
        '11': {'Nine of Spades': 9},
        '12': {'Ten of Spades': 10},
    }

    hearts = {
        '0': {'King of Hearts': 10},
        '1': {'Queen of Hearts': 10},
        '2': {'Jack of Hearts': 10},
        '3': {'Ace of Hearts': (1, 11)},
        '4': {'Two of Hearts': 2},
        '5': {'Three of Hearts': 3},
        '6': {'Four of Hearts': 4},
        '7': {'Five of Hearts': 5},
        '8': {'Six of Hearts': 6},
        '9': {'Seven of Hearts': 7},
        '10': {'Eight of Hearts': 8},
        '11': {'Nine of Hearts': 9},
        '12': {'Ten of Hearts': 10},
    }

    bank = Chips(balance=balances)
    print(bank)
    gives = input('How much do you want to bet: ')
    if gives == '':
        gives = 20
    while gives > '500' or gives < '20':
        print('Bet must be a minimum of $20 or no greater than $500')
        gives = input('How much do you want to bet: ')

    gives = int(gives)
    bank = Chips(balance=balances, give=gives)
    bank.bet()
    # Separate player and dealer hit's
    try:
        run = DeckOfCards(52, clubs, diamonds, spades, hearts)
        result = run.hit()
        first = result[2]
        result2 = run.hit()
        second = result2[2]
        result3 = run.hit()
        third = result3[2]
        result4 = run.hit()
        fourth = result4[2]
        nums = Aces(num1=result[0], num2=result2[0], num3=result3[0], num4=result4[0]).aces()
        Hand(first, second, third, fourth).human()
        player_sum = nums[0] + nums[2]
        print(player_sum)
        print('')
        Hand(first, second, third, 0).computer()
        # Need to hide second card and number for dealer #
        dealer_sum = nums[1]
        print(dealer_sum)
        print('')

        if player_sum <= 21 and dealer_sum <= 21:
            ask_player = input('Do you want to hit or stay: ')
            while ask_player != 'hit' and ask_player != 'stay':
                ask_player = input('Do you want to hit or stay: ')
            if ask_player == 'hit':
                result5 = run.hit()
                fifth = result5[2]
                five = result5[0]
                new_num = Aces(nums[0], nums[1], nums[2], nums[3], five).aces()
                player_sum += new_num[4]
                Hand(first, second, third, fourth).human(fifth)
                if (player_sum > 21 and nums[4] == 11) or (player_sum > 21 and nums[2] == 11) or (player_sum > 21 and nums[0] == 11):
                    check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4]).over21_ace(player_sum)
                    player_sum = check[0] + check[2] + check[4]
                    print(player_sum)
                    Hand(first, second, third, 0).computer()
                    print(dealer_sum)
                    if player_sum > 21:
                        print('Player Busted!')
                        balances = balances - gives
                        return balances
                elif player_sum > 21:
                    print(player_sum)
                    Hand(first, second, third, fourth).computer()
                    print(dealer_sum)
                    print('Player Busted!')
                    balances = balances - gives
                    return balances
                elif player_sum == 21:
                    print(player_sum)
                    dealer_sum = nums[1] + nums[3]
                    if not (17 <= dealer_sum <= 21):
                        if dealer_sum > 21:
                            print("Dealer Busted!")
                            print(f"Player WINS {gives * 2}!")
                            balances = balances + gives * 2
                            return balances
                        result6 = run.hit()
                        sixth = result6[2]
                        six = result6[0]
                        new_num = Aces(nums[0], nums[1], nums[2], nums[3], nums[4], six).aces()
                        dealer_sum += new_num[5]
                        Hand(first, second, third, fourth).computer(sixth)
                        if dealer_sum > 21:
                            check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4],
                                         new_num[5]).over21_ace(
                                player_sum, dealer_sum)
                            dealer_sum = check[1] + check[3] + check[5]
                        print(dealer_sum)
                        if dealer_sum > player_sum:
                            if dealer_sum <= 21:
                                print("Dealer WINS!")
                                balances = balances - gives
                                return balances
                            elif dealer_sum > 21:
                                print("Dealer Busted!")
                                print(f"Player WINS {gives * 2}!")
                                balances = balances + gives * 2
                                return balances
                        if 17 <= dealer_sum == 21:
                            if dealer_sum > player_sum:
                                print("Dealer WINS!")
                                balances = balances - gives
                                return balances
                            elif dealer_sum < player_sum:
                                print(f'Player WINS {gives * 2}!')
                                balances = balances + gives * 2
                                return balances

                        if not (17 <= dealer_sum == 21):
                            Hand(first, second, third, fourth).human()
                            print(player_sum)
                            if dealer_sum > 21:
                                print("Dealer Busted!")
                                print(f"Player WINS {gives * 2}!")
                                balances = balances + gives * 2
                                return balances
                            result8 = run.hit()
                            eighth = result8[2]
                            eight = result8[0]
                            new_num = Aces(nums[0], nums[1], nums[2], nums[3], 0, six, 0, eight).aces()
                            dealer_sum += new_num[7]
                            Hand(first, second, third, fourth).computer(sixth, eighth)
                            if dealer_sum > 21:
                                check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4],
                                             new_num[5], new_num[6], new_num[7]).over21_ace(
                                    player_sum, dealer_sum)
                                dealer_sum = check[1] + check[3] + check[5] + check[7]
                            print(dealer_sum)
                            Hand(first, second, third, fourth).human()
                            print(player_sum)
                            if dealer_sum > 21:
                                print("Dealer Busted!")
                                print(f"Player WINS {gives * 2}!")
                                balances = balances + gives * 2
                                return balances
                            if not (17 <= dealer_sum == 21):
                                result10 = run.hit()
                                tenth = result10[2]
                                ten = result10[0]
                                new_num = Aces(nums[0], nums[1], nums[2], nums[3], 0, six, 0, eighth, 0, ten).aces()
                                dealer_sum += new_num[5]
                                Hand(first, second, third, fourth).computer(sixth, eighth, tenth)
                                if dealer_sum > 21:
                                    check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4],
                                                 new_num[5], new_num[6], new_num[7], new_num[8], new_num[9]).over21_ace(
                                        player_sum, dealer_sum)
                                    dealer_sum = check[1] + check[3] + check[5] + check[7] + check[9]
                                print(dealer_sum)
                                if dealer_sum > player_sum:
                                    if dealer_sum <= 21:
                                        print("Dealer WINS!")
                                        balances = balances - gives
                                        return balances
                                    elif dealer_sum > 21:
                                        print("Dealer Busted!")
                                        print(f"Player WINS {gives * 2}!")
                                        balances = balances + gives * 2
                                        return balances
                            if dealer_sum > player_sum and dealer_sum > 21:
                                print("Dealer Busted!")
                                print(f"Player WINS {gives * 2}!")
                                balances = balances + gives * 2
                                return balances
                            elif player_sum < dealer_sum <= 21:
                                print('Dealer WINS!')
                                balances = balances - gives
                                return balances
                            elif dealer_sum < player_sum:
                                print('Player WINS!')
                                balances = balances + gives * 2
                                return balances
                        elif dealer_sum < player_sum:
                            print(f"Player WINS {gives * 2}!")
                            balances = balances + gives * 2
                            return balances
                        elif dealer_sum > player_sum:
                            print('Dealer WINS!')
                            balances = balances - gives
                            return balances

                    elif dealer_sum > player_sum:
                        if dealer_sum <= 21:
                            print("Dealer WINS!")
                            balances = balances - gives
                            return balances
                        elif dealer_sum > 21:
                            print("Dealer Busted!")
                            print(f"Player WINS {gives * 2}!")
                            balances = balances + gives * 2
                            return balances
                    elif dealer_sum < player_sum:
                        print(f"Player WINS {gives * 2}!")
                        balances = balances + gives * 2
                        return balances
                    if dealer_sum == player_sum:
                        print("It's a tie!")
                        balances = balances + gives
                        return balances
                elif player_sum > 21:
                    print('Player Busted!')
                    balances = balances - gives
                    return balances
                elif player_sum < 21:
                    print(player_sum)
                    Hand(first, second, third, 0).computer()
                    print(dealer_sum)
                    ask_player = input('Do you want to hit or stay: ')

                    if ask_player == 'hit':
                        result7 = run.hit()
                        seventh = result7[2]
                        seven = result7[0]
                        new_num = Aces(nums[0], nums[1], nums[2], nums[3], five, 0, seven).aces()
                        player_sum += new_num[6]
                        if player_sum > 21:  # something wrong when going over 21 #
                            Hand(first, second, third, fourth).human(fifth, seventh)
                            check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4], new_num[5],
                                         new_num[6]).over21_ace(player_sum)
                            player_sum = check[0] + check[2] + check[4] + check[6]
                            print(player_sum)
                            if player_sum > 21:
                                Hand(first, second, third, fourth).computer()
                                print(dealer_sum)
                                print('Player Busted!')
                                print('Dealer WINS!')
                                balances = balances - gives
                                return balances
                        Hand(first, second, third, fourth).human(fifth, seventh)
                        check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4], 0, new_num[6]).over21_ace(player_sum)
                        player_sum = check[0] + check[2] + check[4] + check[6]
                        print(player_sum)
                        Hand(first, second, third, fourth).computer()
                        print(dealer_sum)
                        if player_sum > 21:
                            print('Player Busted!')
                            print('Dealer WINS!')
                            balances = balances - gives
                            return balances
                        ask_player = input('Do you want to hit or stay: ')
                        if ask_player == 'stay':

                            if dealer_sum < player_sum and dealer_sum <= 17:
                                result6 = run.hit()
                                sixth = result6[2]
                                six = result6[0]
                                new_num = Aces(nums[0], nums[1], nums[2], nums[3], five, six, seven).aces()
                                dealer_sum += new_num[5]
                                Hand(first, second, third, fourth).human(fifth, seventh)
                                print(player_sum)
                                Hand(first, second, third, fourth).computer(sixth)
                                if dealer_sum > 21:
                                    check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4], new_num[5], new_num[6]).over21_ace(player_sum, dealer_sum)
                                    dealer_sum = check[1] + check[3] + check[5]
                                print(dealer_sum)
                                if dealer_sum > player_sum:
                                    if dealer_sum <= 21:
                                        print('Dealer WINS!')
                                        balances = balances - gives
                                        return balances
                                elif dealer_sum < player_sum and not (17 <= dealer_sum == 21):
                                    result8 = run.hit()
                                    eighth = result8[2]
                                    eight = result8[0]
                                    new_num = Aces(nums[0], nums[1], nums[2], nums[3], five, six, seven, eight).aces()
                                    dealer_sum += new_num[5]
                                    Hand(first, second, third, fourth).human(fifth, seventh)
                                    print(player_sum)
                                    Hand(first, second, third, fourth).computer(sixth, eighth)
                                    if dealer_sum > 21:
                                        check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4], new_num[5],
                                                     new_num[6], new_num[7]).over21_ace(player_sum, dealer_sum)
                                        dealer_sum = check[1] + check[3] + check[5] + check[7]
                                    print(dealer_sum)
                                elif dealer_sum and player_sum == 21:
                                    print("Y'all tied!")
                                    balances = balances + gives
                                    return balances
                                elif dealer_sum > 21:
                                    print("Dealer Busted!")
                                    print(f"Player WINS {gives * 2}!")
                                    balances = balances + gives * 2
                                    return balances
                                elif dealer_sum == 21:
                                    print('Dealer WINS!')
                                    balances = balances - gives
                                    return balances

                            elif dealer_sum < player_sum == 21:
                                print(f"Player WINS {gives * 2}!")
                                balances = balances + gives * 2
                                return balances
                            elif dealer_sum == player_sum:
                                print("Y'all tied!")
                                balances = balances + gives
                                return balances
                            elif player_sum < dealer_sum:
                                print('Dealer WINS!')
                                balances = balances - gives
                                return balances

                    elif ask_player == 'stay':
                        # now dealer hits #
                        dealer_sum = nums[1] + nums[3]
                        if dealer_sum == player_sum:
                            print("Y'all tied!")
                            balances = balances + gives
                            return balances
                        elif (dealer_sum < player_sum) and not (17 <= dealer_sum == 21):
                            result6 = run.hit()
                            sixth = result6[2]
                            six = result6[0]
                            new_num = Aces(nums[0], nums[1], nums[2], nums[3], five, six).aces()
                            dealer_sum += new_num[5]
                            Hand(first, second, third, fourth).human(fifth)
                            print(player_sum)
                            Hand(first, second, third, fourth).computer(sixth)
                            if dealer_sum > 21:
                                check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4], new_num[5],
                                             new_num[6]).over21_ace(player_sum, dealer_sum)
                                dealer_sum = check[1] + check[3] + check[5]
                            print(dealer_sum)
                            if dealer_sum < player_sum and not (17 <= dealer_sum == 21):
                                result8 = run.hit()
                                eighth = result8[2]
                                eight = result8[0]
                                new_num = Aces(nums[0], nums[1], nums[2], nums[3], five, six, 0, eight).aces()
                                dealer_sum += new_num[5]
                                Hand(first, second, third, fourth).human(fifth)
                                print(player_sum)
                                Hand(first, second, third, fourth).computer(sixth, eighth)
                                if dealer_sum > 21:
                                    check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4], new_num[5],
                                                 new_num[6], new_num[7]).over21_ace(player_sum, dealer_sum)
                                    dealer_sum = check[1] + check[3] + check[5] + check[7]
                                    print(dealer_sum)
                                    if dealer_sum > 21:
                                        print('Dealer Busted!')
                                        balances = balances + gives * 2
                                        return balances
                            elif dealer_sum == player_sum:
                                print("Y'all tied!")
                                balances = balances + gives
                                return balances
                            elif dealer_sum > 21:
                                print("Dealer Busted!")
                                print(f"Player WINS {gives * 2}!")
                                balances = balances + gives * 2
                                return balances
                            elif dealer_sum == 21:
                                print('Dealer WINS!')
                                balances = balances - gives
                                return balances

                        elif dealer_sum < player_sum == 21:
                            print(f"Player WINS {gives * 2}!")
                            balances = balances + gives * 2
                            return balances
                        elif player_sum < dealer_sum <= 21:
                            print("Dealer WINS!")
                            balances = balances - gives
                            return balances

            elif ask_player == 'stay':
                if dealer_sum > player_sum:
                    print("Dealer WINS!")
                    balances = balances - gives
                    return balances
                elif dealer_sum < 17:
                    Hand(first, second, third, fourth).human()
                    print(player_sum)
                    dealer_sum = nums[1] + nums[3]
                    if dealer_sum > 21:
                        print("Dealer Busted!")
                        print(f"Player WINS {gives * 2}!")
                        balances = balances + gives * 2
                        return balances
                    result6 = run.hit()
                    sixth = result6[2]
                    six = result6[0]
                    new_num = Aces(nums[0], nums[1], nums[2], nums[3], 0, six).aces()
                    dealer_sum += new_num[5]
                    Hand(first, second, third, fourth).computer(sixth)
                    if dealer_sum > 21:
                        check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4], new_num[5]).over21_ace(
                            player_sum, dealer_sum)
                        dealer_sum = check[1] + check[3] + check[5]
                        print(dealer_sum)
                        if dealer_sum > player_sum:
                            if dealer_sum <= 21:
                                print("Dealer WINS!")
                                balances = balances - gives
                                return balances
                            elif dealer_sum > 21:
                                print("Dealer Busted!")
                                print(f"Player WINS {gives * 2}!")
                                balances = balances + gives * 2
                                return balances
                        if 17 <= dealer_sum == 21:
                            if dealer_sum > player_sum:
                                print("Dealer WINS!")
                                balances = balances - gives
                                return balances
                            elif dealer_sum < player_sum:
                                print(f'Player WINS {gives * 2}!')
                                balances = balances + gives * 2
                                return balances
                    elif 17 <= dealer_sum <= 21:
                        print(dealer_sum)
                        if dealer_sum > player_sum:
                            print('Dealer WINS!')
                            balances = balances - gives
                            return balances
                        elif dealer_sum < player_sum:
                            print(f'Player WINS {gives * 2}!')
                            balances = balances + gives * 2
                            return balances
                    elif dealer_sum < 17:
                        print(dealer_sum)
                        Hand(first, second, third, fourth).human()
                        print(player_sum)
                        if dealer_sum > 21:
                            print("Dealer Busted!")
                            print(f"Player WINS {gives * 2}!")
                            balances = balances + gives * 2
                            return balances
                        result8 = run.hit()
                        eighth = result8[2]
                        eight = result8[0]
                        new_num = Aces(nums[0], nums[1], nums[2], nums[3], 0, six, 0, eight).aces()
                        dealer_sum += new_num[7]
                        Hand(first, second, third, fourth).computer(sixth, eighth)
                        if dealer_sum > 21:
                            check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4],
                                         new_num[5], new_num[6], new_num[7]).over21_ace(
                                player_sum, dealer_sum)
                            dealer_sum = check[1] + check[3] + check[5] + check[7]
                        print(dealer_sum)
                        if dealer_sum > 21:
                            print("Dealer Busted!")
                            print(f"Player WINS {gives * 2}!")
                            balances = balances + gives * 2
                            return balances
                        elif dealer_sum == player_sum:
                            print("Y'all tied!")
                            balances = balances + gives
                            return balances
                        elif dealer_sum < 17:
                            Hand(first, second, third, fourth).human()
                            print(player_sum)
                            result10 = run.hit()
                            tenth = result10[2]
                            ten = result10[0]
                            new_num = Aces(nums[0], nums[1], nums[2], nums[3], 0, six, 0, eighth, 0, ten).aces()
                            dealer_sum += new_num[5]
                            Hand(first, second, third, fourth).computer(sixth, eighth, tenth)
                            if dealer_sum > 21:
                                check = Aces(new_num[0], new_num[1], new_num[2], new_num[3], new_num[4],
                                             new_num[5], new_num[6], new_num[7], new_num[8], new_num[9]).over21_ace(
                                    player_sum, dealer_sum)
                                dealer_sum = check[1] + check[3] + check[5] + check[7] + check[9]
                            print(dealer_sum)
                            if dealer_sum > player_sum:
                                if dealer_sum <= 21:
                                    print("Dealer WINS!")
                                    balances = balances - gives
                                    return balances
                                elif dealer_sum > 21:
                                    print("Dealer Busted!")
                                    print(f"Player WINS {gives * 2}!")
                                    balances = balances + gives * 2
                                    return balances
                        elif dealer_sum > player_sum and dealer_sum > 21:
                            print("Dealer Busted!")
                            print(f"Player WINS {gives * 2}!")
                            balances = balances + gives * 2
                            return balances
                        elif player_sum < dealer_sum <= 21:
                            print('Dealer WINS!')
                            balances = balances - gives
                            return balances
                        elif dealer_sum < player_sum:
                            print('Player WINS!')
                            balances = balances + gives * 2
                            return balances
                    elif dealer_sum < player_sum:
                        print(f"Player WINS {gives * 2}!")
                        balances = balances + gives * 2
                        return balances
                    elif dealer_sum > player_sum:
                        print('Dealer WINS!')
                        balances = balances - gives
                        return balances

                elif 17 <= dealer_sum <= 21:
                    if dealer_sum > player_sum:
                        print('Dealer WINS!')
                        balances = balances - gives
                        return balances
                    elif dealer_sum < player_sum:
                        print(f'Player WINS {gives * 2}')
                        balances = balances + gives * 2
                        return balances
                elif dealer_sum > player_sum:
                    if dealer_sum <= 21:
                        print("Dealer WINS!")
                        return balances
                    elif dealer_sum > 21:
                        print("Dealer Busted!")
                        print(f"Player WINS {gives * 2}!")
                        balances = balances + gives * 2
                        return balances
                elif dealer_sum < player_sum:
                    print(f"Player WINS {gives * 2}!")
                    balances = balances + gives * 2
                    return balances
                if dealer_sum == player_sum:
                    print("It's a tie!")
                    balances = balances + gives
                    return balances
        if dealer_sum == 21 and player_sum == 21:
            print("Y'all tied!")
            balances = balances - gives
            return balances
        elif player_sum < dealer_sum == 21:
            print('Dealer WINS!')
            balances = balances - gives
            return balances
        elif (dealer_sum <= 21) and (player_sum > 21):
            print(player_sum)
            print('Dealer WINS!')
            balances = balances - gives
            return balances
        elif player_sum > 21:
            print('Player Busted!')
            balances = balances - gives
            return balances
    except TypeError:
        print(player_sum)
        print('Player Busted')
        balances = balances - gives
        return balances


def blackjack():
    print("Welcome to Black Jack!\n")
    balances = 500
    play = play_game(balances)
    print(play)

    while play >= 20:
        play_again = input("\nWould you like to keep playing, yes or no? ")
        if play_again == 'yes':
            play = play_game(play)
        elif play_again == 'no':
            print("\nThanks for playing!")
            break
    else:
        print('Out of Money!')


blackjack()
