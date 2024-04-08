from unittest import TestCase
from board import create_board


class TestCreateBoard(TestCase):
    def test_create_board(self):
        expected = {(0, 0): 'School', (1, 0): 'School', (2, 0): 'School', (3, 0): 'vertical_wall', (4, 0): 'Town',
                    (5, 0): 'Town', (6, 0): 'Town', (7, 0): 'vertical_wall', (8, 0): 'Forest', (9, 0): 'Forest',
                    (10, 0): 'Forest', (0, 1): 'School', (1, 1): 'School', (2, 1): 'School', (3, 1): 'vertical_wall',
                    (4, 1): 'Town', (5, 1): 'Town', (6, 1): 'Town', (7, 1): 'Door to Forest', (8, 1): 'Forest',
                    (9, 1): 'Forest', (10, 1): 'Forest', (0, 2): 'School', (1, 2): 'School', (2, 2): 'School',
                    (3, 2): 'vertical_wall', (4, 2): 'Town', (5, 2): 'Town', (6, 2): 'Town', (7, 2): 'vertical_wall',
                    (8, 2): 'Forest', (9, 2): 'Forest', (10, 2): 'Forest', (0, 3): 'School', (1, 3): 'School',
                    (2, 3): 'School', (3, 3): 'Door to School', (4, 3): 'Town', (5, 3): 'Town', (6, 3): 'Town',
                    (7, 3): 'vertical_wall', (8, 3): 'Forest', (9, 3): 'Forest', (10, 3): 'Forest', (0, 4): 'School',
                    (1, 4): 'School', (2, 4): 'School', (3, 4): 'vertical_wall', (4, 4): 'Town', (5, 4): 'Town',
                    (6, 4): 'Town', (7, 4): 'vertical_wall', (8, 4): 'Forest', (9, 4): 'Forest', (10, 4): 'Forest',
                    (0, 5): 'horizontal_wall', (1, 5): 'horizontal_wall', (2, 5): 'horizontal_wall',
                    (3, 5): 'horizontal_wall', (4, 5): 'Door to Desert', (5, 5): 'horizontal_wall',
                    (6, 5): 'horizontal_wall', (7, 5): 'Desert', (8, 5): 'Forest', (9, 5): 'Forest',
                    (10, 5): 'Forest', (0, 6): 'Desert', (1, 6): 'Desert', (2, 6): 'Desert', (3, 6): 'Desert',
                    (4, 6): 'Desert', (5, 6): 'Desert', (6, 6): 'Desert', (7, 6): 'Desert', (8, 6): 'Forest',
                    (9, 6): 'Forest', (10, 6): 'Forest', (0, 7): 'Desert', (1, 7): 'Desert', (2, 7): 'Desert',
                    (3, 7): 'Desert', (4, 7): 'Desert', (5, 7): 'Desert', (6, 7): 'Desert', (7, 7): 'Desert',
                    (8, 7): 'Forest', (9, 7): 'Forest', (10, 7): 'Forest', (0, 8): 'Desert', (1, 8): 'Desert',
                    (2, 8): 'Desert', (3, 8): 'Desert', (4, 8): 'Desert', (5, 8): 'Desert', (6, 8): 'Castle',
                    (7, 8): 'Castle', (8, 8): 'Castle', (9, 8): 'Castle', (10, 8): 'Castle', (0, 9): 'Desert',
                    (1, 9): 'Desert', (2, 9): 'Desert', (3, 9): 'Desert', (4, 9): 'Desert', (5, 9): 'Desert',
                    (6, 9): 'Castle', (7, 9): 'Castle', (8, 9): 'Castle', (9, 9): 'Castle', (10, 9): 'Castle',
                    (0, 10): 'Desert', (1, 10): 'Desert', (2, 10): 'Desert', (3, 10): 'Desert', (4, 10): 'Desert',
                    (5, 10): 'Desert', (6, 10): 'Castle', (7, 10): 'Castle', (8, 10): 'Castle', (9, 10): 'Castle',
                    (10, 10): 'Castle'}

        actual = create_board()
        self.assertEqual(expected, actual)
