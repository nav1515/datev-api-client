from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PartyModel")



@_attrs_define
class PartyModel:
    """ 
        Attributes:
            id (Union[None, Unset, int]):
            name (Union[None, Unset, str]):
            street (Union[None, Unset, str]):
            zip_ (Union[None, Unset, str]):
            city (Union[None, Unset, str]):
            address_name_line_1 (Union[None, Unset, str]):
            address_name_line_2 (Union[None, Unset, str]):
            address_name_line_3 (Union[None, Unset, str]):
            e_mail (Union[None, Unset, str]):
            country (Union[None, Unset, str]):
            vat_id (Union[None, Unset, str]):
            tax_id (Union[None, Unset, str]):
            iln (Union[None, Unset, str]):
            is_registered (Union[Unset, bool]):
     """

    id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    street: Union[None, Unset, str] = UNSET
    zip_: Union[None, Unset, str] = UNSET
    city: Union[None, Unset, str] = UNSET
    address_name_line_1: Union[None, Unset, str] = UNSET
    address_name_line_2: Union[None, Unset, str] = UNSET
    address_name_line_3: Union[None, Unset, str] = UNSET
    e_mail: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET
    vat_id: Union[None, Unset, str] = UNSET
    tax_id: Union[None, Unset, str] = UNSET
    iln: Union[None, Unset, str] = UNSET
    is_registered: Union[Unset, bool] = UNSET


    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        street: Union[None, Unset, str]
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        zip_: Union[None, Unset, str]
        if isinstance(self.zip_, Unset):
            zip_ = UNSET
        else:
            zip_ = self.zip_

        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        address_name_line_1: Union[None, Unset, str]
        if isinstance(self.address_name_line_1, Unset):
            address_name_line_1 = UNSET
        else:
            address_name_line_1 = self.address_name_line_1

        address_name_line_2: Union[None, Unset, str]
        if isinstance(self.address_name_line_2, Unset):
            address_name_line_2 = UNSET
        else:
            address_name_line_2 = self.address_name_line_2

        address_name_line_3: Union[None, Unset, str]
        if isinstance(self.address_name_line_3, Unset):
            address_name_line_3 = UNSET
        else:
            address_name_line_3 = self.address_name_line_3

        e_mail: Union[None, Unset, str]
        if isinstance(self.e_mail, Unset):
            e_mail = UNSET
        else:
            e_mail = self.e_mail

        country: Union[None, Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        vat_id: Union[None, Unset, str]
        if isinstance(self.vat_id, Unset):
            vat_id = UNSET
        else:
            vat_id = self.vat_id

        tax_id: Union[None, Unset, str]
        if isinstance(self.tax_id, Unset):
            tax_id = UNSET
        else:
            tax_id = self.tax_id

        iln: Union[None, Unset, str]
        if isinstance(self.iln, Unset):
            iln = UNSET
        else:
            iln = self.iln

        is_registered = self.is_registered


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if street is not UNSET:
            field_dict["street"] = street
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if city is not UNSET:
            field_dict["city"] = city
        if address_name_line_1 is not UNSET:
            field_dict["addressNameLine1"] = address_name_line_1
        if address_name_line_2 is not UNSET:
            field_dict["addressNameLine2"] = address_name_line_2
        if address_name_line_3 is not UNSET:
            field_dict["addressNameLine3"] = address_name_line_3
        if e_mail is not UNSET:
            field_dict["eMail"] = e_mail
        if country is not UNSET:
            field_dict["country"] = country
        if vat_id is not UNSET:
            field_dict["vatId"] = vat_id
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if iln is not UNSET:
            field_dict["iln"] = iln
        if is_registered is not UNSET:
            field_dict["isRegistered"] = is_registered

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_street(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street = _parse_street(d.pop("street", UNSET))


        def _parse_zip_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zip_ = _parse_zip_(d.pop("zip", UNSET))


        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_address_name_line_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address_name_line_1 = _parse_address_name_line_1(d.pop("addressNameLine1", UNSET))


        def _parse_address_name_line_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address_name_line_2 = _parse_address_name_line_2(d.pop("addressNameLine2", UNSET))


        def _parse_address_name_line_3(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address_name_line_3 = _parse_address_name_line_3(d.pop("addressNameLine3", UNSET))


        def _parse_e_mail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        e_mail = _parse_e_mail(d.pop("eMail", UNSET))


        def _parse_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country = _parse_country(d.pop("country", UNSET))


        def _parse_vat_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vat_id = _parse_vat_id(d.pop("vatId", UNSET))


        def _parse_tax_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tax_id = _parse_tax_id(d.pop("taxId", UNSET))


        def _parse_iln(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        iln = _parse_iln(d.pop("iln", UNSET))


        is_registered = d.pop("isRegistered", UNSET)

        party_model = cls(
            id=id,
            name=name,
            street=street,
            zip_=zip_,
            city=city,
            address_name_line_1=address_name_line_1,
            address_name_line_2=address_name_line_2,
            address_name_line_3=address_name_line_3,
            e_mail=e_mail,
            country=country,
            vat_id=vat_id,
            tax_id=tax_id,
            iln=iln,
            is_registered=is_registered,
        )

        return party_model

