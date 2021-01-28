import sys

from utils import *

class Game:
    def __init__(self):
        self.bones = generate_bones()
        self.game_scheme = get_initial_bones(self.bones)
        self.player_bones = self.game_scheme[0]
        self.bot_bones = self.game_scheme[1]
        self.free_bones = self.game_scheme[2]
        self.game_tails = None
        self.table_bones = []
        self.current_player = None

    def start_game(self):
        player_first_bone = get_first_bone(self.player_bones)
        bot_first_bone = get_first_bone(self.bot_bones)
        self.current_player = set_current_player(player_first_bone, bot_first_bone)
        self.game_tails = player_first_bone if not self.current_player else bot_first_bone
        print(f"Tails are - {self.game_tails}")
        self.table_bones.append(self.game_tails)
        if self.current_player == 0:
            self.player_bones.remove(self.game_tails)
        else:
            self.bot_bones.remove(self.game_tails)

        # While all get bones
        while self.player_bones and self.bot_bones:
            if check_fish(self.game_tails, self.table_bones):
                count_point(self.player_bones, self.bot_bones)
            self.current_player ^= 1
            chosen_bone = None
            if self.current_player == 0:
                if check_bones(self.player_bones, self.game_tails):
                    chosen_bone = get_correct_bones(self.player_bones, self.game_tails)
                    self.player_bones.remove(chosen_bone)
                if not chosen_bone:
                    chosen_bone = self.pull_bone(self.player_bones)
                    while not get_possible_bones(self.game_tails, self.player_bones):
                        chosen_bone = self.pull_bone(self.player_bones)
                    self.player_bones.remove(chosen_bone)
            elif self.current_player == 1:
                if check_bones(self.bot_bones, self.game_tails):
                    possible_bones = get_possible_bones(self.game_tails, self.bot_bones)
                    if possible_bones:
                        chosen_bone = random.sample(possible_bones, 1)[0]
                        self.bot_bones.remove(chosen_bone)
                else:
                    chosen_bone = self.pull_bone(self.bot_bones)
                    while not get_possible_bones(self.game_tails, self.bot_bones):
                        chosen_bone = self.pull_bone(self.bot_bones)
                    self.bot_bones.remove(chosen_bone)
                print(f"Bot bones: {self.bot_bones}")

            if chosen_bone:
                self.update_tails(self.game_tails, chosen_bone)
                self.table_bones.append(chosen_bone)

        print("Game over")
        print("Bot wins ") if self.player_bones else print("Player wins")

    def update_tails(self, tails, new_bone):
        tails_first, tails_second = tails
        nb_first, nb_second = new_bone

        if tails_first == nb_first:
            self.game_tails = (tails_second, nb_second)
            print(f"Tails are - {self.game_tails}")
            return self.game_tails
        elif tails_first == nb_second:
            self.game_tails = (tails_second, nb_first)
            print(f"Tails are - {self.game_tails}")
            return self.game_tails
        elif tails_second == nb_second:
            self.game_tails = (tails_first, nb_first)
            print(f"Tails are - {self.game_tails}")
            return self.game_tails
        elif tails_second == nb_first:
            self.game_tails = (tails_first, nb_second)
            print(f"Tails are - {self.game_tails}")
            return self.game_tails
        else:
            print("wrong move")
            return self.game_tails

    def pull_bone(self, bones):
        print("Pull bone from the heap")
        try:
            free_bone = random.sample(self.free_bones, 1)[0]
            print(free_bone)
        except:
            sys.exit("You lose the Game ...")
        self.free_bones.remove(free_bone)
        bones.append(free_bone)
        return free_bone

if __name__ == '__main__':
    mygame = Game()
    mygame.start_game()