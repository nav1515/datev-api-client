
""" A client library for accessing DATEV Datenservice Dokumente Personalwirtschaft - REST-API """
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
