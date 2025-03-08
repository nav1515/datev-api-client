from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="EmployeeAddress")



@_attrs_define
class EmployeeAddress:
    """ 
        Attributes:
            street (Union[Unset, str]): Street name Example: West Street.
            house_number (Union[Unset, str]): House number Example: 20.
            country (Union[Unset, str]): Country code Example: DE.
            zip_code (Union[Unset, str]): ZIP/Postal code Example: 90900.
            city (Union[Unset, str]): City name Example: München.
     """

    street: Union[Unset, str] = UNSET
    house_number: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        street = self.street

        house_number = self.house_number

        country = self.country

        zip_code = self.zip_code

        city = self.city


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if street is not UNSET:
            field_dict["street"] = street
        if house_number is not UNSET:
            field_dict["house_number"] = house_number
        if country is not UNSET:
            field_dict["country"] = country
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        street = d.pop("street", UNSET)

        house_number = d.pop("house_number", UNSET)

        country = d.pop("country", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        city = d.pop("city", UNSET)

        employee_address = cls(
            street=street,
            house_number=house_number,
            country=country,
            zip_code=zip_code,
            city=city,
        )


        employee_address.additional_properties = d
        return employee_address

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
