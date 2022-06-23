import unittest

from starfall_bot.definition_sheets_collector import DefinitionSheetsCollector


class DefinitionSheetsCollectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_sheets_collector = DefinitionSheetsCollector('1fys6qXWVRWVXLECZBRRycffQo9VW3X6WnLUxNSV5jmE')


class GetDefinitionTests(DefinitionSheetsCollectorTests):
    def test_google_api_when_working(self):
        # Arrange
        expected_result = '"Non Player Character". A fictional character created by the roleplayer, ' \
                          'administrators, or other roleplayers. Non-player characters are, as their name ' \
                          'suggests, not actively played by any one roleplayer.'

        # Act
        result = self.test_sheets_collector.get_definition("NPC")

        # Assert
        self.assertEqual(expected_result, result)

    def test_given_unknown_word_returns_none(self):
        # Act
        result = self.test_sheets_collector.get_definition("Unknown")

        # Assert
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
