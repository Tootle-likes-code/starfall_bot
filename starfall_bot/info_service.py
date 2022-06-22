from starfall_bot.definition_collector import DefinitionCollector


class InfoService:
    def __init__(self, definition_collector: DefinitionCollector):
        self._definition_collector = definition_collector

    def define(self, word: str):
        definition = self._definition_collector.get_definition(word)
        return f"{word}: {definition}"
