# problem statement: In how many assignment pairs does one range fully contain the other?
with open("input.txt", "r") as f:
    input = f.readlines()
    f.close()


def get_bounds(elf):
    return int(elf[0].strip()), int(elf[1].strip())


def is_fully_contained(elf1, elf2):
    elf1_lowerbound, elf1_upperbound = get_bounds(elf1)
    elf2_lowerbound, elf2_upperbound = get_bounds(elf2)
    if elf1_lowerbound <= elf2_lowerbound and elf1_upperbound >= elf2_upperbound:
        return True
    elif elf2_lowerbound <= elf1_lowerbound and elf2_upperbound >= elf1_upperbound:
        return True
    else:
        return False


def create_series(lowerbound, upperbound):
    x = []
    for i in range(lowerbound, upperbound + 1):
        x.append(i)
    return x


def overlaps(elf1, elf2):
    elf1_lowerbound, elf1_upperbound = get_bounds(elf1)
    elf2_lowerbound, elf2_upperbound = get_bounds(elf2)
    elf1_series = create_series(elf1_lowerbound, elf1_upperbound)
    elf2_series = create_series(elf2_lowerbound, elf2_upperbound)
    for num in elf1_series:
        if num in elf2_series:
            return True
        else:
            continue


def main():
    fully_contained_count = 0
    overlap_count = 0
    for pair in input:
        pair_split = pair.split(",")
        elf1_range = pair_split[0].split("-")
        elf2_range = pair_split[1].split("-")
        # part 1
        if is_fully_contained(elf1_range, elf2_range):
            fully_contained_count += 1
        # part 2
        if overlaps(elf1_range, elf2_range):
            overlap_count += 1
    print("-- Part 1")
    print(fully_contained_count)
    print("-- Part 2")
    print(overlap_count)


if __name__ == "__main__":
    main()
