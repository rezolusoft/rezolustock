from dataclasses import dataclass
from importlib import import_module


@dataclass
class Route:
    """
        ### Route
        Structure representative d'une route déclarative.

        Attributes:
            path (str) : chemin de la route
            module (str) : chemin vers le fichier contenant la vue à partir du répertoire `/src`
            view (str) : nom de la fonction de la vue
            layout (str) : type d'échaffaudage correspondant a la route
            requires_auth (bool) : spécifie si l'accès à cette route nécéssite un utilisateur authentifié
    """
    path: str
    module: str
    view: str
    layout: str = "main"
    requires_auth: bool = False
    requires_root: bool = False
    _view = None


    def get_view(self):
        """
        Permet de charger le module de la vue correspondante a la route

        Returns:
        flet.Control : La vue a charger
        """
        if self._view is None:
            module = import_module(self.module)
            self._view = getattr(module, self.view)
        
        return self._view
