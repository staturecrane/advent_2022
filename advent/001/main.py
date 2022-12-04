from advent import utils


@utils.input_wrapper
def calcualte_elf_calories(input_file):
    input_data = input_file.readlines()

    elf_calories = []

    current_total = 0
    for line in input_data:
        if not line.strip():
            elf_calories.append(current_total)
            current_total = 0
        else:
            current_total += int(line.strip())

    return sorted(elf_calories)


if __name__ == "__main__":
    elf_calories = calcualte_elf_calories()
    print(elf_calories)

    print(elf_calories[-1])
    print(sum(elf_calories[-3 : len(elf_calories)]))
