# import random

# import time
# start = time.time()

# class Card:

#     master = 'Sirt-', 'Xach-', 'Qyap-', 'Xar-'
#     karter = '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
#     mypoints = {'2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

# class Deck(Card):
#     kalod = []

#     def xarnel(self):
#         for i in self.master:
#             for j in self.karter:
#                 self.kalod.append(i + j)
#         random.shuffle(self.kalod)
#         return self.kalod

# class Player(Deck):
#     user_points = 0
#     pc_points = 0
        

#     def __init__(self, name:str):
#         super().xarnel()
#         self.name = name

#     def points(self):
#         p = str(input("enter your name:  ")).capitalize()
#         i1 = 0
#         i2 = 2
#         i3 = 4
#         while True:
#             i1 += 2
#             i2 += 2
#             i3 += 2

#             pc_kart = self.kalod[i1:i2]
#             self.kalod = self.kalod[i2:]
#             l1 = pc_kart
            
#             y = str(pc_kart[0]).split("-"),str(pc_kart[1]).split("-")

#             for k in y[0][1]:
#                 for h in y[1][1]:

#                     for m in Card.mypoints:
#                         if k == m:
#                             Player.pc_points += Card.mypoints[k]
#                     for o in Card.mypoints:
#                         if h == o:
#                             Player.pc_points += Card.mypoints[h]
#                             print(f"Pc === {l1} =  {Player.pc_points}")
#                             user_kart = self.kalod[i2:i3]
#                             self.kalod = self.kalod[i3:]

#                             l2 = user_kart
#                             x = str(user_kart[0]).split("-"),str(user_kart[1]).split("-")

#                             for i in x[0][1]:
#                                 for j in x[1][1]:
                                    
#                                     for m in Card.mypoints: 
#                                         if i == m:
#                                             Player.user_points += Card.mypoints[i]
#                                     for o in Card.mypoints: 
#                                         if j == o:
#                                             Player.user_points += Card.mypoints[j]
#                                             print(f"{p} === {l2} = {Player.user_points}")
#                                             if Player.user_points < 21 and Player.pc_points < 21:
                                
#                                                 x = str(input("enter contiune or not?:  "))
                                            
#                                                 if x == "continue":
#                                                     continue
#                                                 elif x == "not":
#                                                     if Player.user_points > Player.pc_points:
#                                                         return f"{p} === {user_kart} = {Player.user_points}\nPc === {pc_kart} =  {Player.pc_points}\n~~ [winner {p}] ~~"
#                                                     else:
#                                                         return f"{p} === {user_kart} = {Player.user_points}\nPc === {pc_kart} =  {Player.pc_points}\n~~ [winner pc] ~~"
#                                                 else:
#                                                     while x != "continue" or "not":
#                                                         x = str(input("enter contiune or not?:  "))
#                                                         if x == "continue":
#                                                             break
#                                                         elif x == "not":
#                                                             if Player.user_points > Player.pc_points:
#                                                                 return f"{p} === {user_kart} = {Player.user_points}\nPc === {pc_kart} =  {Player.pc_points}\n~~ [winner {p}] ~~"
#                                                             else:
#                                                                 return f"{p} === {user_kart} = {Player.user_points}\nPc === {pc_kart} =  {Player.pc_points}\n~~ [winner pc] ~~"

#                                             elif Player.user_points > 21 and Player.pc_points < 21:
#                                                 return f"~~ [winner {p}] ~~"
#                                             elif Player.user_points < 21 and Player.pc_points > 21:
#                                                 return "~~ [winner pc] ~~"
#                                             elif Player.user_points > 21 and Player.pc_points > 21:
#                                                 if Player.user_points > Player.pc_points:
#                                                     return f"~~ [winner {p}] ~~"
#                                                 elif Player.user_points < Player.pc_points:
#                                                     return "~~ [winner pc] ~~"
#                                                 elif Player.pc_points == Player.pc_points:
#                                                     return "~~ [victory to none] ~~"


# x = Player("user")
# print(x.points())
# finish = time.time()
# print(finish - start)

