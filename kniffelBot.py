import random
import itertools


class YahtzeeBot:
    def __init__(self):
        self.scorecard = {
            "ones": None,
            "twos": None,
            "threes": None,
            "fours": None,
            "fives": None,
            "sixes": None,
            "three_of_a_kind": None,
            "four_of_a_kind": None,
            "full_house": None,
            "small_straight": None,
            "large_straight": None,
            "yahtzee": None,
            "chance": None,
        }
        self.CATEGORY_TO_NUM_DICE = {
            "ones": 1,
            "twos": 1,
            "threes": 1,
            "fours": 1,
            "fives": 1,
            "sixes": 1,
            "three_of_a_kind": 3,
            "four_of_a_kind": 4,
            "full_house": 5,
            "small_straight": 5,
            "large_straight": 5,
            "yahtzee": 5,
            "chance": 5,
        }
        self.average_cache = {}
    def roll_dice(self, num_dice=5):
        # Roll the dice
        dice = [random.randint(1, 6) for i in range(num_dice)]
        return dice
    def choose_category(self):
        # Choose a category to score the roll
        available_categories = [cat for cat in self.scorecard if self.scorecard[cat] is None]
        category = random.choice(available_categories)
        return category
    def calculate_score(self, dice:list, category):
        # Calculate the score for a roll in a given category
        if category in self.average_cache:
            average_score = self.average_cache[category]
        else:
            score_sum = 0
            for roll in dice:
                score_sum += self._score_roll(dice, category)
            average_score = score_sum / 6
            self.average_cache[category] = average_score

        score = self._score_roll(dice, category)
        return score
    def _score_roll(self, dice:list, category):
        category_num = None
        last_char:str = category[-1]
        if last_char.isdigit():
            category_num = int(last_char)
            
        if category_num is not None:
            return dice.count(category_num) * category_num
        elif category == "Chance":
            return sum(dice)
        elif category == "Full House":
            if len(set(dice)) == 2 and (dice.count(dice[0]) in [2, 3]):
                return sum(dice)
            else:
                return 0
        elif category == "Yahtzee":
            if len(set(dice)) == 1:
                return 50
            else:
                return 0
        elif category in ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']:
            if category == 'ones':
                return dice.count(1) * 1
            if category == 'twos':
                return dice.count(2) * 2
            if category == 'threes':
                return dice.count(3) * 3
            if category == 'fours':
                return dice.count(4) * 4
            if category == 'fives':
                return dice.count(5) * 5
            if category == 'sixes':
                return dice.count(6) * 6
                
            return dice.count(category[-1]) * category[-1]
        else:
            return 0
    def play_game(self):
        # Play a full game of Yahtzee against the bot
        for i in range(13):
            print(f"Round {i+1}:")
            dice = self.roll_dice()
            print(f"The bot rolled: {dice}")
            category = self.choose_category(dice)
            print(f"The bot chooses category: {category}")
            score = self.calculate_score(dice, category)
            self.scorecard[category] = score
            print(f"The bot scores {score} in {category}\n")
        
        total_score = sum(filter(lambda x: x is not None, self.scorecard.values()))
        print(f"The bot's final score is: {total_score}")
        return total_score
    def get_best_dice_to_keep(self, dice):
        # Determine which dice to keep for the next roll
        possible_scores = {}
        for category in self.scorecard:
            if self.scorecard[category] is None:
                possible_scores[category] = self.calculate_category_average(category)

        best_category = max(possible_scores, key=possible_scores.get)
        num_dice_to_keep = self.CATEGORY_TO_NUM_DICE[best_category]
        dice_to_keep = sorted(dice, reverse=True)[:num_dice_to_keep]

        return dice_to_keep
    def choose_category(self, dice_rolled):
        # Choose which category to score the roll in
        possible_scores = {}
        for category in self.scorecard:
            if self.scorecard[category] is None:
                possible_scores[category] = self.calculate_score(dice_rolled, category)

        if len(possible_scores) == 1:
            return list(possible_scores.keys())[0]
        
        best_category = max(possible_scores, key=possible_scores.get)
        if possible_scores[best_category] == 0:
            return self.calculate_category_average()
        elif possible_scores[best_category] < self.calculate_category_average(best_category):
            return self.calculate_category_average()
        else:
            return best_category
    def calculate_category_average(self):
        # Choose a random category that hasn't been scored yet
        possible_categories = [c for c in self.CATEGORIES if self.scorecard[c] is None]
        return random.choice(possible_categories)
