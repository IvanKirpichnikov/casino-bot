from abc import ABC
from abc import abstractmethod

from src.application.models import dto


class AbstractUserRepository(ABC):
    @abstractmethod
    async def add(self, model: dto.user.Add) -> None:
        """
        Add user to collections
        
        :param model: dto class
        :return: None
        
        """
    
    @abstractmethod
    async def remove(self, model: dto.user.Delete) -> None:
        """
        Remove a user from a data object
        
        :param model: dto.user.Delete dto class
        :return: None
        
        """
    
    @abstractmethod
    async def get_language(self, model: dto.user.language.Get) -> dto.user.language.Language:
        """
        Get user language code from collections
        
        :param model: dto.user.language.Get dto class
        :return: dto.user.Language dto class
        
        """
    
    @abstractmethod
    async def update_language(self, model: dto.user.language.Update) -> None:
        """
        Update user language in collections
        
        :param model: dto.user.language.Update dto class
        :return: None
        
        """
