from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="HealthInsurance")



@_attrs_define
class HealthInsurance:
    """ 
        Attributes:
            health_insurance_monthly_contribution_employer (Union[Unset, float]): Employer's monthly contribution to health
                insurance (KV-Beitrag AG - laufend) Example: 346.43.
            health_insurance_employers_contribution_non_recurring_payment (Union[Unset, float]): Employer's non recurring
                contribution to health insurance (KV-Beitrag AG - Einmalbezug) Example: 500.43.
            health_insurance_employees_contribution_non_recurring_payment (Union[Unset, float]): Employee's non recurring
                contribution to health insurance (KV-Beitrag AN - Einmalbezug) Example: 500.43.
            health_insurance_monthly_contribution_employee (Union[Unset, float]): Employee's monthly contribution to health
                insurance (KV-Beitrag AN - laufend) Example: 346.43.
            health_insurance_gross (Union[Unset, float]): Gross payment to health insurance (KV-Brutto) Example: 4470.
            health_insurance_gross_non_recurring_payment (Union[Unset, float]): Gross non recurring payment to health
                insurance (KV-Brutto - Einmalbezug) Example: 500.43.
            health_insurance_gross_monthly_contribution (Union[Unset, float]): Gross monthly contribution to health
                insurance (KV-Brutto - laufend) Example: 346.43.
            health_insurance_employees_contribution_total (Union[Unset, float]): Employee's total contribution to health
                insurance) Example: 500.43.
            health_insurance_employer_contribution_total (Union[Unset, float]): Employer's total contribution to health
                insurance Example: 500.43.
     """

    health_insurance_monthly_contribution_employer: Union[Unset, float] = UNSET
    health_insurance_employers_contribution_non_recurring_payment: Union[Unset, float] = UNSET
    health_insurance_employees_contribution_non_recurring_payment: Union[Unset, float] = UNSET
    health_insurance_monthly_contribution_employee: Union[Unset, float] = UNSET
    health_insurance_gross: Union[Unset, float] = UNSET
    health_insurance_gross_non_recurring_payment: Union[Unset, float] = UNSET
    health_insurance_gross_monthly_contribution: Union[Unset, float] = UNSET
    health_insurance_employees_contribution_total: Union[Unset, float] = UNSET
    health_insurance_employer_contribution_total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        health_insurance_monthly_contribution_employer = self.health_insurance_monthly_contribution_employer

        health_insurance_employers_contribution_non_recurring_payment = self.health_insurance_employers_contribution_non_recurring_payment

        health_insurance_employees_contribution_non_recurring_payment = self.health_insurance_employees_contribution_non_recurring_payment

        health_insurance_monthly_contribution_employee = self.health_insurance_monthly_contribution_employee

        health_insurance_gross = self.health_insurance_gross

        health_insurance_gross_non_recurring_payment = self.health_insurance_gross_non_recurring_payment

        health_insurance_gross_monthly_contribution = self.health_insurance_gross_monthly_contribution

        health_insurance_employees_contribution_total = self.health_insurance_employees_contribution_total

        health_insurance_employer_contribution_total = self.health_insurance_employer_contribution_total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if health_insurance_monthly_contribution_employer is not UNSET:
            field_dict["health_insurance_monthly_contribution_employer"] = health_insurance_monthly_contribution_employer
        if health_insurance_employers_contribution_non_recurring_payment is not UNSET:
            field_dict["health_insurance_employers_contribution_non_recurring_payment"] = health_insurance_employers_contribution_non_recurring_payment
        if health_insurance_employees_contribution_non_recurring_payment is not UNSET:
            field_dict["health_insurance_employees_contribution_non_recurring_payment"] = health_insurance_employees_contribution_non_recurring_payment
        if health_insurance_monthly_contribution_employee is not UNSET:
            field_dict["health_insurance_monthly_contribution_employee"] = health_insurance_monthly_contribution_employee
        if health_insurance_gross is not UNSET:
            field_dict["health_insurance_gross"] = health_insurance_gross
        if health_insurance_gross_non_recurring_payment is not UNSET:
            field_dict["health_insurance_gross_non_recurring_payment"] = health_insurance_gross_non_recurring_payment
        if health_insurance_gross_monthly_contribution is not UNSET:
            field_dict["health_insurance_gross_monthly_contribution"] = health_insurance_gross_monthly_contribution
        if health_insurance_employees_contribution_total is not UNSET:
            field_dict["health_insurance_employees_contribution_total"] = health_insurance_employees_contribution_total
        if health_insurance_employer_contribution_total is not UNSET:
            field_dict["health_insurance_employer_contribution_total"] = health_insurance_employer_contribution_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        health_insurance_monthly_contribution_employer = d.pop("health_insurance_monthly_contribution_employer", UNSET)

        health_insurance_employers_contribution_non_recurring_payment = d.pop("health_insurance_employers_contribution_non_recurring_payment", UNSET)

        health_insurance_employees_contribution_non_recurring_payment = d.pop("health_insurance_employees_contribution_non_recurring_payment", UNSET)

        health_insurance_monthly_contribution_employee = d.pop("health_insurance_monthly_contribution_employee", UNSET)

        health_insurance_gross = d.pop("health_insurance_gross", UNSET)

        health_insurance_gross_non_recurring_payment = d.pop("health_insurance_gross_non_recurring_payment", UNSET)

        health_insurance_gross_monthly_contribution = d.pop("health_insurance_gross_monthly_contribution", UNSET)

        health_insurance_employees_contribution_total = d.pop("health_insurance_employees_contribution_total", UNSET)

        health_insurance_employer_contribution_total = d.pop("health_insurance_employer_contribution_total", UNSET)

        health_insurance = cls(
            health_insurance_monthly_contribution_employer=health_insurance_monthly_contribution_employer,
            health_insurance_employers_contribution_non_recurring_payment=health_insurance_employers_contribution_non_recurring_payment,
            health_insurance_employees_contribution_non_recurring_payment=health_insurance_employees_contribution_non_recurring_payment,
            health_insurance_monthly_contribution_employee=health_insurance_monthly_contribution_employee,
            health_insurance_gross=health_insurance_gross,
            health_insurance_gross_non_recurring_payment=health_insurance_gross_non_recurring_payment,
            health_insurance_gross_monthly_contribution=health_insurance_gross_monthly_contribution,
            health_insurance_employees_contribution_total=health_insurance_employees_contribution_total,
            health_insurance_employer_contribution_total=health_insurance_employer_contribution_total,
        )


        health_insurance.additional_properties = d
        return health_insurance

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
