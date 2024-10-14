from abc import ABC, abstractmethod

class IClient(ABC):
    @abstractmethod
    def get_data(self, user_id: str):
        pass