import os

with open(os.path.dirname(__file__) + "/input.txt") as f:
    input = f.readlines()
    f.close()
# Translate letters to priorities
# a-z = 1-26
letter_to_priority = {
    letter: ord(letter.lower()) - ord("a") + 1
    for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
}
# A-Z = 27-52
letter_to_priority.update(
    {letter: ord(letter) - ord("A") + 27 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
)


# This resolves the letter to the priority based on the dict defined in letter_to_priority
def get_priority(letter):
    return letter_to_priority[letter]


# This divides a rucksack into a list of 2 equal parts and returns
# the list
def divide_rucksack(rucksack):
    divided_sack = []
    midpoint = len(rucksack) // 2
    divided_sack.insert(0, rucksack[:midpoint])
    divided_sack.insert(1, rucksack[midpoint:])
    return divided_sack


# iterates through the first compartment and if it finds a match
# returns the priority of that item
def get_duplicate_item(divided_sack):
    for item in divided_sack[0]:
        if item in divided_sack[1]:
            return get_priority(item)


# this takes in a list of rucksacks and returns the priority
# of the first item shared between all 3
def find_badge(rucksacks):
    # we can built a character set from the first rucksack's items
    # but strip the newline and whitespace
    items = set(rucksacks[0].strip())

    for item in items:
        if all(item in sack for sack in rucksacks):
            return item


def main():
    # Part 1
    print("[+] Part 1")
    priority_sum = 0
    for sack in input:
        divided_sack = divide_rucksack(sack)
        priority_sum += get_duplicate_item(divided_sack=divided_sack)
    print(f"Sum of all priority items: {priority_sum}")

    # Part 2
    print("[+] Part 2")
    priority_sum = 0
    for i in range(0, len(input), 3):
        rucksacks = input[i : i + 3]
        badge = find_badge(rucksacks=rucksacks)
        priority_sum += get_priority(badge)
    print(f"Sum of all badges: {priority_sum}")


if __name__ == "__main__":
    main()
