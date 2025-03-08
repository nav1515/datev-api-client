from enum import Enum

class PostV1ClientsClientIdFilesBodyTargetSystem(str, Enum):
    LODAS = "lodas"
    LUG = "lug"

    def __str__(self) -> str:
        return str(self.value)
