from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.service import Service





T = TypeVar("T", bound="Client")



@_attrs_define
class Client:
    """ 
        Attributes:
            client_number (Union[Unset, int]): Client number Example: 55003.
            consultant_number (Union[Unset, int]): Consultant number Example: 29098.
            id (Union[Unset, str]): Client ID (technical) Example: 29098-55003.
            name (Union[Unset, str]): Client name Example: Muster GmbH.
            services (Union[Unset, list['Service']]):
     """

    client_number: Union[Unset, int] = UNSET
    consultant_number: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    services: Union[Unset, list['Service']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.service import Service
        client_number = self.client_number

        consultant_number = self.consultant_number

        id = self.id

        name = self.name

        services: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if client_number is not UNSET:
            field_dict["client_number"] = client_number
        if consultant_number is not UNSET:
            field_dict["consultant_number"] = consultant_number
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.service import Service
        d = src_dict.copy()
        client_number = d.pop("client_number", UNSET)

        consultant_number = d.pop("consultant_number", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in (_services or []):
            services_item = Service.from_dict(services_item_data)



            services.append(services_item)


        client = cls(
            client_number=client_number,
            consultant_number=consultant_number,
            id=id,
            name=name,
            services=services,
        )


        client.additional_properties = d
        return client

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
