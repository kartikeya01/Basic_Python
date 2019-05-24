import math

class Frequency (object):
    def __init__(self, filename='Words.txt'):
        self.total_count = 0  # Total count of chars
        self.freq_dict = {}  # Frequencies of letters
        self.prob_dict = {}  # Probabilities of letters
        self.angle_dict = {}  # Angles of letters

        #Upper and lowercase are counted as the same letter
        with open(filename, 'r') as f:
            for line in f:
                for char in line:
                    if((ord(char.lower()) >= 97 and ord(char.lower()) <= 122)):
                        self.freq_dict[char] = self.freq_dict.get(char, 0) + 1
                    self.total_count = self.total_count + 1


        # Calculate the probabilities and angles of letters
        for char in self.freq_dict:
            self.prob_dict[char] = self.freq_dict[char] / self.total_count
            self.angle_dict[char] = self.prob_dict[char] * math.pi * 2


