from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json

from ..types import UNSET, Unset

from ..types import File, FileJsonType
from ..types import UNSET, Unset
from io import BytesIO
from typing import Union






T = TypeVar("T", bound="UploadDocumentByConsultantClientNumberBody")



@_attrs_define
class UploadDocumentByConsultantClientNumberBody:
    """ 
        Attributes:
            file (Union[Unset, File]):
     """

    file: Union[Unset, File] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict


    def to_multipart(self) -> dict[str, Any]:
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()



        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] =  (None, str(prop).encode(), "text/plain")

        field_dict.update({
        })
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict


    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _file = d.pop("file", UNSET)
        file: Union[Unset, File]
        if isinstance(_file,  Unset):
            file = UNSET
        else:
            file = File(
             payload = BytesIO(_file)
        )




        upload_document_by_consultant_client_number_body = cls(
            file=file,
        )


        upload_document_by_consultant_client_number_body.additional_properties = d
        return upload_document_by_consultant_client_number_body

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
