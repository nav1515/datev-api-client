from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_client_full_addressee_detail_country_of_birth import MasterClientFullAddresseeDetailCountryOfBirth
from ..models.master_client_full_addressee_detail_current_consideration import MasterClientFullAddresseeDetailCurrentConsideration
from ..models.master_client_full_addressee_detail_current_distribution_of_profit import MasterClientFullAddresseeDetailCurrentDistributionOfProfit
from ..models.master_client_full_addressee_detail_current_federal_state_of_legal_person import MasterClientFullAddresseeDetailCurrentFederalStateOfLegalPerson
from ..models.master_client_full_addressee_detail_current_federal_state_of_natural_person import MasterClientFullAddresseeDetailCurrentFederalStateOfNaturalPerson
from ..models.master_client_full_addressee_detail_current_kind_of_register_court import MasterClientFullAddresseeDetailCurrentKindOfRegisterCourt
from ..models.master_client_full_addressee_detail_current_marital_status import MasterClientFullAddresseeDetailCurrentMaritalStatus
from ..models.master_client_full_addressee_detail_name_prefix import MasterClientFullAddresseeDetailNamePrefix
from ..models.master_client_full_addressee_detail_national_right import MasterClientFullAddresseeDetailNationalRight
from ..models.master_client_full_addressee_detail_nationality import MasterClientFullAddresseeDetailNationality
from ..models.master_client_full_addressee_detail_paper_of_identity import MasterClientFullAddresseeDetailPaperOfIdentity
from ..models.master_client_full_addressee_detail_title_of_nobility import MasterClientFullAddresseeDetailTitleOfNobility
from ..models.master_client_full_addressee_detail_winding_up_proceedings import MasterClientFullAddresseeDetailWindingUpProceedings
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.master_client_full_historical_value_integer import MasterClientFullHistoricalValueInteger
  from ..models.master_client_full_historical_value_string import MasterClientFullHistoricalValueString
  from ..models.master_client_full_addressee_detail_other_nationality import MasterClientFullAddresseeDetailOtherNationality





T = TypeVar("T", bound="MasterClientFullAddresseeDetail")



