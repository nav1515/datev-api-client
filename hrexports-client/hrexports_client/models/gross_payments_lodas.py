from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="GrossPaymentsLodas")



@_attrs_define
class GrossPaymentsLodas:
    """ Gross Payments represent 'Lohnarten' with wage_type_number up until 8999 for LODAS

        Attributes:
            wage_type_name (Union[Unset, str]): wage type name (Lohnartbezeichnung) Example: Privatfahrten.
            wage_type_number (Union[Unset, str]): wage type number (Lohnartnummer) Example: 0873, 9001.
            wage_type_amount (Union[Unset, float]): wage type amount (Lohnartbetrag) Example: 400.
            tax_and_social_security_treatment_of_wage_type (Union[Unset, str]): Treatment of wage type in context of tax and
                social security Example: 1.
            component_gross_payment (Union[Unset, bool]): Is component of gross payment Example: True.
     """

    wage_type_name: Union[Unset, str] = UNSET
    wage_type_number: Union[Unset, str] = UNSET
    wage_type_amount: Union[Unset, float] = UNSET
    tax_and_social_security_treatment_of_wage_type: Union[Unset, str] = UNSET
    component_gross_payment: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        wage_type_name = self.wage_type_name

        wage_type_number = self.wage_type_number

        wage_type_amount = self.wage_type_amount

        tax_and_social_security_treatment_of_wage_type = self.tax_and_social_security_treatment_of_wage_type

        component_gross_payment = self.component_gross_payment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if wage_type_name is not UNSET:
            field_dict["wage_type_name"] = wage_type_name
        if wage_type_number is not UNSET:
            field_dict["wage_type_number"] = wage_type_number
        if wage_type_amount is not UNSET:
            field_dict["wage_type_amount"] = wage_type_amount
        if tax_and_social_security_treatment_of_wage_type is not UNSET:
            field_dict["tax_and_social_security_treatment_of_wage_type"] = tax_and_social_security_treatment_of_wage_type
        if component_gross_payment is not UNSET:
            field_dict["component_gross_payment"] = component_gross_payment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        wage_type_name = d.pop("wage_type_name", UNSET)

        wage_type_number = d.pop("wage_type_number", UNSET)

        wage_type_amount = d.pop("wage_type_amount", UNSET)

        tax_and_social_security_treatment_of_wage_type = d.pop("tax_and_social_security_treatment_of_wage_type", UNSET)

        component_gross_payment = d.pop("component_gross_payment", UNSET)

        gross_payments_lodas = cls(
            wage_type_name=wage_type_name,
            wage_type_number=wage_type_number,
            wage_type_amount=wage_type_amount,
            tax_and_social_security_treatment_of_wage_type=tax_and_social_security_treatment_of_wage_type,
            component_gross_payment=component_gross_payment,
        )


        gross_payments_lodas.additional_properties = d
        return gross_payments_lodas

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
