from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Ledgers")



@_attrs_define
class Ledgers:
    """ 
        Attributes:
            is_accounts_payable_ledger_available (Union[Unset, bool]): application for processing accounts payable data is
                existent (= true) or is nonexistent (= false)
            is_accounts_receivable_ledger_available (Union[Unset, bool]): application for processing accounts receivable
                data is existent (= true) or is nonexistent (= false)
            is_cash_ledger_available (Union[Unset, bool]): application for processing cash entries is existent (= true) or
                is nonexistent (= false)
     """

    is_accounts_payable_ledger_available: Union[Unset, bool] = UNSET
    is_accounts_receivable_ledger_available: Union[Unset, bool] = UNSET
    is_cash_ledger_available: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        is_accounts_payable_ledger_available = self.is_accounts_payable_ledger_available

        is_accounts_receivable_ledger_available = self.is_accounts_receivable_ledger_available

        is_cash_ledger_available = self.is_cash_ledger_available


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_accounts_payable_ledger_available is not UNSET:
            field_dict["is_accounts_payable_ledger_available"] = is_accounts_payable_ledger_available
        if is_accounts_receivable_ledger_available is not UNSET:
            field_dict["is_accounts_receivable_ledger_available"] = is_accounts_receivable_ledger_available
        if is_cash_ledger_available is not UNSET:
            field_dict["is_cash_ledger_available"] = is_cash_ledger_available

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        is_accounts_payable_ledger_available = d.pop("is_accounts_payable_ledger_available", UNSET)

        is_accounts_receivable_ledger_available = d.pop("is_accounts_receivable_ledger_available", UNSET)

        is_cash_ledger_available = d.pop("is_cash_ledger_available", UNSET)

        ledgers = cls(
            is_accounts_payable_ledger_available=is_accounts_payable_ledger_available,
            is_accounts_receivable_ledger_available=is_accounts_receivable_ledger_available,
            is_cash_ledger_available=is_cash_ledger_available,
        )


        ledgers.additional_properties = d
        return ledgers

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
