from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_client_full_addressee_detail_other_nationality_nationality import MasterClientFullAddresseeDetailOtherNationalityNationality
from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="MasterClientFullAddresseeDetailOtherNationality")



@_attrs_define
class MasterClientFullAddresseeDetailOtherNationality:
    """ (Weitere Staatsangehörigkeit) Other nationality of a natural person.

        Attributes:
            id (Union[Unset, UUID]): GUID - internal ID of another nationality. Example:
                ba8ce4a6-8eb7-4bb9-a7d7-c54be7b34cd1.
            nationality (Union[Unset, MasterClientFullAddresseeDetailOtherNationalityNationality]): (Weitere
                Staatsangehörigkeit) Other nationality of a natural person. The following values are permissible (Afghanisch,
                Ägyptisch, Albanisch, Algerisch, Amerikanisch, Andorranisch, Angolanisch, Antiguanisch, Äquatorialguineisch,
                Argentinisch, Armenisch, Aserbaidschanisch, Äthiopisch, Australisch, Bahamaisch, Bahrainisch, Bangladeschisch,
                Barbadisch, Belarussisch, Belgisch, Belizisch, Beninisch, Bhutanisch, Bolivianisch, Bosnisch-herzegowinisch,
                Botsuanisch, Brasilianisch, Britisch, Bruneiisch, Bulgarisch, Burkinisch, Burundisch, Chilenisch, Chinesisch,
                Costa-ricanisch, Dänisch, Deutsch, Dominicanisch, Dominikanisch, Dschibutisch, Ecuadorianisch, Eritreisch,
                Estnisch, Fidschianisch, Finnisch, Französisch, Gabunisch, Gambisch, Georgisch, Ghanaisch, Grenadisch,
                Griechisch, Guatemaltekisch, Guinea-bissauisch, Guineisch, Guyanisch, Haitianisch, Honduranisch, Indisch,
                Indonesisch, Irakisch, Iranisch, Irisch, Isländisch, Israelisch, Italienisch, Ivorisch, Jamaikanisch, Japanisch,
                Jemenitisch, Jordanisch, Kambodschanisch, Kamerunisch, Kanadisch, Kap-verdisch, Kasachisch, Katarisch,
                Kenianisch, Kirgisisch, Kiribatisch, Kolumbianisch, Komorisch, Kongolesisch, Koreanisch, Kosovarisch, Kroatisch,
                Kubanisch, Kuwaitisch, Laotisch, Lesothisch, Lettisch, Libanesisch, Liberianisch, Libysch, Liechtensteinisch,
                Litauisch, Lucianisch, Luxemburgisch, Madagassisch, Malawisch, Malaysisch, Maledivisch, Malisch, Maltesisch,
                Marokkanisch, Marshallisch, Mauretanisch, Mauritisch, Mazedonisch, Mexikanisch, Mikronesisch, Moldauisch,
                Monegassisch, Mongolisch, Montenegrinisch, Mosambikanisch, Myanmarisch, Namibisch, Nauruisch, Nepalesisch,
                Neuseeländisch, Nicaraguanisch, Niederländisch, Nigerianisch, Nigrisch, Niueanisch, Norwegisch, Omanisch,
                Österreichisch, Pakistanisch, Palauisch, Panamaisch, Papua-neuguineisch, Paraguayisch, Peruanisch,
                Philippinisch, Polnisch, Portugiesisch, Ruandisch, Rumänisch, Russisch, Salomonisch, Salvadorianisch, Sambisch,
                Samoanisch, San-marinesisch, Sao-toméisch, Saudi-arabisch, Schwedisch, Schweizerisch, Senegalesisch, Serbisch,
                Serbisch-montenegrinisch, Seychellisch, Sierra-leonisch, Simbabwisch, Singapurisch, Slowakisch, Slowenisch,
                Somalisch, Spanisch, Sri-lankisch, Südafrikanisch, Sudanesisch, Südsudanesisch, Surinamisch, Swasiländisch,
                Syrisch, Tadschikisch, Taiwanisch, Tansanisch, Thailändisch, Timorisch, Togoisch, Trinidad Tobago Bürger,
                Tongaisch, Tschadisch, Tschechisch, Tunesisch, Türkisch, Turkmenisch, Tuvaluisch, Ugandisch, Ukrainisch,
                Ungarisch, Uruguayisch, Usbekisch, Vanuatuisch, Vatikanisch, Venezolanisch, Vietnamesisch, Vincentisch,
                Zentralafrikanisch, Zyprisch). Example: Schweizerisch.
     """

    id: Union[Unset, UUID] = UNSET
    nationality: Union[Unset, MasterClientFullAddresseeDetailOtherNationalityNationality] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        nationality: Union[Unset, str] = UNSET
        if not isinstance(self.nationality, Unset):
            nationality = self.nationality.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if nationality is not UNSET:
            field_dict["nationality"] = nationality

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




        _nationality = d.pop("nationality", UNSET)
        nationality: Union[Unset, MasterClientFullAddresseeDetailOtherNationalityNationality]
        if isinstance(_nationality,  Unset):
            nationality = UNSET
        else:
            nationality = MasterClientFullAddresseeDetailOtherNationalityNationality(_nationality)




        master_client_full_addressee_detail_other_nationality = cls(
            id=id,
            nationality=nationality,
        )


        master_client_full_addressee_detail_other_nationality.additional_properties = d
        return master_client_full_addressee_detail_other_nationality

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
