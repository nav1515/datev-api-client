from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="MasterClientFullHistoricalValueString")



@_attrs_define
class MasterClientFullHistoricalValueString:
    """ 
        Attributes:
            value (Union[Unset, str]): Value that was valid from the point in time given by field 'validFrom'
            valid_from (Union[Unset, datetime.date]): Point in time from when the value was valid Example: 2020-12-20.
     """

    value: Union[Unset, str] = UNSET
    valid_from: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        value = self.value

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if value is not UNSET:
            field_dict["value"] = value
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value", UNSET)

        _valid_from = d.pop("valid_from", UNSET)
        valid_from: Union[Unset, datetime.date]
        if isinstance(_valid_from,  Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from).date()




        master_client_full_historical_value_string = cls(
            value=value,
            valid_from=valid_from,
        )


        master_client_full_historical_value_string.additional_properties = d
        return master_client_full_historical_value_string

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
