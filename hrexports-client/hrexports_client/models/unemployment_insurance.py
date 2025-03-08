from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="UnemploymentInsurance")



@_attrs_define
class UnemploymentInsurance:
    """ 
        Attributes:
            unemployment_insurance_monthly_contribution_employer (Union[Unset, float]): Employer's monthly contribution to
                unemployment insurance (AV-Beitrag AG - laufend) Example: 55.88.
            unemployment_insurance_employees_contribution_non_recurring_payment (Union[Unset, float]): Employer's non
                recurring payment to unemployment insurance (AV-Beitrag AG - Einmalbezug) Example: 100.43.
            unemployment_insurance_employers_contribution_non_recurring_payment (Union[Unset, float]): Employee's non
                recurring contribution to unemployment insurance (AV-Beitrag AN - Einmalbezug) Example: 100.43.
            unemployment_insurance_monthly_contribution_employee (Union[Unset, float]): Employee's monthly contribution to
                unemployment insurance (AV-Beitrag AN - laufend) Example: 55.88.
            unemployment_insurance_gross (Union[Unset, float]): Gross payment to unemployment insurance (AV-Brutto) Example:
                64.88.
            unemployment_insurance_gross_non_recurring_payment (Union[Unset, float]): Gross non recurring payment to
                unemployment insurance (AV-Brutto - Einmalbezug) Example: 100.43.
            unemployment_insurance_gross_monthly_contribution (Union[Unset, float]): Gross monthly contribution to
                unemployment insurance (AV-Brutto - laufend) Example: 55.88.
            unemployment_insurance_employees_contribution_total (Union[Unset, float]): Employee's total contribution to
                unemployment insurance) Example: 500.43.
            unemployment_insurance_employer_contribution_total (Union[Unset, float]): Employer's total contribution to
                unemployment insurance Example: 500.43.
     """

    unemployment_insurance_monthly_contribution_employer: Union[Unset, float] = UNSET
    unemployment_insurance_employees_contribution_non_recurring_payment: Union[Unset, float] = UNSET
    unemployment_insurance_employers_contribution_non_recurring_payment: Union[Unset, float] = UNSET
    unemployment_insurance_monthly_contribution_employee: Union[Unset, float] = UNSET
    unemployment_insurance_gross: Union[Unset, float] = UNSET
    unemployment_insurance_gross_non_recurring_payment: Union[Unset, float] = UNSET
    unemployment_insurance_gross_monthly_contribution: Union[Unset, float] = UNSET
    unemployment_insurance_employees_contribution_total: Union[Unset, float] = UNSET
    unemployment_insurance_employer_contribution_total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        unemployment_insurance_monthly_contribution_employer = self.unemployment_insurance_monthly_contribution_employer

        unemployment_insurance_employees_contribution_non_recurring_payment = self.unemployment_insurance_employees_contribution_non_recurring_payment

        unemployment_insurance_employers_contribution_non_recurring_payment = self.unemployment_insurance_employers_contribution_non_recurring_payment

        unemployment_insurance_monthly_contribution_employee = self.unemployment_insurance_monthly_contribution_employee

        unemployment_insurance_gross = self.unemployment_insurance_gross

        unemployment_insurance_gross_non_recurring_payment = self.unemployment_insurance_gross_non_recurring_payment

        unemployment_insurance_gross_monthly_contribution = self.unemployment_insurance_gross_monthly_contribution

        unemployment_insurance_employees_contribution_total = self.unemployment_insurance_employees_contribution_total

        unemployment_insurance_employer_contribution_total = self.unemployment_insurance_employer_contribution_total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if unemployment_insurance_monthly_contribution_employer is not UNSET:
            field_dict["unemployment_insurance_monthly_contribution_employer"] = unemployment_insurance_monthly_contribution_employer
        if unemployment_insurance_employees_contribution_non_recurring_payment is not UNSET:
            field_dict["unemployment_insurance_employees_contribution_non_recurring_payment"] = unemployment_insurance_employees_contribution_non_recurring_payment
        if unemployment_insurance_employers_contribution_non_recurring_payment is not UNSET:
            field_dict["unemployment_insurance_employers_contribution_non_recurring_payment"] = unemployment_insurance_employers_contribution_non_recurring_payment
        if unemployment_insurance_monthly_contribution_employee is not UNSET:
            field_dict["unemployment_insurance_monthly_contribution_employee"] = unemployment_insurance_monthly_contribution_employee
        if unemployment_insurance_gross is not UNSET:
            field_dict["unemployment_insurance_gross"] = unemployment_insurance_gross
        if unemployment_insurance_gross_non_recurring_payment is not UNSET:
            field_dict["unemployment_insurance_gross_non_recurring_payment"] = unemployment_insurance_gross_non_recurring_payment
        if unemployment_insurance_gross_monthly_contribution is not UNSET:
            field_dict["unemployment_insurance_gross_monthly_contribution"] = unemployment_insurance_gross_monthly_contribution
        if unemployment_insurance_employees_contribution_total is not UNSET:
            field_dict["unemployment_insurance_employees_contribution_total"] = unemployment_insurance_employees_contribution_total
        if unemployment_insurance_employer_contribution_total is not UNSET:
            field_dict["unemployment_insurance_employer_contribution_total"] = unemployment_insurance_employer_contribution_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        unemployment_insurance_monthly_contribution_employer = d.pop("unemployment_insurance_monthly_contribution_employer", UNSET)

        unemployment_insurance_employees_contribution_non_recurring_payment = d.pop("unemployment_insurance_employees_contribution_non_recurring_payment", UNSET)

        unemployment_insurance_employers_contribution_non_recurring_payment = d.pop("unemployment_insurance_employers_contribution_non_recurring_payment", UNSET)

        unemployment_insurance_monthly_contribution_employee = d.pop("unemployment_insurance_monthly_contribution_employee", UNSET)

        unemployment_insurance_gross = d.pop("unemployment_insurance_gross", UNSET)

        unemployment_insurance_gross_non_recurring_payment = d.pop("unemployment_insurance_gross_non_recurring_payment", UNSET)

        unemployment_insurance_gross_monthly_contribution = d.pop("unemployment_insurance_gross_monthly_contribution", UNSET)

        unemployment_insurance_employees_contribution_total = d.pop("unemployment_insurance_employees_contribution_total", UNSET)

        unemployment_insurance_employer_contribution_total = d.pop("unemployment_insurance_employer_contribution_total", UNSET)

        unemployment_insurance = cls(
            unemployment_insurance_monthly_contribution_employer=unemployment_insurance_monthly_contribution_employer,
            unemployment_insurance_employees_contribution_non_recurring_payment=unemployment_insurance_employees_contribution_non_recurring_payment,
            unemployment_insurance_employers_contribution_non_recurring_payment=unemployment_insurance_employers_contribution_non_recurring_payment,
            unemployment_insurance_monthly_contribution_employee=unemployment_insurance_monthly_contribution_employee,
            unemployment_insurance_gross=unemployment_insurance_gross,
            unemployment_insurance_gross_non_recurring_payment=unemployment_insurance_gross_non_recurring_payment,
            unemployment_insurance_gross_monthly_contribution=unemployment_insurance_gross_monthly_contribution,
            unemployment_insurance_employees_contribution_total=unemployment_insurance_employees_contribution_total,
            unemployment_insurance_employer_contribution_total=unemployment_insurance_employer_contribution_total,
        )


        unemployment_insurance.additional_properties = d
        return unemployment_insurance

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
