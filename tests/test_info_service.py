import unittest
from unittest.mock import MagicMock

from starfall_bot.definition_collector import DefinitionCollector
from starfall_bot.info_service import InfoService


class InfoServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_definition_collector = MagicMock(spec=DefinitionCollector)
        self.test_info_service = InfoService(self.mock_definition_collector)


class DefineTests(InfoServiceTests):
    def test_ensuring_that_valid_definition_is_passed_on(self):
        # Arrange
        expected_result = "The Definition."
        self.mock_definition_collector.get_definition.return_value = "The Definition."

        # Act
        result = self.test_info_service.define("test")

        # Assert
        self.assertEqual(expected_result, result)

    def test_unknown_word_returns_unknown_message(self):
        # Arrange
        expected_result = "I'm sorry, but I don't know the word 'test' either."
        self.mock_definition_collector.get_definition.return_value = None

        # Act
        result = self.test_info_service.define("test")

        # Assert
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
