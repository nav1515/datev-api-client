from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.metadata_dto import MetadataDto





T = TypeVar("T", bound="ClientDocumentTypeDto")



@_attrs_define
class ClientDocumentTypeDto:
    """ 
        Attributes:
            document_type (Union[Unset, str]):  Example: LOBN.
            document (Union[Unset, list['MetadataDto']]):
     """

    document_type: Union[Unset, str] = UNSET
    document: Union[Unset, list['MetadataDto']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.metadata_dto import MetadataDto
        document_type = self.document_type

        document: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.document, Unset):
            document = []
            for document_item_data in self.document:
                document_item = document_item_data.to_dict()
                document.append(document_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if document is not UNSET:
            field_dict["document"] = document

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.metadata_dto import MetadataDto
        d = src_dict.copy()
        document_type = d.pop("document_type", UNSET)

        document = []
        _document = d.pop("document", UNSET)
        for document_item_data in (_document or []):
            document_item = MetadataDto.from_dict(document_item_data)



            document.append(document_item)


        client_document_type_dto = cls(
            document_type=document_type,
            document=document,
        )


        client_document_type_dto.additional_properties = d
        return client_document_type_dto

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
