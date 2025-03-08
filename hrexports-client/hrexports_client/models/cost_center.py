from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="CostCenter")



@_attrs_define
class CostCenter:
    """ 
        Attributes:
            cost_center_id (Union[Unset, str]): Cost center number (Kostenstellennummer) Example: 3550.
            cost_center_name (Union[Unset, str]): Cost center name (Kostenstellenbezeichnung) Example: Verkauf.
     """

    cost_center_id: Union[Unset, str] = UNSET
    cost_center_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        cost_center_id = self.cost_center_id

        cost_center_name = self.cost_center_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cost_center_id is not UNSET:
            field_dict["cost_center_id"] = cost_center_id
        if cost_center_name is not UNSET:
            field_dict["cost_center_name"] = cost_center_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_center_id = d.pop("cost_center_id", UNSET)

        cost_center_name = d.pop("cost_center_name", UNSET)

        cost_center = cls(
            cost_center_id=cost_center_id,
            cost_center_name=cost_center_name,
        )


        cost_center.additional_properties = d
        return cost_center

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
