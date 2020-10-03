from abc import ABC, abstractmethod


class AbstractOS(ABC):
    @abstractmethod
    def note(self):
        pass

    @abstractmethod
    def calc(self):
        pass

    @abstractmethod
    def browser(self):
        pass

    @abstractmethod
    def filemanager(self):
        pass

    @abstractmethod
    def sysmonitor(self):
        pass
