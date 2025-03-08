from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="MasterClientFullInvoiceRecipientEmail")



@_attrs_define
class MasterClientFullInvoiceRecipientEmail:
    """ (E-Mail-Adresse des Rechnungsempfängers) Email address of invoice recipient.

        Attributes:
            id (Union[Unset, UUID]): GUID - internal ID of an email address. Example: 0b146028-ec91-4ed8-806f-2c060e12d3bc.
            email (Union[Unset, str]): (E-Mail-Adresse) Billing e-mail address of the invoice recipient. Example:
                josef.mustermann@mustermann-schreiner.de.
     """

    id: Union[Unset, UUID] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        email = self.email


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email

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




        email = d.pop("email", UNSET)

        master_client_full_invoice_recipient_email = cls(
            id=id,
            email=email,
        )


        master_client_full_invoice_recipient_email.additional_properties = d
        return master_client_full_invoice_recipient_email

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
