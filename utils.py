import random

def generate_bones():
    temp = []
    for i in range(0, 7):
        for j in range(i, 7):
            temp.append((i, j))
    return temp

# Take first pair for (1, 1) and higher or (0, 0) or bone with smallest sum
# Player: sorted list of pair
def get_first_bone(player):
    for bone in player:
        # Return exist pair unless (0, 0)
        if (bone[0] == bone[1]) and bone[0] != 0:
            return bone
    boneMin = (7, 7)
    for bone in player:
        if bone[0] + bone[1] < boneMin[0] + boneMin[1] and bone[0] != bone[1]:
            boneMin=bone
    return boneMin

def generate_array(new, heap):
    i = 0
    while i < 7:
        index = random.randint(0, len(heap) - 1)
        new.insert(0, heap.pop(index))
        i += 1
    return [
        new,
        heap
    ]

def get_initial_bones(free_bones):
    player_bones, free_bones = generate_array([], free_bones)
    player_bones = sorted(player_bones, key=lambda bone: bone[0])
    print (f"You have bones: {player_bones}")
    # Update heap of freeBones after getting 7 random from it
    bot_bones, free_bones = generate_array([], free_bones)
    bot_bones = sorted(bot_bones, key=lambda bone: bone[0])
    print (f"Bot has bones: {bot_bones}")
    print (f"Heap is: {free_bones}")
    # .sort(key=lambda x: x[0])
    return [
        player_bones,
        bot_bones,
        free_bones
    ]

def set_current_player(p, b):
    if (p[0] == p[1]):
        if (b[0] == b[1]):
            # condition_if_true if condition else condition_if_false
            return 0 if p[0] + p[1] < b[0] + b[1] else 1
        else:
            return 0
    else:
        if (b[0] == b[1]):
            return 1
        else:
            return 0 if p[0] + p[1] < b[0] + b[1] else 1

def get_correct_bones(bones, tails):
    while 1:
        print("Here is your bones \n "
            f"select one by index: {bones}")
        index = int(input('Enter index of element: ')) % len(bones)
        if check_bones([bones[index]], tails):
            return bones[index]

# Check presence correct bone in hand
def check_bones(bones, tails):
    for bone in bones:
        if bone[0] == tails[0] or bone[0] == tails[1] or bone[1] == tails[0] or bone[1] == tails[1]:
            return 1

def get_possible_bones(selected_item, other_bone):
    left_side, right_side = selected_item
    final_res = []
    res1 = [item for item in other_bone if left_side in item]
    if left_side == right_side:
        final_res = res1
        return final_res
    else:
        res2 = [item for item in other_bone if right_side in item]
        final_res = res1 + res2
        return final_res

def check_fish(tails, table):
    begin = 0
    end = 0
    for bone in table:
        if bone[0] == tails[0] or bone[1] == tails[0]:
            begin += 1
        if bone[0] == tails[1] or bone[1] == tails[1]:
            end += 1
    if begin == 7 and end == 7:
        return 1

def count_point(player, bot):
    pp = 0;
    pb = 0;
    for bone in player:
        pp += bone[0] + bone[1]
    for bone in bot:
        pb += bone[0] + bone[1]
    print("Bot wins ") if pp > pb else print("Player wins")