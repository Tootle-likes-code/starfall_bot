""" Loads definition files into memory for access to words. """

import json
import os
from pathlib import Path

from starfall_bot.definition_collector import DefinitionCollector


class DefinitionFileCollector(DefinitionCollector):
    """ Loads JSON files into memory for access to definitions. """
    def __init__(self, file):
        self._definitions = {}
        self._file = Path(os.getcwd() + rf"\{file}")
        self._validate()
        self._load_file()

    def _validate(self):
        if not self._file.exists():
            raise ValueError("File must exist.")
        if not self._file.is_file():
            raise ValueError("File needs to be a valid file.")

    def _load_file(self):
        with open(self._file, "r", encoding="utf-8") as file:
            self._definitions = json.load(file)

    def get_file_path(self) -> str:
        """ Gets the full file path for the definitions. """
        return str(self._file.absolute())

    def get_definition(self, word) -> str:
        return self._definitions[word]
