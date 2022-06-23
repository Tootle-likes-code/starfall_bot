""" Contains methods for assisting teh Info Cog. """

from starfall_bot.definition_collector import DefinitionCollector


class InfoService:
    """ A class for dealing Info Cog requests """
    def __init__(self, definition_collector: DefinitionCollector):
        self._definition_collector = definition_collector

    def define(self, word: str):
        """
        Gets the definition for a given word.
        :param word: The word to get a definition for.
        :return: The definition of the word.
        """
        definition = self._definition_collector.get_definition(word)

        if definition:
            return definition

        return f"I'm sorry, but I don't know the word '{word}' either."
