import string

from advent import utils

lowercase_priority = {
    letter: idx + 1 for idx, letter in enumerate(string.ascii_lowercase)
}
uppercase_priority = {
    letter: idx + 27 for idx, letter in enumerate(string.ascii_uppercase)
}

priority = lowercase_priority | uppercase_priority


@utils.input_wrapper
def calculate_rucksack_priority(input_data):
    total_priority = 0

    for line in input_data:
        line = line.strip()
        rucksack_length = len(line) // 2

        rucksack_a, rucksack_b = line[:rucksack_length], line[rucksack_length:]

        intersection = list(set(rucksack_a).intersection(set(rucksack_b)))
        total_priority += priority[intersection[0]]

    return total_priority


@utils.input_wrapper
def calculate_rucksack_priority_2(input_data):
    total_priority = 0

    for idx in range(0, len(input_data), 3):
        line = input_data[idx].strip()
        rucksack_a, rucksack_b, rucksack_c = input_data[idx : idx + 3]

        intersection = list(
            set(rucksack_a.strip()) & set(rucksack_b.strip()) & set(rucksack_c.strip())
        )
        total_priority += priority[intersection[0]]

    return total_priority


if __name__ == "__main__":
    print(calculate_rucksack_priority())
    print(calculate_rucksack_priority_2())
