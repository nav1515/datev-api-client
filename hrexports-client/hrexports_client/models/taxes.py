from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Taxes")



@_attrs_define
class Taxes:
    """ 
        Attributes:
            denomination (Union[Unset, str]): Employee's denomination (Konfession des Mitarbeiters) Example: 01.
            spouses_denomination (Union[Unset, str]): Spouse's denomination (Konfession des Ehegatten) Example: 01.
            tax_class (Union[Unset, str]): Tax Class (Steuerklasse) Example: 1.
     """

    denomination: Union[Unset, str] = UNSET
    spouses_denomination: Union[Unset, str] = UNSET
    tax_class: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        denomination = self.denomination

        spouses_denomination = self.spouses_denomination

        tax_class = self.tax_class


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if denomination is not UNSET:
            field_dict["denomination"] = denomination
        if spouses_denomination is not UNSET:
            field_dict["spouses_denomination"] = spouses_denomination
        if tax_class is not UNSET:
            field_dict["tax_class"] = tax_class

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        denomination = d.pop("denomination", UNSET)

        spouses_denomination = d.pop("spouses_denomination", UNSET)

        tax_class = d.pop("tax_class", UNSET)

        taxes = cls(
            denomination=denomination,
            spouses_denomination=spouses_denomination,
            tax_class=tax_class,
        )


        taxes.additional_properties = d
        return taxes

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
