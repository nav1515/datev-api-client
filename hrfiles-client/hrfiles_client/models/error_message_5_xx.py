from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="ErrorMessage5Xx")



@_attrs_define
class ErrorMessage5Xx:
    """ 
        Attributes:
            error_description (Union[Unset, str]): Error 5xx description. Example: restapi.InternalServerError.
            request_id (Union[Unset, str]): Protocol entry at DATEV. Example: 0a13eff2-44a9-4de6-90f0-1198241e7c22.
     """

    error_description: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        error_description = self.error_description

        request_id = self.request_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        error_description = d.pop("error_description", UNSET)

        request_id = d.pop("request_id", UNSET)

        error_message_5_xx = cls(
            error_description=error_description,
            request_id=request_id,
        )


        error_message_5_xx.additional_properties = d
        return error_message_5_xx

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
