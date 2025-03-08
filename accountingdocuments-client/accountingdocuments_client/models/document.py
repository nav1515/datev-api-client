from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.file_info import FileInfo





T = TypeVar("T", bound="Document")



@_attrs_define
class Document:
    """ 
        Attributes:
            id (Union[Unset, str]): ID of document
            files (Union[Unset, list['FileInfo']]): file information on the document (read-only)
            document_type (Union[Unset, str]): document type of a document
            note (Union[Unset, str]): note pertaining to the document for the tax consultant
     """

    id: Union[Unset, str] = UNSET
    files: Union[Unset, list['FileInfo']] = UNSET
    document_type: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.file_info import FileInfo
        id = self.id

        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



        document_type = self.document_type

        note = self.note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if files is not UNSET:
            field_dict["files"] = files
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.file_info import FileInfo
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in (_files or []):
            files_item = FileInfo.from_dict(files_item_data)



            files.append(files_item)


        document_type = d.pop("document_type", UNSET)

        note = d.pop("note", UNSET)

        document = cls(
            id=id,
            files=files,
            document_type=document_type,
            note=note,
        )


        document.additional_properties = d
        return document

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
