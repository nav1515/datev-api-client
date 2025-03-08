from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.data_environment_organization_status import DataEnvironmentOrganizationStatus
from ..types import UNSET, Unset
from typing import cast
from typing import Union
from uuid import UUID

if TYPE_CHECKING:
  from ..models.data_environment_establishment import DataEnvironmentEstablishment





T = TypeVar("T", bound="DataEnvironmentOrganization")



@_attrs_define
class DataEnvironmentOrganization:
    """ Information about an organization.

        Attributes:
            id (Union[Unset, UUID]): Unique ID of the organization (stable technical identifier, also referred to as
                "ORGOID", short for "Organization Online Identifier").
            name (Union[Unset, str]): The name of the organization. Example: Musterkanzlei.
            number (Union[Unset, int]): The number of the organization. Example: 1.
            status (Union[Unset, DataEnvironmentOrganizationStatus]): Indicates whether the organization is used actively or
                not. Example: active.
            consultant_zmo_id (Union[Unset, UUID]): (Kanzleimandant) Master Client ID (also referred to as "ZMOID") of the
                consultant client assigned to this organization. Example: 3e6a361e-13b9-4123-971f-b1bc36db9cbb.
            establishments (Union[Unset, list['DataEnvironmentEstablishment']]):
     """

    id: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    status: Union[Unset, DataEnvironmentOrganizationStatus] = UNSET
    consultant_zmo_id: Union[Unset, UUID] = UNSET
    establishments: Union[Unset, list['DataEnvironmentEstablishment']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.data_environment_establishment import DataEnvironmentEstablishment
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        number = self.number

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        consultant_zmo_id: Union[Unset, str] = UNSET
        if not isinstance(self.consultant_zmo_id, Unset):
            consultant_zmo_id = str(self.consultant_zmo_id)

        establishments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.establishments, Unset):
            establishments = []
            for establishments_item_data in self.establishments:
                establishments_item = establishments_item_data.to_dict()
                establishments.append(establishments_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if status is not UNSET:
            field_dict["status"] = status
        if consultant_zmo_id is not UNSET:
            field_dict["consultant_zmo_id"] = consultant_zmo_id
        if establishments is not UNSET:
            field_dict["establishments"] = establishments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_environment_establishment import DataEnvironmentEstablishment
        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DataEnvironmentOrganizationStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = DataEnvironmentOrganizationStatus(_status)




        _consultant_zmo_id = d.pop("consultant_zmo_id", UNSET)
        consultant_zmo_id: Union[Unset, UUID]
        if isinstance(_consultant_zmo_id,  Unset):
            consultant_zmo_id = UNSET
        else:
            consultant_zmo_id = UUID(_consultant_zmo_id)




        establishments = []
        _establishments = d.pop("establishments", UNSET)
        for establishments_item_data in (_establishments or []):
            establishments_item = DataEnvironmentEstablishment.from_dict(establishments_item_data)



            establishments.append(establishments_item)


        data_environment_organization = cls(
            id=id,
            name=name,
            number=number,
            status=status,
            consultant_zmo_id=consultant_zmo_id,
            establishments=establishments,
        )


        data_environment_organization.additional_properties = d
        return data_environment_organization

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
