from typing import Callable
from dataclasses import dataclass


@dataclass
class Route:
    """
        ### Route
        Dataclasse representatif d'un objet route.
        Il nous permettra d'écrire les routes de 
        façon déclarative
    """
    path: str
    view: Callable
    layout: str = "main"
    requires_auth: bool = False
