from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="EmployeeIds")



@_attrs_define
class EmployeeIds:
    """ 
        Attributes:
            personnel_number (Union[Unset, int]): Employee's personnel number in the payroll system Example: 10.
            company_personnel_number (Union[Unset, str]): Company personnel number (Betriebliche Personalnummer) Example:
                123a.
     """

    personnel_number: Union[Unset, int] = UNSET
    company_personnel_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        personnel_number = self.personnel_number

        company_personnel_number = self.company_personnel_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if personnel_number is not UNSET:
            field_dict["personnel_number"] = personnel_number
        if company_personnel_number is not UNSET:
            field_dict["company_personnel_number"] = company_personnel_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        personnel_number = d.pop("personnel_number", UNSET)

        company_personnel_number = d.pop("company_personnel_number", UNSET)

        employee_ids = cls(
            personnel_number=personnel_number,
            company_personnel_number=company_personnel_number,
        )


        employee_ids.additional_properties = d
        return employee_ids

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
