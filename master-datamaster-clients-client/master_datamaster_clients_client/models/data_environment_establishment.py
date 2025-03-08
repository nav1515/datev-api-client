from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.data_environment_establishment_status import DataEnvironmentEstablishmentStatus
from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="DataEnvironmentEstablishment")



@_attrs_define
class DataEnvironmentEstablishment:
    """ Information about an establishment.

        Attributes:
            id (Union[Unset, UUID]): Unique ID of the establishment (stable technical identifier, also referred to as
                "ESTOID", short for "Establishment Online Identifier").
            name (Union[Unset, str]): The name of the establishment. Example: Musterkanzlei - Hauptsitz.
            short_name (Union[Unset, str]): The short name of the establishment. Example: Hauptsitz.
            number (Union[Unset, int]): The number of the establishment. Example: 1.
            status (Union[Unset, DataEnvironmentEstablishmentStatus]): Indicates whether the establishment is used actively
                or not. Example: active.
            consultant_zmo_id (Union[Unset, UUID]): (Kanzleimandant) Master Client ID (also referred to as "ZMOID") of the
                consultant client assigned to this establishment. Example: 3e6a361e-13b9-4123-971f-b1bc36db9cbb.
     """

    id: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    status: Union[Unset, DataEnvironmentEstablishmentStatus] = UNSET
    consultant_zmo_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        short_name = self.short_name

        number = self.number

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        consultant_zmo_id: Union[Unset, str] = UNSET
        if not isinstance(self.consultant_zmo_id, Unset):
            consultant_zmo_id = str(self.consultant_zmo_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["short_name"] = short_name
        if number is not UNSET:
            field_dict["number"] = number
        if status is not UNSET:
            field_dict["status"] = status
        if consultant_zmo_id is not UNSET:
            field_dict["consultant_zmo_id"] = consultant_zmo_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        name = d.pop("name", UNSET)

        short_name = d.pop("short_name", UNSET)

        number = d.pop("number", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DataEnvironmentEstablishmentStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = DataEnvironmentEstablishmentStatus(_status)




        _consultant_zmo_id = d.pop("consultant_zmo_id", UNSET)
        consultant_zmo_id: Union[Unset, UUID]
        if isinstance(_consultant_zmo_id,  Unset):
            consultant_zmo_id = UNSET
        else:
            consultant_zmo_id = UUID(_consultant_zmo_id)




        data_environment_establishment = cls(
            id=id,
            name=name,
            short_name=short_name,
            number=number,
            status=status,
            consultant_zmo_id=consultant_zmo_id,
        )


        data_environment_establishment.additional_properties = d
        return data_environment_establishment

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
