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
            error (Union[Unset, str]): error Example: #DCO02299.
            error_description (Union[Unset, str]): error_description Example: restapi.ExampleErrorDescription.
            error_uri (Union[Unset, str]): error_uri Example: http://www.datev.de/dnlexos/mobile/webApp.aspx?sq=DCO02299.
            request_id (Union[Unset, str]): request_id Example: 0a13eff2-44a9-4de6-90f0-1198241e7c22.
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
            field_dict["errorDescription"] = error_description
        if error_uri is not UNSET:
            field_dict["errorUri"] = error_uri
        if request_id is not UNSET:
            field_dict["requestId"] = request_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        error_uri = d.pop("errorUri", UNSET)

        request_id = d.pop("requestId", UNSET)

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
