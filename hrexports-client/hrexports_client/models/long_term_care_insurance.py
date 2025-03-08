from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="LongTermCareInsurance")



@_attrs_define
class LongTermCareInsurance:
    """ 
        Attributes:
            long_term_care_insurance_monthly_contribution_employer (Union[Unset, float]): Employer's monthly contribution to
                long term care insurance (PV-Beitrag AG - laufend) Example: 68.17.
            long_term_care_insurance_employers_contribution_non_recurring_payment (Union[Unset, float]): Employer's non
                recurring contribution to long term care insurance (PV-Beitrag AG - Einmalbezug) Example: 100.43.
            long_term_care_insurance_employees_contribution_non_recurring_payment (Union[Unset, float]): Employee's non
                recurring contribution to long term care insurance (PV-Beitrag AN - Einmalbezug) Example: 100.43.
            long_term_care_insurance_monthly_contribution_employee (Union[Unset, float]): Employee's monthly contribution to
                long term care insurance (PV-Beitrag AN - laufend) Example: 68.17.
            long_term_care_insurance_gross (Union[Unset, float]): Gross payment to long term care insurance (PV-Brutto)
                Example: 45.99.
            long_term_care_insurance_gross_non_recurring_payment (Union[Unset, float]): Gross non recurring payment to long
                term care insurance (PV-Brutto - Einmalbezug) Example: 100.43.
            long_term_care_insurance_gross_monthly_contribution (Union[Unset, float]): Gross monthly contribution to long
                term care insurance (PV-Brutto - laufend) Example: 68.17.
            long_term_care_insurance_employees_contribution_total (Union[Unset, float]): Employee's total contribution to
                long term care insurance) Example: 500.43.
            long_term_care_insurance_employer_contribution_total (Union[Unset, float]): Employer's total contribution to
                long term care insurance Example: 500.43.
     """

    long_term_care_insurance_monthly_contribution_employer: Union[Unset, float] = UNSET
    long_term_care_insurance_employers_contribution_non_recurring_payment: Union[Unset, float] = UNSET
    long_term_care_insurance_employees_contribution_non_recurring_payment: Union[Unset, float] = UNSET
    long_term_care_insurance_monthly_contribution_employee: Union[Unset, float] = UNSET
    long_term_care_insurance_gross: Union[Unset, float] = UNSET
    long_term_care_insurance_gross_non_recurring_payment: Union[Unset, float] = UNSET
    long_term_care_insurance_gross_monthly_contribution: Union[Unset, float] = UNSET
    long_term_care_insurance_employees_contribution_total: Union[Unset, float] = UNSET
    long_term_care_insurance_employer_contribution_total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        long_term_care_insurance_monthly_contribution_employer = self.long_term_care_insurance_monthly_contribution_employer

        long_term_care_insurance_employers_contribution_non_recurring_payment = self.long_term_care_insurance_employers_contribution_non_recurring_payment

        long_term_care_insurance_employees_contribution_non_recurring_payment = self.long_term_care_insurance_employees_contribution_non_recurring_payment

        long_term_care_insurance_monthly_contribution_employee = self.long_term_care_insurance_monthly_contribution_employee

        long_term_care_insurance_gross = self.long_term_care_insurance_gross

        long_term_care_insurance_gross_non_recurring_payment = self.long_term_care_insurance_gross_non_recurring_payment

        long_term_care_insurance_gross_monthly_contribution = self.long_term_care_insurance_gross_monthly_contribution

        long_term_care_insurance_employees_contribution_total = self.long_term_care_insurance_employees_contribution_total

        long_term_care_insurance_employer_contribution_total = self.long_term_care_insurance_employer_contribution_total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if long_term_care_insurance_monthly_contribution_employer is not UNSET:
            field_dict["long_term_care_insurance_monthly_contribution_employer"] = long_term_care_insurance_monthly_contribution_employer
        if long_term_care_insurance_employers_contribution_non_recurring_payment is not UNSET:
            field_dict["long_term_care_insurance_employers_contribution_non_recurring_payment"] = long_term_care_insurance_employers_contribution_non_recurring_payment
        if long_term_care_insurance_employees_contribution_non_recurring_payment is not UNSET:
            field_dict["long_term_care_insurance_employees_contribution_non_recurring_payment"] = long_term_care_insurance_employees_contribution_non_recurring_payment
        if long_term_care_insurance_monthly_contribution_employee is not UNSET:
            field_dict["long_term_care_insurance_monthly_contribution_employee"] = long_term_care_insurance_monthly_contribution_employee
        if long_term_care_insurance_gross is not UNSET:
            field_dict["long_term_care_insurance_gross"] = long_term_care_insurance_gross
        if long_term_care_insurance_gross_non_recurring_payment is not UNSET:
            field_dict["long_term_care_insurance_gross_non_recurring_payment"] = long_term_care_insurance_gross_non_recurring_payment
        if long_term_care_insurance_gross_monthly_contribution is not UNSET:
            field_dict["long_term_care_insurance_gross_monthly_contribution"] = long_term_care_insurance_gross_monthly_contribution
        if long_term_care_insurance_employees_contribution_total is not UNSET:
            field_dict["long_term_care_insurance_employees_contribution_total"] = long_term_care_insurance_employees_contribution_total
        if long_term_care_insurance_employer_contribution_total is not UNSET:
            field_dict["long_term_care_insurance_employer_contribution_total"] = long_term_care_insurance_employer_contribution_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        long_term_care_insurance_monthly_contribution_employer = d.pop("long_term_care_insurance_monthly_contribution_employer", UNSET)

        long_term_care_insurance_employers_contribution_non_recurring_payment = d.pop("long_term_care_insurance_employers_contribution_non_recurring_payment", UNSET)

        long_term_care_insurance_employees_contribution_non_recurring_payment = d.pop("long_term_care_insurance_employees_contribution_non_recurring_payment", UNSET)

        long_term_care_insurance_monthly_contribution_employee = d.pop("long_term_care_insurance_monthly_contribution_employee", UNSET)

        long_term_care_insurance_gross = d.pop("long_term_care_insurance_gross", UNSET)

        long_term_care_insurance_gross_non_recurring_payment = d.pop("long_term_care_insurance_gross_non_recurring_payment", UNSET)

        long_term_care_insurance_gross_monthly_contribution = d.pop("long_term_care_insurance_gross_monthly_contribution", UNSET)

        long_term_care_insurance_employees_contribution_total = d.pop("long_term_care_insurance_employees_contribution_total", UNSET)

        long_term_care_insurance_employer_contribution_total = d.pop("long_term_care_insurance_employer_contribution_total", UNSET)

        long_term_care_insurance = cls(
            long_term_care_insurance_monthly_contribution_employer=long_term_care_insurance_monthly_contribution_employer,
            long_term_care_insurance_employers_contribution_non_recurring_payment=long_term_care_insurance_employers_contribution_non_recurring_payment,
            long_term_care_insurance_employees_contribution_non_recurring_payment=long_term_care_insurance_employees_contribution_non_recurring_payment,
            long_term_care_insurance_monthly_contribution_employee=long_term_care_insurance_monthly_contribution_employee,
            long_term_care_insurance_gross=long_term_care_insurance_gross,
            long_term_care_insurance_gross_non_recurring_payment=long_term_care_insurance_gross_non_recurring_payment,
            long_term_care_insurance_gross_monthly_contribution=long_term_care_insurance_gross_monthly_contribution,
            long_term_care_insurance_employees_contribution_total=long_term_care_insurance_employees_contribution_total,
            long_term_care_insurance_employer_contribution_total=long_term_care_insurance_employer_contribution_total,
        )


        long_term_care_insurance.additional_properties = d
        return long_term_care_insurance

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
