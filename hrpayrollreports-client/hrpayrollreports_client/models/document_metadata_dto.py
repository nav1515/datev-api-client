from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.employee_document_type_dto import EmployeeDocumentTypeDto
  from ..models.client_document_type_dto import ClientDocumentTypeDto





T = TypeVar("T", bound="DocumentMetadataDto")



@_attrs_define
class DocumentMetadataDto:
    """ 
        Attributes:
            employee_documents (Union[Unset, list['EmployeeDocumentTypeDto']]):
            client_documents (Union[Unset, list['ClientDocumentTypeDto']]):
     """

    employee_documents: Union[Unset, list['EmployeeDocumentTypeDto']] = UNSET
    client_documents: Union[Unset, list['ClientDocumentTypeDto']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.employee_document_type_dto import EmployeeDocumentTypeDto
        from ..models.client_document_type_dto import ClientDocumentTypeDto
        employee_documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.employee_documents, Unset):
            employee_documents = []
            for employee_documents_item_data in self.employee_documents:
                employee_documents_item = employee_documents_item_data.to_dict()
                employee_documents.append(employee_documents_item)



        client_documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.client_documents, Unset):
            client_documents = []
            for client_documents_item_data in self.client_documents:
                client_documents_item = client_documents_item_data.to_dict()
                client_documents.append(client_documents_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if employee_documents is not UNSET:
            field_dict["employee_documents"] = employee_documents
        if client_documents is not UNSET:
            field_dict["client_documents"] = client_documents

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.employee_document_type_dto import EmployeeDocumentTypeDto
        from ..models.client_document_type_dto import ClientDocumentTypeDto
        d = src_dict.copy()
        employee_documents = []
        _employee_documents = d.pop("employee_documents", UNSET)
        for employee_documents_item_data in (_employee_documents or []):
            employee_documents_item = EmployeeDocumentTypeDto.from_dict(employee_documents_item_data)



            employee_documents.append(employee_documents_item)


        client_documents = []
        _client_documents = d.pop("client_documents", UNSET)
        for client_documents_item_data in (_client_documents or []):
            client_documents_item = ClientDocumentTypeDto.from_dict(client_documents_item_data)



            client_documents.append(client_documents_item)


        document_metadata_dto = cls(
            employee_documents=employee_documents,
            client_documents=client_documents,
        )


        document_metadata_dto.additional_properties = d
        return document_metadata_dto

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
