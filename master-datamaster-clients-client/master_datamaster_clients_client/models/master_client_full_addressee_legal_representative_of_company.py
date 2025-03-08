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






T = TypeVar("T", bound="MasterClientFullAddresseeLegalRepresentativeOfCompany")



@_attrs_define
class MasterClientFullAddresseeLegalRepresentativeOfCompany:
    """ (Angaben zum gesetzliche Vertreter des Unternehmens) Legal representative specific data.

        Attributes:
            id (Union[Unset, UUID]): GUID of a relationship - internal identifier.
            display_name (Union[Unset, str]): Comprise a display name of the referenced addressee. Example: Mustermeier,
                Georg.
            addressee_id (Union[Unset, UUID]): GUID of the referenced addressee.
            date_of_waiver (Union[Unset, datetime.date]): (Eintragung der Befreiung ins Handelsregister) Date of waiver from
                paragraph 181 BGB.
            display_in_tax_form (Union[Unset, bool]): (Anzeige im Steuerformular) Indicates wether or not to display in tax
                form. Example: True.
            is_authorized_officer (Union[Unset, bool]): (Prokurist) Indicates wether the referenced addressee is an
                authorized officer. Example: True.
            note (Union[Unset, str]): (Notiz) Field for notes about the legal representative.
            type_of_representation (Union[Unset, str]): (Vertretungsart) Indicates the type of representation.
            valid_from (Union[Unset, datetime.date]): (Gültig von) Indicates the date from which a legal representative is
                valid.
            valid_to (Union[Unset, datetime.date]): (Gültig bis) Indicates the date until which a legal representative is
                valid.
            currently_valid (Union[Unset, bool]): (Gültig) Indicates whether or not the legal representative is currently
                valid. Example: True.
            waiver_of_para181bgb (Union[Unset, bool]): (Befreiung nach §181 BGB) Indicates wether or not the legal
                representative is waived from paragraph 181 BGB. Example: True.
     """

    id: Union[Unset, UUID] = UNSET
    display_name: Union[Unset, str] = UNSET
    addressee_id: Union[Unset, UUID] = UNSET
    date_of_waiver: Union[Unset, datetime.date] = UNSET
    display_in_tax_form: Union[Unset, bool] = UNSET
    is_authorized_officer: Union[Unset, bool] = UNSET
    note: Union[Unset, str] = UNSET
    type_of_representation: Union[Unset, str] = UNSET
    valid_from: Union[Unset, datetime.date] = UNSET
    valid_to: Union[Unset, datetime.date] = UNSET
    currently_valid: Union[Unset, bool] = UNSET
    waiver_of_para181bgb: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        display_name = self.display_name

        addressee_id: Union[Unset, str] = UNSET
        if not isinstance(self.addressee_id, Unset):
            addressee_id = str(self.addressee_id)

        date_of_waiver: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_waiver, Unset):
            date_of_waiver = self.date_of_waiver.isoformat()

        display_in_tax_form = self.display_in_tax_form

        is_authorized_officer = self.is_authorized_officer

        note = self.note

        type_of_representation = self.type_of_representation

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        currently_valid = self.currently_valid

        waiver_of_para181bgb = self.waiver_of_para181bgb


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
        if date_of_waiver is not UNSET:
            field_dict["date_of_waiver"] = date_of_waiver
        if display_in_tax_form is not UNSET:
            field_dict["display_in_tax_form"] = display_in_tax_form
        if is_authorized_officer is not UNSET:
            field_dict["is_authorized_officer"] = is_authorized_officer
        if note is not UNSET:
            field_dict["note"] = note
        if type_of_representation is not UNSET:
            field_dict["type_of_representation"] = type_of_representation
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if valid_to is not UNSET:
            field_dict["valid_to"] = valid_to
        if currently_valid is not UNSET:
            field_dict["currently_valid"] = currently_valid
        if waiver_of_para181bgb is not UNSET:
            field_dict["waiver_of_para181bgb"] = waiver_of_para181bgb

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




        _date_of_waiver = d.pop("date_of_waiver", UNSET)
        date_of_waiver: Union[Unset, datetime.date]
        if isinstance(_date_of_waiver,  Unset):
            date_of_waiver = UNSET
        else:
            date_of_waiver = isoparse(_date_of_waiver).date()




        display_in_tax_form = d.pop("display_in_tax_form", UNSET)

        is_authorized_officer = d.pop("is_authorized_officer", UNSET)

        note = d.pop("note", UNSET)

        type_of_representation = d.pop("type_of_representation", UNSET)

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

        waiver_of_para181bgb = d.pop("waiver_of_para181bgb", UNSET)

        master_client_full_addressee_legal_representative_of_company = cls(
            id=id,
            display_name=display_name,
            addressee_id=addressee_id,
            date_of_waiver=date_of_waiver,
            display_in_tax_form=display_in_tax_form,
            is_authorized_officer=is_authorized_officer,
            note=note,
            type_of_representation=type_of_representation,
            valid_from=valid_from,
            valid_to=valid_to,
            currently_valid=currently_valid,
            waiver_of_para181bgb=waiver_of_para181bgb,
        )


        master_client_full_addressee_legal_representative_of_company.additional_properties = d
        return master_client_full_addressee_legal_representative_of_company

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
