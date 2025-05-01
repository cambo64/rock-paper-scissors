import unittest
from main import determine_winner, get_computer_move, VALID_MOVES

class TestRockPaperScissors(unittest.TestCase):
    def test_determine_winner_tie(self):
        self.assertEqual(determine_winner("R", "R"), "tie")
        self.assertEqual(determine_winner("P", "P"), "tie")
        self.assertEqual(determine_winner("S", "S"), "tie")

    def test_determine_winner_player_wins(self):
        self.assertEqual(determine_winner("R", "S"), "player")
        self.assertEqual(determine_winner("P", "R"), "player")
        self.assertEqual(determine_winner("S", "P"), "player")

    def test_determine_winner_computer_wins(self):
        self.assertEqual(determine_winner("S", "R"), "computer")
        self.assertEqual(determine_winner("R", "P"), "computer")
        self.assertEqual(determine_winner("P", "S"), "computer")

    def test_get_computer_move_returns_valid(self):
        for _ in range(100):
            move = get_computer_move()
            self.assertIn(move, VALID_MOVES)

if __name__ == "__main__":
    unittest.main()
