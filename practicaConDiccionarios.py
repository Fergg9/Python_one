'''Players = ["Embid", 'Doncic', 'Tatum', 'Giannis']
PPG = [33.6, 33.6, 31.0, 30.9, 30.7]

print(list(zip(Players, PPG)))

lol = {Players: PPG for (Players, PPG) in zip(Players, PPG)}
print(lol)

new_dict = {Players[i]:PPG[i] for i in range(len(Players))}
print(new_dict)
'''
