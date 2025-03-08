from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.client import Client





T = TypeVar("T", bound="ClientsResponse")



@_attrs_define
class ClientsResponse:
    """ All available clients

        Attributes:
            clients (list['Client']):
     """

    clients: list['Client']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.client import Client
        clients = []
        for clients_item_data in self.clients:
            clients_item = clients_item_data.to_dict()
            clients.append(clients_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "clients": clients,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.client import Client
        d = src_dict.copy()
        clients = []
        _clients = d.pop("clients")
        for clients_item_data in (_clients):
            clients_item = Client.from_dict(clients_item_data)



            clients.append(clients_item)


        clients_response = cls(
            clients=clients,
        )


        clients_response.additional_properties = d
        return clients_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
