from abc import ABC
from abc import abstractmethod

from src.application.models import dto


class AbstractUserDAO(ABC):
    @abstractmethod
    async def add(self, model: dto.user.Add) -> None:
        """
        Add user to data object
        
        :param model: src.application.dto.user.Add dto class
        :return: None
        
        """
    
    @abstractmethod
    async def remove(self, model: dto.user.Delete) -> None:
        """
        Remove a user from a data object
        
        :param model: src.application.dto.user.Delete dto class
        :return: None
        
        """
    
    @abstractmethod
    async def get_language(self, model: dto.user.GetLanguage) -> dto.user.Language:
        """
        Get user language code from data object
        
        :param model: src.application.dto.user.GetLanguage dto class
        :return: src.application.dto.user.Language dto class
        
        """
    
    @abstractmethod
    async def update_language(self, model: dto.user.UpdateLanguage) -> None:
        """
        Update user language in data object
        
        :param model: src.application.dto.user.UpdateLanguage dto class
        :return: None
        
        """
