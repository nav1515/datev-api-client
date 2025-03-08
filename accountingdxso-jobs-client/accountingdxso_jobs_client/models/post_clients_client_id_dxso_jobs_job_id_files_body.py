from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json

from ..types import UNSET, Unset

from ..types import File, FileJsonType
from ..types import UNSET, Unset
from io import BytesIO
from typing import Union






T = TypeVar("T", bound="PostClientsClientIdDxsoJobsJobIdFilesBody")



@_attrs_define
class PostClientsClientIdDxsoJobsJobIdFilesBody:
    """ 
        Attributes:
            files (Union[Unset, File]): Single file
     """

    files: Union[Unset, File] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        files: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_tuple()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict


    def to_multipart(self) -> dict[str, Any]:
        files: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_tuple()



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
        _files = d.pop("files", UNSET)
        files: Union[Unset, File]
        if isinstance(_files,  Unset):
            files = UNSET
        else:
            files = File(
             payload = BytesIO(_files)
        )




        post_clients_client_id_dxso_jobs_job_id_files_body = cls(
            files=files,
        )


        post_clients_client_id_dxso_jobs_job_id_files_body.additional_properties = d
        return post_clients_client_id_dxso_jobs_job_id_files_body

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
