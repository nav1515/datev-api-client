from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="BrickContext")



@_attrs_define
class BrickContext:
    """ Context on which the contained bricks should be applied.

        Attributes:
            key (str): Key that identifies the context.<br>The following keys are possible:
                | key | name (german) | possible bricks |
                | --- | ------------- | --------------- |
                | `Client` | Mandant | `ClientData`, `Gwg`, `InvoiceRecipient`, `CorrespondenceRecipient`,
                `AccountHolderForBilling` |
                | `ClientLegalPerson` | Mandatsadressat Unternehmen | all bricks for legal person contexts |
                | `ClientNaturalPerson` | Mandatsadressat Natürliche Person | all bricks for natural person contexts |
                | `ClientMarriage` | Ehekontakt des Mandanten | all bricks for marriage contexts |
                | `Spouse` | Ehe-/Lebenspartner | all bricks for natural person contexts |
                | `Child` | Kind einer natürlichen Person | all bricks for natural person contexts |
                | `LegalRepresentativeOfNaturalPerson#natural_person` | Natürliche Person des gesetzlichen Vertreters einer
                natürlichen Person | all bricks for natural person contexts |
                | `LegalRepresentativeOfNaturalPerson#legal_person` | Unternehmen des gesetzlichen Vertreters einer natürlichen
                Person | all bricks for legal person contexts |
                | `UltimateBeneficialOwnerOfNaturalPerson` | Natürliche Person des wirtschaftlich Berechtigten einer natürlichen
                Person | all bricks for natural person contexts |
                | `ContactPersonOfNaturalPerson` | Natürliche Person des Ansprechpartner einer natürlichen Person | all bricks
                for natural person contexts |
                | `LegalRepresentativeOfCompany#natural_person` | Natürliche Person des gesetzlichen Vertreters eines
                Unternehmens | all bricks for natural person contexts |
                | `LegalRepresentativeOfCompany#legal_person` | Unternehmen des gesetzlichen Vertreters eines Unternehmens | all
                bricks for legal person contexts |
                | `UltimateBeneficialOwnerOfCompany` | Natürliche Person des wirtschaftlich Berechtigten eines Unternehmens |
                all bricks for natural person contexts |
                | `ContactPersonOfCompany` | Natürliche Person des Ansprechpartner eines Unternehmens | all bricks for natural
                person contexts |
                | `Proprietor` | Natürliche Person des Betriebsinhabers | all bricks for natural person contexts |
                | `AccountHolderForBillingAddressee#natural_person` | Natürliche Person des Kontoinhaber für Rechnungsschreibung
                | all bricks for natural person contexts |
                | `AccountHolderForBillingAddressee#legal_person` | Unternehmen des Kontoinhaber für Rechnungsschreibung | all
                bricks for legal person contexts |
                | `AccountHolderForBillingMarriage` | Ehekontakt des Kontoinhaber für Rechnungsschreibung | all bricks for
                marriage contexts |
                | `CorrespondenceRecipientAddressee#natural_person` | Natürliche Person des Empfängers für
                Mandantenkorrespondenz | all bricks for natural person contexts |
                | `CorrespondenceRecipientAddressee#legal_person` | Unternehmen des Empfängers für Mandantenkorrespondenz | all
                bricks for legal person contexts |
                | `CorrespondenceRecipientMarriage` | Ehekontakt des Empfängers für Mandantenkorrespondenz | all bricks for
                marriage contexts |
                | `InvoiceRecipientAddressee#natural_person` | Natürliche Person des Rechnungsempfänger | all bricks for natural
                person contexts |
                | `InvoiceRecipientAddressee#legal_person` | Unternehmen des Rechnungsempfänger | all bricks for legal person
                contexts |
                | `InvoiceRecipientMarriage` | Ehekontakt des Rechnungsempfänger | all bricks for marriage contexts |
                 Example: Client.
            bricks (Union[Unset, list[str]]): The keys of the bricks which should be applied for this context.<br>The
                following keys for bricks are possible:
                | key | name (german) | possible contexts |
                | --- | ------------- | ----------------- |
                | `ClientData` | Mandantendaten | `Client` context |
                | `Gwg` | Daten zum Geldwäschegesetz | `Client` context |
                | `InvoiceRecipient` | Rechnungsempfänger | `Client` context |
                | `CorrespondenceRecipient` | Empfänger für Mandantenkorrespondenz | `Client` context |
                | `AccountHolderForBilling` | Kontoinhaber für Rechnungsschreibung | `Client` context |
                | `AddressOfAddressee` | Adresse | all natural person and legal person contexts |
                | `CommunicationOfAddressee` | Kommunikation | all natural person and legal person contexts |
                | `BankAccountOfAddressee` | Bank | all natural person and legal person contexts |
                | `TaxOffice` | Finanzamt | all natural person and legal person contexts |
                | `ContactPerson` | Ansprechpartner | all natural person and legal person contexts |
                | `UltimateBeneficialOwner` | Wirtschaftlich Berechtigter | all natural person and legal person contexts |
                | `NaturalPersonBasic` | Basisdaten zur natürlichen Person | all natural person contexts |
                | `NaturalPersonExtended` | Sonstige persönliche Daten der natürlichen Person | all natural person contexts |
                | `NaturalPersonLegitimation` | Legitimationsdaten der natürlichen Person | all natural person contexts |
                | `NaturalPersonTaxInfo` | Steueridentifikationsdaten der natürlichen Person | all natural person contexts |
                | `Child` | Basisdaten zum Kind | all natural person contexts |
                | `LegalRepresentativeOfNaturalPerson` | Gesetzlicher Vertreter der Person | all natural person contexts |
                | `LegalPerson` | Unternehmensdaten | all legal person contexts |
                | `Proprietor` | Betriebsinhaber | all legal person contexts |
                | `LegalRepresentativeOfCompany` | Gesetzlicher Vertreter des Unternehmens | all legal person contexts |
                | `Marriage` | Gemeinsame Kontaktdaten des Ehepaars | `ClientMarriage`, `AccountHolderForBillingMarriage`,
                `CorrespondenceRecipientMarriage`, `InvoiceRecipientMarriage` |
                | `AddressOfMarriage` | Gemeinsame Adressen des Ehepaars | `ClientMarriage`, `AccountHolderForBillingMarriage`,
                `CorrespondenceRecipientMarriage`, `InvoiceRecipientMarriage` |
                | `CommunicationOfMarriage` | Gemeinsame Kommunikationsverbindungen des Ehepaars | `ClientMarriage`,
                `AccountHolderForBillingMarriage`, `CorrespondenceRecipientMarriage`, `InvoiceRecipientMarriage` |
                | `BankAccountOfMarriage` | Gemeinsame Bankkonten des Ehepaars | `ClientMarriage`,
                `AccountHolderForBillingMarriage`, `CorrespondenceRecipientMarriage`, `InvoiceRecipientMarriage` |
     """

    key: str
    bricks: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        key = self.key

        bricks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.bricks, Unset):
            bricks = self.bricks




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
        })
        if bricks is not UNSET:
            field_dict["bricks"] = bricks

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        bricks = cast(list[str], d.pop("bricks", UNSET))


        brick_context = cls(
            key=key,
            bricks=bricks,
        )


        brick_context.additional_properties = d
        return brick_context

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
