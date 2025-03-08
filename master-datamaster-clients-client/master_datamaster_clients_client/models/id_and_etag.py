from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="IdAndEtag")



@_attrs_define
class IdAndEtag:
    """ A tuple of Master Client ID together with an ETag value of the corresponding Master Client.

        Attributes:
            id (UUID): Master Client ID (stable technical identifier, also referred to as "ZMOID", short for "Zentraler
                Mandant Online Identifier"). This is the value to be used as the master client ID parameter when accessing a
                single master client through this API. Example: 76ace1ef-0c0a-446d-a35f-c8909e59708e.
            etag (Union[Unset, str]): An opaque value assigned by the origin server that can be used to determine whether
                two representations of a master client are the same. Example: 30b0b391.
     """

    id: UUID
    etag: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        etag = self.etag


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
        })
        if etag is not UNSET:
            field_dict["etag"] = etag

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = UUID(d.pop("id"))




        etag = d.pop("etag", UNSET)

        id_and_etag = cls(
            id=id,
            etag=etag,
        )


        id_and_etag.additional_properties = d
        return id_and_etag

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
