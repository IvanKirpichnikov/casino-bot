from abc import ABC, abstractmethod


class AbstractReferrals(ABC):
    @abstractmethod
    async def add(self, tid: int, referral_link: str) -> None:
        """
        Add user's referral link
        
        :param tid: user telegram id
        :param referral_link: referral link
        :return: None
        
        """
    
    @abstractmethod
    async def get_referrals_count(self, tid: int) -> int:
        """
        Get the number of user referrals
        
        :param tid: user telegram id
        :return: int
        
        """
