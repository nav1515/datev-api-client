from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.org_info_data_environment_address_country import OrgInfoDataEnvironmentAddressCountry
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="OrgInfoDataEnvironment")



@_attrs_define
class OrgInfoDataEnvironment:
    """ Information about a data environment.

        Attributes:
            label (Union[Unset, str]): The label of the data environment. Example: Basisdaten online.
            number (Union[Unset, int]): The number of the data environment. Example: 977552.
            consultant_number (Union[Unset, int]): The consultant number associated with the data environment. Example:
                29011.
            address_country (Union[Unset, OrgInfoDataEnvironmentAddressCountry]): The country code which may be used as
                defaults when a new master client is created. Example: DE.
            client_number_maximum_number_of_digits (Union[Unset, int]): The maximum number of allowed digits for the client
                number. This constraint is only checked when a new master client is created. Example: 5.
            client_number_start (Union[Unset, int]): The starting client number which is used to determine the next unused
                client number. Example: 10000.
     """

    label: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    consultant_number: Union[Unset, int] = UNSET
    address_country: Union[Unset, OrgInfoDataEnvironmentAddressCountry] = UNSET
    client_number_maximum_number_of_digits: Union[Unset, int] = UNSET
    client_number_start: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        label = self.label

        number = self.number

        consultant_number = self.consultant_number

        address_country: Union[Unset, str] = UNSET
        if not isinstance(self.address_country, Unset):
            address_country = self.address_country.value


        client_number_maximum_number_of_digits = self.client_number_maximum_number_of_digits

        client_number_start = self.client_number_start


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if label is not UNSET:
            field_dict["label"] = label
        if number is not UNSET:
            field_dict["number"] = number
        if consultant_number is not UNSET:
            field_dict["consultant_number"] = consultant_number
        if address_country is not UNSET:
            field_dict["address_country"] = address_country
        if client_number_maximum_number_of_digits is not UNSET:
            field_dict["client_number_maximum_number_of_digits"] = client_number_maximum_number_of_digits
        if client_number_start is not UNSET:
            field_dict["client_number_start"] = client_number_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label", UNSET)

        number = d.pop("number", UNSET)

        consultant_number = d.pop("consultant_number", UNSET)

        _address_country = d.pop("address_country", UNSET)
        address_country: Union[Unset, OrgInfoDataEnvironmentAddressCountry]
        if isinstance(_address_country,  Unset):
            address_country = UNSET
        else:
            address_country = OrgInfoDataEnvironmentAddressCountry(_address_country)




        client_number_maximum_number_of_digits = d.pop("client_number_maximum_number_of_digits", UNSET)

        client_number_start = d.pop("client_number_start", UNSET)

        org_info_data_environment = cls(
            label=label,
            number=number,
            consultant_number=consultant_number,
            address_country=address_country,
            client_number_maximum_number_of_digits=client_number_maximum_number_of_digits,
            client_number_start=client_number_start,
        )


        org_info_data_environment.additional_properties = d
        return org_info_data_environment

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
