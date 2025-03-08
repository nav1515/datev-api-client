from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="DocumentTypes")



@_attrs_define
class DocumentTypes:
    """ 
        Attributes:
            access_granted (Union[Unset, list[str]]):  Example: ['LOBN', 'LSTB'].
            access_denied (Union[Unset, list[str]]):  Example: ['BUBE', 'KOST'].
     """

    access_granted: Union[Unset, list[str]] = UNSET
    access_denied: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        access_granted: Union[Unset, list[str]] = UNSET
        if not isinstance(self.access_granted, Unset):
            access_granted = self.access_granted



        access_denied: Union[Unset, list[str]] = UNSET
        if not isinstance(self.access_denied, Unset):
            access_denied = self.access_denied




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_granted is not UNSET:
            field_dict["access_granted"] = access_granted
        if access_denied is not UNSET:
            field_dict["access_denied"] = access_denied

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        access_granted = cast(list[str], d.pop("access_granted", UNSET))


        access_denied = cast(list[str], d.pop("access_denied", UNSET))


        document_types = cls(
            access_granted=access_granted,
            access_denied=access_denied,
        )


        document_types.additional_properties = d
        return document_types

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
