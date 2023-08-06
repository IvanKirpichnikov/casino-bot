from dataclasses import dataclass


@dataclass(frozen=True)
class DeepLinkDTO:
    link: str
