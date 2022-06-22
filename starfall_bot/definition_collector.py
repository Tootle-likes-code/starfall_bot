from abc import abstractmethod, ABC


class DefinitionCollector(ABC):
    @abstractmethod
    def get_definition(self, word) -> str:
        pass
