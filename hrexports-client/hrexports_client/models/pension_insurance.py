from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="PensionInsurance")



@_attrs_define
class PensionInsurance:
    """ 
        Attributes:
            pension_insurance_monthly_contribution_employer (Union[Unset, float]): Employer's monthly contribution to
                pension insurance (RV-Beitrag AG - laufend) Example: 415.71.
            pension_insurance_employers_contribution_non_recurring_payment (Union[Unset, float]): Employer's non recurring
                payment to pension insurance (RV-Beitrag AG - Einmalbezug) Example: 500.43.
            pension_insurance_employees_contribution_non_recurring_payment (Union[Unset, float]): Employee's non recurring
                payment to pension insurance (RV-Beitrag AN - Einmalbezug) Example: 500.43.
            pension_insurance_monthly_contribution_employee (Union[Unset, float]): Employee's monthly contribution to
                pension insurance (RV-Beitrag AN - laufend) Example: 415.71.
            pension_insurance_gross (Union[Unset, float]): Gross payment to pension insurance (RV-Brutto) Example: 77.98.
            pension_insurance_gross_non_recurring_payment (Union[Unset, float]): Gross non recurring payment to pension
                insurance (RV-Brutto - Einmalbezug) Example: 500.43.
            pension_insurance_gross_monthly_contribution (Union[Unset, float]): Gross monthly contribution to pension
                insurance (RV-Brutto - laufend) Example: 415.71.
            pension_insurance_employees_contribution_total (Union[Unset, float]): Employee's total contribution to pension
                insurance) Example: 500.43.
            pension_insurance_employer_contribution_total (Union[Unset, float]): Employer's total contribution to pension
                insurance Example: 500.43.
     """

    pension_insurance_monthly_contribution_employer: Union[Unset, float] = UNSET
    pension_insurance_employers_contribution_non_recurring_payment: Union[Unset, float] = UNSET
    pension_insurance_employees_contribution_non_recurring_payment: Union[Unset, float] = UNSET
    pension_insurance_monthly_contribution_employee: Union[Unset, float] = UNSET
    pension_insurance_gross: Union[Unset, float] = UNSET
    pension_insurance_gross_non_recurring_payment: Union[Unset, float] = UNSET
    pension_insurance_gross_monthly_contribution: Union[Unset, float] = UNSET
    pension_insurance_employees_contribution_total: Union[Unset, float] = UNSET
    pension_insurance_employer_contribution_total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        pension_insurance_monthly_contribution_employer = self.pension_insurance_monthly_contribution_employer

        pension_insurance_employers_contribution_non_recurring_payment = self.pension_insurance_employers_contribution_non_recurring_payment

        pension_insurance_employees_contribution_non_recurring_payment = self.pension_insurance_employees_contribution_non_recurring_payment

        pension_insurance_monthly_contribution_employee = self.pension_insurance_monthly_contribution_employee

        pension_insurance_gross = self.pension_insurance_gross

        pension_insurance_gross_non_recurring_payment = self.pension_insurance_gross_non_recurring_payment

        pension_insurance_gross_monthly_contribution = self.pension_insurance_gross_monthly_contribution

        pension_insurance_employees_contribution_total = self.pension_insurance_employees_contribution_total

        pension_insurance_employer_contribution_total = self.pension_insurance_employer_contribution_total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if pension_insurance_monthly_contribution_employer is not UNSET:
            field_dict["pension_insurance_monthly_contribution_employer"] = pension_insurance_monthly_contribution_employer
        if pension_insurance_employers_contribution_non_recurring_payment is not UNSET:
            field_dict["pension_insurance_employers_contribution_non_recurring_payment"] = pension_insurance_employers_contribution_non_recurring_payment
        if pension_insurance_employees_contribution_non_recurring_payment is not UNSET:
            field_dict["pension_insurance_employees_contribution_non_recurring_payment"] = pension_insurance_employees_contribution_non_recurring_payment
        if pension_insurance_monthly_contribution_employee is not UNSET:
            field_dict["pension_insurance_monthly_contribution_employee"] = pension_insurance_monthly_contribution_employee
        if pension_insurance_gross is not UNSET:
            field_dict["pension_insurance_gross"] = pension_insurance_gross
        if pension_insurance_gross_non_recurring_payment is not UNSET:
            field_dict["pension_insurance_gross_non_recurring_payment"] = pension_insurance_gross_non_recurring_payment
        if pension_insurance_gross_monthly_contribution is not UNSET:
            field_dict["pension_insurance_gross_monthly_contribution"] = pension_insurance_gross_monthly_contribution
        if pension_insurance_employees_contribution_total is not UNSET:
            field_dict["pension_insurance_employees_contribution_total"] = pension_insurance_employees_contribution_total
        if pension_insurance_employer_contribution_total is not UNSET:
            field_dict["pension_insurance_employer_contribution_total"] = pension_insurance_employer_contribution_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        pension_insurance_monthly_contribution_employer = d.pop("pension_insurance_monthly_contribution_employer", UNSET)

        pension_insurance_employers_contribution_non_recurring_payment = d.pop("pension_insurance_employers_contribution_non_recurring_payment", UNSET)

        pension_insurance_employees_contribution_non_recurring_payment = d.pop("pension_insurance_employees_contribution_non_recurring_payment", UNSET)

        pension_insurance_monthly_contribution_employee = d.pop("pension_insurance_monthly_contribution_employee", UNSET)

        pension_insurance_gross = d.pop("pension_insurance_gross", UNSET)

        pension_insurance_gross_non_recurring_payment = d.pop("pension_insurance_gross_non_recurring_payment", UNSET)

        pension_insurance_gross_monthly_contribution = d.pop("pension_insurance_gross_monthly_contribution", UNSET)

        pension_insurance_employees_contribution_total = d.pop("pension_insurance_employees_contribution_total", UNSET)

        pension_insurance_employer_contribution_total = d.pop("pension_insurance_employer_contribution_total", UNSET)

        pension_insurance = cls(
            pension_insurance_monthly_contribution_employer=pension_insurance_monthly_contribution_employer,
            pension_insurance_employers_contribution_non_recurring_payment=pension_insurance_employers_contribution_non_recurring_payment,
            pension_insurance_employees_contribution_non_recurring_payment=pension_insurance_employees_contribution_non_recurring_payment,
            pension_insurance_monthly_contribution_employee=pension_insurance_monthly_contribution_employee,
            pension_insurance_gross=pension_insurance_gross,
            pension_insurance_gross_non_recurring_payment=pension_insurance_gross_non_recurring_payment,
            pension_insurance_gross_monthly_contribution=pension_insurance_gross_monthly_contribution,
            pension_insurance_employees_contribution_total=pension_insurance_employees_contribution_total,
            pension_insurance_employer_contribution_total=pension_insurance_employer_contribution_total,
        )


        pension_insurance.additional_properties = d
        return pension_insurance

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
