from dataclasses import dataclass


@dataclass(frozen=True)
class Permission():

    ressource : str
    action : str

    @property
    def code(self):
        return f"{self.action}_{self.ressource}"
    