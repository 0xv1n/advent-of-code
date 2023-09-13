-- Load the file
local file = io.open("puzzleinput.txt", "r")
if not file then
    error("Failed to open file")
end

-- Read the file line by line
local input = {}
local cals = 0
for line in file:lines() do
    if line ~= "" then
        cals = cals + tonumber(line)
    else
        table.insert(input, cals)
        cals = 0
    end
end
file:close()

-- Calculate and print the highest calorie count
local maxCalories = math.max(table.unpack(input, 1, #input))
print(maxCalories)

-- Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
table.sort(input, function(a, b) return a > b end)
local topThreeCalories = 0
for i = 1, 3 do
    topThreeCalories = topThreeCalories + (input[i] or 0)
end
print(topThreeCalories)
