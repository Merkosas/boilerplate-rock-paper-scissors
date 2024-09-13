def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    # Strategy against Quincy
    if len(opponent_history) % 5 == 0:
        return "P"  # Quincy will play "R"
    elif len(opponent_history) % 5 == 1:
        return "P"  # Quincy will play "R"
    elif len(opponent_history) % 5 == 2:
        return "S"  # Quincy will play "P"
    elif len(opponent_history) % 5 == 3:
        return "S"  # Quincy will play "P"
    elif len(opponent_history) % 5 == 4:
        return "R"  # Quincy will play "S"

    # Strategy against Kris
    if prev_play == "R":
        return "P"
    elif prev_play == "P":
        return "S"
    elif prev_play == "S":
        return "R"

    # Strategy against Mrugesh and Abbey
    return "R"  # Play randomly or use a more sophisticated strategy

# Example usage
if __name__ == "__main__":
    from RPS_game import play, quincy, abbey, kris, mrugesh

    play(player, quincy, 1000)
    play(player, abbey, 1000)
    play(player, kris, 1000)
    play(player, mrugesh, 1000)
