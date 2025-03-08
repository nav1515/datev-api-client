from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="NetPayments")



@_attrs_define
class NetPayments:
    """ Net Payments represent 'Nettobezüge' and 'Nettoabzüge' with wage_type_number equal to or greater than 9000

        Attributes:
            net_payment_number (Union[Unset, str]): net type number (Nettobezugsnummer) Example: 9800.
            net_payment_name (Union[Unset, str]): net type name (Nettobezugsbezeichnung) Example: Essensgeld.
            net_payment_amount (Union[Unset, float]): net type amount (Nettobezugsbetrag) Example: 23.5.
     """

    net_payment_number: Union[Unset, str] = UNSET
    net_payment_name: Union[Unset, str] = UNSET
    net_payment_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        net_payment_number = self.net_payment_number

        net_payment_name = self.net_payment_name

        net_payment_amount = self.net_payment_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if net_payment_number is not UNSET:
            field_dict["net_payment_number"] = net_payment_number
        if net_payment_name is not UNSET:
            field_dict["net_payment_name"] = net_payment_name
        if net_payment_amount is not UNSET:
            field_dict["net_payment_amount"] = net_payment_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        net_payment_number = d.pop("net_payment_number", UNSET)

        net_payment_name = d.pop("net_payment_name", UNSET)

        net_payment_amount = d.pop("net_payment_amount", UNSET)

        net_payments = cls(
            net_payment_number=net_payment_number,
            net_payment_name=net_payment_name,
            net_payment_amount=net_payment_amount,
        )


        net_payments.additional_properties = d
        return net_payments

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
