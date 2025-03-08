from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="OrgInfoBusinessPartner")



@_attrs_define
class OrgInfoBusinessPartner:
    """ Information about a business partner in the current users context.

        Attributes:
            name (Union[Unset, str]): The name of the business partner. Example: Steuermeister Rechtsanwälte GmbH.
            number (Union[Unset, int]): The ID of the business partner. Example: 489345.
            is_home (Union[Unset, bool]): A flag indicating whether the current user belongs to this business partner or the
                business parnter is added as authorized business partner via RVO (MÜG). Example: True.
     """

    name: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    is_home: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        name = self.name

        number = self.number

        is_home = self.is_home


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if is_home is not UNSET:
            field_dict["is_home"] = is_home

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        is_home = d.pop("is_home", UNSET)

        org_info_business_partner = cls(
            name=name,
            number=number,
            is_home=is_home,
        )


        org_info_business_partner.additional_properties = d
        return org_info_business_partner

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
