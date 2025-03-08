from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="FileInfo")



@_attrs_define
class FileInfo:
    """ 
        Attributes:
            id (Union[Unset, str]): ID of the file of the document
            name (Union[Unset, str]): name of the file of the document
            size (Union[Unset, int]): file size in bytes
            upload_date (Union[Unset, datetime.datetime]): import time  in accordance with ISO8601 „YYYY-MM-
                DDThh:mm:ss±hh:mm“
            media_type (Union[Unset, str]): Internet media type of the file
     """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    upload_date: Union[Unset, datetime.datetime] = UNSET
    media_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        size = self.size

        upload_date: Union[Unset, str] = UNSET
        if not isinstance(self.upload_date, Unset):
            upload_date = self.upload_date.isoformat()

        media_type = self.media_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if upload_date is not UNSET:
            field_dict["upload_date"] = upload_date
        if media_type is not UNSET:
            field_dict["media_type"] = media_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        _upload_date = d.pop("upload_date", UNSET)
        upload_date: Union[Unset, datetime.datetime]
        if isinstance(_upload_date,  Unset):
            upload_date = UNSET
        else:
            upload_date = isoparse(_upload_date)




        media_type = d.pop("media_type", UNSET)

        file_info = cls(
            id=id,
            name=name,
            size=size,
            upload_date=upload_date,
            media_type=media_type,
        )


        file_info.additional_properties = d
        return file_info

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
