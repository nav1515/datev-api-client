from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="MasterClientFullAccountHolderForBillingBankAccountReference")



@_attrs_define
class MasterClientFullAccountHolderForBillingBankAccountReference:
    """ (Bankverbindung) Reference to the bank account.

        Attributes:
            id (Union[Unset, UUID]): GUID - internal ID of a bank account. Example: 31b9d6d9-117b-4555-b0b0-3659eb0279d0.
            bic (Union[Unset, str]): (BIC) Unique identifier for a SWIFT-participant (BIC - Bank Identifier Code). SWIFT is
                the abbreviation for "Society for Worldwide Interbank Financial Telecommunications". Example: SSKNDE77XXX.
            iban (Union[Unset, str]): (IBAN) Identifies a bank account worldwide (ISO 13616). Example:
                DE12760501010003225553.
     """

    id: Union[Unset, UUID] = UNSET
    bic: Union[Unset, str] = UNSET
    iban: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        bic = self.bic

        iban = self.iban


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if bic is not UNSET:
            field_dict["bic"] = bic
        if iban is not UNSET:
            field_dict["iban"] = iban

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




        bic = d.pop("bic", UNSET)

        iban = d.pop("iban", UNSET)

        master_client_full_account_holder_for_billing_bank_account_reference = cls(
            id=id,
            bic=bic,
            iban=iban,
        )


        master_client_full_account_holder_for_billing_bank_account_reference.additional_properties = d
        return master_client_full_account_holder_for_billing_bank_account_reference

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
