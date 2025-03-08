from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_client_full_addressee_child_relationship_to_child import MasterClientFullAddresseeChildRelationshipToChild
from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="MasterClientFullAddresseeChild")



@_attrs_define
class MasterClientFullAddresseeChild:
    """ (Angaben zum Kind) Specific data for the child.

        Attributes:
            id (Union[Unset, UUID]): GUID of a relationship - internal identifier.
            display_name (Union[Unset, str]): Comprise a display name of the referenced addressee. Example: Mustermeier,
                Georg.
            natural_person_id (Union[Unset, UUID]): GUID of the referenced natural person addressee. Example:
                4715fa7c-3e81-4255-9a3a-df12c97ad443.
            relationship_to_child (Union[Unset, MasterClientFullAddresseeChildRelationshipToChild]): (Kindschaftsverhältnis)
                Type of relationship from the addressee to the child. The following values are possible (ADOPT=Adoptivkind,
                ENKEL=Im Haushalt aufgen. Enkelkind, LEIBL=Leibliches Kind, PFLEG=Pflegekind, STIEF=Im Haushalt aufgen.
                Stiefkind). Example: LEIBL.
     """

    id: Union[Unset, UUID] = UNSET
    display_name: Union[Unset, str] = UNSET
    natural_person_id: Union[Unset, UUID] = UNSET
    relationship_to_child: Union[Unset, MasterClientFullAddresseeChildRelationshipToChild] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        display_name = self.display_name

        natural_person_id: Union[Unset, str] = UNSET
        if not isinstance(self.natural_person_id, Unset):
            natural_person_id = str(self.natural_person_id)

        relationship_to_child: Union[Unset, str] = UNSET
        if not isinstance(self.relationship_to_child, Unset):
            relationship_to_child = self.relationship_to_child.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if natural_person_id is not UNSET:
            field_dict["natural_person_id"] = natural_person_id
        if relationship_to_child is not UNSET:
            field_dict["relationship_to_child"] = relationship_to_child

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




        display_name = d.pop("display_name", UNSET)

        _natural_person_id = d.pop("natural_person_id", UNSET)
        natural_person_id: Union[Unset, UUID]
        if isinstance(_natural_person_id,  Unset):
            natural_person_id = UNSET
        else:
            natural_person_id = UUID(_natural_person_id)




        _relationship_to_child = d.pop("relationship_to_child", UNSET)
        relationship_to_child: Union[Unset, MasterClientFullAddresseeChildRelationshipToChild]
        if isinstance(_relationship_to_child,  Unset):
            relationship_to_child = UNSET
        else:
            relationship_to_child = MasterClientFullAddresseeChildRelationshipToChild(_relationship_to_child)




        master_client_full_addressee_child = cls(
            id=id,
            display_name=display_name,
            natural_person_id=natural_person_id,
            relationship_to_child=relationship_to_child,
        )


        master_client_full_addressee_child.additional_properties = d
        return master_client_full_addressee_child

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
