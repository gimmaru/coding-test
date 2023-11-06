def solution(players, callings):
    position = {
        name: idx for idx, name in enumerate(players)
    }

    for name in callings:
        idx = position[name]
        ahead = players[idx - 1]
        position[ahead], position[name] = idx, idx - 1
        players[idx], players[idx - 1] = ahead, name

    return players