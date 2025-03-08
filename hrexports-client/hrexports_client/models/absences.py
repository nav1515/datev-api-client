from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Absences")



@_attrs_define
class Absences:
    """ 
        Attributes:
            personnel_number (Union[Unset, int]): Employee's personnel number in the payroll system Example: 10.
            company_personnel_number (Union[Unset, str]): Company personnel number (Betriebliche Personalnummer) Example:
                10.
            accounting_month (Union[Unset, str]): Accounting month (Abrechnungsmonat) Example: 2020-01.
            month_of_recalculation (Union[Unset, str]): Month of recalculation (Nachberechnungsmonat) Example: 2020-01.
            total_vacation_entitlement (Union[Unset, float]): total vacation entitlement without remaining vacation days
                from the previous year Example: 30.
            vacation_days_taken (Union[Unset, float]): number of vacation days taken in the current year Example: 12.5.
            remaining_vacation_days_previous_year (Union[Unset, float]): number of remaining vacation days from the previous
                year Example: 3.
            remaining_vacation_days_current_year (Union[Unset, float]): number of remaining vacation days in the current
                year Example: 27.5.
            sick_leave_month (Union[Unset, float]): Number of sick days for current month Example: 1.
            sick_leave_hours (Union[Unset, float]): Number of sick days as hours Example: 8.
            overtime (Union[Unset, float]): number of overtime hours Example: 4.5.
     """

    personnel_number: Union[Unset, int] = UNSET
    company_personnel_number: Union[Unset, str] = UNSET
    accounting_month: Union[Unset, str] = UNSET
    month_of_recalculation: Union[Unset, str] = UNSET
    total_vacation_entitlement: Union[Unset, float] = UNSET
    vacation_days_taken: Union[Unset, float] = UNSET
    remaining_vacation_days_previous_year: Union[Unset, float] = UNSET
    remaining_vacation_days_current_year: Union[Unset, float] = UNSET
    sick_leave_month: Union[Unset, float] = UNSET
    sick_leave_hours: Union[Unset, float] = UNSET
    overtime: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        personnel_number = self.personnel_number

        company_personnel_number = self.company_personnel_number

        accounting_month = self.accounting_month

        month_of_recalculation = self.month_of_recalculation

        total_vacation_entitlement = self.total_vacation_entitlement

        vacation_days_taken = self.vacation_days_taken

        remaining_vacation_days_previous_year = self.remaining_vacation_days_previous_year

        remaining_vacation_days_current_year = self.remaining_vacation_days_current_year

        sick_leave_month = self.sick_leave_month

        sick_leave_hours = self.sick_leave_hours

        overtime = self.overtime


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
        if total_vacation_entitlement is not UNSET:
            field_dict["total_vacation_entitlement"] = total_vacation_entitlement
        if vacation_days_taken is not UNSET:
            field_dict["vacation_days_taken"] = vacation_days_taken
        if remaining_vacation_days_previous_year is not UNSET:
            field_dict["remaining_vacation_days_previous_year"] = remaining_vacation_days_previous_year
        if remaining_vacation_days_current_year is not UNSET:
            field_dict["remaining_vacation_days_current_year"] = remaining_vacation_days_current_year
        if sick_leave_month is not UNSET:
            field_dict["sick_leave_month"] = sick_leave_month
        if sick_leave_hours is not UNSET:
            field_dict["sick_leave_hours"] = sick_leave_hours
        if overtime is not UNSET:
            field_dict["overtime"] = overtime

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        personnel_number = d.pop("personnel_number", UNSET)

        company_personnel_number = d.pop("company_personnel_number", UNSET)

        accounting_month = d.pop("accounting_month", UNSET)

        month_of_recalculation = d.pop("month_of_recalculation", UNSET)

        total_vacation_entitlement = d.pop("total_vacation_entitlement", UNSET)

        vacation_days_taken = d.pop("vacation_days_taken", UNSET)

        remaining_vacation_days_previous_year = d.pop("remaining_vacation_days_previous_year", UNSET)

        remaining_vacation_days_current_year = d.pop("remaining_vacation_days_current_year", UNSET)

        sick_leave_month = d.pop("sick_leave_month", UNSET)

        sick_leave_hours = d.pop("sick_leave_hours", UNSET)

        overtime = d.pop("overtime", UNSET)

        absences = cls(
            personnel_number=personnel_number,
            company_personnel_number=company_personnel_number,
            accounting_month=accounting_month,
            month_of_recalculation=month_of_recalculation,
            total_vacation_entitlement=total_vacation_entitlement,
            vacation_days_taken=vacation_days_taken,
            remaining_vacation_days_previous_year=remaining_vacation_days_previous_year,
            remaining_vacation_days_current_year=remaining_vacation_days_current_year,
            sick_leave_month=sick_leave_month,
            sick_leave_hours=sick_leave_hours,
            overtime=overtime,
        )


        absences.additional_properties = d
        return absences

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
