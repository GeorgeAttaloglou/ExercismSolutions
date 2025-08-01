class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        
        if len(self.card_num.strip()) == 1:
            return False

        if not self.card_num.replace(" ", "").isdigit():
            return False

        card_num_list = [int(digit) for digit in self.card_num.strip().replace(" ", "")]

        for i in range(len(card_num_list)-2, -1, -2):
            card_num_list[i] *= 2
            if card_num_list[i] > 9:
                card_num_list[i] -= 9

        return sum(card_num_list) % 10 == 0
