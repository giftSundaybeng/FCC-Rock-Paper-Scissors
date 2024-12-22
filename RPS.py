from collections import Counter

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # Predict the opponent's next move based on the most common patterns
    n = 3  # Length of pattern to match
    if len(opponent_history) >= n:
        recent = ''.join(opponent_history[-n:])
        patterns = [''.join(opponent_history[i:i + n]) for i in range(len(opponent_history) - n)]
        next_moves = [opponent_history[i + n] for i in range(len(patterns)) if patterns[i] == recent]
        if next_moves:
            prediction = Counter(next_moves).most_common(1)[0][0]
            counter = {"R": "P", "P": "S", "S": "R"}
            return counter[prediction]

    # Default move
    return "R"
