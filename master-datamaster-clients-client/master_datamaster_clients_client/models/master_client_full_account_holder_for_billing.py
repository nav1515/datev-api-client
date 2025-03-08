from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union
from uuid import UUID

if TYPE_CHECKING:
  from ..models.master_client_full_account_holder_for_billing_bank_account_reference import MasterClientFullAccountHolderForBillingBankAccountReference





T = TypeVar("T", bound="MasterClientFullAccountHolderForBilling")



@_attrs_define
class MasterClientFullAccountHolderForBilling:
    """ (Angaben zum Kontoinhaber für Rechnungsschreibung) Specific data for the account holder for billing.

        Attributes:
            id (Union[Unset, UUID]): GUID of a relationship - internal identifier.
            display_name (Union[Unset, str]): Comprise a display name of the referenced addressee. Example: Mustermeier,
                Georg.
            addressee_id (Union[Unset, UUID]): GUID of the referenced addressee. Only either addresseeId or marriageId is
                filled.
            marriage_id (Union[Unset, UUID]): GUID of the referenced marriage. Only either addresseeId or marriageId is
                filled. Example: 84322f6f-77f6-4b91-ac06-c05a6999c41e.
            bank_account_for_billing (Union[Unset, MasterClientFullAccountHolderForBillingBankAccountReference]):
                (Bankverbindung) Reference to the bank account.
     """

    id: Union[Unset, UUID] = UNSET
    display_name: Union[Unset, str] = UNSET
    addressee_id: Union[Unset, UUID] = UNSET
    marriage_id: Union[Unset, UUID] = UNSET
    bank_account_for_billing: Union[Unset, 'MasterClientFullAccountHolderForBillingBankAccountReference'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.master_client_full_account_holder_for_billing_bank_account_reference import MasterClientFullAccountHolderForBillingBankAccountReference
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

        bank_account_for_billing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bank_account_for_billing, Unset):
            bank_account_for_billing = self.bank_account_for_billing.to_dict()


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
        if bank_account_for_billing is not UNSET:
            field_dict["bank_account_for_billing"] = bank_account_for_billing

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.master_client_full_account_holder_for_billing_bank_account_reference import MasterClientFullAccountHolderForBillingBankAccountReference
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




        _bank_account_for_billing = d.pop("bank_account_for_billing", UNSET)
        bank_account_for_billing: Union[Unset, MasterClientFullAccountHolderForBillingBankAccountReference]
        if isinstance(_bank_account_for_billing,  Unset):
            bank_account_for_billing = UNSET
        else:
            bank_account_for_billing = MasterClientFullAccountHolderForBillingBankAccountReference.from_dict(_bank_account_for_billing)




        master_client_full_account_holder_for_billing = cls(
            id=id,
            display_name=display_name,
            addressee_id=addressee_id,
            marriage_id=marriage_id,
            bank_account_for_billing=bank_account_for_billing,
        )


        master_client_full_account_holder_for_billing.additional_properties = d
        return master_client_full_account_holder_for_billing

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
