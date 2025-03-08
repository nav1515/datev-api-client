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
  from ..models.master_client_full_invoice_recipient_email import MasterClientFullInvoiceRecipientEmail





T = TypeVar("T", bound="MasterClientFullInvoiceRecipient")



@_attrs_define
class MasterClientFullInvoiceRecipient:
    """ (Angaben zum Rechnungsempfänger) Invoice recipient specific data.

        Attributes:
            id (Union[Unset, UUID]): GUID of a relationship - internal identifier.
            display_name (Union[Unset, str]): Comprise a display name of the referenced addressee. Example: Mustermeier,
                Georg.
            addressee_id (Union[Unset, UUID]): GUID of the referenced addressee. Only either addresseeId or marriageId is
                filled.
            marriage_id (Union[Unset, UUID]): GUID of the referenced marriage. Only either addresseeId or marriageId is
                filled. Example: 84322f6f-77f6-4b91-ac06-c05a6999c41e.
            billing_addresses (Union[Unset, list['MasterClientFullAddressReference']]): (Rechnungsadresse) Billing addresses
                of the invoice recipient.<br>When 'Eigenorganisation comfort' is installed, multiple billing addresses may
                exist. In all other cases, at most one billing address exists.
            billing_emails (Union[Unset, list['MasterClientFullInvoiceRecipientEmail']]): (E-Mail-Adresse) Billing e-mail
                addresses of the invoice recipient.When 'Eigenorganisation comfort' is installed, multiple billing e-mail
                addresses may exist. In all other cases, at most one billing e-mail address exists.
     """

    id: Union[Unset, UUID] = UNSET
    display_name: Union[Unset, str] = UNSET
    addressee_id: Union[Unset, UUID] = UNSET
    marriage_id: Union[Unset, UUID] = UNSET
    billing_addresses: Union[Unset, list['MasterClientFullAddressReference']] = UNSET
    billing_emails: Union[Unset, list['MasterClientFullInvoiceRecipientEmail']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.master_client_full_address_reference import MasterClientFullAddressReference
        from ..models.master_client_full_invoice_recipient_email import MasterClientFullInvoiceRecipientEmail
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

        billing_addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_addresses, Unset):
            billing_addresses = []
            for billing_addresses_item_data in self.billing_addresses:
                billing_addresses_item = billing_addresses_item_data.to_dict()
                billing_addresses.append(billing_addresses_item)



        billing_emails: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.billing_emails, Unset):
            billing_emails = []
            for billing_emails_item_data in self.billing_emails:
                billing_emails_item = billing_emails_item_data.to_dict()
                billing_emails.append(billing_emails_item)




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
        if billing_addresses is not UNSET:
            field_dict["billing_addresses"] = billing_addresses
        if billing_emails is not UNSET:
            field_dict["billing_emails"] = billing_emails

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.master_client_full_address_reference import MasterClientFullAddressReference
        from ..models.master_client_full_invoice_recipient_email import MasterClientFullInvoiceRecipientEmail
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




        billing_addresses = []
        _billing_addresses = d.pop("billing_addresses", UNSET)
        for billing_addresses_item_data in (_billing_addresses or []):
            billing_addresses_item = MasterClientFullAddressReference.from_dict(billing_addresses_item_data)



            billing_addresses.append(billing_addresses_item)


        billing_emails = []
        _billing_emails = d.pop("billing_emails", UNSET)
        for billing_emails_item_data in (_billing_emails or []):
            billing_emails_item = MasterClientFullInvoiceRecipientEmail.from_dict(billing_emails_item_data)



            billing_emails.append(billing_emails_item)


        master_client_full_invoice_recipient = cls(
            id=id,
            display_name=display_name,
            addressee_id=addressee_id,
            marriage_id=marriage_id,
            billing_addresses=billing_addresses,
            billing_emails=billing_emails,
        )


        master_client_full_invoice_recipient.additional_properties = d
        return master_client_full_invoice_recipient

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
