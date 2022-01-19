# format for dictionary works as the following: word: (chaotic-lawful) (evil-good)

import json

with open('allignDict.json', 'r') as f:
    align = json.load(f)


def calculate_alignment(messages):
    total_C_L = 0
    total_E_G = 0
    message_string = ' '.join(messages).lower()
    total_words_added = 0

    for msg_word in message_string.split(" "):
        for align_word in align:
            if align_word in msg_word:
                total_C_L += align[align_word][0]
                total_E_G += align[align_word][1]
                total_words_added += 1

    if not total_words_added == 0:
        total_C_L /= total_words_added
        total_E_G /= total_words_added

    print(total_C_L)
    print(total_E_G)

    alignment_values = [0, 0]
    if total_C_L < -5:
        alignment_values[0] = -1
    elif -5 <= total_C_L <= 5:
        alignment_values[0] = 0
    elif 5 < total_C_L:
        alignment_values[0] = 1
    if total_E_G < -5:
        alignment_values[1] = -1
    elif -5 <= total_E_G <= 5:
        alignment_values[1] = 0
    elif 5 < total_E_G:
        alignment_values[1] = 1

    alignment = alignment_values

    if alignment == [1, 1]:
        alignment_text = "lawful good"
    elif alignment == [1, 0]:
        alignment_text = "lawful neutral"
    elif alignment == [1, -1]:
        alignment_text = "lawful evil"
    elif alignment == [0, 1]:
        alignment_text = "neutral good"
    elif alignment == [0, 0]:
        alignment_text = "true neutral"
    elif alignment == [0, -1]:
        alignment_text = "neutral evil"
    elif alignment == [-1, 1]:
        alignment_text = "chaotic good"
    elif alignment == [-1, 0]:
        alignment_text = "chaotic neutral"
    elif alignment == [-1, -1]:
        alignment_text = "chaotic evil"
    else:
        alignment_text = "true neutral"

    return alignment_text


if __name__ == "__main__":
    calculate_alignment(["superhappy", "poggers"])
