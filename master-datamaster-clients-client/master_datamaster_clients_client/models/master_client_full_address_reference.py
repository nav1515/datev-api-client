from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="MasterClientFullAddressReference")



@_attrs_define
class MasterClientFullAddressReference:
    """ (Adresse) Address specific data.

        Attributes:
            id (Union[Unset, UUID]): GUID of a reference - internal identifier. Example: 80f27603-0c9c-4dfd-
                bf98-6a9bff21c5e0.
            address_manually_edited (Union[Unset, str]): (Manuell geänderte Addresse) Indicates a manually edited address.
     """

    id: Union[Unset, UUID] = UNSET
    address_manually_edited: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        address_manually_edited = self.address_manually_edited


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if address_manually_edited is not UNSET:
            field_dict["address_manually_edited"] = address_manually_edited

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        address_manually_edited = d.pop("address_manually_edited", UNSET)

        master_client_full_address_reference = cls(
            id=id,
            address_manually_edited=address_manually_edited,
        )


        master_client_full_address_reference.additional_properties = d
        return master_client_full_address_reference

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
