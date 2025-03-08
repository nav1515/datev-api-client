from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="DXSoJob")



@_attrs_define
class DXSoJob:
    r""" 
        Attributes:
            id (Union[Unset, str]): ID of the data transfer (dxso-job)
            account_length (Union[Unset, int]): length of general ledger account of the requested account book and fiscal
                year
            cash_ledger_names (Union[Unset, list[str]]): list of names of the existing cash books of the requested fiscal
                year of the application Kassenbuch online (import_type = cashLedgerImport)
            ledger_folder_names (Union[Unset, list[str]]): "list of names of existing invoice folders of the requested
                fiscal year of Belege online (editing form \"extended\" ) or of Rechnungseingangsbuch online (for import_type =
                accountsPayableLedgerImport) or of Rechnungsausgangsbuch online (import_type = accountsReceivableLedgerImport)"
            datev_chart_of_accounts (Union[Unset, int]): DATEV Sachkontorahmen of the requested account book and fiscal year
     """

    id: Union[Unset, str] = UNSET
    account_length: Union[Unset, int] = UNSET
    cash_ledger_names: Union[Unset, list[str]] = UNSET
    ledger_folder_names: Union[Unset, list[str]] = UNSET
    datev_chart_of_accounts: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_length = self.account_length

        cash_ledger_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cash_ledger_names, Unset):
            cash_ledger_names = self.cash_ledger_names



        ledger_folder_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ledger_folder_names, Unset):
            ledger_folder_names = self.ledger_folder_names



        datev_chart_of_accounts = self.datev_chart_of_accounts


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if account_length is not UNSET:
            field_dict["account_length"] = account_length
        if cash_ledger_names is not UNSET:
            field_dict["cash_ledger_names"] = cash_ledger_names
        if ledger_folder_names is not UNSET:
            field_dict["ledger_folder_names"] = ledger_folder_names
        if datev_chart_of_accounts is not UNSET:
            field_dict["datev_chart_of_accounts"] = datev_chart_of_accounts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        account_length = d.pop("account_length", UNSET)

        cash_ledger_names = cast(list[str], d.pop("cash_ledger_names", UNSET))


        ledger_folder_names = cast(list[str], d.pop("ledger_folder_names", UNSET))


        datev_chart_of_accounts = d.pop("datev_chart_of_accounts", UNSET)

        dx_so_job = cls(
            id=id,
            account_length=account_length,
            cash_ledger_names=cash_ledger_names,
            ledger_folder_names=ledger_folder_names,
            datev_chart_of_accounts=datev_chart_of_accounts,
        )


        dx_so_job.additional_properties = d
        return dx_so_job

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
