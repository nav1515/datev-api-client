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






T = TypeVar("T", bound="MasterClientFullBankAccount")



@_attrs_define
class MasterClientFullBankAccount:
    """ (Angaben zur Bankverbindung) Bank account specific data.

        Attributes:
            id (Union[Unset, UUID]): GUID - internal ID of a bank account. Example: 31b9d6d9-117b-4555-b0b0-3659eb0279d0.
            bank_account_number (Union[Unset, str]): (Kontonummer) Number of the bank account. The maximum length depends on
                the country in which the bank account is located (property country_code). For 'DE' 10 digits; for 'AT' 11
                digits; for 'PL' 16 digits; for 'IT' 20 digits; for 'CZ' 17 digits. For any other country 30 digits are
                permissible. Example: 3225553.
            bank_code (Union[Unset, str]): (Bankleitzahl) Code number for identification all banks within a country. Bank
                branches are not identified. The maximum length depends on the country in which the bank is located (property
                country_code). For 'DE' 8 digits; for 'AT' 5 digits; for 'PL' 8 digits. For any other country 10 digits are
                permissible. Example: 76050101.
            bank_name (Union[Unset, str]): (Bezeichnung) Name of the bank. Example: Sparkasse Nürnberg.
            bic (Union[Unset, str]): (BIC) Unique identifier for a SWIFT-participant (BIC - Bank Identifier Code). SWIFT is
                the abbreviation for "Society for Worldwide Interbank Financial Telecommunications". Example: SSKNDE77XXX.
            country_code (Union[Unset, str]): (Land) Indicates the country in which the bank is located. A list of all
                available country codes can be retrieved via `GET /country-codes`. Example: DE.
            differing_account_holder (Union[Unset, str]): (Abw. Kontoinhaber) Name of the account holder, if is not the
                associated addressee. Example: Max Mustermann.
            iban (Union[Unset, str]): (IBAN) Identifies a bank account worldwide (ISO 13616). Example:
                DE12760501010003225553.
            note (Union[Unset, str]): (Notiz) Field for notes about the bank account. Example: Das ist eine Notiz zur
                Bankverbindung..
            valid_from (Union[Unset, datetime.date]): (Gültig von) Indicates the date from which a bank account is valid.
            valid_to (Union[Unset, datetime.date]): (Gültig bis) Indicates the date until which a bank account is valid.
            currently_valid (Union[Unset, bool]): (Gültig) Indicates whether or not the bank account is currently valid.
                Example: True.
            is_main_bank_account (Union[Unset, bool]): (Hauptbank) Indicates whether this is the main bank account. Among
                all valid bank accounts of an addressee, this property must be marked with 'true' exactly once. Example: True.
     """

    id: Union[Unset, UUID] = UNSET
    bank_account_number: Union[Unset, str] = UNSET
    bank_code: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    bic: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    differing_account_holder: Union[Unset, str] = UNSET
    iban: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    valid_from: Union[Unset, datetime.date] = UNSET
    valid_to: Union[Unset, datetime.date] = UNSET
    currently_valid: Union[Unset, bool] = UNSET
    is_main_bank_account: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        bank_account_number = self.bank_account_number

        bank_code = self.bank_code

        bank_name = self.bank_name

        bic = self.bic

        country_code = self.country_code

        differing_account_holder = self.differing_account_holder

        iban = self.iban

        note = self.note

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        currently_valid = self.currently_valid

        is_main_bank_account = self.is_main_bank_account


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if bank_account_number is not UNSET:
            field_dict["bank_account_number"] = bank_account_number
        if bank_code is not UNSET:
            field_dict["bank_code"] = bank_code
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if bic is not UNSET:
            field_dict["bic"] = bic
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if differing_account_holder is not UNSET:
            field_dict["differing_account_holder"] = differing_account_holder
        if iban is not UNSET:
            field_dict["iban"] = iban
        if note is not UNSET:
            field_dict["note"] = note
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if valid_to is not UNSET:
            field_dict["valid_to"] = valid_to
        if currently_valid is not UNSET:
            field_dict["currently_valid"] = currently_valid
        if is_main_bank_account is not UNSET:
            field_dict["is_main_bank_account"] = is_main_bank_account

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




        bank_account_number = d.pop("bank_account_number", UNSET)

        bank_code = d.pop("bank_code", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        bic = d.pop("bic", UNSET)

        country_code = d.pop("country_code", UNSET)

        differing_account_holder = d.pop("differing_account_holder", UNSET)

        iban = d.pop("iban", UNSET)

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

        is_main_bank_account = d.pop("is_main_bank_account", UNSET)

        master_client_full_bank_account = cls(
            id=id,
            bank_account_number=bank_account_number,
            bank_code=bank_code,
            bank_name=bank_name,
            bic=bic,
            country_code=country_code,
            differing_account_holder=differing_account_holder,
            iban=iban,
            note=note,
            valid_from=valid_from,
            valid_to=valid_to,
            currently_valid=currently_valid,
            is_main_bank_account=is_main_bank_account,
        )


        master_client_full_bank_account.additional_properties = d
        return master_client_full_bank_account

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
