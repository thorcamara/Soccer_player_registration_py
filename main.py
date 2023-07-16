player = dict()
matches = list()
player['Name'] = str(input('Name of the Player: '))
total = int(input(f'    How many matches {player["Name"]} played? '))
for c in range(0, total):
    matches.append(int(input(f'   How many goals in the match {c}? ')))
player['Goals'] = matches[:]
player['Total'] = sum(matches)
print('-=' * 30)
print(f'\033[1;34m{player}\033[m')
print('-=' * 30)
for k, v in player.items():
    print(f'The field \033[1;33m{k}\033[m has the value \033[1;32m{v}\033[m')
print('-=' * 30)
print(f'The player \033[1;32m{player["Name"]}\033[m played {len(player["Goals"])} matches.')
for i, v in enumerate(player['Goals']):
    print(f'    => In the match \033[1;33m{i}\033[m, made \033[1;32m{v}\033[m goals.')
print(f'Was a total of \033[1;32m{player["Total"]}\033[m goals.')
