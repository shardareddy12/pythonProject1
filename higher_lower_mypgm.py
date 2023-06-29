import random
from art import logo
from art import vs
from game_data import data

print(logo)
new_list1 = []
new_list2 = []

should_repeat_game = False
while not should_repeat_game:

    def slect_random(data):
        sel_2dict = random.sample(range(0, len(data)), 2)
        new_list1.append(data[sel_2dict[0]])
        new_list2.append(data[sel_2dict[1]])
        return new_list1, new_list2


    slect_random(data)


    def compare():
        Final_score = 0
        for key1 in new_list1:
            for key2 in new_list2:
                print(key1['name'], ":", key1['follower_count'])
                print(f"Compare A:{key1['name']},a {key1['description']}, from {key1['country']}")
                print(vs)
                print(key2['name'], ":", key2['follower_count'])
                print(f"Compare B:{key2['name']},a {key2['description']}, from {key2['country']}")
                maxfollower = max(key1['follower_count'], key2['follower_count'])
                type_inp = input("who has the more follower? type 'A' or 'B':")
                if type_inp == 'A':
                    if maxfollower == key1['follower_count']:
                        Final_score += 1
                        print(f"You're right! current score:{Final_score}")
                    else:
                        print(f"sorry that's wrong! final score:{Final_score}")
                        should_repeat_game = True
                elif type_inp == 'B':
                    if maxfollower == key2['follower_count']:
                        Final_score += 1
                        print(f"You're right! current score:{Final_score}")
                    else:
                        print(f"sorry that's wrong! final score:{Final_score}")
                        should_repeat_game = True
                else:
                    should_repeat_game = True


    compare()




