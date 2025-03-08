from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ErrorMessage")



@_attrs_define
class ErrorMessage:
    """ 
        Attributes:
            error (Union[Unset, str]): Error code. Example: #DCO02000.
            error_description (Union[Unset, str]): Error description. Example: restapi.FileEmpty.
            error_uri (Union[Unset, str]): URI to further information. Example:
                https://apps.datev.de/knowledge/help/search?q=DCO02000.
            request_id (Union[Unset, str]): Protocol entry at DATEV. Example: 0a13eff2-44a9-4de6-90f0-1198241e7c22.
     """

    error: Union[Unset, str] = UNSET
    error_description: Union[Unset, str] = UNSET
    error_uri: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        error = self.error

        error_description = self.error_description

        error_uri = self.error_uri

        request_id = self.request_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if error_uri is not UNSET:
            field_dict["error_uri"] = error_uri
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        error_description = d.pop("error_description", UNSET)

        error_uri = d.pop("error_uri", UNSET)

        request_id = d.pop("request_id", UNSET)

        error_message = cls(
            error=error,
            error_description=error_description,
            error_uri=error_uri,
            request_id=request_id,
        )


        error_message.additional_properties = d
        return error_message

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
