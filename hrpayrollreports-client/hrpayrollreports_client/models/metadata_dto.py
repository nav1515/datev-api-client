from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="MetadataDto")



@_attrs_define
class MetadataDto:
    """ 
        Attributes:
            period (Union[Unset, str]):  Example: 2021-07-01.
            timestamp (Union[Unset, str]):  Example: 2021-07-01 15:04:11.
     """

    period: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        period = self.period

        timestamp = self.timestamp


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if period is not UNSET:
            field_dict["period"] = period
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        period = d.pop("period", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        metadata_dto = cls(
            period=period,
            timestamp=timestamp,
        )


        metadata_dto.additional_properties = d
        return metadata_dto

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
