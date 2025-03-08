from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="MasterClientFullAddresseeProprietor")



@_attrs_define
class MasterClientFullAddresseeProprietor:
    """ (Angaben zum Betriebsinhaber) Proprietor specific data.

        Attributes:
            id (Union[Unset, UUID]): GUID of a relationship - internal identifier.
            display_name (Union[Unset, str]): Comprise a display name of the referenced addressee. Example: Mustermeier,
                Georg.
            addressee_id (Union[Unset, UUID]): GUID of the referenced addressee.
     """

    id: Union[Unset, UUID] = UNSET
    display_name: Union[Unset, str] = UNSET
    addressee_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        display_name = self.display_name

        addressee_id: Union[Unset, str] = UNSET
        if not isinstance(self.addressee_id, Unset):
            addressee_id = str(self.addressee_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if addressee_id is not UNSET:
            field_dict["addressee_id"] = addressee_id

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




        display_name = d.pop("display_name", UNSET)

        _addressee_id = d.pop("addressee_id", UNSET)
        addressee_id: Union[Unset, UUID]
        if isinstance(_addressee_id,  Unset):
            addressee_id = UNSET
        else:
            addressee_id = UUID(_addressee_id)




        master_client_full_addressee_proprietor = cls(
            id=id,
            display_name=display_name,
            addressee_id=addressee_id,
        )


        master_client_full_addressee_proprietor.additional_properties = d
        return master_client_full_addressee_proprietor

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
