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
            error (Union[Unset, str]): contains a DATEV-specific error code – optional
            request_id (Union[Unset, str]): contains a unique request ID; this might be used to find a protocol entry by
                DATEV – optional
            error_description (Union[Unset, str]): the technical name of the error (please note that the meaning may vary
                depending on the request!) – optional
            error_uri (Union[Unset, str]): URI for further information about the error – optional
     """

    error: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    error_description: Union[Unset, str] = UNSET
    error_uri: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        error = self.error

        request_id = self.request_id

        error_description = self.error_description

        error_uri = self.error_uri


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if error_uri is not UNSET:
            field_dict["error_uri"] = error_uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        request_id = d.pop("request_id", UNSET)

        error_description = d.pop("error_description", UNSET)

        error_uri = d.pop("error_uri", UNSET)

        error_message = cls(
            error=error,
            request_id=request_id,
            error_description=error_description,
            error_uri=error_uri,
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
