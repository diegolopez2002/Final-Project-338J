import random

class Blackjack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(self.deck)
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]

    def calculate_hand(self, hand):
        total = sum(hand)
        aces = hand.count(11)
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def play(self, action):
        if action == "hit":
            self.player_hand.append(self.deck.pop())
            if self.calculate_hand(self.player_hand) > 21:
                return {"result": "bust", "player_hand": self.player_hand}
        elif action == "stand":
            while self.calculate_hand(self.dealer_hand) < 17:
                self.dealer_hand.append(self.deck.pop())
            dealer_total = self.calculate_hand(self.dealer_hand)
            player_total = self.calculate_hand(self.player_hand)

            if dealer_total > 21 or player_total > dealer_total:
                return {"result": "win", "player_hand": self.player_hand, "dealer_hand": self.dealer_hand}
            elif player_total < dealer_total:
                return {"result": "lose", "player_hand": self.player_hand, "dealer_hand": self.dealer_hand}
            else:
                return {"result": "draw", "player_hand": self.player_hand, "dealer_hand": self.dealer_hand}

        return {"player_hand": self.player_hand}

