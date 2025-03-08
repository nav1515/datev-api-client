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






T = TypeVar("T", bound="MasterClientFullTaxOffice")



@_attrs_define
class MasterClientFullTaxOffice:
    """ (Angaben zum Finanzamt) Tax office specific data.

        Attributes:
            id (Union[Unset, UUID]): GUID - internal ID of a tax office. Example: 43b9d6d9-117b-4555-b0b0-3659eb0279d4.
            country_code (Union[Unset, str]): (Land) Indicates the country in which the tax office is located. A list of all
                available country codes can be retrieved via `GET /country-codes`. Example: DE.
            note (Union[Unset, str]): (Notiz) Field for notes about the tax office. Example: Das ist eine Notiz zur
                Finanzamtsverbindung..
            tax_number (Union[Unset, str]): (Steuernummer) Indicates the tax number which is assigned to the tax payer.
                Example: 216/345/98763.
            tax_number_standardized (Union[Unset, str]): (Steuernummer normiert) Indicates the tax number without special
                characters (purely as a sequence of digits). Example: 21634598763.
            tax_office_name (Union[Unset, str]): (Bezeichnung) Name of the tax office. Example: Erlangen.
            tax_office_number (Union[Unset, int]): (Finanzamtsnummer) Indicates the number of the tax office. This number
                identifies a tax office. Example: 9216.
            valid_from (Union[Unset, datetime.date]): (Gültig von) Indicates the date from which a tax office is valid.
            valid_to (Union[Unset, datetime.date]): (Gültig bis) Indicates the date until which a tax office is valid.
            currently_valid (Union[Unset, bool]): (Gültig) Indicates whether or not the tax office is currently valid.
                Example: True.
            is_competent_for_operational_income_tax (Union[Unset, bool]): (Betriebsfinanzamt) Indicates whether the tax
                office is competent for operating tax respectively income tax. Among all valid tax offices of an addressee, this
                property must be marked with 'true' exactly once. Example: True.
            is_competent_for_turnover_tax (Union[Unset, bool]): (Umsatzsteuerfinanzamt) Indicates whether the tax office is
                competent for turnover tax. Among all valid tax offices of an addressee, this property must be marked with
                'true' no more than once.
            is_competent_for_wage_tax (Union[Unset, bool]): (Lohnsteuerfinzanzamt) Indicates whether the tax office is
                competent for wage tax. Among all valid tax offices of an addressee, this property must be marked with 'true' no
                more than once.
     """

    id: Union[Unset, UUID] = UNSET
    country_code: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    tax_number: Union[Unset, str] = UNSET
    tax_number_standardized: Union[Unset, str] = UNSET
    tax_office_name: Union[Unset, str] = UNSET
    tax_office_number: Union[Unset, int] = UNSET
    valid_from: Union[Unset, datetime.date] = UNSET
    valid_to: Union[Unset, datetime.date] = UNSET
    currently_valid: Union[Unset, bool] = UNSET
    is_competent_for_operational_income_tax: Union[Unset, bool] = UNSET
    is_competent_for_turnover_tax: Union[Unset, bool] = UNSET
    is_competent_for_wage_tax: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        country_code = self.country_code

        note = self.note

        tax_number = self.tax_number

        tax_number_standardized = self.tax_number_standardized

        tax_office_name = self.tax_office_name

        tax_office_number = self.tax_office_number

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        currently_valid = self.currently_valid

        is_competent_for_operational_income_tax = self.is_competent_for_operational_income_tax

        is_competent_for_turnover_tax = self.is_competent_for_turnover_tax

        is_competent_for_wage_tax = self.is_competent_for_wage_tax


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if note is not UNSET:
            field_dict["note"] = note
        if tax_number is not UNSET:
            field_dict["tax_number"] = tax_number
        if tax_number_standardized is not UNSET:
            field_dict["tax_number_standardized"] = tax_number_standardized
        if tax_office_name is not UNSET:
            field_dict["tax_office_name"] = tax_office_name
        if tax_office_number is not UNSET:
            field_dict["tax_office_number"] = tax_office_number
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if valid_to is not UNSET:
            field_dict["valid_to"] = valid_to
        if currently_valid is not UNSET:
            field_dict["currently_valid"] = currently_valid
        if is_competent_for_operational_income_tax is not UNSET:
            field_dict["is_competent_for_operational_income_tax"] = is_competent_for_operational_income_tax
        if is_competent_for_turnover_tax is not UNSET:
            field_dict["is_competent_for_turnover_tax"] = is_competent_for_turnover_tax
        if is_competent_for_wage_tax is not UNSET:
            field_dict["is_competent_for_wage_tax"] = is_competent_for_wage_tax

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




        country_code = d.pop("country_code", UNSET)

        note = d.pop("note", UNSET)

        tax_number = d.pop("tax_number", UNSET)

        tax_number_standardized = d.pop("tax_number_standardized", UNSET)

        tax_office_name = d.pop("tax_office_name", UNSET)

        tax_office_number = d.pop("tax_office_number", UNSET)

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

        is_competent_for_operational_income_tax = d.pop("is_competent_for_operational_income_tax", UNSET)

        is_competent_for_turnover_tax = d.pop("is_competent_for_turnover_tax", UNSET)

        is_competent_for_wage_tax = d.pop("is_competent_for_wage_tax", UNSET)

        master_client_full_tax_office = cls(
            id=id,
            country_code=country_code,
            note=note,
            tax_number=tax_number,
            tax_number_standardized=tax_number_standardized,
            tax_office_name=tax_office_name,
            tax_office_number=tax_office_number,
            valid_from=valid_from,
            valid_to=valid_to,
            currently_valid=currently_valid,
            is_competent_for_operational_income_tax=is_competent_for_operational_income_tax,
            is_competent_for_turnover_tax=is_competent_for_turnover_tax,
            is_competent_for_wage_tax=is_competent_for_wage_tax,
        )


        master_client_full_tax_office.additional_properties = d
        return master_client_full_tax_office

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
