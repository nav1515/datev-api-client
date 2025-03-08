from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_client_full_addressee_current_legal_form_id import MasterClientFullAddresseeCurrentLegalFormId
from ..models.master_client_full_addressee_sex import MasterClientFullAddresseeSex
from ..models.master_client_full_addressee_status import MasterClientFullAddresseeStatus
from ..models.master_client_full_addressee_type import MasterClientFullAddresseeType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.master_client_full_address import MasterClientFullAddress
  from ..models.master_client_full_addressee_proprietor import MasterClientFullAddresseeProprietor
  from ..models.master_client_full_addressee_ultimate_beneficial_owner import MasterClientFullAddresseeUltimateBeneficialOwner
  from ..models.master_client_full_addressee_contact_person import MasterClientFullAddresseeContactPerson
  from ..models.master_client_full_bank_account import MasterClientFullBankAccount
  from ..models.master_client_full_historical_value_string import MasterClientFullHistoricalValueString
  from ..models.master_client_full_addressee_detail import MasterClientFullAddresseeDetail
  from ..models.master_client_full_tax_office import MasterClientFullTaxOffice
  from ..models.master_client_full_addressee_child import MasterClientFullAddresseeChild
  from ..models.master_client_full_communication import MasterClientFullCommunication
  from ..models.master_client_full_addressee_legal_representative_of_company import MasterClientFullAddresseeLegalRepresentativeOfCompany
  from ..models.master_client_full_addressee_legal_representative_of_natural_person import MasterClientFullAddresseeLegalRepresentativeOfNaturalPerson





T = TypeVar("T", bound="MasterClientFullAddressee")



