from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_client_full_marriage_status import MasterClientFullMarriageStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.master_client_full_address import MasterClientFullAddress
  from ..models.master_client_full_communication import MasterClientFullCommunication
  from ..models.master_client_full_bank_account import MasterClientFullBankAccount





T = TypeVar("T", bound="MasterClientFullMarriage")



@_attrs_define
class MasterClientFullMarriage:
    """ (Angaben zu Ehe-/Lebenspartner) Marriage specific data.

        Attributes:
            id (Union[Unset, UUID]): GUID of a marriage - internal identifier.  Example:
                f2de7381-5836-4fc4-81ef-d05e2a87ba55.
            is_addressee_id (Union[Unset, UUID]): (GUID des 'ist' Adressaten der Ehebeziehung) GUID of the 'is' addressee of
                the marriage. Usually the wife or partner. Example: 1f6f2f45-631a-480c-b7f1-aadb565f4307.
            has_addressee_id (Union[Unset, UUID]): (GUID des 'hat' Adressaten der Ehebeziehung) GUID of the 'has' addressee
                of the marriage. Usually the husband. Example: 851684d3-776b-491c-87ed-0552c74caa77.
            complimentary_close (Union[Unset, str]): (Grußformel) The complimentary close defines the sign-off used for a
                marriage in correspondence. Example: Mit freundlichen Grüßen.
            correspondence_title (Union[Unset, str]): (Anrede der Ehe) The title is the way in which a marriage is
                addressed. Example: Herrn und Frau.
            matrimonial_property_regime (Union[Unset, int]): (Güterstand) Matrimonial property regime of the marriage. The
                following values are possible:<br>1 = Zugewinngemeinschaft (gesetzlicher Güterstand),<br>2 = Modifizierte
                Zugewinngemeinschaft,<br>3 = Gütergemeinschaft,
                4 = Fortgesetzte Gütergemeinschaft,<br>5 = Gütertrennung,
                6 = Anderer vertraglicher Güterstand,<br>7 = Eigentums- und Vermögensgemeinschaft (gesetzlicher Güterstand
                DDR),<br>8 = Errungenschaftsgemeinschaft,<br>9 = Fahrnisgemeinschaft,<br>10 = Güterstand nach ausländischem
                Recht
            name (Union[Unset, str]): (Bezeichnung des Ehekontakts) The name of the married addressees. Example: Eheleute
                Mustermeier.
            salutation (Union[Unset, str]): (Briefanrede des Ehepaars) Salutation for correspondence as it appears in
                letters. Example: Sehr geehrte Herr und Frau,.
            status (Union[Unset, MasterClientFullMarriageStatus]): (Status) Indicates whether the marriage is active or
                inactive.  Example: active.
            surrogate_name (Union[Unset, str]): (Alternativer Suchname) Alias of a marriage for search purposes. Example:
                Meier.
            timestamp (Union[Unset, datetime.datetime]): (Zeitstempel) Indicates when the marriage was last edited.
            bank_accounts (Union[Unset, list['MasterClientFullBankAccount']]): (Bankverbindungen des Ehekontakts) Bank
                accounts of a marriage.
            communications (Union[Unset, list['MasterClientFullCommunication']]): (Kommunikationsverbindungen des
                Ehekontakts) Communication data of a marriage.
            shared_addresses (Union[Unset, list['MasterClientFullAddress']]): (Gemeinsame Adressen) Shared addresses of a
                marriage.
     """

    id: Union[Unset, UUID] = UNSET
    is_addressee_id: Union[Unset, UUID] = UNSET
    has_addressee_id: Union[Unset, UUID] = UNSET
    complimentary_close: Union[Unset, str] = UNSET
    correspondence_title: Union[Unset, str] = UNSET
    matrimonial_property_regime: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    salutation: Union[Unset, str] = UNSET
    status: Union[Unset, MasterClientFullMarriageStatus] = UNSET
    surrogate_name: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    bank_accounts: Union[Unset, list['MasterClientFullBankAccount']] = UNSET
    communications: Union[Unset, list['MasterClientFullCommunication']] = UNSET
    shared_addresses: Union[Unset, list['MasterClientFullAddress']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.master_client_full_address import MasterClientFullAddress
        from ..models.master_client_full_communication import MasterClientFullCommunication
        from ..models.master_client_full_bank_account import MasterClientFullBankAccount
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_addressee_id: Union[Unset, str] = UNSET
        if not isinstance(self.is_addressee_id, Unset):
            is_addressee_id = str(self.is_addressee_id)

        has_addressee_id: Union[Unset, str] = UNSET
        if not isinstance(self.has_addressee_id, Unset):
            has_addressee_id = str(self.has_addressee_id)

        complimentary_close = self.complimentary_close

        correspondence_title = self.correspondence_title

        matrimonial_property_regime = self.matrimonial_property_regime

        name = self.name

        salutation = self.salutation

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        surrogate_name = self.surrogate_name

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        bank_accounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bank_accounts, Unset):
            bank_accounts = []
            for bank_accounts_item_data in self.bank_accounts:
                bank_accounts_item = bank_accounts_item_data.to_dict()
                bank_accounts.append(bank_accounts_item)



        communications: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.communications, Unset):
            communications = []
            for communications_item_data in self.communications:
                communications_item = communications_item_data.to_dict()
                communications.append(communications_item)



        shared_addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shared_addresses, Unset):
            shared_addresses = []
            for shared_addresses_item_data in self.shared_addresses:
                shared_addresses_item = shared_addresses_item_data.to_dict()
                shared_addresses.append(shared_addresses_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_addressee_id is not UNSET:
            field_dict["is_addressee_id"] = is_addressee_id
        if has_addressee_id is not UNSET:
            field_dict["has_addressee_id"] = has_addressee_id
        if complimentary_close is not UNSET:
            field_dict["complimentary_close"] = complimentary_close
        if correspondence_title is not UNSET:
            field_dict["correspondence_title"] = correspondence_title
        if matrimonial_property_regime is not UNSET:
            field_dict["matrimonial_property_regime"] = matrimonial_property_regime
        if name is not UNSET:
            field_dict["name"] = name
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if status is not UNSET:
            field_dict["status"] = status
        if surrogate_name is not UNSET:
            field_dict["surrogate_name"] = surrogate_name
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if bank_accounts is not UNSET:
            field_dict["bank_accounts"] = bank_accounts
        if communications is not UNSET:
            field_dict["communications"] = communications
        if shared_addresses is not UNSET:
            field_dict["shared_addresses"] = shared_addresses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.master_client_full_address import MasterClientFullAddress
        from ..models.master_client_full_communication import MasterClientFullCommunication
        from ..models.master_client_full_bank_account import MasterClientFullBankAccount
        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _is_addressee_id = d.pop("is_addressee_id", UNSET)
        is_addressee_id: Union[Unset, UUID]
        if isinstance(_is_addressee_id,  Unset):
            is_addressee_id = UNSET
        else:
            is_addressee_id = UUID(_is_addressee_id)




        _has_addressee_id = d.pop("has_addressee_id", UNSET)
        has_addressee_id: Union[Unset, UUID]
        if isinstance(_has_addressee_id,  Unset):
            has_addressee_id = UNSET
        else:
            has_addressee_id = UUID(_has_addressee_id)




        complimentary_close = d.pop("complimentary_close", UNSET)

        correspondence_title = d.pop("correspondence_title", UNSET)

        matrimonial_property_regime = d.pop("matrimonial_property_regime", UNSET)

        name = d.pop("name", UNSET)

        salutation = d.pop("salutation", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MasterClientFullMarriageStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = MasterClientFullMarriageStatus(_status)




        surrogate_name = d.pop("surrogate_name", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp,  Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)




        bank_accounts = []
        _bank_accounts = d.pop("bank_accounts", UNSET)
        for bank_accounts_item_data in (_bank_accounts or []):
            bank_accounts_item = MasterClientFullBankAccount.from_dict(bank_accounts_item_data)



            bank_accounts.append(bank_accounts_item)


        communications = []
        _communications = d.pop("communications", UNSET)
        for communications_item_data in (_communications or []):
            communications_item = MasterClientFullCommunication.from_dict(communications_item_data)



            communications.append(communications_item)


        shared_addresses = []
        _shared_addresses = d.pop("shared_addresses", UNSET)
        for shared_addresses_item_data in (_shared_addresses or []):
            shared_addresses_item = MasterClientFullAddress.from_dict(shared_addresses_item_data)



            shared_addresses.append(shared_addresses_item)


        master_client_full_marriage = cls(
            id=id,
            is_addressee_id=is_addressee_id,
            has_addressee_id=has_addressee_id,
            complimentary_close=complimentary_close,
            correspondence_title=correspondence_title,
            matrimonial_property_regime=matrimonial_property_regime,
            name=name,
            salutation=salutation,
            status=status,
            surrogate_name=surrogate_name,
            timestamp=timestamp,
            bank_accounts=bank_accounts,
            communications=communications,
            shared_addresses=shared_addresses,
        )


        master_client_full_marriage.additional_properties = d
        return master_client_full_marriage

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
