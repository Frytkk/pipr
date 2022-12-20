from random import randint


class Casino:

    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def get_players(self):
        return self.players

    def dice_throw(self):
        return [randint(1, 6) for _ in range(4)]

    def get_winner(self):
        max_points = 0
        winners = 0
        for player in self.players:
            if player.points > max_points:
                max_points = player.points
                winners = 1
                winner = player
            elif player.points == max_points:
                winners += 1
        if winners == 1:
            return winner
        return None

    def play(self):
        for player in self.players:
            player.set = self.dice_throw()
            player.points = player.count_points()
            print(player.name, player.get_set(), player.points)
        return self.get_winner()


class Player:
    def __init__(self,  name):
        self.name = name
        self.set = None
        self.points = 0

    def get_set(self):
        return self.set

    def all_scores_even(self):
        for num in self.set:
            if num % 2 == 1:
                return False
        return True

    def all_scores_odd(self):
        for num in self.set:
            if num % 2 == 0:
                return False
        return True

    def count_points(self):
        points = 0
        help_points = 0

        if self.all_scores_even():
            points = sum(self.set) + 2
        elif self.all_scores_odd():
            points = sum(self.set) + 3

        if len(set(self.set)) != len(self.set):
            help_list = list(self.set)
            for element in set(self.set):
                help_list.remove(element)
            if len(help_list) == 1:
                help_points += 2 * help_list[0]
            elif len(help_list) == 2:
                if help_list[0] == help_list[1]:
                    help_points += 4 * help_list[0]
                else:
                    help_points += 2 * help_list[0]
                    help_points += 2 * help_list[1]
            else:
                help_points += 6 * help_list[0]

        self.points = max(points, help_points)
        return self.points
