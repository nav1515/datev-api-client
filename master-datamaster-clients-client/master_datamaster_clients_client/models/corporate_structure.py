from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="CorporateStructure")



@_attrs_define
class CorporateStructure:
    """ Corporate structure of a master client. Consists of organization and establishment the master client is currently
    assigned to.

        Attributes:
            organization_name (Union[Unset, str]): The name of the organization. Example: Musterkanzlei.
            organization_number (Union[Unset, int]): The number of the organization. Example: 1.
            establishment_name (Union[Unset, str]): The name of the establishment. Example: Musterkanzlei - Hauptsitz.
            establishment_number (Union[Unset, int]): The number of the establishment. Example: 1.
            establishment_short_name (Union[Unset, str]): The short name of the establishment. Example: Hauptsitz.
     """

    organization_name: Union[Unset, str] = UNSET
    organization_number: Union[Unset, int] = UNSET
    establishment_name: Union[Unset, str] = UNSET
    establishment_number: Union[Unset, int] = UNSET
    establishment_short_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        organization_name = self.organization_name

        organization_number = self.organization_number

        establishment_name = self.establishment_name

        establishment_number = self.establishment_number

        establishment_short_name = self.establishment_short_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if organization_name is not UNSET:
            field_dict["organization_name"] = organization_name
        if organization_number is not UNSET:
            field_dict["organization_number"] = organization_number
        if establishment_name is not UNSET:
            field_dict["establishment_name"] = establishment_name
        if establishment_number is not UNSET:
            field_dict["establishment_number"] = establishment_number
        if establishment_short_name is not UNSET:
            field_dict["establishment_short_name"] = establishment_short_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        organization_name = d.pop("organization_name", UNSET)

        organization_number = d.pop("organization_number", UNSET)

        establishment_name = d.pop("establishment_name", UNSET)

        establishment_number = d.pop("establishment_number", UNSET)

        establishment_short_name = d.pop("establishment_short_name", UNSET)

        corporate_structure = cls(
            organization_name=organization_name,
            organization_number=organization_number,
            establishment_name=establishment_name,
            establishment_number=establishment_number,
            establishment_short_name=establishment_short_name,
        )


        corporate_structure.additional_properties = d
        return corporate_structure

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
