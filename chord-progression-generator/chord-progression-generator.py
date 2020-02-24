from random import random

class ChordState:
    def __init__(self, name, transition_matrix):
        self.name = name
        self.transition_matrix = transition_matrix

    def matrix_is_valid(self):
        sum = 0
        for chance in self.transition_matrix:
            sum += chance
        if round(sum, 2) == 1:
            return True
        else:
            print(sum)
            return False


i_chord = ChordState("I", [0, 0.05, 0.05, 0.05, 0.10, 0.05, 0.15, 0.2, 0.05, 0.10, 0.10, 0.10])
bii_chord = ChordState("bII", [0.10, 0, 0.10, 0.05, 0.15, 0.15, 0.05, 0.10, 0.05, 0.10, 0.10, 0.05])
ii_chord = ChordState("II", [0.10, 0.10, 0, 0.10, 0.15, 0.15, 0.05, 0.10, 0.05, 0.05, 0.10, 0.05])
biii_chord = ChordState("bIII", [0.10, 0.05, 0.10, 0, 0.15, 0.10, 0.05, 0.10, 0.10, 0.10, 0.10, 0.05])
iii_chord = ChordState("III", [0.10, 0.05, 0.10, 0.15, 0, 0.15, 0.10, 0.15, 0.05, 0.05, 0.05, 0.05])
iv_chord = ChordState("IV", [0.10, 0.05, 0.05, 0.05, 0.15, 0, 0.10, 0.15, 0.05, 0.10, 0.15, 0.05])
bv_chord = ChordState("bV", [0.10, 0.10, 0.10, 0.05, 0.05, 0.15, 0, 0.10, 0.10, 0.10, 0.10, 0.05])
v_chord = ChordState("V", [0.10, 0.05, 0.10, 0.05, 0.10, 0.15, 0.05, 0, 0.10, 0.10, 0.15, 0.05])
bvi_chord = ChordState("bVI", [0.10, 0.10, 0.05, 0.05, 0.15, 0.10, 0.05, 0.10, 0.05, 0.10, 0.10, 0.05])
vi_chord = ChordState("VI", [0.10, 0.10, 0.05, 0.05, 0.15, 0.15, 0.05, 0.10, 0.10, 0, 0.10, 0.05])
bvii_chord = ChordState("bVII", [0.10, 0.10, 0.05, 0.05, 0.15, 0.15, 0.05, 0.10, 0.05, 0.10, 0, 0.10])
vii_chord = ChordState("VII", [0.10, 0.10, 0.05, 0.05, 0.15, 0.15, 0.05, 0.10, 0.05, 0.10, 0.10, 0])

chord_states = [i_chord, bii_chord, ii_chord, biii_chord, iii_chord, iv_chord, bv_chord, v_chord, bvi_chord, vi_chord,
                bvii_chord, vii_chord]

current_chord_state = i_chord
number_of_chords_in_progression = 8


def get_new_chord_state(chord_state):
    minimum_target_value = 0.0
    maximum_target_value = 0.0

    random_value = random()

    if chord_state.matrix_is_valid():
        for i in range(len(chord_state.transition_matrix)):
            minimum_target_value = maximum_target_value
            maximum_target_value = minimum_target_value + chord_state.transition_matrix[i]
            if round(minimum_target_value, 2) <= random_value <= round(maximum_target_value, 2):
                return chord_states[i]
    else:
        raise Exception("Matrix invalid!")


for i in range(number_of_chords_in_progression):
    print(current_chord_state.name, end=" ")
    current_chord_state = get_new_chord_state(current_chord_state)