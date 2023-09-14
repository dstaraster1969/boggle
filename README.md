# boggle

Program that implements the game Boggle.

To run:
`python boggle.py`

Boggle rules (adapted from https://en.wikipedia.org/wiki/Boggle):
* Game consists of 16 dice with specific letters on each one randomly distributed across a 4x4 board.
* Words much be at least 3 letters in length.
* Each letter after the first must be a horizontal, vertical, or diagonal neighbor of the one before it.
* No individual die may be used more than once per word.
* Words may not be duplicated.
* In the board game, players have 3 minutes to find words, so the program has to complete in under 3 minutes.

The implementation recursively checks for words with each neighboring die. The naive implementation is not performant.
Performance enhancements include:
* Implementing concurrency. Each new die visited spawns 8 recursive calls, resulting in thousands of calls per run.
Allowing them to run in parallel dramatically improves performance.
* The original implementation compared each candidate word to every word in the dictionary. Sorting the dictionary and
exiting the loop when the candidate can no longer be matched to any words in the dictionary (the dictionary word is
later in the sorted dictionary than the proposed word/prefix, i.e. if the proposed prefix is "an", then when a
dictionary word is larger in sorted order - say "cat" the loop exits.)

With these improvements, the runtime is decreased to well under 3 minutes.