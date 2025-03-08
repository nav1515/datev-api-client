from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union
from uuid import UUID

if TYPE_CHECKING:
  from ..models.master_client_full_address_reference import MasterClientFullAddressReference





T = TypeVar("T", bound="MasterClientFullCorrespondenceRecipient")



@_attrs_define
class MasterClientFullCorrespondenceRecipient:
    """ (Angaben zum Korrespondenzempfänger) Correspondence recipient specific data.

        Attributes:
            id (Union[Unset, UUID]): GUID of a relationship - internal identifier.
            display_name (Union[Unset, str]): Comprise a display name of the referenced addressee. Example: Mustermeier,
                Georg.
            addressee_id (Union[Unset, UUID]): GUID of the referenced addressee. Only either addresseeId or marriageId is
                filled.
            marriage_id (Union[Unset, UUID]): GUID of the referenced marriage. Only either addresseeId or marriageId is
                filled. Example: 84322f6f-77f6-4b91-ac06-c05a6999c41e.
            correspondence_address (Union[Unset, MasterClientFullAddressReference]): (Adresse) Address specific data.
     """

    id: Union[Unset, UUID] = UNSET
    display_name: Union[Unset, str] = UNSET
    addressee_id: Union[Unset, UUID] = UNSET
    marriage_id: Union[Unset, UUID] = UNSET
    correspondence_address: Union[Unset, 'MasterClientFullAddressReference'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.master_client_full_address_reference import MasterClientFullAddressReference
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        display_name = self.display_name

        addressee_id: Union[Unset, str] = UNSET
        if not isinstance(self.addressee_id, Unset):
            addressee_id = str(self.addressee_id)

        marriage_id: Union[Unset, str] = UNSET
        if not isinstance(self.marriage_id, Unset):
            marriage_id = str(self.marriage_id)

        correspondence_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.correspondence_address, Unset):
            correspondence_address = self.correspondence_address.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if addressee_id is not UNSET:
            field_dict["addressee_id"] = addressee_id
        if marriage_id is not UNSET:
            field_dict["marriage_id"] = marriage_id
        if correspondence_address is not UNSET:
            field_dict["correspondence_address"] = correspondence_address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.master_client_full_address_reference import MasterClientFullAddressReference
        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        display_name = d.pop("display_name", UNSET)

        _addressee_id = d.pop("addressee_id", UNSET)
        addressee_id: Union[Unset, UUID]
        if isinstance(_addressee_id,  Unset):
            addressee_id = UNSET
        else:
            addressee_id = UUID(_addressee_id)




        _marriage_id = d.pop("marriage_id", UNSET)
        marriage_id: Union[Unset, UUID]
        if isinstance(_marriage_id,  Unset):
            marriage_id = UNSET
        else:
            marriage_id = UUID(_marriage_id)




        _correspondence_address = d.pop("correspondence_address", UNSET)
        correspondence_address: Union[Unset, MasterClientFullAddressReference]
        if isinstance(_correspondence_address,  Unset):
            correspondence_address = UNSET
        else:
            correspondence_address = MasterClientFullAddressReference.from_dict(_correspondence_address)




        master_client_full_correspondence_recipient = cls(
            id=id,
            display_name=display_name,
            addressee_id=addressee_id,
            marriage_id=marriage_id,
            correspondence_address=correspondence_address,
        )


        master_client_full_correspondence_recipient.additional_properties = d
        return master_client_full_correspondence_recipient

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
