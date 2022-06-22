import os
import unittest
from pathlib import Path
from unittest.mock import patch

from starfall_bot.definition_file_collector import DefinitionFileCollector

test_file_path: Path


def setUpModule():
    _initialise_test_file()


def _initialise_test_file():
    dir_path = os.path.dirname(os.getcwd() + r"\tests")
    global test_file_path
    test_file_path = os.path.join(dir_path, "test.json")
    with open(test_file_path, "w", encoding="utf-8") as file:
        file.write('{"test":"This is a test"}')


def tearDownModule() -> None:
    os.remove(test_file_path)


class DefinitionFileCollectorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_file_collector: DefinitionFileCollector = DefinitionFileCollector("test.json")


@patch("starfall_bot.definition_file_collector.Path.is_file", return_value=True)
@patch("starfall_bot.definition_file_collector.Path.exists", return_value=True)
class GetFilePath(DefinitionFileCollectorTests):
    def test_get_file_returns_file_path_text(self, _, __):
        # Arrange
        expected_result = os.getcwd() + r"\test.json"

        # Act
        result = self.test_file_collector.get_file_path()

        # Assert
        self.assertEqual(expected_result, result)


class GetDefinitionTests(DefinitionFileCollectorTests):
    def test_get_definition_with_valid_value_returns_value(self):
        # Arrange
        expected_result = "This is a test"

        # Act
        result = self.test_file_collector.get_definition("test")

        # Assert
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
