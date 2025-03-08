from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_client_legal_form_id import MasterClientLegalFormId
from ..models.master_client_legal_form_nation import MasterClientLegalFormNation
from ..models.master_client_legal_form_type import MasterClientLegalFormType
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="MasterClientLegalForm")



@_attrs_define
class MasterClientLegalForm:
    """ (Rechtsform) Current legal form of the enterprise (= value as at system date).
    A list of all available legal forms can be retreived via `GET /legal-forms`.

        Attributes:
            id (Union[Unset, MasterClientLegalFormId]): ID of the legal form. The following values are permissible
                (S01101=Aktiebolag, S00010=Aktiengesellschaft, S00110=Aktiengesellschaft, S00112=AG & Co. KG, S00019=AG & Co.
                KG, S00049=Aktiengesellschaft & Co. OHG, S00130=AG & Still, S01502=Anstalt d. priv. Rechts, S00031=Anstalt des
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
                Gegenseitigkeit, S00045=Wohnungseigentümergemeinschaft). Example: S00009.
            short_name (Union[Unset, str]):  Example: GmbH.
            long_name (Union[Unset, str]):  Example: Gesellschaft mit beschränkter Haftung.
            nation (Union[Unset, MasterClientLegalFormNation]): Country to which the legal form relates. Example: DE.
            type_ (Union[Unset, MasterClientLegalFormType]): Indicates the legal form of the enterprise. The following
                values are permissible (1 = Einzelunternehmen, 2 = Personengesellschaft, 3 = Kapitalgesellschaft, 4 =
                Sonderform). Example: 3.
     """

    id: Union[Unset, MasterClientLegalFormId] = UNSET
    short_name: Union[Unset, str] = UNSET
    long_name: Union[Unset, str] = UNSET
    nation: Union[Unset, MasterClientLegalFormNation] = UNSET
    type_: Union[Unset, MasterClientLegalFormType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.value


        short_name = self.short_name

        long_name = self.long_name

        nation: Union[Unset, str] = UNSET
        if not isinstance(self.nation, Unset):
            nation = self.nation.value


        type_: Union[Unset, int] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if short_name is not UNSET:
            field_dict["short_name"] = short_name
        if long_name is not UNSET:
            field_dict["long_name"] = long_name
        if nation is not UNSET:
            field_dict["nation"] = nation
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, MasterClientLegalFormId]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = MasterClientLegalFormId(_id)




        short_name = d.pop("short_name", UNSET)

        long_name = d.pop("long_name", UNSET)

        _nation = d.pop("nation", UNSET)
        nation: Union[Unset, MasterClientLegalFormNation]
        if isinstance(_nation,  Unset):
            nation = UNSET
        else:
            nation = MasterClientLegalFormNation(_nation)




        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, MasterClientLegalFormType]
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = MasterClientLegalFormType(_type_)




        master_client_legal_form = cls(
            id=id,
            short_name=short_name,
            long_name=long_name,
            nation=nation,
            type_=type_,
        )


        master_client_legal_form.additional_properties = d
        return master_client_legal_form

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
