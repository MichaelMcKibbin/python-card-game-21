# Card Game 21

A simple command-line card game where you try to beat the house by drawing three random cards from a standard deck.

## How to play

- The values of your three cards are added together.
- You win the round if your total is 21 or less; otherwise, the house wins.
- Aces are worth 1, number cards are worth their number, and Jack, Queen, and King are worth 11, 12, and 13
  respectively.
- The game keeps track of player and house wins.
- If you play long enough to reach 21 wins or losses the game ends.
- You can change the number of wins or losses required to end the game by editing ```match_win_limit``` on line 12 of
  ```play.py```

Cards are displayed using text, numbers, and Unicode playing-card symbols.

Run the game with:

```
python play.py
```