@_attrs_define
class MasterClientFullAddressee:
    """ (Adressat) An addressee of a master client.

        Attributes:
            type_ (MasterClientFullAddresseeType): (Adressattyp) Indicates whether the addressee is a person or an
                enterprise. Example: legal_person.
            id (Union[Unset, UUID]): GUID of an addressee – internal identifier. Example:
                16b9d6d3-117b-4553-b0b0-3659eb0279d7.
            eu_vat_id_country_code (Union[Unset, str]): (UStId-Länderkennzeichen) VAT ID country codes (AT = Österreich, BE
                = Belgien, BG = Bulgarien, CY = Zypern, CZ = Tschechische Republik, DE = Deutschland, DK = Dänemark, EE =
                Estland, EL = Griechenland, ES = Spanien, EU = Europäische Union, FI = Finnland, FR = Frankreich, GB =
                Großbritannien, HR = Kroatien, HU = Ungarn, IE = Irland, IT = Italien, LT = Litauen, LU = Luxemburg, LV =
                Lettland, MT = Malta, NL = Niederlande, PL = Polen, PT = Portugal, RO = Rumänien, SE = Schweden, SI = Slowenien,
                SK = Slowakei). Both the country code and number must be set to form a valid VAT ID. Example: DE.
            eu_vat_id_number (Union[Unset, str]): (UStId ohne Länderkennzeichen) European VAT ID without country code. Both
                the country code and number must be set to form a valid VAT ID. Example: 812277765.
            economic_identification_number (Union[Unset, str]): (W-IdNr.) Originally, the economic identification number was
                intended as a uniform and permanent identification feature in accordance with Section 139a Paragraph 1 AO for
                the purpose of clear identification in the taxation process. In addition, the business identification number
                will also serve as a nationwide business number for companies in accordance with Section 2 Paragraph 1 UBRegG
                (Corporate Basic Data Register Act). The economic identification number for the purpose of taxation procedures
                is described in more detail in Section 139c AO and is issued to economically active persons. Example:
                DE812277765.
            economic_identification_number_differentiator (Union[Unset, str]): (W-IdNr. Unterscheidungsmerkmal) For each
                economically active person, the economic identification number is supplemented by a five-digit distinguishing
                feature for each of their economic activities, each of their businesses and for each of their permanent
                establishments, so that the activities, businesses and permanent establishments of the economically active
                person can be clearly identified in taxation procedures. The Federal Central Tax Office assigns the distinctive
                feature 00001 to the first economic activity of the economically active person, their first business or their
                first permanent establishment. At the request of the responsible tax authority, the Federal Central Tax Office
                continually assigns each additional economic activity, each additional business and each additional permanent
                establishment of the economically active person its own distinguishing feature.. Example: 00001.
            current_short_name (Union[Unset, str]): (Name kurz) Current short name of the addressee (= value as at system
                date). Example: Muster.
            short_names (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'Muster',
                'valid_from': '2020-12-20'}, {'value': 'Muster', 'valid_from': '2020-12-20'}, {'value': 'Muster', 'valid_from':
                '2020-12-20'}].
            status (Union[Unset, MasterClientFullAddresseeStatus]): (Status) Indicates whether the addressee is active or
                inactive.  Example: active.
            surrogate_name (Union[Unset, str]): (Alternativer Suchname) Alias of an addressee for search purposes. Example:
                Meier.
            timestamp (Union[Unset, datetime.datetime]): (Zeitstempel) Indicates when the addressee was last edited.
            current_company_name (Union[Unset, str]): (Unternehmensname) The company name. (= value as at system date)
                Example: Schreinerei Mustermann.
            company_names (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'Schreinerei
                Mustermann', 'valid_from': '2020-12-20'}, {'value': 'Schreinerei Mustermann', 'valid_from': '2020-12-20'},
                {'value': 'Schreinerei Mustermann', 'valid_from': '2020-12-20'}].
            date_of_foundation (Union[Unset, datetime.date]): (Gründungsdatum) Date on which an operational commercial
                enterprise is established (date of foundation).
            current_legal_form_id (Union[Unset, MasterClientFullAddresseeCurrentLegalFormId]): (Rechtsform) Current legal
                form of the enterprise (= value as at system date). The following values are permissible (S01101=Aktiebolag,
                S00010=Aktiengesellschaft, S00110=Aktiengesellschaft, S00112=AG & Co. KG, S00019=AG & Co. KG,
                S00049=Aktiengesellschaft & Co. OHG, S00130=AG & Still, S01502=Anstalt d. priv. Rechts, S00031=Anstalt des
                öffentlichen Rechts, S00109=Arbeitsgemeinschaft, S00122=Atypische Stille Gesellschaft, S00061=Atypische Stille
                Gesellschaft, S00059=Behörde, Amt, S00013=Bergrechtliche Gewerkschaft, S00051=Bruchteilsgemeinschaft,
                S00012=Eingetragene Genossenschaft, S00015=Eingetragener Verein, S00001=Einzelkaufmann,
                S00101=Einzelunternehmer, S00026=Erbengemeinschaft, S00035=Europäische wirtschaftliche Interessenvereinigung,
                S00002=Freier Beruf, S00102=Freier Beruf, S00006=Gesellschaft des bürgerlichen Rechts, S00025=Gemeinschaft,
                S00113=Genossenschaft beschränkte Haftung, S00114=Genossenschaft unbeschränkte Haftung, S00107=Gesellschaft
                bürgerlichen Rechts, S00036=Gewerkschaft, S00054=gemeinnützige GmbH, S00009=Gesellschaft mit beschränkter
                Haftung, S00105=Gesellschaft mit beschränkter Haftung, S00115=GmbH & Co. KG, S00007=GmbH & Co. KG, S00052=GmbH &
                Co. KGaA, S00048=GmbH & Co. OHG, S00129=GmbH & Still, S00053=GmbH i.G., S00057=GmbH I.L.,
                S00050=Grundstücksgemeinschaft, S00121=Grundstücksgemeinschaft, S01402=Inc.,
                S00062=Investmentkommanditgesellschaft, S00063=gemeinnützige Unternehmergesellschaft (haftungsbeschränkt),
                S00064=Stiftung & Co. KG, S00065=eingetragene Gesellschaft bürgerlichen Rechts, S00056=Jur. Person kirchl.
                Rechts, S00022=Körperschaft des öffentlichen Rechts, S00005=Kommanditgesellschaft, S00111=Kommanditgesellschaft,
                S00011=Kommanditgesellschaft auf Aktien, S00017=Kleingewerbe, S00104=Kleingewerbe, S00020=Komplementär GmbH,
                S00126=Körperschaft des öffentlichen Rechts, S01701=Sociedade Limitada , S00024=Limited, S01401=Limited
                Liability Company , S01403=Limited Liability Partnership , S00802=limited partnership, S00804=private company
                limited by shares, S00037=Limited & Co. KG, S00003=Land- und Forstwirtschaftliches Einzelunternehmen,
                S00103=Land- und Forstwirtschaftliches Einzelunternehmen, S00123=Miteigentümerschaft, S00029=Nicht eingetragener
                Verein, S00106=Offene Gesellschaft, S00004=Offene Handelsgesellschaft, S00038=OHG & Co. KG, S01201=Osakeyhtiö,
                S00018=Partnerschaftsgesellschaft, S00060=Partnerschaftsgesellschaft mit beschränkter Berufshaftung,
                S00803=public company limited by shares, S00039=Politische Partei, S00118=Privatstiftung, S00040=Reederei,
                S01601=Sociedad Anónima, S01702=Sociedade Anónima, S01603=Sociedad Limitada, S01602=Sociedad de Responsabilidad
                Limitada, S01301=Společnost s ručením omezeným , S00034=Europäische Genossenschaft (mit Vorstand/Aufsichtsrat),
                S00033=Europäische Genossenschaft (mit Verwaltungsrat), S00021=Europäische Aktiengesellschaft (mit
                Vorstand/Aufsichtsrat), S00032=Europäische Aktiengesellschaft (mit Verwaltungsrat), S00041=Seerechtliche
                Gesellschaft, S00014=Sonstige, S00027=Sonstige & Co. KG, S00028=Sonstige & Co. OHG, S00023=Sonstige juristische
                Person des privaten Rechts, S00030=Sonstige Kapitalgesellschaft, S00008=Sonstige Personengesellschaft,
                S00047=Sonstiges Einzelunternehmen, S00124=Sparkasse, S00117=Stiftung altes Recht, S00042=Stiftung des
                öffentlichen Rechts, S00016=Stiftung des Privatrechts, S00128=Stille Gesellschaft, S01501=Treuunternehmen reg.,
                S00055=Unternehmerges. (haftungsbeschr.)& Co KG, S00046=Unternehmergesellschaft (haftungsbeschränkt),
                S00043=Verband, S00116=Verein, S00058=Versicherungsverein auf Aktien, S00044=Versicherungsverein auf
                Gegenseitigkeit, S00045=Wohnungseigentümergemeinschaft).

                The property may only be filled if the addressee is of the type 'legal_person'. Example: S00009.
            legal_form_ids (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'S00009',
                'valid_from': '2020-12-20'}, {'value': 'S00009', 'valid_from': '2020-12-20'}, {'value': 'S00009', 'valid_from':
                '2020-12-20'}].
            date_of_birth (Union[Unset, datetime.date]): (Geburtsdatum) Date of birth of a natural person. Example:
                1988-11-25.
            etin (Union[Unset, str]): (eTIN) The eTIN is an income tax-related identification number given to every employee
                in Germany; the legal basis is Section 41b (2) of the German Income Tax Act (EStG). However, the calculation
                method does not exclude the possibility that the same eTIN might be assigned to more than one person. As it is
                sufficiently unlikely, however, that two different people with the same eTIN fall within the jurisdiction of the
                same tax authority, this is acceptable for the purposes of the eTIN. The eTIN is a 14-character code that is
                made up of the following personal data; last name, first name, and date of birth; it comprises the upper-case
                letters A to Z, as well as the digits 0 to 9. As long as this personal data does not change (e.g. a change of
                name upon marriage), the eTIN will remain valid; otherwise, it has to be amended to reflect the change in name.
                Example: MLLRSTFN99J17B.
            firstname (Union[Unset, str]): (Vorname) First name of a natural person. Example: Josef.
            politically_exposed_person (Union[Unset, bool]): (Politisch exponierte Person) Indicates wether the addressee is
                a politically exposed person (PEP).
            sex (Union[Unset, MasterClientFullAddresseeSex]): (Geschlecht) Gender of a natural person. Example: male.
            current_surname (Union[Unset, str]): (Nachname) Current last name of a natural person (= value as at system
                date). Example: Mustermann.
            surnames (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'Mustermann',
                'valid_from': '2020-12-20'}, {'value': 'Mustermann', 'valid_from': '2020-12-20'}, {'value': 'Mustermann',
                'valid_from': '2020-12-20'}].
            tax_identification_number (Union[Unset, str]): (Steueridentifikationsnummer) The natural person's tax
                identification number as issued by German financial authorities. Example: 52618937442.
            detail (Union[Unset, MasterClientFullAddresseeDetail]): (Persönliche Daten bzw. Unternehmensdaten) Personal or
                corporate data for the addressee.
            addresses (Union[Unset, list['MasterClientFullAddress']]): (Adressen) Addresses of an addressee.
            communications (Union[Unset, list['MasterClientFullCommunication']]): (Kommunikationsverbindungen) Communication
                data of an addressee.
            bank_accounts (Union[Unset, list['MasterClientFullBankAccount']]): (Bankverbindungen) Bank accounts of an
                addressee.
            tax_offices (Union[Unset, list['MasterClientFullTaxOffice']]): (Finanzamt) Tax offices of an addressee.
            children (Union[Unset, list['MasterClientFullAddresseeChild']]): (Kinder) Children of a natural person.
            contact_persons (Union[Unset, list['MasterClientFullAddresseeContactPerson']]): (Ansprechpartner) Contact
                persons of an addressee.
            legal_representatives_of_company (Union[Unset, list['MasterClientFullAddresseeLegalRepresentativeOfCompany']]):
                (Gesetzliche Vertreter des Unternehmens) Legal representatives of a legal person.
            legal_representatives_of_natural_person (Union[Unset,
                list['MasterClientFullAddresseeLegalRepresentativeOfNaturalPerson']]): (Gesetzliche Vertreter der Person) Legal
                representatives of a natural person.
            ultimate_beneficial_owners (Union[Unset, list['MasterClientFullAddresseeUltimateBeneficialOwner']]):
                (Wirtschaftliche Berechtigte) Ultimate benefical owner of an addressee.
            proprietor (Union[Unset, MasterClientFullAddresseeProprietor]): (Angaben zum Betriebsinhaber) Proprietor
                specific data.
     """

    type_: MasterClientFullAddresseeType
    id: Union[Unset, UUID] = UNSET
    eu_vat_id_country_code: Union[Unset, str] = UNSET
    eu_vat_id_number: Union[Unset, str] = UNSET
    economic_identification_number: Union[Unset, str] = UNSET
    economic_identification_number_differentiator: Union[Unset, str] = UNSET
    current_short_name: Union[Unset, str] = UNSET
    short_names: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    status: Union[Unset, MasterClientFullAddresseeStatus] = UNSET
    surrogate_name: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    current_company_name: Union[Unset, str] = UNSET
    company_names: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    date_of_foundation: Union[Unset, datetime.date] = UNSET
    current_legal_form_id: Union[Unset, MasterClientFullAddresseeCurrentLegalFormId] = UNSET
    legal_form_ids: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    date_of_birth: Union[Unset, datetime.date] = UNSET
    etin: Union[Unset, str] = UNSET
    firstname: Union[Unset, str] = UNSET
    politically_exposed_person: Union[Unset, bool] = UNSET
    sex: Union[Unset, MasterClientFullAddresseeSex] = UNSET
    current_surname: Union[Unset, str] = UNSET
    surnames: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    tax_identification_number: Union[Unset, str] = UNSET
    detail: Union[Unset, 'MasterClientFullAddresseeDetail'] = UNSET
    addresses: Union[Unset, list['MasterClientFullAddress']] = UNSET
    communications: Union[Unset, list['MasterClientFullCommunication']] = UNSET
    bank_accounts: Union[Unset, list['MasterClientFullBankAccount']] = UNSET
    tax_offices: Union[Unset, list['MasterClientFullTaxOffice']] = UNSET
    children: Union[Unset, list['MasterClientFullAddresseeChild']] = UNSET
    contact_persons: Union[Unset, list['MasterClientFullAddresseeContactPerson']] = UNSET
    legal_representatives_of_company: Union[Unset, list['MasterClientFullAddresseeLegalRepresentativeOfCompany']] = UNSET
    legal_representatives_of_natural_person: Union[Unset, list['MasterClientFullAddresseeLegalRepresentativeOfNaturalPerson']] = UNSET
    ultimate_beneficial_owners: Union[Unset, list['MasterClientFullAddresseeUltimateBeneficialOwner']] = UNSET
    proprietor: Union[Unset, 'MasterClientFullAddresseeProprietor'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.master_client_full_address import MasterClientFullAddress
        from ..models.master_client_full_addressee_proprietor import MasterClientFullAddresseeProprietor
        from ..models.master_client_full_addressee_ultimate_beneficial_owner import MasterClientFullAddresseeUltimateBeneficialOwner
        from ..models.master_client_full_addressee_contact_person import MasterClientFullAddresseeContactPerson
        from ..models.master_client_full_bank_account import MasterClientFullBankAccount
        from ..models.master_client_full_historical_value_string import MasterClientFullHistoricalValueString
        from ..models.master_client_full_addressee_detail import MasterClientFullAddresseeDetail
        from ..models.master_client_full_tax_office import MasterClientFullTaxOffice
        from ..models.master_client_full_addressee_child import MasterClientFullAddresseeChild
        from ..models.master_client_full_communication import MasterClientFullCommunication
        from ..models.master_client_full_addressee_legal_representative_of_company import MasterClientFullAddresseeLegalRepresentativeOfCompany
        from ..models.master_client_full_addressee_legal_representative_of_natural_person import MasterClientFullAddresseeLegalRepresentativeOfNaturalPerson
        type_ = self.type_.value

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        eu_vat_id_country_code = self.eu_vat_id_country_code

        eu_vat_id_number = self.eu_vat_id_number

        economic_identification_number = self.economic_identification_number

        economic_identification_number_differentiator = self.economic_identification_number_differentiator

        current_short_name = self.current_short_name

        short_names: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.short_names, Unset):
            short_names = []
            for short_names_item_data in self.short_names:
                short_names_item = short_names_item_data.to_dict()
                short_names.append(short_names_item)



        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        surrogate_name = self.surrogate_name

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        current_company_name = self.current_company_name

        company_names: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.company_names, Unset):
            company_names = []
            for company_names_item_data in self.company_names:
                company_names_item = company_names_item_data.to_dict()
                company_names.append(company_names_item)



        date_of_foundation: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_foundation, Unset):
            date_of_foundation = self.date_of_foundation.isoformat()

        current_legal_form_id: Union[Unset, str] = UNSET
        if not isinstance(self.current_legal_form_id, Unset):
            current_legal_form_id = self.current_legal_form_id.value


        legal_form_ids: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.legal_form_ids, Unset):
            legal_form_ids = []
            for legal_form_ids_item_data in self.legal_form_ids:
                legal_form_ids_item = legal_form_ids_item_data.to_dict()
                legal_form_ids.append(legal_form_ids_item)



        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        etin = self.etin

        firstname = self.firstname

        politically_exposed_person = self.politically_exposed_person

        sex: Union[Unset, str] = UNSET
        if not isinstance(self.sex, Unset):
            sex = self.sex.value


        current_surname = self.current_surname

        surnames: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.surnames, Unset):
            surnames = []
            for surnames_item_data in self.surnames:
                surnames_item = surnames_item_data.to_dict()
                surnames.append(surnames_item)



        tax_identification_number = self.tax_identification_number

        detail: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)



        communications: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.communications, Unset):
            communications = []
            for communications_item_data in self.communications:
                communications_item = communications_item_data.to_dict()
                communications.append(communications_item)



        bank_accounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bank_accounts, Unset):
            bank_accounts = []
            for bank_accounts_item_data in self.bank_accounts:
                bank_accounts_item = bank_accounts_item_data.to_dict()
                bank_accounts.append(bank_accounts_item)



        tax_offices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tax_offices, Unset):
            tax_offices = []
            for tax_offices_item_data in self.tax_offices:
                tax_offices_item = tax_offices_item_data.to_dict()
                tax_offices.append(tax_offices_item)



        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)



        contact_persons: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.contact_persons, Unset):
            contact_persons = []
            for contact_persons_item_data in self.contact_persons:
                contact_persons_item = contact_persons_item_data.to_dict()
                contact_persons.append(contact_persons_item)



        legal_representatives_of_company: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.legal_representatives_of_company, Unset):
            legal_representatives_of_company = []
            for legal_representatives_of_company_item_data in self.legal_representatives_of_company:
                legal_representatives_of_company_item = legal_representatives_of_company_item_data.to_dict()
                legal_representatives_of_company.append(legal_representatives_of_company_item)



        legal_representatives_of_natural_person: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.legal_representatives_of_natural_person, Unset):
            legal_representatives_of_natural_person = []
            for legal_representatives_of_natural_person_item_data in self.legal_representatives_of_natural_person:
                legal_representatives_of_natural_person_item = legal_representatives_of_natural_person_item_data.to_dict()
                legal_representatives_of_natural_person.append(legal_representatives_of_natural_person_item)



        ultimate_beneficial_owners: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ultimate_beneficial_owners, Unset):
            ultimate_beneficial_owners = []
            for ultimate_beneficial_owners_item_data in self.ultimate_beneficial_owners:
                ultimate_beneficial_owners_item = ultimate_beneficial_owners_item_data.to_dict()
                ultimate_beneficial_owners.append(ultimate_beneficial_owners_item)



        proprietor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.proprietor, Unset):
            proprietor = self.proprietor.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if eu_vat_id_country_code is not UNSET:
            field_dict["eu_vat_id_country_code"] = eu_vat_id_country_code
        if eu_vat_id_number is not UNSET:
            field_dict["eu_vat_id_number"] = eu_vat_id_number
        if economic_identification_number is not UNSET:
            field_dict["economic_identification_number"] = economic_identification_number
        if economic_identification_number_differentiator is not UNSET:
            field_dict["economic_identification_number_differentiator"] = economic_identification_number_differentiator
        if current_short_name is not UNSET:
            field_dict["current_short_name"] = current_short_name
        if short_names is not UNSET:
            field_dict["short_names"] = short_names
        if status is not UNSET:
            field_dict["status"] = status
        if surrogate_name is not UNSET:
            field_dict["surrogate_name"] = surrogate_name
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if current_company_name is not UNSET:
            field_dict["current_company_name"] = current_company_name
        if company_names is not UNSET:
            field_dict["company_names"] = company_names
        if date_of_foundation is not UNSET:
            field_dict["date_of_foundation"] = date_of_foundation
        if current_legal_form_id is not UNSET:
            field_dict["current_legal_form_id"] = current_legal_form_id
        if legal_form_ids is not UNSET:
            field_dict["legal_form_ids"] = legal_form_ids
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if etin is not UNSET:
            field_dict["etin"] = etin
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if politically_exposed_person is not UNSET:
            field_dict["politically_exposed_person"] = politically_exposed_person
        if sex is not UNSET:
            field_dict["sex"] = sex
        if current_surname is not UNSET:
            field_dict["current_surname"] = current_surname
        if surnames is not UNSET:
            field_dict["surnames"] = surnames
        if tax_identification_number is not UNSET:
            field_dict["tax_identification_number"] = tax_identification_number
        if detail is not UNSET:
            field_dict["detail"] = detail
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if communications is not UNSET:
            field_dict["communications"] = communications
        if bank_accounts is not UNSET:
            field_dict["bank_accounts"] = bank_accounts
        if tax_offices is not UNSET:
            field_dict["tax_offices"] = tax_offices
        if children is not UNSET:
            field_dict["children"] = children
        if contact_persons is not UNSET:
            field_dict["contact_persons"] = contact_persons
        if legal_representatives_of_company is not UNSET:
            field_dict["legal_representatives_of_company"] = legal_representatives_of_company
        if legal_representatives_of_natural_person is not UNSET:
            field_dict["legal_representatives_of_natural_person"] = legal_representatives_of_natural_person
        if ultimate_beneficial_owners is not UNSET:
            field_dict["ultimate_beneficial_owners"] = ultimate_beneficial_owners
        if proprietor is not UNSET:
            field_dict["proprietor"] = proprietor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.master_client_full_address import MasterClientFullAddress
        from ..models.master_client_full_addressee_proprietor import MasterClientFullAddresseeProprietor
        from ..models.master_client_full_addressee_ultimate_beneficial_owner import MasterClientFullAddresseeUltimateBeneficialOwner
        from ..models.master_client_full_addressee_contact_person import MasterClientFullAddresseeContactPerson
        from ..models.master_client_full_bank_account import MasterClientFullBankAccount
        from ..models.master_client_full_historical_value_string import MasterClientFullHistoricalValueString
        from ..models.master_client_full_addressee_detail import MasterClientFullAddresseeDetail
        from ..models.master_client_full_tax_office import MasterClientFullTaxOffice
        from ..models.master_client_full_addressee_child import MasterClientFullAddresseeChild
        from ..models.master_client_full_communication import MasterClientFullCommunication
        from ..models.master_client_full_addressee_legal_representative_of_company import MasterClientFullAddresseeLegalRepresentativeOfCompany
        from ..models.master_client_full_addressee_legal_representative_of_natural_person import MasterClientFullAddresseeLegalRepresentativeOfNaturalPerson
        d = src_dict.copy()
        type_ = MasterClientFullAddresseeType(d.pop("type"))




        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        eu_vat_id_country_code = d.pop("eu_vat_id_country_code", UNSET)

        eu_vat_id_number = d.pop("eu_vat_id_number", UNSET)

        economic_identification_number = d.pop("economic_identification_number", UNSET)

        economic_identification_number_differentiator = d.pop("economic_identification_number_differentiator", UNSET)

        current_short_name = d.pop("current_short_name", UNSET)

        short_names = []
        _short_names = d.pop("short_names", UNSET)
        for short_names_item_data in (_short_names or []):
            short_names_item = MasterClientFullHistoricalValueString.from_dict(short_names_item_data)



            short_names.append(short_names_item)


        _status = d.pop("status", UNSET)
        status: Union[Unset, MasterClientFullAddresseeStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = MasterClientFullAddresseeStatus(_status)




        surrogate_name = d.pop("surrogate_name", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp,  Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)




        current_company_name = d.pop("current_company_name", UNSET)

        company_names = []
        _company_names = d.pop("company_names", UNSET)
        for company_names_item_data in (_company_names or []):
            company_names_item = MasterClientFullHistoricalValueString.from_dict(company_names_item_data)



            company_names.append(company_names_item)


        _date_of_foundation = d.pop("date_of_foundation", UNSET)
        date_of_foundation: Union[Unset, datetime.date]
        if isinstance(_date_of_foundation,  Unset):
            date_of_foundation = UNSET
        else:
            date_of_foundation = isoparse(_date_of_foundation).date()




        _current_legal_form_id = d.pop("current_legal_form_id", UNSET)
        current_legal_form_id: Union[Unset, MasterClientFullAddresseeCurrentLegalFormId]
        if isinstance(_current_legal_form_id,  Unset):
            current_legal_form_id = UNSET
        else:
            current_legal_form_id = MasterClientFullAddresseeCurrentLegalFormId(_current_legal_form_id)




        legal_form_ids = []
        _legal_form_ids = d.pop("legal_form_ids", UNSET)
        for legal_form_ids_item_data in (_legal_form_ids or []):
            legal_form_ids_item = MasterClientFullHistoricalValueString.from_dict(legal_form_ids_item_data)



            legal_form_ids.append(legal_form_ids_item)


        _date_of_birth = d.pop("date_of_birth", UNSET)
        date_of_birth: Union[Unset, datetime.date]
        if isinstance(_date_of_birth,  Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth).date()




        etin = d.pop("etin", UNSET)

        firstname = d.pop("firstname", UNSET)

        politically_exposed_person = d.pop("politically_exposed_person", UNSET)

        _sex = d.pop("sex", UNSET)
        sex: Union[Unset, MasterClientFullAddresseeSex]
        if isinstance(_sex,  Unset):
            sex = UNSET
        else:
            sex = MasterClientFullAddresseeSex(_sex)




        current_surname = d.pop("current_surname", UNSET)

        surnames = []
        _surnames = d.pop("surnames", UNSET)
        for surnames_item_data in (_surnames or []):
            surnames_item = MasterClientFullHistoricalValueString.from_dict(surnames_item_data)



            surnames.append(surnames_item)


        tax_identification_number = d.pop("tax_identification_number", UNSET)

        _detail = d.pop("detail", UNSET)
        detail: Union[Unset, MasterClientFullAddresseeDetail]
        if isinstance(_detail,  Unset):
            detail = UNSET
        else:
            detail = MasterClientFullAddresseeDetail.from_dict(_detail)




        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in (_addresses or []):
            addresses_item = MasterClientFullAddress.from_dict(addresses_item_data)



            addresses.append(addresses_item)


        communications = []
        _communications = d.pop("communications", UNSET)
        for communications_item_data in (_communications or []):
            communications_item = MasterClientFullCommunication.from_dict(communications_item_data)



            communications.append(communications_item)


        bank_accounts = []
        _bank_accounts = d.pop("bank_accounts", UNSET)
        for bank_accounts_item_data in (_bank_accounts or []):
            bank_accounts_item = MasterClientFullBankAccount.from_dict(bank_accounts_item_data)



            bank_accounts.append(bank_accounts_item)


        tax_offices = []
        _tax_offices = d.pop("tax_offices", UNSET)
        for tax_offices_item_data in (_tax_offices or []):
            tax_offices_item = MasterClientFullTaxOffice.from_dict(tax_offices_item_data)



            tax_offices.append(tax_offices_item)


        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in (_children or []):
            children_item = MasterClientFullAddresseeChild.from_dict(children_item_data)



            children.append(children_item)


        contact_persons = []
        _contact_persons = d.pop("contact_persons", UNSET)
        for contact_persons_item_data in (_contact_persons or []):
            contact_persons_item = MasterClientFullAddresseeContactPerson.from_dict(contact_persons_item_data)



            contact_persons.append(contact_persons_item)


        legal_representatives_of_company = []
        _legal_representatives_of_company = d.pop("legal_representatives_of_company", UNSET)
        for legal_representatives_of_company_item_data in (_legal_representatives_of_company or []):
            legal_representatives_of_company_item = MasterClientFullAddresseeLegalRepresentativeOfCompany.from_dict(legal_representatives_of_company_item_data)



            legal_representatives_of_company.append(legal_representatives_of_company_item)


        legal_representatives_of_natural_person = []
        _legal_representatives_of_natural_person = d.pop("legal_representatives_of_natural_person", UNSET)
        for legal_representatives_of_natural_person_item_data in (_legal_representatives_of_natural_person or []):
            legal_representatives_of_natural_person_item = MasterClientFullAddresseeLegalRepresentativeOfNaturalPerson.from_dict(legal_representatives_of_natural_person_item_data)



            legal_representatives_of_natural_person.append(legal_representatives_of_natural_person_item)


        ultimate_beneficial_owners = []
        _ultimate_beneficial_owners = d.pop("ultimate_beneficial_owners", UNSET)
        for ultimate_beneficial_owners_item_data in (_ultimate_beneficial_owners or []):
            ultimate_beneficial_owners_item = MasterClientFullAddresseeUltimateBeneficialOwner.from_dict(ultimate_beneficial_owners_item_data)



            ultimate_beneficial_owners.append(ultimate_beneficial_owners_item)


        _proprietor = d.pop("proprietor", UNSET)
        proprietor: Union[Unset, MasterClientFullAddresseeProprietor]
        if isinstance(_proprietor,  Unset):
            proprietor = UNSET
        else:
            proprietor = MasterClientFullAddresseeProprietor.from_dict(_proprietor)




        master_client_full_addressee = cls(
            type_=type_,
            id=id,
            eu_vat_id_country_code=eu_vat_id_country_code,
            eu_vat_id_number=eu_vat_id_number,
            economic_identification_number=economic_identification_number,
            economic_identification_number_differentiator=economic_identification_number_differentiator,
            current_short_name=current_short_name,
            short_names=short_names,
            status=status,
            surrogate_name=surrogate_name,
            timestamp=timestamp,
            current_company_name=current_company_name,
            company_names=company_names,
            date_of_foundation=date_of_foundation,
            current_legal_form_id=current_legal_form_id,
            legal_form_ids=legal_form_ids,
            date_of_birth=date_of_birth,
            etin=etin,
            firstname=firstname,
            politically_exposed_person=politically_exposed_person,
            sex=sex,
            current_surname=current_surname,
            surnames=surnames,
            tax_identification_number=tax_identification_number,
            detail=detail,
            addresses=addresses,
            communications=communications,
            bank_accounts=bank_accounts,
            tax_offices=tax_offices,
            children=children,
            contact_persons=contact_persons,
            legal_representatives_of_company=legal_representatives_of_company,
            legal_representatives_of_natural_person=legal_representatives_of_natural_person,
            ultimate_beneficial_owners=ultimate_beneficial_owners,
            proprietor=proprietor,
        )


        master_client_full_addressee.additional_properties = d
        return master_client_full_addressee

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
