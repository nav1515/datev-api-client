from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json

from ..types import UNSET, Unset

from ..types import File, FileJsonType
from ..types import UNSET, Unset
from io import BytesIO
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostDocumentsOutboxBody")



@_attrs_define
class PostDocumentsOutboxBody:
    """ 
        Attributes:
            files (Union[None, Unset, list[File]]): The files.
     """

    files: Union[None, Unset, list[File]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        files: Union[None, Unset, list[FileJsonType]]
        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            files = []
            for files_type_0_item_data in self.files:
                files_type_0_item = files_type_0_item_data.to_tuple()

                files.append(files_type_0_item)


        else:
            files = self.files


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict


    def to_multipart(self) -> dict[str, Any]:
        files: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.files, Unset):
            files = UNSET
        elif isinstance(self.files, list):
            _temp_files = []
            for files_type_0_item_data in self.files:
                files_type_0_item = files_type_0_item_data.to_tuple()

                _temp_files.append(files_type_0_item)
            files = (None, json.dumps(_temp_files).encode(), 'application/json')
        else:
            files =  (None, str(self.files).encode(), "text/plain")



        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] =  (None, str(prop).encode(), "text/plain")

        field_dict.update({
        })
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict


    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        def _parse_files(data: object) -> Union[None, Unset, list[File]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                files_type_0 = []
                _files_type_0 = data
                for files_type_0_item_data in (_files_type_0):
                    files_type_0_item = File(
                         payload = BytesIO(files_type_0_item_data)
                    )



                    files_type_0.append(files_type_0_item)

                return files_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[File]], data)

        files = _parse_files(d.pop("files", UNSET))


        post_documents_outbox_body = cls(
            files=files,
        )


        post_documents_outbox_body.additional_properties = d
        return post_documents_outbox_body

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
