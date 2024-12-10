def selection_sort(players):
    n = len(players)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if players[j][1] < players[min_index][1]:
                min_index = j
        players[i], players[min_index] = players[min_index], players[i]
    return players

players_data = [
    ("Alice", 50),
    ("Bob", 20),
    ("Carlos", 70),
    ("Diana", 40)
]

sorted_players = selection_sort(players_data)
print(sorted_players)
