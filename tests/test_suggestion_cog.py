import unittest

from starfall_bot.suggestion_cog import SuggestionCog


class SuggestionCogTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_suggestion_cog = SuggestionCog()
        

class SuggestionTests(SuggestionCogTests):
    def test_suggestion_makes_new_thread(self):
        # Arrange
        
        
        # Act
        
        
        # Assert
        self.assert_fail("Not Implemented")


if __name__ == '__main__':
    unittest.main()
