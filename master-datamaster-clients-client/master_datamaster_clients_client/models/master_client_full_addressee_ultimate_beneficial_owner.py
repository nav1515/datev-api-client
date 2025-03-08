from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
from uuid import UUID
import datetime






T = TypeVar("T", bound="MasterClientFullAddresseeUltimateBeneficialOwner")



@_attrs_define
class MasterClientFullAddresseeUltimateBeneficialOwner:
    """ (Angaben zum wirtschaftlich Berechtigten) Ultimate beneficial owner specific data.

        Attributes:
            id (Union[Unset, UUID]): GUID of a relationship - internal identifier.
            display_name (Union[Unset, str]): Comprise a display name of the referenced addressee. Example: Mustermeier,
                Georg.
            natural_person_id (Union[Unset, UUID]): GUID of the referenced natural person addressee. Example:
                4715fa7c-3e81-4255-9a3a-df12c97ad443.
            note (Union[Unset, str]): (Notiz) Field for notes about the ultimate benefical owner.
            valid_from (Union[Unset, datetime.date]): (Gültig von) Indicates the date from which an ultimate benefical owner
                is valid.
            valid_to (Union[Unset, datetime.date]): (Gültig bis) Indicates the date until which an ultimate benefical owner
                is valid.
            currently_valid (Union[Unset, bool]): (Gültig) Indicates whether or not an ultimate benefical owner is currently
                valid. Example: True.
     """

    id: Union[Unset, UUID] = UNSET
    display_name: Union[Unset, str] = UNSET
    natural_person_id: Union[Unset, UUID] = UNSET
    note: Union[Unset, str] = UNSET
    valid_from: Union[Unset, datetime.date] = UNSET
    valid_to: Union[Unset, datetime.date] = UNSET
    currently_valid: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        display_name = self.display_name

        natural_person_id: Union[Unset, str] = UNSET
        if not isinstance(self.natural_person_id, Unset):
            natural_person_id = str(self.natural_person_id)

        note = self.note

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        currently_valid = self.currently_valid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if natural_person_id is not UNSET:
            field_dict["natural_person_id"] = natural_person_id
        if note is not UNSET:
            field_dict["note"] = note
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if valid_to is not UNSET:
            field_dict["valid_to"] = valid_to
        if currently_valid is not UNSET:
            field_dict["currently_valid"] = currently_valid

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

        _natural_person_id = d.pop("natural_person_id", UNSET)
        natural_person_id: Union[Unset, UUID]
        if isinstance(_natural_person_id,  Unset):
            natural_person_id = UNSET
        else:
            natural_person_id = UUID(_natural_person_id)




        note = d.pop("note", UNSET)

        _valid_from = d.pop("valid_from", UNSET)
        valid_from: Union[Unset, datetime.date]
        if isinstance(_valid_from,  Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from).date()




        _valid_to = d.pop("valid_to", UNSET)
        valid_to: Union[Unset, datetime.date]
        if isinstance(_valid_to,  Unset):
            valid_to = UNSET
        else:
            valid_to = isoparse(_valid_to).date()




        currently_valid = d.pop("currently_valid", UNSET)

        master_client_full_addressee_ultimate_beneficial_owner = cls(
            id=id,
            display_name=display_name,
            natural_person_id=natural_person_id,
            note=note,
            valid_from=valid_from,
            valid_to=valid_to,
            currently_valid=currently_valid,
        )


        master_client_full_addressee_ultimate_beneficial_owner.additional_properties = d
        return master_client_full_addressee_ultimate_beneficial_owner

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
