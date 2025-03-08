from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.ledgers import Ledgers





T = TypeVar("T", bound="BasicAccountingInformation")



@_attrs_define
class BasicAccountingInformation:
    """ 
        Attributes:
            fiscal_year_start (Union[Unset, datetime.date]): start of the fiscal year
            fiscal_year_end (Union[Unset, datetime.date]): end of the fiscal year
            account_length (Union[Unset, int]): length of general ledger account of the determined fiscal year (length is
                between 4 and 8)
            datev_chart_of_accounts (Union[Unset, int]): 'DATEV Sachkontorahmen'
                 of the determined fiscal year
            ledgers (Union[Unset, Ledgers]):
     """

    fiscal_year_start: Union[Unset, datetime.date] = UNSET
    fiscal_year_end: Union[Unset, datetime.date] = UNSET
    account_length: Union[Unset, int] = UNSET
    datev_chart_of_accounts: Union[Unset, int] = UNSET
    ledgers: Union[Unset, 'Ledgers'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.ledgers import Ledgers
        fiscal_year_start: Union[Unset, str] = UNSET
        if not isinstance(self.fiscal_year_start, Unset):
            fiscal_year_start = self.fiscal_year_start.isoformat()

        fiscal_year_end: Union[Unset, str] = UNSET
        if not isinstance(self.fiscal_year_end, Unset):
            fiscal_year_end = self.fiscal_year_end.isoformat()

        account_length = self.account_length

        datev_chart_of_accounts = self.datev_chart_of_accounts

        ledgers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ledgers, Unset):
            ledgers = self.ledgers.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fiscal_year_start is not UNSET:
            field_dict["fiscal_year_start"] = fiscal_year_start
        if fiscal_year_end is not UNSET:
            field_dict["fiscal_year_end"] = fiscal_year_end
        if account_length is not UNSET:
            field_dict["account_length"] = account_length
        if datev_chart_of_accounts is not UNSET:
            field_dict["datev_chart_of_accounts"] = datev_chart_of_accounts
        if ledgers is not UNSET:
            field_dict["ledgers"] = ledgers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.ledgers import Ledgers
        d = src_dict.copy()
        _fiscal_year_start = d.pop("fiscal_year_start", UNSET)
        fiscal_year_start: Union[Unset, datetime.date]
        if isinstance(_fiscal_year_start,  Unset):
            fiscal_year_start = UNSET
        else:
            fiscal_year_start = isoparse(_fiscal_year_start).date()




        _fiscal_year_end = d.pop("fiscal_year_end", UNSET)
        fiscal_year_end: Union[Unset, datetime.date]
        if isinstance(_fiscal_year_end,  Unset):
            fiscal_year_end = UNSET
        else:
            fiscal_year_end = isoparse(_fiscal_year_end).date()




        account_length = d.pop("account_length", UNSET)

        datev_chart_of_accounts = d.pop("datev_chart_of_accounts", UNSET)

        _ledgers = d.pop("ledgers", UNSET)
        ledgers: Union[Unset, Ledgers]
        if isinstance(_ledgers,  Unset):
            ledgers = UNSET
        else:
            ledgers = Ledgers.from_dict(_ledgers)




        basic_accounting_information = cls(
            fiscal_year_start=fiscal_year_start,
            fiscal_year_end=fiscal_year_end,
            account_length=account_length,
            datev_chart_of_accounts=datev_chart_of_accounts,
            ledgers=ledgers,
        )


        basic_accounting_information.additional_properties = d
        return basic_accounting_information

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
