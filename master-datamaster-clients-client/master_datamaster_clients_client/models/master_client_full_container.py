from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_client_full_container_identification_status import MasterClientFullContainerIdentificationStatus
from ..models.master_client_full_container_risk_assessment import MasterClientFullContainerRiskAssessment
from ..models.master_client_full_container_status import MasterClientFullContainerStatus
from ..models.master_client_full_container_transparency_register import MasterClientFullContainerTransparencyRegister
from ..models.master_client_full_container_type import MasterClientFullContainerType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.master_client_full_correspondence_recipient import MasterClientFullCorrespondenceRecipient
  from ..models.master_client_full_account_holder_for_billing import MasterClientFullAccountHolderForBilling
  from ..models.master_client_full_addressee import MasterClientFullAddressee
  from ..models.master_client_full_marriage import MasterClientFullMarriage
  from ..models.master_client_full_invoice_recipient import MasterClientFullInvoiceRecipient





T = TypeVar("T", bound="MasterClientFullContainer")



@_attrs_define
class MasterClientFullContainer:
    """ The master client container contains the data of the master client.

        Attributes:
            name (str): (Mandantenbezeichnung) Master client name. A recognizable label given to the master client by the
                data responsible. This must not be confused with the natural or legal persons (also referred to as addressee)
                actual name. Example: Mandant Schreiner Josef Mustermann.
            number (int): (Zentrale Mandantennummer) The master client number. All master clients in one data environment
                have different values of the master client number. Master clients in different data environments may have the
                same master client number. For a given master client, the value of the master client number is not guaranteed to
                be stable. It can be changed by authorized users. The master client number is used for access decisions, too.
                Example: 10000.
            consultant_number (int): (Beraternummer) Consultant number used for access decisions. The value of the
                consultant number is not guaranteed to be stable, as it can be changed by authorized users. Example: 29098.
            status (MasterClientFullContainerStatus): (Status) Status of the master client, either active or inactive.
                Example: active.
            type_ (MasterClientFullContainerType): (Mandantentyp) Type of the master client. Example: individual_enterprise.
            id (Union[Unset, UUID]): OnPremise GUID of a client – internal identifier. Example:
                d13f9c3c-380c-494e-97c8-d12fff738189.
            client_since (Union[Unset, datetime.date]): (Mandant seit) Indicates the start date of a client relationship.
            client_to (Union[Unset, datetime.date]): (Mandant bis) Indicates the end date of a client relationship.
            differing_name (Union[Unset, str]): (Abw. Mandantenbezeichnung) Differing client name. Example: Abweichender
                Mustermeier.
            business_partner_id (Union[Unset, int]): (Geschäftspartnernummer) The business partner ID to which the master
                client belongs. The business partner ID is a stable, unique identifier for the business partner. Example:
                489345.
            note (Union[Unset, str]): (Notiz) Field for notes about the client. Example: Das ist eine Notiz zum Mandant..
            legal_person_id (Union[Unset, UUID]): GUID of an enterprise - internal identifier. Reference to the enterprise
                that is a client (client addressee). Example: fd3b2877-7505-4811-a53f-cd1c28ef627c.
            natural_person_id (Union[Unset, UUID]): GUID of a person – internal identifier. Reference to the person who is a
                client (client addressee).  Example: dc187309-392d-4e3b-b1f9-29c581178a06.
            timestamp (Union[Unset, datetime.datetime]): (Zeitstempel) Indicates when the client was last edited.
            identification_status (Union[Unset, MasterClientFullContainerIdentificationStatus]): (Identifizierungstatus nach
                GWG) Indicates status of identification according to GWG guidelines Example: complete.
            identification_checked_on (Union[Unset, datetime.date]): (Identifizierungsdatum nach GWG) Indicates date of
                identification according to GWG guidelines
            identification_comment (Union[Unset, str]): (Kommentar) Field for comments about the identification according to
                GWG guidelines Example: Das ist ein Kommentar zur GWG-Identifizierung..
            risk_assessment_date (Union[Unset, datetime.date]): (Risikobewertungsdatum nach GWG) Indicates date of risk
                assessment according to GWG guidelines
            risk_assessment_reason (Union[Unset, str]): (Begründung) Field for reasons about the risk assessment according
                to GWG guidelines Example: Das ist eine Begründung zur GWG-Risikobewertung..
            risk_assessment (Union[Unset, MasterClientFullContainerRiskAssessment]): (Risikobewertung nach GWG) Indicates
                risk assessment according to GWG guidelines Example: medium.
            transparency_register_comment (Union[Unset, str]): (Kommentar) Field for comments about the transparency
                register check according to GWG guidelines Example: Das ist ein Kommentar zur Transparenzregister..
            transparency_register_checked_on (Union[Unset, datetime.date]): (Transparenzregisterprüfungsdatum nach GWG)
                Indicates date of transparency register check according to GWG guidelines
            transparency_register (Union[Unset, MasterClientFullContainerTransparencyRegister]): (Transparenzregisterprüfung
                nach GWG) Indicates status of transparency register check according to GWG guidelines Example: entries_correct.
            esto_id (Union[Unset, UUID]): (ID einer Niederlassung) The establishment ID (stable technical identifier, also
                referred to as "ESTOID", short for "Establishment Online Identifier"). This is the reference to the
                establishment this master client is currently assigned to.A list of available establishments can be retrieved
                via `GET /data-environments/{number}`. Example: 4850466e-ad07-446c-9e2d-f31a15053f60.
            invoice_recipients (Union[Unset, list['MasterClientFullInvoiceRecipient']]): (Rechnungsempfänger) Invoice
                recipients of a master client.
                When 'Eigenorganisation comfort' is installed, multiple invoice recipients may exist.  In all other cases, at
                most one invoice recipient exists.
            correspondence_recipient (Union[Unset, MasterClientFullCorrespondenceRecipient]): (Angaben zum
                Korrespondenzempfänger) Correspondence recipient specific data.
            account_holder_for_billing (Union[Unset, MasterClientFullAccountHolderForBilling]): (Angaben zum Kontoinhaber
                für Rechnungsschreibung) Specific data for the account holder for billing.
            addressees (Union[Unset, list['MasterClientFullAddressee']]): (Adressaten) Addressees of a master client.
            marriages (Union[Unset, list['MasterClientFullMarriage']]): (Ehe-/Lebenspartner) Marriage of a master client.
     """

    name: str
    number: int
    consultant_number: int
    status: MasterClientFullContainerStatus
    type_: MasterClientFullContainerType
    id: Union[Unset, UUID] = UNSET
    client_since: Union[Unset, datetime.date] = UNSET
    client_to: Union[Unset, datetime.date] = UNSET
    differing_name: Union[Unset, str] = UNSET
    business_partner_id: Union[Unset, int] = UNSET
    note: Union[Unset, str] = UNSET
    legal_person_id: Union[Unset, UUID] = UNSET
    natural_person_id: Union[Unset, UUID] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    identification_status: Union[Unset, MasterClientFullContainerIdentificationStatus] = UNSET
    identification_checked_on: Union[Unset, datetime.date] = UNSET
    identification_comment: Union[Unset, str] = UNSET
    risk_assessment_date: Union[Unset, datetime.date] = UNSET
    risk_assessment_reason: Union[Unset, str] = UNSET
    risk_assessment: Union[Unset, MasterClientFullContainerRiskAssessment] = UNSET
    transparency_register_comment: Union[Unset, str] = UNSET
    transparency_register_checked_on: Union[Unset, datetime.date] = UNSET
    transparency_register: Union[Unset, MasterClientFullContainerTransparencyRegister] = UNSET
    esto_id: Union[Unset, UUID] = UNSET
    invoice_recipients: Union[Unset, list['MasterClientFullInvoiceRecipient']] = UNSET
    correspondence_recipient: Union[Unset, 'MasterClientFullCorrespondenceRecipient'] = UNSET
    account_holder_for_billing: Union[Unset, 'MasterClientFullAccountHolderForBilling'] = UNSET
    addressees: Union[Unset, list['MasterClientFullAddressee']] = UNSET
    marriages: Union[Unset, list['MasterClientFullMarriage']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.master_client_full_correspondence_recipient import MasterClientFullCorrespondenceRecipient
        from ..models.master_client_full_account_holder_for_billing import MasterClientFullAccountHolderForBilling
        from ..models.master_client_full_addressee import MasterClientFullAddressee
        from ..models.master_client_full_marriage import MasterClientFullMarriage
        from ..models.master_client_full_invoice_recipient import MasterClientFullInvoiceRecipient
        name = self.name

        number = self.number

        consultant_number = self.consultant_number

        status = self.status.value

        type_ = self.type_.value

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        client_since: Union[Unset, str] = UNSET
        if not isinstance(self.client_since, Unset):
            client_since = self.client_since.isoformat()

        client_to: Union[Unset, str] = UNSET
        if not isinstance(self.client_to, Unset):
            client_to = self.client_to.isoformat()

        differing_name = self.differing_name

        business_partner_id = self.business_partner_id

        note = self.note

        legal_person_id: Union[Unset, str] = UNSET
        if not isinstance(self.legal_person_id, Unset):
            legal_person_id = str(self.legal_person_id)

        natural_person_id: Union[Unset, str] = UNSET
        if not isinstance(self.natural_person_id, Unset):
            natural_person_id = str(self.natural_person_id)

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        identification_status: Union[Unset, str] = UNSET
        if not isinstance(self.identification_status, Unset):
            identification_status = self.identification_status.value


        identification_checked_on: Union[Unset, str] = UNSET
        if not isinstance(self.identification_checked_on, Unset):
            identification_checked_on = self.identification_checked_on.isoformat()

        identification_comment = self.identification_comment

        risk_assessment_date: Union[Unset, str] = UNSET
        if not isinstance(self.risk_assessment_date, Unset):
            risk_assessment_date = self.risk_assessment_date.isoformat()

        risk_assessment_reason = self.risk_assessment_reason

        risk_assessment: Union[Unset, str] = UNSET
        if not isinstance(self.risk_assessment, Unset):
            risk_assessment = self.risk_assessment.value


        transparency_register_comment = self.transparency_register_comment

        transparency_register_checked_on: Union[Unset, str] = UNSET
        if not isinstance(self.transparency_register_checked_on, Unset):
            transparency_register_checked_on = self.transparency_register_checked_on.isoformat()

        transparency_register: Union[Unset, str] = UNSET
        if not isinstance(self.transparency_register, Unset):
            transparency_register = self.transparency_register.value


        esto_id: Union[Unset, str] = UNSET
        if not isinstance(self.esto_id, Unset):
            esto_id = str(self.esto_id)

        invoice_recipients: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invoice_recipients, Unset):
            invoice_recipients = []
            for invoice_recipients_item_data in self.invoice_recipients:
                invoice_recipients_item = invoice_recipients_item_data.to_dict()
                invoice_recipients.append(invoice_recipients_item)



        correspondence_recipient: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.correspondence_recipient, Unset):
            correspondence_recipient = self.correspondence_recipient.to_dict()

        account_holder_for_billing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.account_holder_for_billing, Unset):
            account_holder_for_billing = self.account_holder_for_billing.to_dict()

        addressees: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.addressees, Unset):
            addressees = []
            for addressees_item_data in self.addressees:
                addressees_item = addressees_item_data.to_dict()
                addressees.append(addressees_item)



        marriages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.marriages, Unset):
            marriages = []
            for marriages_item_data in self.marriages:
                marriages_item = marriages_item_data.to_dict()
                marriages.append(marriages_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "number": number,
            "consultant_number": consultant_number,
            "status": status,
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if client_since is not UNSET:
            field_dict["client_since"] = client_since
        if client_to is not UNSET:
            field_dict["client_to"] = client_to
        if differing_name is not UNSET:
            field_dict["differing_name"] = differing_name
        if business_partner_id is not UNSET:
            field_dict["business_partner_id"] = business_partner_id
        if note is not UNSET:
            field_dict["note"] = note
        if legal_person_id is not UNSET:
            field_dict["legal_person_id"] = legal_person_id
        if natural_person_id is not UNSET:
            field_dict["natural_person_id"] = natural_person_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if identification_status is not UNSET:
            field_dict["identification_status"] = identification_status
        if identification_checked_on is not UNSET:
            field_dict["identification_checked_on"] = identification_checked_on
        if identification_comment is not UNSET:
            field_dict["identification_comment"] = identification_comment
        if risk_assessment_date is not UNSET:
            field_dict["risk_assessment_date"] = risk_assessment_date
        if risk_assessment_reason is not UNSET:
            field_dict["risk_assessment_reason"] = risk_assessment_reason
        if risk_assessment is not UNSET:
            field_dict["risk_assessment"] = risk_assessment
        if transparency_register_comment is not UNSET:
            field_dict["transparency_register_comment"] = transparency_register_comment
        if transparency_register_checked_on is not UNSET:
            field_dict["transparency_register_checked_on"] = transparency_register_checked_on
        if transparency_register is not UNSET:
            field_dict["transparency_register"] = transparency_register
        if esto_id is not UNSET:
            field_dict["esto_id"] = esto_id
        if invoice_recipients is not UNSET:
            field_dict["invoice_recipients"] = invoice_recipients
        if correspondence_recipient is not UNSET:
            field_dict["correspondence_recipient"] = correspondence_recipient
        if account_holder_for_billing is not UNSET:
            field_dict["account_holder_for_billing"] = account_holder_for_billing
        if addressees is not UNSET:
            field_dict["addressees"] = addressees
        if marriages is not UNSET:
            field_dict["marriages"] = marriages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.master_client_full_correspondence_recipient import MasterClientFullCorrespondenceRecipient
        from ..models.master_client_full_account_holder_for_billing import MasterClientFullAccountHolderForBilling
        from ..models.master_client_full_addressee import MasterClientFullAddressee
        from ..models.master_client_full_marriage import MasterClientFullMarriage
        from ..models.master_client_full_invoice_recipient import MasterClientFullInvoiceRecipient
        d = src_dict.copy()
        name = d.pop("name")

        number = d.pop("number")

        consultant_number = d.pop("consultant_number")

        status = MasterClientFullContainerStatus(d.pop("status"))




        type_ = MasterClientFullContainerType(d.pop("type"))




        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _client_since = d.pop("client_since", UNSET)
        client_since: Union[Unset, datetime.date]
        if isinstance(_client_since,  Unset):
            client_since = UNSET
        else:
            client_since = isoparse(_client_since).date()




        _client_to = d.pop("client_to", UNSET)
        client_to: Union[Unset, datetime.date]
        if isinstance(_client_to,  Unset):
            client_to = UNSET
        else:
            client_to = isoparse(_client_to).date()




        differing_name = d.pop("differing_name", UNSET)

        business_partner_id = d.pop("business_partner_id", UNSET)

        note = d.pop("note", UNSET)

        _legal_person_id = d.pop("legal_person_id", UNSET)
        legal_person_id: Union[Unset, UUID]
        if isinstance(_legal_person_id,  Unset):
            legal_person_id = UNSET
        else:
            legal_person_id = UUID(_legal_person_id)




        _natural_person_id = d.pop("natural_person_id", UNSET)
        natural_person_id: Union[Unset, UUID]
        if isinstance(_natural_person_id,  Unset):
            natural_person_id = UNSET
        else:
            natural_person_id = UUID(_natural_person_id)




        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp,  Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)




        _identification_status = d.pop("identification_status", UNSET)
        identification_status: Union[Unset, MasterClientFullContainerIdentificationStatus]
        if isinstance(_identification_status,  Unset):
            identification_status = UNSET
        else:
            identification_status = MasterClientFullContainerIdentificationStatus(_identification_status)




        _identification_checked_on = d.pop("identification_checked_on", UNSET)
        identification_checked_on: Union[Unset, datetime.date]
        if isinstance(_identification_checked_on,  Unset):
            identification_checked_on = UNSET
        else:
            identification_checked_on = isoparse(_identification_checked_on).date()




        identification_comment = d.pop("identification_comment", UNSET)

        _risk_assessment_date = d.pop("risk_assessment_date", UNSET)
        risk_assessment_date: Union[Unset, datetime.date]
        if isinstance(_risk_assessment_date,  Unset):
            risk_assessment_date = UNSET
        else:
            risk_assessment_date = isoparse(_risk_assessment_date).date()




        risk_assessment_reason = d.pop("risk_assessment_reason", UNSET)

        _risk_assessment = d.pop("risk_assessment", UNSET)
        risk_assessment: Union[Unset, MasterClientFullContainerRiskAssessment]
        if isinstance(_risk_assessment,  Unset):
            risk_assessment = UNSET
        else:
            risk_assessment = MasterClientFullContainerRiskAssessment(_risk_assessment)




        transparency_register_comment = d.pop("transparency_register_comment", UNSET)

        _transparency_register_checked_on = d.pop("transparency_register_checked_on", UNSET)
        transparency_register_checked_on: Union[Unset, datetime.date]
        if isinstance(_transparency_register_checked_on,  Unset):
            transparency_register_checked_on = UNSET
        else:
            transparency_register_checked_on = isoparse(_transparency_register_checked_on).date()




        _transparency_register = d.pop("transparency_register", UNSET)
        transparency_register: Union[Unset, MasterClientFullContainerTransparencyRegister]
        if isinstance(_transparency_register,  Unset):
            transparency_register = UNSET
        else:
            transparency_register = MasterClientFullContainerTransparencyRegister(_transparency_register)




        _esto_id = d.pop("esto_id", UNSET)
        esto_id: Union[Unset, UUID]
        if isinstance(_esto_id,  Unset):
            esto_id = UNSET
        else:
            esto_id = UUID(_esto_id)




        invoice_recipients = []
        _invoice_recipients = d.pop("invoice_recipients", UNSET)
        for invoice_recipients_item_data in (_invoice_recipients or []):
            invoice_recipients_item = MasterClientFullInvoiceRecipient.from_dict(invoice_recipients_item_data)



            invoice_recipients.append(invoice_recipients_item)


        _correspondence_recipient = d.pop("correspondence_recipient", UNSET)
        correspondence_recipient: Union[Unset, MasterClientFullCorrespondenceRecipient]
        if isinstance(_correspondence_recipient,  Unset):
            correspondence_recipient = UNSET
        else:
            correspondence_recipient = MasterClientFullCorrespondenceRecipient.from_dict(_correspondence_recipient)




        _account_holder_for_billing = d.pop("account_holder_for_billing", UNSET)
        account_holder_for_billing: Union[Unset, MasterClientFullAccountHolderForBilling]
        if isinstance(_account_holder_for_billing,  Unset):
            account_holder_for_billing = UNSET
        else:
            account_holder_for_billing = MasterClientFullAccountHolderForBilling.from_dict(_account_holder_for_billing)




        addressees = []
        _addressees = d.pop("addressees", UNSET)
        for addressees_item_data in (_addressees or []):
            addressees_item = MasterClientFullAddressee.from_dict(addressees_item_data)



            addressees.append(addressees_item)


        marriages = []
        _marriages = d.pop("marriages", UNSET)
        for marriages_item_data in (_marriages or []):
            marriages_item = MasterClientFullMarriage.from_dict(marriages_item_data)



            marriages.append(marriages_item)


        master_client_full_container = cls(
            name=name,
            number=number,
            consultant_number=consultant_number,
            status=status,
            type_=type_,
            id=id,
            client_since=client_since,
            client_to=client_to,
            differing_name=differing_name,
            business_partner_id=business_partner_id,
            note=note,
            legal_person_id=legal_person_id,
            natural_person_id=natural_person_id,
            timestamp=timestamp,
            identification_status=identification_status,
            identification_checked_on=identification_checked_on,
            identification_comment=identification_comment,
            risk_assessment_date=risk_assessment_date,
            risk_assessment_reason=risk_assessment_reason,
            risk_assessment=risk_assessment,
            transparency_register_comment=transparency_register_comment,
            transparency_register_checked_on=transparency_register_checked_on,
            transparency_register=transparency_register,
            esto_id=esto_id,
            invoice_recipients=invoice_recipients,
            correspondence_recipient=correspondence_recipient,
            account_holder_for_billing=account_holder_for_billing,
            addressees=addressees,
            marriages=marriages,
        )


        master_client_full_container.additional_properties = d
        return master_client_full_container

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
