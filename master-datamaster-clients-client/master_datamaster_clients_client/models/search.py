from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union
from uuid import UUID

if TYPE_CHECKING:
  from ..models.id_and_etag import IdAndEtag





T = TypeVar("T", bound="Search")



@_attrs_define
class Search:
    """ The extended search parameters.

        Attributes:
            ids (Union[Unset, list[UUID]]): A list of Master Client IDs (also referred to as "ZMOID") to search for. With
                this parameter, it is possible to selectively request the data of clients. Maximum length is 100. Example:
                ['76ace1ef-0c0a-446d-a35f-c8909e59708e', '6765b277-34ea-42ec-85e9-17f6cf4d7744', '7fed28dc-1b0b-4424-91ba-
                ea97aeb5efdf'].
            ids_and_updated (Union[Unset, list['IdAndEtag']]): A list of Master Client IDs (also referred to as "ZMOID") and
                corresponding ETag values to search for. Only Master Clients with differing ETag will be returned. With this
                parameter, it is possible to selectively request the data of clients that have changed. Maximum length is 100.
     """

    ids: Union[Unset, list[UUID]] = UNSET
    ids_and_updated: Union[Unset, list['IdAndEtag']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.id_and_etag import IdAndEtag
        ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = []
            for ids_item_data in self.ids:
                ids_item = str(ids_item_data)
                ids.append(ids_item)



        ids_and_updated: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ids_and_updated, Unset):
            ids_and_updated = []
            for ids_and_updated_item_data in self.ids_and_updated:
                ids_and_updated_item = ids_and_updated_item_data.to_dict()
                ids_and_updated.append(ids_and_updated_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ids is not UNSET:
            field_dict["ids"] = ids
        if ids_and_updated is not UNSET:
            field_dict["ids_and_updated"] = ids_and_updated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.id_and_etag import IdAndEtag
        d = src_dict.copy()
        ids = []
        _ids = d.pop("ids", UNSET)
        for ids_item_data in (_ids or []):
            ids_item = UUID(ids_item_data)



            ids.append(ids_item)


        ids_and_updated = []
        _ids_and_updated = d.pop("ids_and_updated", UNSET)
        for ids_and_updated_item_data in (_ids_and_updated or []):
            ids_and_updated_item = IdAndEtag.from_dict(ids_and_updated_item_data)



            ids_and_updated.append(ids_and_updated_item)


        search = cls(
            ids=ids,
            ids_and_updated=ids_and_updated,
        )


        search.additional_properties = d
        return search

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
