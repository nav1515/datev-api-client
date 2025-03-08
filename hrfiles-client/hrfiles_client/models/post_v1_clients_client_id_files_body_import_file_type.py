from enum import Enum

class PostV1ClientsClientIdFilesBodyImportFileType(str, Enum):
    BWD = "bwd"
    PSD = "psd"

    def __str__(self) -> str:
        return str(self.value)
