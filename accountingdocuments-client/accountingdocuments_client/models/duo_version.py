from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="DuoVersion")



@_attrs_define
class DuoVersion:
    """ 
        Attributes:
            allowed_file_extensions (Union[Unset, str]): list of file extensions for single-file upload
            allowed_staple_file_extensions (Union[Unset, str]): list of file extensions for single-file upload
            staple_logic (Union[Unset, str]): logic of stapled upload
     """

    allowed_file_extensions: Union[Unset, str] = UNSET
    allowed_staple_file_extensions: Union[Unset, str] = UNSET
    staple_logic: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        allowed_file_extensions = self.allowed_file_extensions

        allowed_staple_file_extensions = self.allowed_staple_file_extensions

        staple_logic = self.staple_logic


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed_file_extensions is not UNSET:
            field_dict["allowed_file_extensions"] = allowed_file_extensions
        if allowed_staple_file_extensions is not UNSET:
            field_dict["allowed_staple_file_extensions"] = allowed_staple_file_extensions
        if staple_logic is not UNSET:
            field_dict["staple_logic"] = staple_logic

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_file_extensions = d.pop("allowed_file_extensions", UNSET)

        allowed_staple_file_extensions = d.pop("allowed_staple_file_extensions", UNSET)

        staple_logic = d.pop("staple_logic", UNSET)

        duo_version = cls(
            allowed_file_extensions=allowed_file_extensions,
            allowed_staple_file_extensions=allowed_staple_file_extensions,
            staple_logic=staple_logic,
        )


        duo_version.additional_properties = d
        return duo_version

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
