from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Client")



@_attrs_define
class Client:
    """ 
        Attributes:
            client_id (Union[Unset, str]):  Example: 123456-123.
            consultant_number (Union[Unset, int]):  Example: 123456.
            client_number (Union[Unset, int]):  Example: 123.
     """

    client_id: Union[Unset, str] = UNSET
    consultant_number: Union[Unset, int] = UNSET
    client_number: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        consultant_number = self.consultant_number

        client_number = self.client_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if consultant_number is not UNSET:
            field_dict["consultant_number"] = consultant_number
        if client_number is not UNSET:
            field_dict["client_number"] = client_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("client_id", UNSET)

        consultant_number = d.pop("consultant_number", UNSET)

        client_number = d.pop("client_number", UNSET)

        client = cls(
            client_id=client_id,
            consultant_number=consultant_number,
            client_number=client_number,
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
