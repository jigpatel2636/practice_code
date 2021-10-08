import  math

WORD = 'facebook'
def get_num_stickers(name):
    count = {}
    for c in WORD:
        count[c] = (count[c] + 1) if (c in count) else 1
    # print(count)
    input_count = {}
    for c in name:
        input_count[c] = (input_count[c] + 1) if (c in input_count) else 1
    max_numbers = 0
    # print(input_count)
    for letter in input_count:
        if letter == ' ':
            continue
        num_needed = input_count[letter]
        num_in_sticker = count[letter]
        num_stickers_needed = int(math.ceil(float(num_needed)/float(num_in_sticker)))
        max_numbers = max(num_stickers_needed, max_numbers)

    print(max_numbers)


get_num_stickers('coffee kebab')

