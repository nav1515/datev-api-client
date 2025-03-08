from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="SalaryTotalValues")



@_attrs_define
class SalaryTotalValues:
    """ 
        Attributes:
            personnel_number (Union[Unset, int]): Employee's personnel number in the payroll system Example: 10.
            company_personnel_number (Union[Unset, str]): Company personnel number (Betriebliche Personalnummer) Example:
                A10.
            accounting_month (Union[Unset, str]): Accounting month (Abrechnungsmonat) Example: 2020-01.
            month_of_recalculation (Union[Unset, str]): Month of recalculation (Nachberechnungsmonat) Example: 2020-01.
            current_gross_payment (Union[Unset, float]): Total gross amount of the employee Example: 2990.
            amount_paid (Union[Unset, float]): Amount paid out by the employee Example: 1606.92.
            net_income (Union[Unset, float]): Employee's net income Example: 3326.92.
            net_payments_and_net_deductions (Union[Unset, float]): Sum of net renumeration and net deductions of an employee
                Example: -70.
            total_statutory_deductions (Union[Unset, float]): Sum of statutory deductions Example: -70.
     """

    personnel_number: Union[Unset, int] = UNSET
    company_personnel_number: Union[Unset, str] = UNSET
    accounting_month: Union[Unset, str] = UNSET
    month_of_recalculation: Union[Unset, str] = UNSET
    current_gross_payment: Union[Unset, float] = UNSET
    amount_paid: Union[Unset, float] = UNSET
    net_income: Union[Unset, float] = UNSET
    net_payments_and_net_deductions: Union[Unset, float] = UNSET
    total_statutory_deductions: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        personnel_number = self.personnel_number

        company_personnel_number = self.company_personnel_number

        accounting_month = self.accounting_month

        month_of_recalculation = self.month_of_recalculation

        current_gross_payment = self.current_gross_payment

        amount_paid = self.amount_paid

        net_income = self.net_income

        net_payments_and_net_deductions = self.net_payments_and_net_deductions

        total_statutory_deductions = self.total_statutory_deductions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if personnel_number is not UNSET:
            field_dict["personnel_number"] = personnel_number
        if company_personnel_number is not UNSET:
            field_dict["company_personnel_number"] = company_personnel_number
        if accounting_month is not UNSET:
            field_dict["accounting_month"] = accounting_month
        if month_of_recalculation is not UNSET:
            field_dict["month_of_recalculation"] = month_of_recalculation
        if current_gross_payment is not UNSET:
            field_dict["current_gross_payment"] = current_gross_payment
        if amount_paid is not UNSET:
            field_dict["amount_paid"] = amount_paid
        if net_income is not UNSET:
            field_dict["net_income"] = net_income
        if net_payments_and_net_deductions is not UNSET:
            field_dict["net_payments_and_net_deductions"] = net_payments_and_net_deductions
        if total_statutory_deductions is not UNSET:
            field_dict["total_statutory_deductions"] = total_statutory_deductions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        personnel_number = d.pop("personnel_number", UNSET)

        company_personnel_number = d.pop("company_personnel_number", UNSET)

        accounting_month = d.pop("accounting_month", UNSET)

        month_of_recalculation = d.pop("month_of_recalculation", UNSET)

        current_gross_payment = d.pop("current_gross_payment", UNSET)

        amount_paid = d.pop("amount_paid", UNSET)

        net_income = d.pop("net_income", UNSET)

        net_payments_and_net_deductions = d.pop("net_payments_and_net_deductions", UNSET)

        total_statutory_deductions = d.pop("total_statutory_deductions", UNSET)

        salary_total_values = cls(
            personnel_number=personnel_number,
            company_personnel_number=company_personnel_number,
            accounting_month=accounting_month,
            month_of_recalculation=month_of_recalculation,
            current_gross_payment=current_gross_payment,
            amount_paid=amount_paid,
            net_income=net_income,
            net_payments_and_net_deductions=net_payments_and_net_deductions,
            total_statutory_deductions=total_statutory_deductions,
        )


        salary_total_values.additional_properties = d
        return salary_total_values

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
