# MAX_RED = 12
# MAX_GREEN = 13
# MAX_BLUE = 14
# total_sum = 0

# with open("input.txt", "r") as f:
#     for line in f:
#         line = line.strip()
#         game_part, sets_part = line.split(":")
#         game_id = int(game_part.split()[1])
#         sets = sets_part.split(";")
#         possible = True
        
#         for set_str in sets:
#             counts = {"red": 0, "green": 0, "blue": 0}
#             cubes = set_str.split(",")
            
#             for cube in cubes:
#                 cube = cube.strip()
#                 number_str, color = cube.split()
#                 number = int(number_str)
#                 counts[color] = number
            
#             if (counts["red"] > MAX_RED or 
#                 counts["green"] > MAX_GREEN or 
#                 counts["blue"] > MAX_BLUE):
#                 possible = False
#                 break

#         if possible:
#             total_sum += game_id

# print(total_sum) #result 2810



total_sum = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        _, sets_part = line.split(":")
        sets = sets_part.split(";")
        max_red = 0
        max_green = 0
        max_blue = 0
        for set_str in sets:
            counts = {"red": 0, "green": 0, "blue": 0}
            cubes = set_str.split(",")
            for cube in cubes:
                cube = cube.strip()
                number_str, color = cube.split()
                number = int(number_str)
                counts[color] = number
            max_red = max(max_red, counts["red"])
            max_green = max(max_green, counts["green"])
            max_blue = max(max_blue, counts["blue"])
        power = max_red * max_green * max_blue
        total_sum += power

print(total_sum) #result 69110