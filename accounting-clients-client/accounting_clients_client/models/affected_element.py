from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="AffectedElement")



@_attrs_define
class AffectedElement:
    """ 
        Attributes:
            name (Union[Unset, str]): Name of the affected element. Example: skip.
            reason (Union[Unset, str]): Reason for the error. Example: Must be a positive integer.
     """

    name: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        name = self.name

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        reason = d.pop("reason", UNSET)

        affected_element = cls(
            name=name,
            reason=reason,
        )


        affected_element.additional_properties = d
        return affected_element

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
