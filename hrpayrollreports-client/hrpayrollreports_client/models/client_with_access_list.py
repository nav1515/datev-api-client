from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.document_types import DocumentTypes





T = TypeVar("T", bound="ClientWithAccessList")



@_attrs_define
class ClientWithAccessList:
    """ 
        Attributes:
            client_id (Union[Unset, str]):  Example: 123456-123.
            consultant_number (Union[Unset, int]):  Example: 123456.
            client_number (Union[Unset, int]):  Example: 123.
            document_types (Union[Unset, DocumentTypes]):
     """

    client_id: Union[Unset, str] = UNSET
    consultant_number: Union[Unset, int] = UNSET
    client_number: Union[Unset, int] = UNSET
    document_types: Union[Unset, 'DocumentTypes'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.document_types import DocumentTypes
        client_id = self.client_id

        consultant_number = self.consultant_number

        client_number = self.client_number

        document_types: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_types, Unset):
            document_types = self.document_types.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if consultant_number is not UNSET:
            field_dict["consultant_number"] = consultant_number
        if client_number is not UNSET:
            field_dict["client_number"] = client_number
        if document_types is not UNSET:
            field_dict["document_types"] = document_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.document_types import DocumentTypes
        d = src_dict.copy()
        client_id = d.pop("client_id", UNSET)

        consultant_number = d.pop("consultant_number", UNSET)

        client_number = d.pop("client_number", UNSET)

        _document_types = d.pop("document_types", UNSET)
        document_types: Union[Unset, DocumentTypes]
        if isinstance(_document_types,  Unset):
            document_types = UNSET
        else:
            document_types = DocumentTypes.from_dict(_document_types)




        client_with_access_list = cls(
            client_id=client_id,
            consultant_number=consultant_number,
            client_number=client_number,
            document_types=document_types,
        )


        client_with_access_list.additional_properties = d
        return client_with_access_list

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
