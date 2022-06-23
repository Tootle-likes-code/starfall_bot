""" Collects word definitions. """

from abc import abstractmethod, ABC


class DefinitionCollector(ABC):
    """ Collects word definitions. """
    @abstractmethod
    def get_definition(self, word) -> str:
        """
        Gets a definition for a word.
        :param word: The word you wish to get the definition for.
        :return: A string containing the definition for the word.
        """
        pass