@_attrs_define
class MasterClientFullAddresseeDetail:
    """ (Persönliche Daten bzw. Unternehmensdaten) Personal or corporate data for the addressee.

        Attributes:
            complimentary_close (Union[Unset, str]): (Grußformel) The complimentary close defines the sign-off used for an
                addressee in correspondence. Example: Mit freundlichen Grüßen.
            correspondence_title (Union[Unset, str]): (Anrede) The title is the way in which an addressee is addressed.
                Examples are "Ms." or "Mr." Example: Herrn.
            national_right (Union[Unset, MasterClientFullAddresseeDetailNationalRight]): (Nationales Recht) Indicates which
                national law governs the provision of services to the addressee. Accounting may, for example, be carried out in
                accordance with Austrian law. It is currently possible to choose between German (DE) and Austrian (AT) law.
                Example: DE.
            note (Union[Unset, str]): (Notiz) Note about an addressee (free text). Example: Notiz zu Adressat Erwin
                Mustermeier.
            salutation (Union[Unset, str]): (Briefanrede) Salutation for correspondence as it appears in letters. Example:
                Sehr geehrte Damen und Herren,.
            current_code_of_classification_of_economic_activities_2008 (Union[Unset, str]): (Klassifikation der
                Wirtschszweige nach WZ 2008/Branchenschlüssel) Current (= value as at system date) code of classification of
                economic activities as per the 2008 classification. These codes are used to classify enterprises by industry,
                type and sector. The code is a prerequisite for comparing enterprises. This code is the official code of the
                German Federal Statistical Office (w/o DATEV extensions Example: 43.32.0.
            codes_of_classification_of_economic_activities_2008 (Union[Unset,
                list['MasterClientFullHistoricalValueString']]):  Example: [{'value': '43.32.0', 'valid_from': '2020-12-20'},
                {'value': '43.32.0', 'valid_from': '2020-12-20'}, {'value': '43.32.0', 'valid_from': '2020-12-20'}].
            current_description_of_classification_of_economic_activities_2008 (Union[Unset, str]): (Klassifikation der
                Wirtschaftszweige nach WZ 2008/Bezeichnungen) Current (= value as at system date) description of classification
                of economic activities as per the 2008 classification. Example: Bautischlerei und -schlosserei.
            descriptions_of_classification_of_economic_activities_2008 (Union[Unset,
                list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'Bautischlerei und -schlosserei',
                'valid_from': '2020-12-20'}, {'value': 'Bautischlerei und -schlosserei', 'valid_from': '2020-12-20'}, {'value':
                'Bautischlerei und -schlosserei', 'valid_from': '2020-12-20'}].
            current_mad_code_of_classification_of_economic_activities_2008 (Union[Unset, str]): (Klassifikation der
                Wirtschaftsszweige nach WZ 2008/Branchenschlüssel MAD) Current (= value as at system date) code (MAD) of
                classification of economic activities as per the 2008 classification. Example: D01.00FF43.32.0000000000000000.
            mad_codes_of_classification_of_economic_activities_2008 (Union[Unset,
                list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'D01.00FF43.32.0000000000000000',
                'valid_from': '2020-12-20'}, {'value': 'D01.00FF43.32.0000000000000000', 'valid_from': '2020-12-20'}, {'value':
                'D01.00FF43.32.0000000000000000', 'valid_from': '2020-12-20'}].
            current_code_of_classification_of_economic_activities_2003 (Union[Unset, str]): (Klassifikation der
                Wirtschaftszweige nach WZ 2003/Branchenschlüssel) Current (= value as at system date) code of classification of
                economic activities as per the 2003 classification. These codes are used to classify enterprises by industry,
                type and sector. The code is a prerequisite for comparing enterprises. This code is the official code of the
                German Federal Statistical Office (w/o DATEV extensions Example: 45.42.0.
            codes_of_classification_of_economic_activities_2003 (Union[Unset,
                list['MasterClientFullHistoricalValueString']]):  Example: [{'value': '45.42.0', 'valid_from': '2020-12-20'},
                {'value': '45.42.0', 'valid_from': '2020-12-20'}, {'value': '45.42.0', 'valid_from': '2020-12-20'}].
            current_description_of_classification_of_economic_activities_2003 (Union[Unset, str]): (Klassifikation der
                Wirtschaftszweige nach WZ 2003/Bezeichnungen) Current (= value as at system date) description of classification
                of economic activities as per the 2003 classification. Example: Bautischlerei und -schlosserei.
            descriptions_of_classification_of_economic_activities_2003 (Union[Unset,
                list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'Bautischlerei und -schlosserei',
                'valid_from': '2020-12-20'}, {'value': 'Bautischlerei und -schlosserei', 'valid_from': '2020-12-20'}, {'value':
                'Bautischlerei und -schlosserei', 'valid_from': '2020-12-20'}].
            current_mad_code_of_classification_of_economic_activities_2003 (Union[Unset, str]): (Klassifikation der
                Wirtschaftszweige nach WZ 2003/Branchenschlüssel MAD) Current (= value as at system date) code (MAD) of
                classification of economic activities as per the 2003 classification. Example: 01.00AFA45.42.0000000000000000.
            mad_codes_of_classification_of_economic_activities_2003 (Union[Unset,
                list['MasterClientFullHistoricalValueString']]):  Example: [{'value': '01.00AFA45.42.0000000000000000',
                'valid_from': '2020-12-20'}, {'value': '01.00AFA45.42.0000000000000000', 'valid_from': '2020-12-20'}, {'value':
                '01.00AFA45.42.0000000000000000', 'valid_from': '2020-12-20'}].
            current_country_of_head_office (Union[Unset, str]): (Land des Firmensitzes) Current (= value as at system date)
                country in which the company has its head office. A list of all available country codes can be retrieved via
                `GET /country-codes`. Example: DE.
            countries_of_head_office (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value':
                'DE', 'valid_from': '2020-12-20'}, {'value': 'DE', 'valid_from': '2020-12-20'}, {'value': 'DE', 'valid_from':
                '2020-12-20'}].
            date_of_memorandum_of_association (Union[Unset, datetime.date]): (Gesellschaftsvertrag vom) Indicates the date
                of the memorandum of association.
            current_distribution_of_profit (Union[Unset, MasterClientFullAddresseeDetailCurrentDistributionOfProfit]): (Art
                der Ergebnisaufteilung) Indicates the method used to distribute profit (or loss) among the shareholders (= value
                as at system date). The following values are permissible (ANDERER=Anderer Aufteilungsschlüssel, BRUCH=Nach
                Bruchteilen, BRUCHAUTO=Nach Bruchteilen mit automatischer Ermittlung des Gesamtnenners, EINKAP=Nach eingezahltem
                Kapital, GEZKAP=Nach gezeichnetem Kapital, KOPFMKOMP=Automatische Aufteilung nach Köpfen mit Berücksichtigung
                der Komplementäre, KOPFOKOMP=Automatische Aufteilung nach Köpfen ohne Berücksichtigung der Komplementäre,
                PROZENT=Nach Prozentanteilen). Example: BRUCH.
            distributions_of_profit (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value':
                'BRUCH', 'valid_from': '2020-12-20'}, {'value': 'BRUCH', 'valid_from': '2020-12-20'}, {'value': 'BRUCH',
                'valid_from': '2020-12-20'}].
            current_enterprise_purpose (Union[Unset, str]): (Unternehmensgegenstand) The current activity or the main output
                that a company produces (= value as at system date). The main product line of a company can be derived from the
                enterprise purpose. Example: Schreinerei.
            enterprise_purposes (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value':
                'Schreinerei', 'valid_from': '2020-12-20'}, {'value': 'Schreinerei', 'valid_from': '2020-12-20'}, {'value':
                'Schreinerei', 'valid_from': '2020-12-20'}].
            current_federal_state_mad_of_legal_person (Union[Unset, int]): (Bundesland MAD) Current federal state (MAD) of
                the company (= value as at system date). A federal state is a subdivision of a federal country.
                "FederalStateMAD" (client address data) includes extensions. In addition to the federal states, the following
                values are required - "Berlin-Ost" (for measuring the contribution assessment ceiling), "Nordbaden" (for
                checking the tax authorities responsible for Nordbaden), and "Bremerhaven" (which has different rules to Bremen
                on the distribution of church tax). The following values are permissible (1 = Baden-Württemberg ohne Nordbaden,
                10 = Saarland, 11 = Schleswig-Holstein, 2 = Bayern, 3 = Berlin (ehem. West), 30 = Nordbaden, 31 = Bremerhaven, 4
                = Bremen ohne Bremerhaven, 41 = Berlin (ehem. Ost), 42 = Brandenburg, 43 = Mecklenburg-Vorpommern, 44 = Sachsen,
                45 = Sachsen-Anhalt, 46 = Thüringen, 5 = Hamburg, 6 = Hessen, 7 = Niedersachsen, 8 = Nordrhein-Westfalen, 9 =
                Rheinland-Pfalz). Example: 2.
            federal_states_mad_of_legal_person (Union[Unset, list['MasterClientFullHistoricalValueInteger']]):  Example:
                [{'value': '2', 'valid_from': '2020-12-20'}, {'value': '2', 'valid_from': '2020-12-20'}, {'value': '2',
                'valid_from': '2020-12-20'}].
            current_federal_state_of_legal_person (Union[Unset,
                MasterClientFullAddresseeDetailCurrentFederalStateOfLegalPerson]): (Bundesland) Current federal state of the
                company (= value as at system date). A federal state is a subdivision of a federal country. The values depend on
                the national law applicable to the natural/legal person. If national_right='DE', the following values are
                permissible (BAY=Bayern, BBG=Brandenburg, BDW=Baden-Württemberg, BER=Berlin, BRE=Bremen, HBG=Hamburg,
                HES=Hessen, MLB=Mecklenburg-Vorpommern, NRS=Niedersachsen, NRW=Nordrhein-Westfalen, RLP=Rheinland-Pfalz,
                SAA=Sachsen-Anhalt, SAC=Sachsen, SAR=Saarland, SWH=Schleswig-Holstein, THG=Thüringen). If national_right='AT',
                the following values are permissible (BGL=Burgenland, KTN=Kärnten, NOE=Niederösterreich, OOE=Oberösterreich,
                SBG=Salzburg, STM=Steiermark, TIR=Tirol, VBG=Vorarlberg, W=Wien). Example: BAY.
            federal_states_of_legal_person (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example:
                [{'value': 'BAY', 'valid_from': '2020-12-20'}, {'value': 'BAY', 'valid_from': '2020-12-20'}, {'value': 'BAY',
                'valid_from': '2020-12-20'}].
            current_fiscal_year (Union[Unset, str]): (Wirtschaftsjahr) Current fiscal year of the company (= value as at
                system date). The fiscal year indicates the date on which the fiscal year begins and the date on which the
                fiscal year ends. The fiscal year entry is valid for multiple years (e.g. 01013112 --> 01/01– 12/31 ; the fiscal
                year begins on January 1 and ends on December 31). Example: 01013112.
            fiscal_years (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value': '01013112',
                'valid_from': '2020-12-20'}, {'value': '01013112', 'valid_from': '2020-12-20'}, {'value': '01013112',
                'valid_from': '2020-12-20'}].
            current_kind_of_register_court (Union[Unset, MasterClientFullAddresseeDetailCurrentKindOfRegisterCourt]):
                (Registergerichtsart) The type of court register in which a company is registered with the court. The values
                depend on the national law applicable to the legal person. If the company is registered in Germany, the
                following values are permissible (GEN=Genossenschaftsregister, GRB=Grundbuch, HAN=Handelsregister,
                PAR=Partnerschaftsregister, VER=Vereinsregister, GES=Gesellschaftsregister). If the company is registered in
                Austria, the following values are permissible (FIR=Firmenbuch, GRU=Grundbuch, PRT=Partnerschaftsregister,
                VER=Vereinsregister). Example: HAN.
            kind_of_register_courts (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value':
                'HAN', 'valid_from': '2020-12-20'}, {'value': 'HAN', 'valid_from': '2020-12-20'}, {'value': 'HAN', 'valid_from':
                '2020-12-20'}].
            current_location_of_head_office (Union[Unset, str]): (Ort des Firmensitzes) Current location of head office (=
                value as at system date). Example: München.
            locations_of_head_office (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value':
                'München', 'valid_from': '2020-12-20'}, {'value': 'München', 'valid_from': '2020-12-20'}, {'value': 'München',
                'valid_from': '2020-12-20'}].
            current_name_of_register_court (Union[Unset, str]): (Registergerichtsbezeichnung) Name of register court (place
                of register court) (= value as at system date). Example: München.
            names_of_register_court (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value':
                'München', 'valid_from': '2020-12-20'}, {'value': 'München', 'valid_from': '2020-12-20'}, {'value': 'München',
                'valid_from': '2020-12-20'}].
            current_registered_company_name (Union[Unset, str]): (Firmenname laut Registergericht) Current company name as
                listed by the register court (= value as at system date). Example: Schreinerei Mustermeier GmbH.
            registered_company_names (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value':
                'Schreinerei Mustermeier GmbH', 'valid_from': '2020-12-20'}, {'value': 'Schreinerei Mustermeier GmbH',
                'valid_from': '2020-12-20'}, {'value': 'Schreinerei Mustermeier GmbH', 'valid_from': '2020-12-20'}].
            registration_date (Union[Unset, datetime.date]): (Eingetragen am) Date on which the company was entered into the
                register court. Example: 2008-08-22.
            current_registration_number (Union[Unset, str]): (Registernummer) Registration number of the company (= value as
                at system date). The registration number is the number under which a company is registered with a register
                court. Example: HRB 123.
            registration_numbers (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'HRB
                123', 'valid_from': '2020-12-20'}, {'value': 'HRB 123', 'valid_from': '2020-12-20'}, {'value': 'HRB 123',
                'valid_from': '2020-12-20'}].
            current_three_lined_company_name_first_line (Union[Unset, str]): (Unternehmensnamen 3 zeilig/1. Zeile) Current
                first line of the three-line company name (= value as at system date). Example: Mustermeier.
            three_lined_company_names_first_line (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example:
                [{'value': 'Mustermeier', 'valid_from': '2020-12-20'}, {'value': 'Mustermeier', 'valid_from': '2020-12-20'},
                {'value': 'Mustermeier', 'valid_from': '2020-12-20'}].
            current_three_lined_company_name_second_line (Union[Unset, str]): (Unternehmensnamen 3 zeilig/2. Zeile) Current
                second line of the three-line company name (= value as at system date). Example: Gesellschaft mit beschränkter
                Haftung.
            three_lined_company_names_second_line (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example:
                [{'value': 'Gesellschaft mit beschränkter Haftung', 'valid_from': '2020-12-20'}, {'value': 'Gesellschaft mit
                beschränkter Haftung', 'valid_from': '2020-12-20'}, {'value': 'Gesellschaft mit beschränkter Haftung',
                'valid_from': '2020-12-20'}].
            current_three_lined_company_name_third_line (Union[Unset, str]): (Unternehmensnamen 3 zeilig/3. Zeile) Current
                third line of the three-line company name (= value as at system date). Example: Schreinerei.
            three_lined_company_names_third_line (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example:
                [{'value': 'Schreinerei', 'valid_from': '2020-12-20'}, {'value': 'Schreinerei', 'valid_from': '2020-12-20'},
                {'value': 'Schreinerei', 'valid_from': '2020-12-20'}].
            current_two_lined_company_name_first_line (Union[Unset, str]): (Unternehmensnamen 2 zeilig/1. Zeile) Current
                first line of the two-line company name (= value as at system date). Example: Schreinerei Mustermeier.
            two_lined_company_names_first_line (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example:
                [{'value': 'Schreinerei Mustermeier', 'valid_from': '2020-12-20'}, {'value': 'Schreinerei Mustermeier',
                'valid_from': '2020-12-20'}, {'value': 'Schreinerei Mustermeier', 'valid_from': '2020-12-20'}].
            current_two_lined_company_name_second_line (Union[Unset, str]): (Unternehmensnamen 2 zeilig/2. Zeile) Current
                second line of the two-line company name (= value as at system date). Example: Gesellschaft mit beschränkter
                Haftung.
            two_lined_company_names_second_line (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example:
                [{'value': 'Gesellschaft mit beschränkter Haftung', 'valid_from': '2020-12-20'}, {'value': 'Gesellschaft mit
                beschränkter Haftung', 'valid_from': '2020-12-20'}, {'value': 'Gesellschaft mit beschränkter Haftung',
                'valid_from': '2020-12-20'}].
            winding_up_date (Union[Unset, datetime.date]): (Auflösungsdatum) Indicates the date on which a company was wound
                up.
            winding_up_proceedings (Union[Unset, MasterClientFullAddresseeDetailWindingUpProceedings]):
                (Auflösungsverfahren) In corporate and associations law, "winding-up" describes the start of the period in which
                the entity moves from commercial operations into the phase of liquidation/administration of its operations –
                until it ceases to exist. The following values are permissible (IA=i.A., IL=i.L., INABW=in Abwicklung, INLIQ=in
                Liquidation). Example: IA.
            all_first_names (Union[Unset, str]): (Vollständige Vornamen) All first names of a natural person. Example:
                Albrecht Wenzel Eusebius.
            birth_name (Union[Unset, str]): (Geburtsname) Birth name of a natural person. Example: Schmidtmuster.
            current_consideration (Union[Unset, MasterClientFullAddresseeDetailCurrentConsideration]):
                (Berücksichtigungsgrund) Current consideration of a natural person (= value as at system date). The following
                values are permissible (ARBEITSU=Arbeit suchend, AUSBILDG=Schul-/Berufsausbildung, BEHINDERG=Wegen Behinderung
                außerstande, sich selbst zu unterhalten, FEHLAUSB=Fehlender Ausbildungsplatz, FREIDST=Freiwilligendienst - kein
                Zivildienst, FREIWEHR=Freiwilliger Wehrdienst, GRDDST=Gesetzlicher Grundwehr-/Zivildienst oder davon befreiender
                Dienst, UEBERGANG=Übergangszeit von höchstens vier Monaten). Example: AUSBILDG.
            considerations (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'AUSBILDG',
                'valid_from': '2020-12-20'}, {'value': 'AUSBILDG', 'valid_from': '2020-12-20'}, {'value': 'AUSBILDG',
                'valid_from': '2020-12-20'}].
            country_of_birth (Union[Unset, MasterClientFullAddresseeDetailCountryOfBirth]): (Geburtsland) Country of birth
                of a natural person. The following values are permissible (AD=Andorra, AE=Vereinigte Arabische Emirate,
                AF=Afghanistan, AG=Antigua und Barbuda, AI=Anguilla, AL=Albanien, AM=Armenien, AN=Niederländische Antillen (bis
                2010), AO=Angola, AQ=Antarktis, AR=Argentinien, AS=Amerikanisch-Samoa, AT=Österreich, AU=Australien, AW=Aruba,
                AX=Ålandinseln, AZ=Aserbaidschan, BA=Bosnien und Herzegowina, BB=Barbados, BD=Bangladesch, BE=Belgien,
                BF=Burkina Faso, BG=Bulgarien, BH=Bahrain, BI=Burundi, BJ=Benin, BL=St. Barthélemy, BM=Bermuda, BN=Brunei
                Darussalam, BO=Bolivie, Plurinationaler Staat, BQ=Bonaire, St. Eustatius und Saba, BR=Brasilien, BS=Bahamas,
                BT=Bhutan, BV=Bouvetinsel, BW=Botsuana, BY=Belarus, BZ=Belize, CA=Kanada, CC=Kokosinseln, CD=Kongo,
                Demokratische Republik, CF=Zentralafrikanische Republik, CG=Kongo, CH=Schweiz, CI=Cote d'Ivoire, CK=Cookinseln,
                CL=Chile, CM=Kamerun, CN=China, CO=Kolumbien, CR=Costa Rica, CS=Serbien und Montenegro (bis 2006), CU=Kuba,
                CV=Cabo Verde, CW=Curaçao, CX=Weihnachtsinsel, CY=Zypern, CZ=Tschechien, DE=Deutschland, DJ=Dschibuti,
                DK=Dänemark, DM=Dominica, DO=Dominikanische Republik, DZ=Algerien, EC=Ecuador, EE=Estland, EG=Ägypten,
                EH=Westsahara, ER=Eritrea, ES=Spanien, ET=Äthiopien, FI=Finnland, FJ=Fidschi, FK=Falklandinseln, FM=Mikronesien,
                Föderierte Staaten von, FO=Färöer, FR=Frankreich, GA=Gabun, GB=Großbritannien, GD=Grenada, GE=Georgien,
                GF=Französisch-Guayana, GG=Guernsey, GH=Ghana, GI=Gibraltar, GL=Grönland, GM=Gambia, GN=Guinea, GP=Guadeloupe,
                GQ=Äquatorialguinea, GR=Griechenland, GS=Südgeorgien und die Südlichen Sandwichinseln, GT=Guatemala, GU=Guam,
                GW=Guinea-Bissau, GY=Guyana, HK=Hongkong, HM=Heard und McDonaldinseln, HN=Honduras, HR=Kroatien, HT=Haiti,
                HU=Ungarn, ID=Indonesien, IE=Irland, IL=Israel, IM=Insel Man, IN=Indien, IO=Britisches Territorium im Indischen
                Ozean, IQ=Irak, IR=Iran, Islamische Republik, IS=Island, IT=Italien, JE=Jersey, JM=Jamaika, JO=Jordanien,
                JP=Japan, KE=Kenia, KG=Kirgisistan, KH=Kambodscha, KI=Kiribati, KM=Komoren, KN=St. Kitts und Nevis, KP=Korea,
                Demokratische Volksrepublik, KR=Korea, Republik, KW=Kuwait, KY=Kaimaninseln, KZ=Kasachstan, LA=Laos,
                Demokratische Volksrepublik, LB=Libanon, LC=St. Lucia, LI=Liechtenstein, LK=Sri Lanka, LR=Liberia, LS=Lesotho,
                LT=Litauen, LU=Luxemburg, LV=Lettland, LY=Libyen, MA=Marokko, MC=Monaco, MD=Moldau, Republik, ME=Montenegro,
                MF=St. Martin (französischer Teil), MG=Madagaskar, MH=Marshallinseln, MK= Nordmazedonien, ML=Mali, MM=Myanmar,
                MN=Mongolei, MO=Macau, MP=Nördliche Marianen, MQ=Martinique, MR=Mauretanien, MS=Montserrat, MT=Malta,
                MU=Mauritius, MV=Malediven, MW=Malawi, MX=Mexiko, MY=Malaysia, MZ=Mosambik, NA=Namibia, NC=Neukaledonien,
                NE=Niger, NF=Norfolkinsel, NG=Nigeria, NI=Nicaragua, NL=Niederlande, NO=Norwegen, NP=Nepal, NR=Nauru, NU=Niue,
                NZ=Neuseeland, OM=Oman, PA=Panama, PE=Peru, PF=Französisch-Polynesien, PG=Papua-Neuguinea, PH=Philippinen,
                PK=Pakistan, PL=Polen, PM=St. Pierre und Miquelon, PN=Pitcairninseln, PR=Puerto Rico, PS=Palästinensische
                Gebiete, PT=Portugal, PW=Palau, PY=Paraguay, QA=Katar, RE=Réunion, RO=Rumänien, RS=Serbien, RU=Russische
                Föderation, RW=Ruanda, SA=Saudi-Arabien, SB=Salomonen, SC=Seychellen, SD=Sudan, SE=Schweden, SG=Singapur, SH=St.
                Helena, Ascension und Tristan da Cunha, SI=Slowenien, SJ=Svalbard und Jan Mayen, SK=Slowakei, SL=Sierra Leone,
                SM=San Marino, SN=Senegal, SO=Somalia, SR=Suriname, SS=Südsudan, ST=Sao Tomé und Principe, SV=El Salvador,
                SX=St. Martin (niederländischer Teil), SY=Syrien, Arabische Republik, SZ=Eswatini, TC=Turks- und Caicosinseln,
                TD=Tschad, TF=Französische Süd- und Antarktisgebiete, TG=Togo, TH=Thailand, TJ=Tadschikistan, TK=Tokelau,
                TL=Timor-Leste, TM=Turkmenistan, TN=Tunesien, TO=Tonga, TR=Türkei, TT=Trinidad und Tobago, TV=Tuvalu, TW=Taiwan,
                TZ=Tansania, Vereinigte Republik, UA=Ukraine, UG=Uganda, UM=Amerikanische Überseeinseln, Kleinere, US=Vereinigte
                Staaten von Amerika, UY=Uruguay, UZ=Usbekistan, VA=Vatikanstadt, VC=St. Vincent und die Grenadinen,
                VE=Venezuela, Bolivarische Republik, VG=Britische Jungferninseln, VI=Amerikanische Jungferninseln, VN=Vietnam,
                VU=Vanuatu, WF=Wallis und Futuna, WS=Samoa, XI=Nordirland, XK=Kosovo, YE=Jemen, YT=Mayotte, ZA=Südafrika,
                ZM=Sambia, ZW=Simbabwe). Example: DE.
            date_of_death (Union[Unset, datetime.date]): (Todesdatum) Date of death of a natural person.
            date_of_expiry (Union[Unset, datetime.date]): (Gültig bis) Indicates the date until which the identity document
                is valid.
            date_of_issue (Union[Unset, datetime.date]): (Ausgestellt am) Indicates the date on which the issuing authority
                issued the identity document.
            degree (Union[Unset, str]): (Titel/Akademischer Grad) This is either an academic degree acquired following a
                completed higher education program or an academic title awarded by a higher education institution. Example: Dr..
            current_federal_state_of_natural_person (Union[Unset,
                MasterClientFullAddresseeDetailCurrentFederalStateOfNaturalPerson]): (Bundesland) Current federal state of a
                natural person (= value as at system date). A federal state is a subdivision of a federal country. The values
                depend on the national law applicable to the natural/legal person. If national_right='DE', the following values
                are permissible (BAY=Bayern, BBG=Brandenburg, BDW=Baden-Württemberg, BER=Berlin, BRE=Bremen, HBG=Hamburg,
                HES=Hessen, MLB=Mecklenburg-Vorpommern, NRS=Niedersachsen, NRW=Nordrhein-Westfalen, RLP=Rheinland-Pfalz,
                SAA=Sachsen-Anhalt, SAC=Sachsen, SAR=Saarland, SWH=Schleswig-Holstein, THG=Thüringen). If national_right='AT',
                the following values are permissible (BGL=Burgenland, KTN=Kärnten, NOE=Niederösterreich, OOE=Oberösterreich,
                SBG=Salzburg, STM=Steiermark, TIR=Tirol, VBG=Vorarlberg, W=Wien). Example: BAY.
            federal_states_of_natural_person (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example:
                [{'value': 'BAY', 'valid_from': '2020-12-20'}, {'value': 'BAY', 'valid_from': '2020-12-20'}, {'value': 'BAY',
                'valid_from': '2020-12-20'}].
            identification_number (Union[Unset, str]): (Ausweisnummer) Unique identifier of an ID card or passport. Example:
                T220001293.
            issuing_authority (Union[Unset, str]): (Ausstellende Behörde) The issuing authority that issued the identity
                document. Example: VGM Musterhausen.
            current_job_title (Union[Unset, str]): (Beruf) Current profession of a natural person (= value as at system
                date). Example: Bäcker.
            job_titles (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'Bäcker',
                'valid_from': '2020-12-20'}, {'value': 'Bäcker', 'valid_from': '2020-12-20'}, {'value': 'Bäcker', 'valid_from':
                '2020-12-20'}].
            legitimation_comment (Union[Unset, str]): (Kommentar) Comments on legitimation. Example: Dies ist ein Kommentar
                zur Legitimation.
            current_marital_status (Union[Unset, MasterClientFullAddresseeDetailCurrentMaritalStatus]): (Familienstand)
                Current marital status of a natural person (= value as at system date). The status of a natural person in
                respect of their family circumstances. The values depend on the national law applicable to the natural person.
                If the natural person is registered in Germany, the following values are permissible (GS=Geschieden, GT=Dauernd
                getrennt lebend, LE=Ledig, PA=Lebenspartnerschaft aufgehoben, PE=Lebenspartnerschaft eingetragen,
                VH=Verheiratet, VW=Verwitwet). If the naturalperson is registered in Austria, the following values are
                permissible (GS=Geschieden, GT=Dauernd getrennt lebend, LE=Ledig, PL=In Partnerschaft lebend, VH=Verheiratet).
                Example: VH.
            marital_statuses (Union[Unset, list['MasterClientFullHistoricalValueString']]):  Example: [{'value': 'VH',
                'valid_from': '2020-12-20'}, {'value': 'VH', 'valid_from': '2020-12-20'}, {'value': 'VH', 'valid_from':
                '2020-12-20'}].
            name_prefix (Union[Unset, MasterClientFullAddresseeDetailNamePrefix]): (Namensvorsatz) Prefixes include von, von
                und zu. The following values are permissible (a, aan de, aan den, al, am, an, an der, auf, auf dem, auf der, auf
                m, auff m, aus, aus dem, aus den, aus der, b, bar, be, bei, bei der, beim, ben, bey, bey der, Che, Cid, d, d',
                d., da, da costa, da las, da silva, dal, dall, dall', dalla, dalle, dallo, das, de, de la, de las, de le, degli,
                dei, del, del coz, deli, dell, dell', della, delle, delli, dello, den, der, des, di, dit, do, Don, dos, dos
                Santos, du, dy, el, g, gen, Gil, gli, Grosse, i, im, in, in den, in der, in't, kl, kleine, l, l', l., la, le,
                lee, li, lo, m, Mac, mc, o, o', op, op de, op den, op gen, op het, op ten, pla, pro, rr, St., t, te, ten, ter,
                Tho, Thom, Thum, to, Tom, Tor, tu, tum, unter, unterm, v., v. d., v. dem, v. den, v. der, van, van de, van dem,
                van den, van der, van gen, van t, vande, vandem, vanden, vander, ven, vo, vom, vom und zu, von, von de, von dem,
                von den, von der, von einem, von Mast, von und zu, von und zu der, von und zur, von zum, vonde, vondem, vonden,
                vonder, vor, vor dem, vor den, vor der, vorm, vorn, y, y del, zu, zum, zur). Example: von.
            nationality (Union[Unset, MasterClientFullAddresseeDetailNationality]): (Staatsangehörigkeit) Nationality of a
                natural person. The following values are permissible (Afghanisch, Ägyptisch, Albanisch, Algerisch, Amerikanisch,
                Andorranisch, Angolanisch, Antiguanisch, Äquatorialguineisch, Argentinisch, Armenisch, Aserbaidschanisch,
                Äthiopisch, Australisch, Bahamaisch, Bahrainisch, Bangladeschisch, Barbadisch, Belarussisch, Belgisch,
                Belizisch, Beninisch, Bhutanisch, Bolivianisch, Bosnisch-herzegowinisch, Botsuanisch, Brasilianisch, Britisch,
                Bruneiisch, Bulgarisch, Burkinisch, Burundisch, Chilenisch, Chinesisch, Costa-ricanisch, Dänisch, Deutsch,
                Dominicanisch, Dominikanisch, Dschibutisch, Ecuadorianisch, Eritreisch, Estnisch, Fidschianisch, Finnisch,
                Französisch, Gabunisch, Gambisch, Georgisch, Ghanaisch, Grenadisch, Griechisch, Guatemaltekisch, Guinea-
                bissauisch, Guineisch, Guyanisch, Haitianisch, Honduranisch, Indisch, Indonesisch, Irakisch, Iranisch, Irisch,
                Isländisch, Israelisch, Italienisch, Ivorisch, Jamaikanisch, Japanisch, Jemenitisch, Jordanisch,
                Kambodschanisch, Kamerunisch, Kanadisch, Kap-verdisch, Kasachisch, Katarisch, Kenianisch, Kirgisisch,
                Kiribatisch, Kolumbianisch, Komorisch, Kongolesisch, Koreanisch, Kosovarisch, Kroatisch, Kubanisch, Kuwaitisch,
                Laotisch, Lesothisch, Lettisch, Libanesisch, Liberianisch, Libysch, Liechtensteinisch, Litauisch, Lucianisch,
                Luxemburgisch, Madagassisch, Malawisch, Malaysisch, Maledivisch, Malisch, Maltesisch, Marokkanisch,
                Marshallisch, Mauretanisch, Mauritisch, Mazedonisch, Mexikanisch, Mikronesisch, Moldauisch, Monegassisch,
                Mongolisch, Montenegrinisch, Mosambikanisch, Myanmarisch, Namibisch, Nauruisch, Nepalesisch, Neuseeländisch,
                Nicaraguanisch, Niederländisch, Nigerianisch, Nigrisch, Niueanisch, Norwegisch, Omanisch, Österreichisch,
                Pakistanisch, Palauisch, Panamaisch, Papua-neuguineisch, Paraguayisch, Peruanisch, Philippinisch, Polnisch,
                Portugiesisch, Ruandisch, Rumänisch, Russisch, Salomonisch, Salvadorianisch, Sambisch, Samoanisch, San-
                marinesisch, Sao-toméisch, Saudi-arabisch, Schwedisch, Schweizerisch, Senegalesisch, Serbisch, Serbisch-
                montenegrinisch, Seychellisch, Sierra-leonisch, Simbabwisch, Singapurisch, Slowakisch, Slowenisch, Somalisch,
                Spanisch, Sri-lankisch, Südafrikanisch, Sudanesisch, Südsudanesisch, Surinamisch, Swasiländisch, Syrisch,
                Tadschikisch, Taiwanisch, Tansanisch, Thailändisch, Timorisch, Togoisch, Trinidad Tobago Bürger, Tongaisch,
                Tschadisch, Tschechisch, Tunesisch, Türkisch, Turkmenisch, Tuvaluisch, Ugandisch, Ukrainisch, Ungarisch,
                Uruguayisch, Usbekisch, Vanuatuisch, Vatikanisch, Venezolanisch, Vietnamesisch, Vincentisch, Zentralafrikanisch,
                Zyprisch). Example: Deutsch.
            other_nationalities (Union[Unset, list['MasterClientFullAddresseeDetailOtherNationality']]): (Weitere
                Staatsangehörigkeiten) Other nationalities of a natural person.
            paper_of_identity (Union[Unset, MasterClientFullAddresseeDetailPaperOfIdentity]): (Legitimationsart) Indicates
                the way in which identity has been confirmed. The following values are permissible (EZ=Erkennungszeuge,
                FS=Führerschein, PA=Personalausweis, PB=Persönliche Bekanntschaft, RP=Reisepass, SA=Sonstiger Ausweis,
                SK=Besondere Sachkunde, UK=Urkunde, IN=Elektronischer Identitätsnachweis, ES=Qualifizierte elektronische
                Signatur, IS=Elektronisches Identifizierungssystem). Example: PA.
            pension_insurance_institute (Union[Unset, str]): (Rentenversicherungsträger) Pension insurance institute is the
                name of the insurer/organization with which a natural person holds a pension. Example: Rentenversicherung.
            place_of_birth (Union[Unset, str]): (Geburtsort) Place of birth of a natural person. Example: München.
            register_of_births_number (Union[Unset, str]): (Geburtsregisternummer) Number issued by the register office when
                a child is born. It appears on the person’s birth certificate. Example: 1980/123.
            register_office_of_birth (Union[Unset, str]): (Geburtsstandesamt) Register office where a natural person’s birth
                was registered. Example: München.
            social_security_number (Union[Unset, str]): (Rentenversicherungsnummer) Unique social security number. The
                maximum length depends on the national law applicable to the natural person. If national_right='DE', the max.
                length is 12 characters. If national_right='AT', the max. length is 13 characters. Example: 66150872P080.
            title_of_nobility (Union[Unset, MasterClientFullAddresseeDetailTitleOfNobility]): (Adelstitel) A title of
                nobility is the hereditary title of a group of natural persons. Such titles conferred certain privileges in
                former times. The following values are permissible (Baron, Baronesse, Baronin, Brand, Condesa, Earl, Edle,
                Edler, Erbgraf, Erbprinz, Freifrau, Freiherr, Freiin, Fürst, Fürstin, Graf, Gräfin, Großherzog, Großherzogin,
                Herzog, Herzogin, Landgraf, Landgräfin, Marques, Marquis, Marschall, Ostoja, Prinz, Prinzessin, Reichsgraf,
                Reichsgräfin, Ritter, Truchsess). Example: Graf.
     """

    complimentary_close: Union[Unset, str] = UNSET
    correspondence_title: Union[Unset, str] = UNSET
    national_right: Union[Unset, MasterClientFullAddresseeDetailNationalRight] = UNSET
    note: Union[Unset, str] = UNSET
    salutation: Union[Unset, str] = UNSET
    current_code_of_classification_of_economic_activities_2008: Union[Unset, str] = UNSET
    codes_of_classification_of_economic_activities_2008: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_description_of_classification_of_economic_activities_2008: Union[Unset, str] = UNSET
    descriptions_of_classification_of_economic_activities_2008: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_mad_code_of_classification_of_economic_activities_2008: Union[Unset, str] = UNSET
    mad_codes_of_classification_of_economic_activities_2008: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_code_of_classification_of_economic_activities_2003: Union[Unset, str] = UNSET
    codes_of_classification_of_economic_activities_2003: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_description_of_classification_of_economic_activities_2003: Union[Unset, str] = UNSET
    descriptions_of_classification_of_economic_activities_2003: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_mad_code_of_classification_of_economic_activities_2003: Union[Unset, str] = UNSET
    mad_codes_of_classification_of_economic_activities_2003: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_country_of_head_office: Union[Unset, str] = UNSET
    countries_of_head_office: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    date_of_memorandum_of_association: Union[Unset, datetime.date] = UNSET
    current_distribution_of_profit: Union[Unset, MasterClientFullAddresseeDetailCurrentDistributionOfProfit] = UNSET
    distributions_of_profit: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_enterprise_purpose: Union[Unset, str] = UNSET
    enterprise_purposes: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_federal_state_mad_of_legal_person: Union[Unset, int] = UNSET
    federal_states_mad_of_legal_person: Union[Unset, list['MasterClientFullHistoricalValueInteger']] = UNSET
    current_federal_state_of_legal_person: Union[Unset, MasterClientFullAddresseeDetailCurrentFederalStateOfLegalPerson] = UNSET
    federal_states_of_legal_person: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_fiscal_year: Union[Unset, str] = UNSET
    fiscal_years: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_kind_of_register_court: Union[Unset, MasterClientFullAddresseeDetailCurrentKindOfRegisterCourt] = UNSET
    kind_of_register_courts: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_location_of_head_office: Union[Unset, str] = UNSET
    locations_of_head_office: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_name_of_register_court: Union[Unset, str] = UNSET
    names_of_register_court: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_registered_company_name: Union[Unset, str] = UNSET
    registered_company_names: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    registration_date: Union[Unset, datetime.date] = UNSET
    current_registration_number: Union[Unset, str] = UNSET
    registration_numbers: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_three_lined_company_name_first_line: Union[Unset, str] = UNSET
    three_lined_company_names_first_line: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_three_lined_company_name_second_line: Union[Unset, str] = UNSET
    three_lined_company_names_second_line: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_three_lined_company_name_third_line: Union[Unset, str] = UNSET
    three_lined_company_names_third_line: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_two_lined_company_name_first_line: Union[Unset, str] = UNSET
    two_lined_company_names_first_line: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    current_two_lined_company_name_second_line: Union[Unset, str] = UNSET
    two_lined_company_names_second_line: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    winding_up_date: Union[Unset, datetime.date] = UNSET
    winding_up_proceedings: Union[Unset, MasterClientFullAddresseeDetailWindingUpProceedings] = UNSET
    all_first_names: Union[Unset, str] = UNSET
    birth_name: Union[Unset, str] = UNSET
    current_consideration: Union[Unset, MasterClientFullAddresseeDetailCurrentConsideration] = UNSET
    considerations: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    country_of_birth: Union[Unset, MasterClientFullAddresseeDetailCountryOfBirth] = UNSET
    date_of_death: Union[Unset, datetime.date] = UNSET
    date_of_expiry: Union[Unset, datetime.date] = UNSET
    date_of_issue: Union[Unset, datetime.date] = UNSET
    degree: Union[Unset, str] = UNSET
    current_federal_state_of_natural_person: Union[Unset, MasterClientFullAddresseeDetailCurrentFederalStateOfNaturalPerson] = UNSET
    federal_states_of_natural_person: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    identification_number: Union[Unset, str] = UNSET
    issuing_authority: Union[Unset, str] = UNSET
    current_job_title: Union[Unset, str] = UNSET
    job_titles: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    legitimation_comment: Union[Unset, str] = UNSET
    current_marital_status: Union[Unset, MasterClientFullAddresseeDetailCurrentMaritalStatus] = UNSET
    marital_statuses: Union[Unset, list['MasterClientFullHistoricalValueString']] = UNSET
    name_prefix: Union[Unset, MasterClientFullAddresseeDetailNamePrefix] = UNSET
    nationality: Union[Unset, MasterClientFullAddresseeDetailNationality] = UNSET
    other_nationalities: Union[Unset, list['MasterClientFullAddresseeDetailOtherNationality']] = UNSET
    paper_of_identity: Union[Unset, MasterClientFullAddresseeDetailPaperOfIdentity] = UNSET
    pension_insurance_institute: Union[Unset, str] = UNSET
    place_of_birth: Union[Unset, str] = UNSET
    register_of_births_number: Union[Unset, str] = UNSET
    register_office_of_birth: Union[Unset, str] = UNSET
    social_security_number: Union[Unset, str] = UNSET
    title_of_nobility: Union[Unset, MasterClientFullAddresseeDetailTitleOfNobility] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.master_client_full_historical_value_integer import MasterClientFullHistoricalValueInteger
        from ..models.master_client_full_historical_value_string import MasterClientFullHistoricalValueString
        from ..models.master_client_full_addressee_detail_other_nationality import MasterClientFullAddresseeDetailOtherNationality
        complimentary_close = self.complimentary_close

        correspondence_title = self.correspondence_title

        national_right: Union[Unset, str] = UNSET
        if not isinstance(self.national_right, Unset):
            national_right = self.national_right.value


        note = self.note

        salutation = self.salutation

        current_code_of_classification_of_economic_activities_2008 = self.current_code_of_classification_of_economic_activities_2008

        codes_of_classification_of_economic_activities_2008: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.codes_of_classification_of_economic_activities_2008, Unset):
            codes_of_classification_of_economic_activities_2008 = []
            for codes_of_classification_of_economic_activities_2008_item_data in self.codes_of_classification_of_economic_activities_2008:
                codes_of_classification_of_economic_activities_2008_item = codes_of_classification_of_economic_activities_2008_item_data.to_dict()
                codes_of_classification_of_economic_activities_2008.append(codes_of_classification_of_economic_activities_2008_item)



        current_description_of_classification_of_economic_activities_2008 = self.current_description_of_classification_of_economic_activities_2008

        descriptions_of_classification_of_economic_activities_2008: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.descriptions_of_classification_of_economic_activities_2008, Unset):
            descriptions_of_classification_of_economic_activities_2008 = []
            for descriptions_of_classification_of_economic_activities_2008_item_data in self.descriptions_of_classification_of_economic_activities_2008:
                descriptions_of_classification_of_economic_activities_2008_item = descriptions_of_classification_of_economic_activities_2008_item_data.to_dict()
                descriptions_of_classification_of_economic_activities_2008.append(descriptions_of_classification_of_economic_activities_2008_item)



        current_mad_code_of_classification_of_economic_activities_2008 = self.current_mad_code_of_classification_of_economic_activities_2008

        mad_codes_of_classification_of_economic_activities_2008: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mad_codes_of_classification_of_economic_activities_2008, Unset):
            mad_codes_of_classification_of_economic_activities_2008 = []
            for mad_codes_of_classification_of_economic_activities_2008_item_data in self.mad_codes_of_classification_of_economic_activities_2008:
                mad_codes_of_classification_of_economic_activities_2008_item = mad_codes_of_classification_of_economic_activities_2008_item_data.to_dict()
                mad_codes_of_classification_of_economic_activities_2008.append(mad_codes_of_classification_of_economic_activities_2008_item)



        current_code_of_classification_of_economic_activities_2003 = self.current_code_of_classification_of_economic_activities_2003

        codes_of_classification_of_economic_activities_2003: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.codes_of_classification_of_economic_activities_2003, Unset):
            codes_of_classification_of_economic_activities_2003 = []
            for codes_of_classification_of_economic_activities_2003_item_data in self.codes_of_classification_of_economic_activities_2003:
                codes_of_classification_of_economic_activities_2003_item = codes_of_classification_of_economic_activities_2003_item_data.to_dict()
                codes_of_classification_of_economic_activities_2003.append(codes_of_classification_of_economic_activities_2003_item)



        current_description_of_classification_of_economic_activities_2003 = self.current_description_of_classification_of_economic_activities_2003

        descriptions_of_classification_of_economic_activities_2003: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.descriptions_of_classification_of_economic_activities_2003, Unset):
            descriptions_of_classification_of_economic_activities_2003 = []
            for descriptions_of_classification_of_economic_activities_2003_item_data in self.descriptions_of_classification_of_economic_activities_2003:
                descriptions_of_classification_of_economic_activities_2003_item = descriptions_of_classification_of_economic_activities_2003_item_data.to_dict()
                descriptions_of_classification_of_economic_activities_2003.append(descriptions_of_classification_of_economic_activities_2003_item)



        current_mad_code_of_classification_of_economic_activities_2003 = self.current_mad_code_of_classification_of_economic_activities_2003

        mad_codes_of_classification_of_economic_activities_2003: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mad_codes_of_classification_of_economic_activities_2003, Unset):
            mad_codes_of_classification_of_economic_activities_2003 = []
            for mad_codes_of_classification_of_economic_activities_2003_item_data in self.mad_codes_of_classification_of_economic_activities_2003:
                mad_codes_of_classification_of_economic_activities_2003_item = mad_codes_of_classification_of_economic_activities_2003_item_data.to_dict()
                mad_codes_of_classification_of_economic_activities_2003.append(mad_codes_of_classification_of_economic_activities_2003_item)



        current_country_of_head_office = self.current_country_of_head_office

        countries_of_head_office: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.countries_of_head_office, Unset):
            countries_of_head_office = []
            for countries_of_head_office_item_data in self.countries_of_head_office:
                countries_of_head_office_item = countries_of_head_office_item_data.to_dict()
                countries_of_head_office.append(countries_of_head_office_item)



        date_of_memorandum_of_association: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_memorandum_of_association, Unset):
            date_of_memorandum_of_association = self.date_of_memorandum_of_association.isoformat()

        current_distribution_of_profit: Union[Unset, str] = UNSET
        if not isinstance(self.current_distribution_of_profit, Unset):
            current_distribution_of_profit = self.current_distribution_of_profit.value


        distributions_of_profit: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.distributions_of_profit, Unset):
            distributions_of_profit = []
            for distributions_of_profit_item_data in self.distributions_of_profit:
                distributions_of_profit_item = distributions_of_profit_item_data.to_dict()
                distributions_of_profit.append(distributions_of_profit_item)



        current_enterprise_purpose = self.current_enterprise_purpose

        enterprise_purposes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.enterprise_purposes, Unset):
            enterprise_purposes = []
            for enterprise_purposes_item_data in self.enterprise_purposes:
                enterprise_purposes_item = enterprise_purposes_item_data.to_dict()
                enterprise_purposes.append(enterprise_purposes_item)



        current_federal_state_mad_of_legal_person = self.current_federal_state_mad_of_legal_person

        federal_states_mad_of_legal_person: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.federal_states_mad_of_legal_person, Unset):
            federal_states_mad_of_legal_person = []
            for federal_states_mad_of_legal_person_item_data in self.federal_states_mad_of_legal_person:
                federal_states_mad_of_legal_person_item = federal_states_mad_of_legal_person_item_data.to_dict()
                federal_states_mad_of_legal_person.append(federal_states_mad_of_legal_person_item)



        current_federal_state_of_legal_person: Union[Unset, str] = UNSET
        if not isinstance(self.current_federal_state_of_legal_person, Unset):
            current_federal_state_of_legal_person = self.current_federal_state_of_legal_person.value


        federal_states_of_legal_person: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.federal_states_of_legal_person, Unset):
            federal_states_of_legal_person = []
            for federal_states_of_legal_person_item_data in self.federal_states_of_legal_person:
                federal_states_of_legal_person_item = federal_states_of_legal_person_item_data.to_dict()
                federal_states_of_legal_person.append(federal_states_of_legal_person_item)



        current_fiscal_year = self.current_fiscal_year

        fiscal_years: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fiscal_years, Unset):
            fiscal_years = []
            for fiscal_years_item_data in self.fiscal_years:
                fiscal_years_item = fiscal_years_item_data.to_dict()
                fiscal_years.append(fiscal_years_item)



        current_kind_of_register_court: Union[Unset, str] = UNSET
        if not isinstance(self.current_kind_of_register_court, Unset):
            current_kind_of_register_court = self.current_kind_of_register_court.value


        kind_of_register_courts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.kind_of_register_courts, Unset):
            kind_of_register_courts = []
            for kind_of_register_courts_item_data in self.kind_of_register_courts:
                kind_of_register_courts_item = kind_of_register_courts_item_data.to_dict()
                kind_of_register_courts.append(kind_of_register_courts_item)



        current_location_of_head_office = self.current_location_of_head_office

        locations_of_head_office: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locations_of_head_office, Unset):
            locations_of_head_office = []
            for locations_of_head_office_item_data in self.locations_of_head_office:
                locations_of_head_office_item = locations_of_head_office_item_data.to_dict()
                locations_of_head_office.append(locations_of_head_office_item)



        current_name_of_register_court = self.current_name_of_register_court

        names_of_register_court: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.names_of_register_court, Unset):
            names_of_register_court = []
            for names_of_register_court_item_data in self.names_of_register_court:
                names_of_register_court_item = names_of_register_court_item_data.to_dict()
                names_of_register_court.append(names_of_register_court_item)



        current_registered_company_name = self.current_registered_company_name

        registered_company_names: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.registered_company_names, Unset):
            registered_company_names = []
            for registered_company_names_item_data in self.registered_company_names:
                registered_company_names_item = registered_company_names_item_data.to_dict()
                registered_company_names.append(registered_company_names_item)



        registration_date: Union[Unset, str] = UNSET
        if not isinstance(self.registration_date, Unset):
            registration_date = self.registration_date.isoformat()

        current_registration_number = self.current_registration_number

        registration_numbers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.registration_numbers, Unset):
            registration_numbers = []
            for registration_numbers_item_data in self.registration_numbers:
                registration_numbers_item = registration_numbers_item_data.to_dict()
                registration_numbers.append(registration_numbers_item)



        current_three_lined_company_name_first_line = self.current_three_lined_company_name_first_line

        three_lined_company_names_first_line: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.three_lined_company_names_first_line, Unset):
            three_lined_company_names_first_line = []
            for three_lined_company_names_first_line_item_data in self.three_lined_company_names_first_line:
                three_lined_company_names_first_line_item = three_lined_company_names_first_line_item_data.to_dict()
                three_lined_company_names_first_line.append(three_lined_company_names_first_line_item)



        current_three_lined_company_name_second_line = self.current_three_lined_company_name_second_line

        three_lined_company_names_second_line: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.three_lined_company_names_second_line, Unset):
            three_lined_company_names_second_line = []
            for three_lined_company_names_second_line_item_data in self.three_lined_company_names_second_line:
                three_lined_company_names_second_line_item = three_lined_company_names_second_line_item_data.to_dict()
                three_lined_company_names_second_line.append(three_lined_company_names_second_line_item)



        current_three_lined_company_name_third_line = self.current_three_lined_company_name_third_line

        three_lined_company_names_third_line: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.three_lined_company_names_third_line, Unset):
            three_lined_company_names_third_line = []
            for three_lined_company_names_third_line_item_data in self.three_lined_company_names_third_line:
                three_lined_company_names_third_line_item = three_lined_company_names_third_line_item_data.to_dict()
                three_lined_company_names_third_line.append(three_lined_company_names_third_line_item)



        current_two_lined_company_name_first_line = self.current_two_lined_company_name_first_line

        two_lined_company_names_first_line: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.two_lined_company_names_first_line, Unset):
            two_lined_company_names_first_line = []
            for two_lined_company_names_first_line_item_data in self.two_lined_company_names_first_line:
                two_lined_company_names_first_line_item = two_lined_company_names_first_line_item_data.to_dict()
                two_lined_company_names_first_line.append(two_lined_company_names_first_line_item)



        current_two_lined_company_name_second_line = self.current_two_lined_company_name_second_line

        two_lined_company_names_second_line: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.two_lined_company_names_second_line, Unset):
            two_lined_company_names_second_line = []
            for two_lined_company_names_second_line_item_data in self.two_lined_company_names_second_line:
                two_lined_company_names_second_line_item = two_lined_company_names_second_line_item_data.to_dict()
                two_lined_company_names_second_line.append(two_lined_company_names_second_line_item)



        winding_up_date: Union[Unset, str] = UNSET
        if not isinstance(self.winding_up_date, Unset):
            winding_up_date = self.winding_up_date.isoformat()

        winding_up_proceedings: Union[Unset, str] = UNSET
        if not isinstance(self.winding_up_proceedings, Unset):
            winding_up_proceedings = self.winding_up_proceedings.value


        all_first_names = self.all_first_names

        birth_name = self.birth_name

        current_consideration: Union[Unset, str] = UNSET
        if not isinstance(self.current_consideration, Unset):
            current_consideration = self.current_consideration.value


        considerations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.considerations, Unset):
            considerations = []
            for considerations_item_data in self.considerations:
                considerations_item = considerations_item_data.to_dict()
                considerations.append(considerations_item)



        country_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.country_of_birth, Unset):
            country_of_birth = self.country_of_birth.value


        date_of_death: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_death, Unset):
            date_of_death = self.date_of_death.isoformat()

        date_of_expiry: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_expiry, Unset):
            date_of_expiry = self.date_of_expiry.isoformat()

        date_of_issue: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_issue, Unset):
            date_of_issue = self.date_of_issue.isoformat()

        degree = self.degree

        current_federal_state_of_natural_person: Union[Unset, str] = UNSET
        if not isinstance(self.current_federal_state_of_natural_person, Unset):
            current_federal_state_of_natural_person = self.current_federal_state_of_natural_person.value


        federal_states_of_natural_person: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.federal_states_of_natural_person, Unset):
            federal_states_of_natural_person = []
            for federal_states_of_natural_person_item_data in self.federal_states_of_natural_person:
                federal_states_of_natural_person_item = federal_states_of_natural_person_item_data.to_dict()
                federal_states_of_natural_person.append(federal_states_of_natural_person_item)



        identification_number = self.identification_number

        issuing_authority = self.issuing_authority

        current_job_title = self.current_job_title

        job_titles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.job_titles, Unset):
            job_titles = []
            for job_titles_item_data in self.job_titles:
                job_titles_item = job_titles_item_data.to_dict()
                job_titles.append(job_titles_item)



        legitimation_comment = self.legitimation_comment

        current_marital_status: Union[Unset, str] = UNSET
        if not isinstance(self.current_marital_status, Unset):
            current_marital_status = self.current_marital_status.value


        marital_statuses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.marital_statuses, Unset):
            marital_statuses = []
            for marital_statuses_item_data in self.marital_statuses:
                marital_statuses_item = marital_statuses_item_data.to_dict()
                marital_statuses.append(marital_statuses_item)



        name_prefix: Union[Unset, str] = UNSET
        if not isinstance(self.name_prefix, Unset):
            name_prefix = self.name_prefix.value


        nationality: Union[Unset, str] = UNSET
        if not isinstance(self.nationality, Unset):
            nationality = self.nationality.value


        other_nationalities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.other_nationalities, Unset):
            other_nationalities = []
            for other_nationalities_item_data in self.other_nationalities:
                other_nationalities_item = other_nationalities_item_data.to_dict()
                other_nationalities.append(other_nationalities_item)



        paper_of_identity: Union[Unset, str] = UNSET
        if not isinstance(self.paper_of_identity, Unset):
            paper_of_identity = self.paper_of_identity.value


        pension_insurance_institute = self.pension_insurance_institute

        place_of_birth = self.place_of_birth

        register_of_births_number = self.register_of_births_number

        register_office_of_birth = self.register_office_of_birth

        social_security_number = self.social_security_number

        title_of_nobility: Union[Unset, str] = UNSET
        if not isinstance(self.title_of_nobility, Unset):
            title_of_nobility = self.title_of_nobility.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if complimentary_close is not UNSET:
            field_dict["complimentary_close"] = complimentary_close
        if correspondence_title is not UNSET:
            field_dict["correspondence_title"] = correspondence_title
        if national_right is not UNSET:
            field_dict["national_right"] = national_right
        if note is not UNSET:
            field_dict["note"] = note
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if current_code_of_classification_of_economic_activities_2008 is not UNSET:
            field_dict["current_code_of_classification_of_economic_activities_2008"] = current_code_of_classification_of_economic_activities_2008
        if codes_of_classification_of_economic_activities_2008 is not UNSET:
            field_dict["codes_of_classification_of_economic_activities_2008"] = codes_of_classification_of_economic_activities_2008
        if current_description_of_classification_of_economic_activities_2008 is not UNSET:
            field_dict["current_description_of_classification_of_economic_activities_2008"] = current_description_of_classification_of_economic_activities_2008
        if descriptions_of_classification_of_economic_activities_2008 is not UNSET:
            field_dict["descriptions_of_classification_of_economic_activities_2008"] = descriptions_of_classification_of_economic_activities_2008
        if current_mad_code_of_classification_of_economic_activities_2008 is not UNSET:
            field_dict["current_mad_code_of_classification_of_economic_activities_2008"] = current_mad_code_of_classification_of_economic_activities_2008
        if mad_codes_of_classification_of_economic_activities_2008 is not UNSET:
            field_dict["mad_codes_of_classification_of_economic_activities_2008"] = mad_codes_of_classification_of_economic_activities_2008
        if current_code_of_classification_of_economic_activities_2003 is not UNSET:
            field_dict["current_code_of_classification_of_economic_activities_2003"] = current_code_of_classification_of_economic_activities_2003
        if codes_of_classification_of_economic_activities_2003 is not UNSET:
            field_dict["codes_of_classification_of_economic_activities_2003"] = codes_of_classification_of_economic_activities_2003
        if current_description_of_classification_of_economic_activities_2003 is not UNSET:
            field_dict["current_description_of_classification_of_economic_activities_2003"] = current_description_of_classification_of_economic_activities_2003
        if descriptions_of_classification_of_economic_activities_2003 is not UNSET:
            field_dict["descriptions_of_classification_of_economic_activities_2003"] = descriptions_of_classification_of_economic_activities_2003
        if current_mad_code_of_classification_of_economic_activities_2003 is not UNSET:
            field_dict["current_mad_code_of_classification_of_economic_activities_2003"] = current_mad_code_of_classification_of_economic_activities_2003
        if mad_codes_of_classification_of_economic_activities_2003 is not UNSET:
            field_dict["mad_codes_of_classification_of_economic_activities_2003"] = mad_codes_of_classification_of_economic_activities_2003
        if current_country_of_head_office is not UNSET:
            field_dict["current_country_of_head_office"] = current_country_of_head_office
        if countries_of_head_office is not UNSET:
            field_dict["countries_of_head_office"] = countries_of_head_office
        if date_of_memorandum_of_association is not UNSET:
            field_dict["date_of_memorandum_of_association"] = date_of_memorandum_of_association
        if current_distribution_of_profit is not UNSET:
            field_dict["current_distribution_of_profit"] = current_distribution_of_profit
        if distributions_of_profit is not UNSET:
            field_dict["distributions_of_profit"] = distributions_of_profit
        if current_enterprise_purpose is not UNSET:
            field_dict["current_enterprise_purpose"] = current_enterprise_purpose
        if enterprise_purposes is not UNSET:
            field_dict["enterprise_purposes"] = enterprise_purposes
        if current_federal_state_mad_of_legal_person is not UNSET:
            field_dict["current_federal_state_mad_of_legal_person"] = current_federal_state_mad_of_legal_person
        if federal_states_mad_of_legal_person is not UNSET:
            field_dict["federal_states_mad_of_legal_person"] = federal_states_mad_of_legal_person
        if current_federal_state_of_legal_person is not UNSET:
            field_dict["current_federal_state_of_legal_person"] = current_federal_state_of_legal_person
        if federal_states_of_legal_person is not UNSET:
            field_dict["federal_states_of_legal_person"] = federal_states_of_legal_person
        if current_fiscal_year is not UNSET:
            field_dict["current_fiscal_year"] = current_fiscal_year
        if fiscal_years is not UNSET:
            field_dict["fiscal_years"] = fiscal_years
        if current_kind_of_register_court is not UNSET:
            field_dict["current_kind_of_register_court"] = current_kind_of_register_court
        if kind_of_register_courts is not UNSET:
            field_dict["kind_of_register_courts"] = kind_of_register_courts
        if current_location_of_head_office is not UNSET:
            field_dict["current_location_of_head_office"] = current_location_of_head_office
        if locations_of_head_office is not UNSET:
            field_dict["locations_of_head_office"] = locations_of_head_office
        if current_name_of_register_court is not UNSET:
            field_dict["current_name_of_register_court"] = current_name_of_register_court
        if names_of_register_court is not UNSET:
            field_dict["names_of_register_court"] = names_of_register_court
        if current_registered_company_name is not UNSET:
            field_dict["current_registered_company_name"] = current_registered_company_name
        if registered_company_names is not UNSET:
            field_dict["registered_company_names"] = registered_company_names
        if registration_date is not UNSET:
            field_dict["registration_date"] = registration_date
        if current_registration_number is not UNSET:
            field_dict["current_registration_number"] = current_registration_number
        if registration_numbers is not UNSET:
            field_dict["registration_numbers"] = registration_numbers
        if current_three_lined_company_name_first_line is not UNSET:
            field_dict["current_three_lined_company_name_first_line"] = current_three_lined_company_name_first_line
        if three_lined_company_names_first_line is not UNSET:
            field_dict["three_lined_company_names_first_line"] = three_lined_company_names_first_line
        if current_three_lined_company_name_second_line is not UNSET:
            field_dict["current_three_lined_company_name_second_line"] = current_three_lined_company_name_second_line
        if three_lined_company_names_second_line is not UNSET:
            field_dict["three_lined_company_names_second_line"] = three_lined_company_names_second_line
        if current_three_lined_company_name_third_line is not UNSET:
            field_dict["current_three_lined_company_name_third_line"] = current_three_lined_company_name_third_line
        if three_lined_company_names_third_line is not UNSET:
            field_dict["three_lined_company_names_third_line"] = three_lined_company_names_third_line
        if current_two_lined_company_name_first_line is not UNSET:
            field_dict["current_two_lined_company_name_first_line"] = current_two_lined_company_name_first_line
        if two_lined_company_names_first_line is not UNSET:
            field_dict["two_lined_company_names_first_line"] = two_lined_company_names_first_line
        if current_two_lined_company_name_second_line is not UNSET:
            field_dict["current_two_lined_company_name_second_line"] = current_two_lined_company_name_second_line
        if two_lined_company_names_second_line is not UNSET:
            field_dict["two_lined_company_names_second_line"] = two_lined_company_names_second_line
        if winding_up_date is not UNSET:
            field_dict["winding_up_date"] = winding_up_date
        if winding_up_proceedings is not UNSET:
            field_dict["winding_up_proceedings"] = winding_up_proceedings
        if all_first_names is not UNSET:
            field_dict["all_first_names"] = all_first_names
        if birth_name is not UNSET:
            field_dict["birth_name"] = birth_name
        if current_consideration is not UNSET:
            field_dict["current_consideration"] = current_consideration
        if considerations is not UNSET:
            field_dict["considerations"] = considerations
        if country_of_birth is not UNSET:
            field_dict["country_of_birth"] = country_of_birth
        if date_of_death is not UNSET:
            field_dict["date_of_death"] = date_of_death
        if date_of_expiry is not UNSET:
            field_dict["date_of_expiry"] = date_of_expiry
        if date_of_issue is not UNSET:
            field_dict["date_of_issue"] = date_of_issue
        if degree is not UNSET:
            field_dict["degree"] = degree
        if current_federal_state_of_natural_person is not UNSET:
            field_dict["current_federal_state_of_natural_person"] = current_federal_state_of_natural_person
        if federal_states_of_natural_person is not UNSET:
            field_dict["federal_states_of_natural_person"] = federal_states_of_natural_person
        if identification_number is not UNSET:
            field_dict["identification_number"] = identification_number
        if issuing_authority is not UNSET:
            field_dict["issuing_authority"] = issuing_authority
        if current_job_title is not UNSET:
            field_dict["current_job_title"] = current_job_title
        if job_titles is not UNSET:
            field_dict["job_titles"] = job_titles
        if legitimation_comment is not UNSET:
            field_dict["legitimation_comment"] = legitimation_comment
        if current_marital_status is not UNSET:
            field_dict["current_marital_status"] = current_marital_status
        if marital_statuses is not UNSET:
            field_dict["marital_statuses"] = marital_statuses
        if name_prefix is not UNSET:
            field_dict["name_prefix"] = name_prefix
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if other_nationalities is not UNSET:
            field_dict["other_nationalities"] = other_nationalities
        if paper_of_identity is not UNSET:
            field_dict["paper_of_identity"] = paper_of_identity
        if pension_insurance_institute is not UNSET:
            field_dict["pension_insurance_institute"] = pension_insurance_institute
        if place_of_birth is not UNSET:
            field_dict["place_of_birth"] = place_of_birth
        if register_of_births_number is not UNSET:
            field_dict["register_of_births_number"] = register_of_births_number
        if register_office_of_birth is not UNSET:
            field_dict["register_office_of_birth"] = register_office_of_birth
        if social_security_number is not UNSET:
            field_dict["social_security_number"] = social_security_number
        if title_of_nobility is not UNSET:
            field_dict["title_of_nobility"] = title_of_nobility

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.master_client_full_historical_value_integer import MasterClientFullHistoricalValueInteger
        from ..models.master_client_full_historical_value_string import MasterClientFullHistoricalValueString
        from ..models.master_client_full_addressee_detail_other_nationality import MasterClientFullAddresseeDetailOtherNationality
        d = src_dict.copy()
        complimentary_close = d.pop("complimentary_close", UNSET)

        correspondence_title = d.pop("correspondence_title", UNSET)

        _national_right = d.pop("national_right", UNSET)
        national_right: Union[Unset, MasterClientFullAddresseeDetailNationalRight]
        if isinstance(_national_right,  Unset):
            national_right = UNSET
        else:
            national_right = MasterClientFullAddresseeDetailNationalRight(_national_right)




        note = d.pop("note", UNSET)

        salutation = d.pop("salutation", UNSET)

        current_code_of_classification_of_economic_activities_2008 = d.pop("current_code_of_classification_of_economic_activities_2008", UNSET)

        codes_of_classification_of_economic_activities_2008 = []
        _codes_of_classification_of_economic_activities_2008 = d.pop("codes_of_classification_of_economic_activities_2008", UNSET)
        for codes_of_classification_of_economic_activities_2008_item_data in (_codes_of_classification_of_economic_activities_2008 or []):
            codes_of_classification_of_economic_activities_2008_item = MasterClientFullHistoricalValueString.from_dict(codes_of_classification_of_economic_activities_2008_item_data)



            codes_of_classification_of_economic_activities_2008.append(codes_of_classification_of_economic_activities_2008_item)


        current_description_of_classification_of_economic_activities_2008 = d.pop("current_description_of_classification_of_economic_activities_2008", UNSET)

        descriptions_of_classification_of_economic_activities_2008 = []
        _descriptions_of_classification_of_economic_activities_2008 = d.pop("descriptions_of_classification_of_economic_activities_2008", UNSET)
        for descriptions_of_classification_of_economic_activities_2008_item_data in (_descriptions_of_classification_of_economic_activities_2008 or []):
            descriptions_of_classification_of_economic_activities_2008_item = MasterClientFullHistoricalValueString.from_dict(descriptions_of_classification_of_economic_activities_2008_item_data)



            descriptions_of_classification_of_economic_activities_2008.append(descriptions_of_classification_of_economic_activities_2008_item)


        current_mad_code_of_classification_of_economic_activities_2008 = d.pop("current_mad_code_of_classification_of_economic_activities_2008", UNSET)

        mad_codes_of_classification_of_economic_activities_2008 = []
        _mad_codes_of_classification_of_economic_activities_2008 = d.pop("mad_codes_of_classification_of_economic_activities_2008", UNSET)
        for mad_codes_of_classification_of_economic_activities_2008_item_data in (_mad_codes_of_classification_of_economic_activities_2008 or []):
            mad_codes_of_classification_of_economic_activities_2008_item = MasterClientFullHistoricalValueString.from_dict(mad_codes_of_classification_of_economic_activities_2008_item_data)



            mad_codes_of_classification_of_economic_activities_2008.append(mad_codes_of_classification_of_economic_activities_2008_item)


        current_code_of_classification_of_economic_activities_2003 = d.pop("current_code_of_classification_of_economic_activities_2003", UNSET)

        codes_of_classification_of_economic_activities_2003 = []
        _codes_of_classification_of_economic_activities_2003 = d.pop("codes_of_classification_of_economic_activities_2003", UNSET)
        for codes_of_classification_of_economic_activities_2003_item_data in (_codes_of_classification_of_economic_activities_2003 or []):
            codes_of_classification_of_economic_activities_2003_item = MasterClientFullHistoricalValueString.from_dict(codes_of_classification_of_economic_activities_2003_item_data)



            codes_of_classification_of_economic_activities_2003.append(codes_of_classification_of_economic_activities_2003_item)


        current_description_of_classification_of_economic_activities_2003 = d.pop("current_description_of_classification_of_economic_activities_2003", UNSET)

        descriptions_of_classification_of_economic_activities_2003 = []
        _descriptions_of_classification_of_economic_activities_2003 = d.pop("descriptions_of_classification_of_economic_activities_2003", UNSET)
        for descriptions_of_classification_of_economic_activities_2003_item_data in (_descriptions_of_classification_of_economic_activities_2003 or []):
            descriptions_of_classification_of_economic_activities_2003_item = MasterClientFullHistoricalValueString.from_dict(descriptions_of_classification_of_economic_activities_2003_item_data)



            descriptions_of_classification_of_economic_activities_2003.append(descriptions_of_classification_of_economic_activities_2003_item)


        current_mad_code_of_classification_of_economic_activities_2003 = d.pop("current_mad_code_of_classification_of_economic_activities_2003", UNSET)

        mad_codes_of_classification_of_economic_activities_2003 = []
        _mad_codes_of_classification_of_economic_activities_2003 = d.pop("mad_codes_of_classification_of_economic_activities_2003", UNSET)
        for mad_codes_of_classification_of_economic_activities_2003_item_data in (_mad_codes_of_classification_of_economic_activities_2003 or []):
            mad_codes_of_classification_of_economic_activities_2003_item = MasterClientFullHistoricalValueString.from_dict(mad_codes_of_classification_of_economic_activities_2003_item_data)



            mad_codes_of_classification_of_economic_activities_2003.append(mad_codes_of_classification_of_economic_activities_2003_item)


        current_country_of_head_office = d.pop("current_country_of_head_office", UNSET)

        countries_of_head_office = []
        _countries_of_head_office = d.pop("countries_of_head_office", UNSET)
        for countries_of_head_office_item_data in (_countries_of_head_office or []):
            countries_of_head_office_item = MasterClientFullHistoricalValueString.from_dict(countries_of_head_office_item_data)



            countries_of_head_office.append(countries_of_head_office_item)


        _date_of_memorandum_of_association = d.pop("date_of_memorandum_of_association", UNSET)
        date_of_memorandum_of_association: Union[Unset, datetime.date]
        if isinstance(_date_of_memorandum_of_association,  Unset):
            date_of_memorandum_of_association = UNSET
        else:
            date_of_memorandum_of_association = isoparse(_date_of_memorandum_of_association).date()




        _current_distribution_of_profit = d.pop("current_distribution_of_profit", UNSET)
        current_distribution_of_profit: Union[Unset, MasterClientFullAddresseeDetailCurrentDistributionOfProfit]
        if isinstance(_current_distribution_of_profit,  Unset):
            current_distribution_of_profit = UNSET
        else:
            current_distribution_of_profit = MasterClientFullAddresseeDetailCurrentDistributionOfProfit(_current_distribution_of_profit)




        distributions_of_profit = []
        _distributions_of_profit = d.pop("distributions_of_profit", UNSET)
        for distributions_of_profit_item_data in (_distributions_of_profit or []):
            distributions_of_profit_item = MasterClientFullHistoricalValueString.from_dict(distributions_of_profit_item_data)



            distributions_of_profit.append(distributions_of_profit_item)


        current_enterprise_purpose = d.pop("current_enterprise_purpose", UNSET)

        enterprise_purposes = []
        _enterprise_purposes = d.pop("enterprise_purposes", UNSET)
        for enterprise_purposes_item_data in (_enterprise_purposes or []):
            enterprise_purposes_item = MasterClientFullHistoricalValueString.from_dict(enterprise_purposes_item_data)



            enterprise_purposes.append(enterprise_purposes_item)


        current_federal_state_mad_of_legal_person = d.pop("current_federal_state_mad_of_legal_person", UNSET)

        federal_states_mad_of_legal_person = []
        _federal_states_mad_of_legal_person = d.pop("federal_states_mad_of_legal_person", UNSET)
        for federal_states_mad_of_legal_person_item_data in (_federal_states_mad_of_legal_person or []):
            federal_states_mad_of_legal_person_item = MasterClientFullHistoricalValueInteger.from_dict(federal_states_mad_of_legal_person_item_data)



            federal_states_mad_of_legal_person.append(federal_states_mad_of_legal_person_item)


        _current_federal_state_of_legal_person = d.pop("current_federal_state_of_legal_person", UNSET)
        current_federal_state_of_legal_person: Union[Unset, MasterClientFullAddresseeDetailCurrentFederalStateOfLegalPerson]
        if isinstance(_current_federal_state_of_legal_person,  Unset):
            current_federal_state_of_legal_person = UNSET
        else:
            current_federal_state_of_legal_person = MasterClientFullAddresseeDetailCurrentFederalStateOfLegalPerson(_current_federal_state_of_legal_person)




        federal_states_of_legal_person = []
        _federal_states_of_legal_person = d.pop("federal_states_of_legal_person", UNSET)
        for federal_states_of_legal_person_item_data in (_federal_states_of_legal_person or []):
            federal_states_of_legal_person_item = MasterClientFullHistoricalValueString.from_dict(federal_states_of_legal_person_item_data)



            federal_states_of_legal_person.append(federal_states_of_legal_person_item)


        current_fiscal_year = d.pop("current_fiscal_year", UNSET)

        fiscal_years = []
        _fiscal_years = d.pop("fiscal_years", UNSET)
        for fiscal_years_item_data in (_fiscal_years or []):
            fiscal_years_item = MasterClientFullHistoricalValueString.from_dict(fiscal_years_item_data)



            fiscal_years.append(fiscal_years_item)


        _current_kind_of_register_court = d.pop("current_kind_of_register_court", UNSET)
        current_kind_of_register_court: Union[Unset, MasterClientFullAddresseeDetailCurrentKindOfRegisterCourt]
        if isinstance(_current_kind_of_register_court,  Unset):
            current_kind_of_register_court = UNSET
        else:
            current_kind_of_register_court = MasterClientFullAddresseeDetailCurrentKindOfRegisterCourt(_current_kind_of_register_court)




        kind_of_register_courts = []
        _kind_of_register_courts = d.pop("kind_of_register_courts", UNSET)
        for kind_of_register_courts_item_data in (_kind_of_register_courts or []):
            kind_of_register_courts_item = MasterClientFullHistoricalValueString.from_dict(kind_of_register_courts_item_data)



            kind_of_register_courts.append(kind_of_register_courts_item)


        current_location_of_head_office = d.pop("current_location_of_head_office", UNSET)

        locations_of_head_office = []
        _locations_of_head_office = d.pop("locations_of_head_office", UNSET)
        for locations_of_head_office_item_data in (_locations_of_head_office or []):
            locations_of_head_office_item = MasterClientFullHistoricalValueString.from_dict(locations_of_head_office_item_data)



            locations_of_head_office.append(locations_of_head_office_item)


        current_name_of_register_court = d.pop("current_name_of_register_court", UNSET)

        names_of_register_court = []
        _names_of_register_court = d.pop("names_of_register_court", UNSET)
        for names_of_register_court_item_data in (_names_of_register_court or []):
            names_of_register_court_item = MasterClientFullHistoricalValueString.from_dict(names_of_register_court_item_data)



            names_of_register_court.append(names_of_register_court_item)


        current_registered_company_name = d.pop("current_registered_company_name", UNSET)

        registered_company_names = []
        _registered_company_names = d.pop("registered_company_names", UNSET)
        for registered_company_names_item_data in (_registered_company_names or []):
            registered_company_names_item = MasterClientFullHistoricalValueString.from_dict(registered_company_names_item_data)



            registered_company_names.append(registered_company_names_item)


        _registration_date = d.pop("registration_date", UNSET)
        registration_date: Union[Unset, datetime.date]
        if isinstance(_registration_date,  Unset):
            registration_date = UNSET
        else:
            registration_date = isoparse(_registration_date).date()




        current_registration_number = d.pop("current_registration_number", UNSET)

        registration_numbers = []
        _registration_numbers = d.pop("registration_numbers", UNSET)
        for registration_numbers_item_data in (_registration_numbers or []):
            registration_numbers_item = MasterClientFullHistoricalValueString.from_dict(registration_numbers_item_data)



            registration_numbers.append(registration_numbers_item)


        current_three_lined_company_name_first_line = d.pop("current_three_lined_company_name_first_line", UNSET)

        three_lined_company_names_first_line = []
        _three_lined_company_names_first_line = d.pop("three_lined_company_names_first_line", UNSET)
        for three_lined_company_names_first_line_item_data in (_three_lined_company_names_first_line or []):
            three_lined_company_names_first_line_item = MasterClientFullHistoricalValueString.from_dict(three_lined_company_names_first_line_item_data)



            three_lined_company_names_first_line.append(three_lined_company_names_first_line_item)


        current_three_lined_company_name_second_line = d.pop("current_three_lined_company_name_second_line", UNSET)

        three_lined_company_names_second_line = []
        _three_lined_company_names_second_line = d.pop("three_lined_company_names_second_line", UNSET)
        for three_lined_company_names_second_line_item_data in (_three_lined_company_names_second_line or []):
            three_lined_company_names_second_line_item = MasterClientFullHistoricalValueString.from_dict(three_lined_company_names_second_line_item_data)



            three_lined_company_names_second_line.append(three_lined_company_names_second_line_item)


        current_three_lined_company_name_third_line = d.pop("current_three_lined_company_name_third_line", UNSET)

        three_lined_company_names_third_line = []
        _three_lined_company_names_third_line = d.pop("three_lined_company_names_third_line", UNSET)
        for three_lined_company_names_third_line_item_data in (_three_lined_company_names_third_line or []):
            three_lined_company_names_third_line_item = MasterClientFullHistoricalValueString.from_dict(three_lined_company_names_third_line_item_data)



            three_lined_company_names_third_line.append(three_lined_company_names_third_line_item)


        current_two_lined_company_name_first_line = d.pop("current_two_lined_company_name_first_line", UNSET)

        two_lined_company_names_first_line = []
        _two_lined_company_names_first_line = d.pop("two_lined_company_names_first_line", UNSET)
        for two_lined_company_names_first_line_item_data in (_two_lined_company_names_first_line or []):
            two_lined_company_names_first_line_item = MasterClientFullHistoricalValueString.from_dict(two_lined_company_names_first_line_item_data)



            two_lined_company_names_first_line.append(two_lined_company_names_first_line_item)


        current_two_lined_company_name_second_line = d.pop("current_two_lined_company_name_second_line", UNSET)

        two_lined_company_names_second_line = []
        _two_lined_company_names_second_line = d.pop("two_lined_company_names_second_line", UNSET)
        for two_lined_company_names_second_line_item_data in (_two_lined_company_names_second_line or []):
            two_lined_company_names_second_line_item = MasterClientFullHistoricalValueString.from_dict(two_lined_company_names_second_line_item_data)



            two_lined_company_names_second_line.append(two_lined_company_names_second_line_item)


        _winding_up_date = d.pop("winding_up_date", UNSET)
        winding_up_date: Union[Unset, datetime.date]
        if isinstance(_winding_up_date,  Unset):
            winding_up_date = UNSET
        else:
            winding_up_date = isoparse(_winding_up_date).date()




        _winding_up_proceedings = d.pop("winding_up_proceedings", UNSET)
        winding_up_proceedings: Union[Unset, MasterClientFullAddresseeDetailWindingUpProceedings]
        if isinstance(_winding_up_proceedings,  Unset):
            winding_up_proceedings = UNSET
        else:
            winding_up_proceedings = MasterClientFullAddresseeDetailWindingUpProceedings(_winding_up_proceedings)




        all_first_names = d.pop("all_first_names", UNSET)

        birth_name = d.pop("birth_name", UNSET)

        _current_consideration = d.pop("current_consideration", UNSET)
        current_consideration: Union[Unset, MasterClientFullAddresseeDetailCurrentConsideration]
        if isinstance(_current_consideration,  Unset):
            current_consideration = UNSET
        else:
            current_consideration = MasterClientFullAddresseeDetailCurrentConsideration(_current_consideration)




        considerations = []
        _considerations = d.pop("considerations", UNSET)
        for considerations_item_data in (_considerations or []):
            considerations_item = MasterClientFullHistoricalValueString.from_dict(considerations_item_data)



            considerations.append(considerations_item)


        _country_of_birth = d.pop("country_of_birth", UNSET)
        country_of_birth: Union[Unset, MasterClientFullAddresseeDetailCountryOfBirth]
        if isinstance(_country_of_birth,  Unset):
            country_of_birth = UNSET
        else:
            country_of_birth = MasterClientFullAddresseeDetailCountryOfBirth(_country_of_birth)




        _date_of_death = d.pop("date_of_death", UNSET)
        date_of_death: Union[Unset, datetime.date]
        if isinstance(_date_of_death,  Unset):
            date_of_death = UNSET
        else:
            date_of_death = isoparse(_date_of_death).date()




        _date_of_expiry = d.pop("date_of_expiry", UNSET)
        date_of_expiry: Union[Unset, datetime.date]
        if isinstance(_date_of_expiry,  Unset):
            date_of_expiry = UNSET
        else:
            date_of_expiry = isoparse(_date_of_expiry).date()




        _date_of_issue = d.pop("date_of_issue", UNSET)
        date_of_issue: Union[Unset, datetime.date]
        if isinstance(_date_of_issue,  Unset):
            date_of_issue = UNSET
        else:
            date_of_issue = isoparse(_date_of_issue).date()




        degree = d.pop("degree", UNSET)

        _current_federal_state_of_natural_person = d.pop("current_federal_state_of_natural_person", UNSET)
        current_federal_state_of_natural_person: Union[Unset, MasterClientFullAddresseeDetailCurrentFederalStateOfNaturalPerson]
        if isinstance(_current_federal_state_of_natural_person,  Unset):
            current_federal_state_of_natural_person = UNSET
        else:
            current_federal_state_of_natural_person = MasterClientFullAddresseeDetailCurrentFederalStateOfNaturalPerson(_current_federal_state_of_natural_person)




        federal_states_of_natural_person = []
        _federal_states_of_natural_person = d.pop("federal_states_of_natural_person", UNSET)
        for federal_states_of_natural_person_item_data in (_federal_states_of_natural_person or []):
            federal_states_of_natural_person_item = MasterClientFullHistoricalValueString.from_dict(federal_states_of_natural_person_item_data)



            federal_states_of_natural_person.append(federal_states_of_natural_person_item)


        identification_number = d.pop("identification_number", UNSET)

        issuing_authority = d.pop("issuing_authority", UNSET)

        current_job_title = d.pop("current_job_title", UNSET)

        job_titles = []
        _job_titles = d.pop("job_titles", UNSET)
        for job_titles_item_data in (_job_titles or []):
            job_titles_item = MasterClientFullHistoricalValueString.from_dict(job_titles_item_data)



            job_titles.append(job_titles_item)


        legitimation_comment = d.pop("legitimation_comment", UNSET)

        _current_marital_status = d.pop("current_marital_status", UNSET)
        current_marital_status: Union[Unset, MasterClientFullAddresseeDetailCurrentMaritalStatus]
        if isinstance(_current_marital_status,  Unset):
            current_marital_status = UNSET
        else:
            current_marital_status = MasterClientFullAddresseeDetailCurrentMaritalStatus(_current_marital_status)




        marital_statuses = []
        _marital_statuses = d.pop("marital_statuses", UNSET)
        for marital_statuses_item_data in (_marital_statuses or []):
            marital_statuses_item = MasterClientFullHistoricalValueString.from_dict(marital_statuses_item_data)



            marital_statuses.append(marital_statuses_item)


        _name_prefix = d.pop("name_prefix", UNSET)
        name_prefix: Union[Unset, MasterClientFullAddresseeDetailNamePrefix]
        if isinstance(_name_prefix,  Unset):
            name_prefix = UNSET
        else:
            name_prefix = MasterClientFullAddresseeDetailNamePrefix(_name_prefix)




        _nationality = d.pop("nationality", UNSET)
        nationality: Union[Unset, MasterClientFullAddresseeDetailNationality]
        if isinstance(_nationality,  Unset):
            nationality = UNSET
        else:
            nationality = MasterClientFullAddresseeDetailNationality(_nationality)




        other_nationalities = []
        _other_nationalities = d.pop("other_nationalities", UNSET)
        for other_nationalities_item_data in (_other_nationalities or []):
            other_nationalities_item = MasterClientFullAddresseeDetailOtherNationality.from_dict(other_nationalities_item_data)



            other_nationalities.append(other_nationalities_item)


        _paper_of_identity = d.pop("paper_of_identity", UNSET)
        paper_of_identity: Union[Unset, MasterClientFullAddresseeDetailPaperOfIdentity]
        if isinstance(_paper_of_identity,  Unset):
            paper_of_identity = UNSET
        else:
            paper_of_identity = MasterClientFullAddresseeDetailPaperOfIdentity(_paper_of_identity)




        pension_insurance_institute = d.pop("pension_insurance_institute", UNSET)

        place_of_birth = d.pop("place_of_birth", UNSET)

        register_of_births_number = d.pop("register_of_births_number", UNSET)

        register_office_of_birth = d.pop("register_office_of_birth", UNSET)

        social_security_number = d.pop("social_security_number", UNSET)

        _title_of_nobility = d.pop("title_of_nobility", UNSET)
        title_of_nobility: Union[Unset, MasterClientFullAddresseeDetailTitleOfNobility]
        if isinstance(_title_of_nobility,  Unset):
            title_of_nobility = UNSET
        else:
            title_of_nobility = MasterClientFullAddresseeDetailTitleOfNobility(_title_of_nobility)




        master_client_full_addressee_detail = cls(
            complimentary_close=complimentary_close,
            correspondence_title=correspondence_title,
            national_right=national_right,
            note=note,
            salutation=salutation,
            current_code_of_classification_of_economic_activities_2008=current_code_of_classification_of_economic_activities_2008,
            codes_of_classification_of_economic_activities_2008=codes_of_classification_of_economic_activities_2008,
            current_description_of_classification_of_economic_activities_2008=current_description_of_classification_of_economic_activities_2008,
            descriptions_of_classification_of_economic_activities_2008=descriptions_of_classification_of_economic_activities_2008,
            current_mad_code_of_classification_of_economic_activities_2008=current_mad_code_of_classification_of_economic_activities_2008,
            mad_codes_of_classification_of_economic_activities_2008=mad_codes_of_classification_of_economic_activities_2008,
            current_code_of_classification_of_economic_activities_2003=current_code_of_classification_of_economic_activities_2003,
            codes_of_classification_of_economic_activities_2003=codes_of_classification_of_economic_activities_2003,
            current_description_of_classification_of_economic_activities_2003=current_description_of_classification_of_economic_activities_2003,
            descriptions_of_classification_of_economic_activities_2003=descriptions_of_classification_of_economic_activities_2003,
            current_mad_code_of_classification_of_economic_activities_2003=current_mad_code_of_classification_of_economic_activities_2003,
            mad_codes_of_classification_of_economic_activities_2003=mad_codes_of_classification_of_economic_activities_2003,
            current_country_of_head_office=current_country_of_head_office,
            countries_of_head_office=countries_of_head_office,
            date_of_memorandum_of_association=date_of_memorandum_of_association,
            current_distribution_of_profit=current_distribution_of_profit,
            distributions_of_profit=distributions_of_profit,
            current_enterprise_purpose=current_enterprise_purpose,
            enterprise_purposes=enterprise_purposes,
            current_federal_state_mad_of_legal_person=current_federal_state_mad_of_legal_person,
            federal_states_mad_of_legal_person=federal_states_mad_of_legal_person,
            current_federal_state_of_legal_person=current_federal_state_of_legal_person,
            federal_states_of_legal_person=federal_states_of_legal_person,
            current_fiscal_year=current_fiscal_year,
            fiscal_years=fiscal_years,
            current_kind_of_register_court=current_kind_of_register_court,
            kind_of_register_courts=kind_of_register_courts,
            current_location_of_head_office=current_location_of_head_office,
            locations_of_head_office=locations_of_head_office,
            current_name_of_register_court=current_name_of_register_court,
            names_of_register_court=names_of_register_court,
            current_registered_company_name=current_registered_company_name,
            registered_company_names=registered_company_names,
            registration_date=registration_date,
            current_registration_number=current_registration_number,
            registration_numbers=registration_numbers,
            current_three_lined_company_name_first_line=current_three_lined_company_name_first_line,
            three_lined_company_names_first_line=three_lined_company_names_first_line,
            current_three_lined_company_name_second_line=current_three_lined_company_name_second_line,
            three_lined_company_names_second_line=three_lined_company_names_second_line,
            current_three_lined_company_name_third_line=current_three_lined_company_name_third_line,
            three_lined_company_names_third_line=three_lined_company_names_third_line,
            current_two_lined_company_name_first_line=current_two_lined_company_name_first_line,
            two_lined_company_names_first_line=two_lined_company_names_first_line,
            current_two_lined_company_name_second_line=current_two_lined_company_name_second_line,
            two_lined_company_names_second_line=two_lined_company_names_second_line,
            winding_up_date=winding_up_date,
            winding_up_proceedings=winding_up_proceedings,
            all_first_names=all_first_names,
            birth_name=birth_name,
            current_consideration=current_consideration,
            considerations=considerations,
            country_of_birth=country_of_birth,
            date_of_death=date_of_death,
            date_of_expiry=date_of_expiry,
            date_of_issue=date_of_issue,
            degree=degree,
            current_federal_state_of_natural_person=current_federal_state_of_natural_person,
            federal_states_of_natural_person=federal_states_of_natural_person,
            identification_number=identification_number,
            issuing_authority=issuing_authority,
            current_job_title=current_job_title,
            job_titles=job_titles,
            legitimation_comment=legitimation_comment,
            current_marital_status=current_marital_status,
            marital_statuses=marital_statuses,
            name_prefix=name_prefix,
            nationality=nationality,
            other_nationalities=other_nationalities,
            paper_of_identity=paper_of_identity,
            pension_insurance_institute=pension_insurance_institute,
            place_of_birth=place_of_birth,
            register_of_births_number=register_of_births_number,
            register_office_of_birth=register_office_of_birth,
            social_security_number=social_security_number,
            title_of_nobility=title_of_nobility,
        )


        master_client_full_addressee_detail.additional_properties = d
        return master_client_full_addressee_detail

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
