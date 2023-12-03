import linecache
import re

# initialize 9 stacks as empty lists
stacks = [[] for i in range(9)]

column_indices = []
with open("input.txt", "r", encoding="UTF-8") as f:
    input = f.readlines()


# Looks at line 9 and stores index of each "stack" column
def get_stack_indices():
    stack_nums = linecache.getline(r"input.txt", 9)
    for i in range(0, len(stack_nums)):
        if stack_nums[i].isnumeric():
            column_indices.append(i)


# Reach the first 8 lines and get each stack "row"
def get_initial_stacks():
    stack_rows = []
    for i in range(0, 9):
        stack_rows.append(linecache.getline(r"input.txt", i))
    return stack_rows


# use calculated indices to append items on stack per row
def init_stacks():
    get_stack_indices()
    print(column_indices)
    stack_rows = get_initial_stacks()
    for row in stack_rows:
        for i in range(0, len(row)):
            if i in column_indices:
                if row[i].isalpha():
                    index = column_indices.index(i)
                    stacks[index].append(row[i])
            else:
                continue


# parse instruction
def parse_instruction(instruction):
    match = re.search("move (\d+) from (\d+) to (\d+)", instruction)
    print(instruction)
    move_amount = match.group(1)
    source_stack = match.group(2)
    dest_stack = match.group(3)


def main():
    # initializes the "stacks"
    # init_stacks()
    # print(stacks)
    # iterate through instructions
    for i in range(11, 514):
        instruction = linecache.getline(r"input.txt", i).strip()
        parse_instruction(instruction)


if __name__ == "__main__":
    main()
