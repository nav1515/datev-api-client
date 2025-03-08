from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="Client")



@_attrs_define
class Client:
    """ 
        Example:
            [{'client_guid': '54ceb6cf-baff-49b8-bdc3-2a0b56fd5cf3', 'consultant_number': 402248, 'client_number': 12345,
                'name': 'Sample Enterprise 1'}]

        Attributes:
            client_guid (UUID): Unique client id
            consultant_number (int): The consultant id (Beraternummer) Example: 402248.
            client_number (int): The client id (Mandantennummer) Example: 17100.
            name (Union[Unset, str]): Name of the client Example: Sample Enterprise.
     """

    client_guid: UUID
    consultant_number: int
    client_number: int
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        client_guid = str(self.client_guid)

        consultant_number = self.consultant_number

        client_number = self.client_number

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "client_guid": client_guid,
            "consultant_number": consultant_number,
            "client_number": client_number,
        })
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        client_guid = UUID(d.pop("client_guid"))




        consultant_number = d.pop("consultant_number")

        client_number = d.pop("client_number")

        name = d.pop("name", UNSET)

        client = cls(
            client_guid=client_guid,
            consultant_number=consultant_number,
            client_number=client_number,
            name=name,
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
