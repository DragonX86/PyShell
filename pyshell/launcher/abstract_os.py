from abc import ABC, abstractmethod


class AbstractOS(ABC):
    @abstractmethod
    def notepad(self):
        pass

    @abstractmethod
    def calculator(self):
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

    @abstractmethod
    def execute(self):
        pass
