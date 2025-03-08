from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.employees_document_dto import EmployeesDocumentDto





T = TypeVar("T", bound="EmployeeDocumentTypeDto")



@_attrs_define
class EmployeeDocumentTypeDto:
    """ 
        Attributes:
            document_type (Union[Unset, str]):  Example: LOBN.
            employees (Union[Unset, list['EmployeesDocumentDto']]):
     """

    document_type: Union[Unset, str] = UNSET
    employees: Union[Unset, list['EmployeesDocumentDto']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.employees_document_dto import EmployeesDocumentDto
        document_type = self.document_type

        employees: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.employees, Unset):
            employees = []
            for employees_item_data in self.employees:
                employees_item = employees_item_data.to_dict()
                employees.append(employees_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if employees is not UNSET:
            field_dict["employees"] = employees

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.employees_document_dto import EmployeesDocumentDto
        d = src_dict.copy()
        document_type = d.pop("document_type", UNSET)

        employees = []
        _employees = d.pop("employees", UNSET)
        for employees_item_data in (_employees or []):
            employees_item = EmployeesDocumentDto.from_dict(employees_item_data)



            employees.append(employees_item)


        employee_document_type_dto = cls(
            document_type=document_type,
            employees=employees,
        )


        employee_document_type_dto.additional_properties = d
        return employee_document_type_dto

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
