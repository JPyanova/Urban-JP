def all_variants(text):
    for letter in range(len(text)):
        for next_letter in range(len(text) - letter):
            yield text[letter:next_letter + letter + 1]

get_all_variants = all_variants('ABC')
for variant in get_all_variants:
    print(variant)

