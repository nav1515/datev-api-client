from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json

from ..types import UNSET, Unset

from ..types import File, FileJsonType
from ..types import UNSET, Unset
from io import BytesIO
from typing import cast
from typing import Union






T = TypeVar("T", bound="PutClientsClientIdDocumentsStapledBody")



@_attrs_define
class PutClientsClientIdDocumentsStapledBody:
    """ 
        Attributes:
            files (Union[Unset, list[File]]): array of files
            metadata (Union[Unset, Any]):  Example: {'document_type': 'Rechnungseingang', 'note': 'This is an example
                note.', 'category': 'MySoftwareCompany', 'folder': 'Invoices', 'register': '2023/03'}.
     """

    files: Union[Unset, list[File]] = UNSET
    metadata: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        files: Union[Unset, list[FileJsonType]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_tuple()

                files.append(files_item)



        metadata = self.metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if files is not UNSET:
            field_dict["files"] = files
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict


    def to_multipart(self) -> dict[str, Any]:
        files: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.files, Unset):
            _temp_files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_tuple()

                _temp_files.append(files_item)
            files = (None, json.dumps(_temp_files).encode(), 'application/json')



        metadata = self.metadata if isinstance(self.metadata, Unset) else (None, str(self.metadata).encode(), "text/plain")



        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] =  (None, str(prop).encode(), "text/plain")

        field_dict.update({
        })
        if files is not UNSET:
            field_dict["files"] = files
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict


    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in (_files or []):
            files_item = File(
                 payload = BytesIO(files_item_data)
            )



            files.append(files_item)


        metadata = d.pop("metadata", UNSET)

        put_clients_client_id_documents_stapled_body = cls(
            files=files,
            metadata=metadata,
        )


        put_clients_client_id_documents_stapled_body.additional_properties = d
        return put_clients_client_id_documents_stapled_body

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
