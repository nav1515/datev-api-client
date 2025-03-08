from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union
from uuid import UUID

if TYPE_CHECKING:
  from ..models.master_client_full_container import MasterClientFullContainer





T = TypeVar("T", bound="MasterClientFull")



@_attrs_define
class MasterClientFull:
    """ The master client entity is most commonly used to represent clients (customers) of DATEV members, but its use is not
    restricted to that business role.

    Each master client entity is contained in exactly one data environment. Each data environment is owned and
    controlled by exactly one organization (such as a tax consultant or a lawyer that is a DATEV member).

        Attributes:
            id (UUID): Master Client ID (stable technical identifier, also referred to as "ZMOID", short for "Zentraler
                Mandant Online Identifier"). This is the value to be used as the master client ID parameter when accessing a
                single master client through this API. Example: 76ace1ef-0c0a-446d-a35f-c8909e59708e.
            data_environment_number (int): (Datenumgebungsnummer) The number of the data environment to which the master
                client belongs. The data environment number is a stable, unique identifier for the data environment. Example:
                876870.
            revision (Union[Unset, str]): A number indicating the revision of the master client. For internal use. Example:
                1.
            etag (Union[Unset, str]): An opaque value assigned by the origin server that can be used to determine whether
                two representations of a master client are the same. All subresources will be included in the calculation of the
                ETag value regardless of them being embedded in the master client or not. Example: 30b0b391.
            container (Union[Unset, MasterClientFullContainer]): The master client container contains the data of the master
                client.
     """

    id: UUID
    data_environment_number: int
    revision: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    container: Union[Unset, 'MasterClientFullContainer'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.master_client_full_container import MasterClientFullContainer
        id = str(self.id)

        data_environment_number = self.data_environment_number

        revision = self.revision

        etag = self.etag

        container: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.container, Unset):
            container = self.container.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "data_environment_number": data_environment_number,
        })
        if revision is not UNSET:
            field_dict["revision"] = revision
        if etag is not UNSET:
            field_dict["etag"] = etag
        if container is not UNSET:
            field_dict["container"] = container

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.master_client_full_container import MasterClientFullContainer
        d = src_dict.copy()
        id = UUID(d.pop("id"))




        data_environment_number = d.pop("data_environment_number")

        revision = d.pop("revision", UNSET)

        etag = d.pop("etag", UNSET)

        _container = d.pop("container", UNSET)
        container: Union[Unset, MasterClientFullContainer]
        if isinstance(_container,  Unset):
            container = UNSET
        else:
            container = MasterClientFullContainer.from_dict(_container)




        master_client_full = cls(
            id=id,
            data_environment_number=data_environment_number,
            revision=revision,
            etag=etag,
            container=container,
        )


        master_client_full.additional_properties = d
        return master_client_full

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
