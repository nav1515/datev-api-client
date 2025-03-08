from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_client_full_address_type import MasterClientFullAddressType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
from uuid import UUID
import datetime






T = TypeVar("T", bound="MasterClientFullAddress")



@_attrs_define
class MasterClientFullAddress:
    """ A postal address. Location part only, not containing the addressee's name.

        Attributes:
            type_ (MasterClientFullAddressType): (Adressart) The address type. Example: street.
            id (Union[Unset, UUID]): GUID - internal ID of an address. Example: 17b9d6d3-117b-4555-b0b0-3659eb0279d7.
            city (Union[Unset, str]): (Ort) Indicates the location. The maximum length depends on the country in which the
                address is located (for 'DE' and 'AT' 30 characters; for 'PL' 41 characters; for any other country or if no
                country has been defined 62 characters are permissible). Example: Mannheim.
            country_code (Union[Unset, str]): (Land) Indicates the country in which the address is located. Two-character
                country code as per ISO 3166. A list of all available country codes can be retrieved via `GET /country-codes`.
                Example: DE.
            postal_code (Union[Unset, str]): (Postleitzahl) Indicates the postal code. The maximum length depends on the
                country in which the address is located ('DE' 5 digits, 'AT' 4 digits, 'IT' 5 digits, 'CZ' 6 digits, 'PL' 6
                digits.  For 'DE' and 'AT', the maximum and minimum lengths are the same. For any other country or if no country
                has been defined 10 digits are permissible). Example: 68199.
            post_office_box (Union[Unset, str]): (Postfach) The post office box number. For address types other than
                "post_office_box" this attribute is empty.
            street (Union[Unset, str]): (Straße) The street part of the address, including street name, number and optional
                number extensions. For address types other than "street" this attribute is empty. The maximum length depends on
                the country in which the address is located (for 'DE' and 'AT' 36 characters; for any other country or if no
                country has been defined 41 characters are permissible). Example: Wacholderstr. 16 a.
            additional_correspondence_title (Union[Unset, str]): (Abw. Anrede) Indicates a differing title in
                correspondence. Example: Herrn/Frau/Firma.
            additional_delivery_text1 (Union[Unset, str]): (Abweichender Zustelladdressat) Indicates the first part of the
                name of the differing delivery addressee. Example: Schreinerei Musterholz.
            additional_delivery_text2 (Union[Unset, str]): (Abweichender Zustelladdressat) Indicates the second part of the
                name of the differing delivery addressee. Example: Offene Handelsgesellschaft.
            additional_shipping_information (Union[Unset, str]): (Versandzusatz) Indicates additional shipping information
                in correspondence, e.g. private/confidential or a shipment. Example: Wenn unzustellbar, zurück.
            address_appendix (Union[Unset, str]): Indicates an address appendix in correspondence, e.g. "c/o". Example: z.
                H. Herrn Mustermann.
            address_manually_edited (Union[Unset, str]): (Manuell geänderte Addresse) Indicates a manually edited address.
            is_address_manually_edited (Union[Unset, bool]): (Manuell geändert) Indicates whether the address has been
                manually edited.
            is_shared (Union[Unset, bool]): (Manuell geändert) Indicates whether the address is shared.
            note (Union[Unset, str]): (Notiz) Field for notes about the address. Example: Das ist eine Notiz zur Anschrift.
            valid_from (Union[Unset, datetime.date]): (Gültig von) Indicates the date from which an address is valid.
            valid_to (Union[Unset, datetime.date]): (Gültig bis) Indicates the date until which an address is valid.
            currently_valid (Union[Unset, bool]): (Gültig) Indicates whether or not the address is currently valid. Example:
                True.
            is_correspondence_address (Union[Unset, bool]): (Korrespondezadresse) Indicates whether this is the
                correspondence address. Among all valid addresses  of an addressee, this property must be marked with 'true'
                exactly once. Example: True.
            is_debitor_address (Union[Unset, bool]): (Debitoren-Rechnungsadresse) Indicates whether this is the debtor
                address. Among all valid addresses of an addressee, this property must be marked with 'true' no more than once.
                Example: True.
            is_main_post_office_box_address (Union[Unset, bool]): (Hauptpostfachadresse) Indicates whether this is the main
                post office box address. Only relevant if the address is a post office box address (type=post_office_box). Among
                all valid post office box addresses of an addressee, this property must be marked with 'true' exactly once.
            is_main_street_address (Union[Unset, bool]): (Hauptstraßenadresse) Indicates whether this is the main street
                address. Only relevant if the address is a street address (type=street). Among all valid street addresses of an
                addressee, this property must be marked with 'true' exactly once. Example: True.
            is_management_address (Union[Unset, bool]): (Geschäftsleitungsadresse) Indicates whether this is the management
                address. Only relevant if the associated addressee is of the type 'legal_person'. Among all valid addresses of
                an addressee (legal_person), this property must be marked with 'true' exactly once. Example: True.
     """

    type_: MasterClientFullAddressType
    id: Union[Unset, UUID] = UNSET
    city: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    post_office_box: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    additional_correspondence_title: Union[Unset, str] = UNSET
    additional_delivery_text1: Union[Unset, str] = UNSET
    additional_delivery_text2: Union[Unset, str] = UNSET
    additional_shipping_information: Union[Unset, str] = UNSET
    address_appendix: Union[Unset, str] = UNSET
    address_manually_edited: Union[Unset, str] = UNSET
    is_address_manually_edited: Union[Unset, bool] = UNSET
    is_shared: Union[Unset, bool] = UNSET
    note: Union[Unset, str] = UNSET
    valid_from: Union[Unset, datetime.date] = UNSET
    valid_to: Union[Unset, datetime.date] = UNSET
    currently_valid: Union[Unset, bool] = UNSET
    is_correspondence_address: Union[Unset, bool] = UNSET
    is_debitor_address: Union[Unset, bool] = UNSET
    is_main_post_office_box_address: Union[Unset, bool] = UNSET
    is_main_street_address: Union[Unset, bool] = UNSET
    is_management_address: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        city = self.city

        country_code = self.country_code

        postal_code = self.postal_code

        post_office_box = self.post_office_box

        street = self.street

        additional_correspondence_title = self.additional_correspondence_title

        additional_delivery_text1 = self.additional_delivery_text1

        additional_delivery_text2 = self.additional_delivery_text2

        additional_shipping_information = self.additional_shipping_information

        address_appendix = self.address_appendix

        address_manually_edited = self.address_manually_edited

        is_address_manually_edited = self.is_address_manually_edited

        is_shared = self.is_shared

        note = self.note

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        valid_to: Union[Unset, str] = UNSET
        if not isinstance(self.valid_to, Unset):
            valid_to = self.valid_to.isoformat()

        currently_valid = self.currently_valid

        is_correspondence_address = self.is_correspondence_address

        is_debitor_address = self.is_debitor_address

        is_main_post_office_box_address = self.is_main_post_office_box_address

        is_main_street_address = self.is_main_street_address

        is_management_address = self.is_management_address


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if city is not UNSET:
            field_dict["city"] = city
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if post_office_box is not UNSET:
            field_dict["post_office_box"] = post_office_box
        if street is not UNSET:
            field_dict["street"] = street
        if additional_correspondence_title is not UNSET:
            field_dict["additional_correspondence_title"] = additional_correspondence_title
        if additional_delivery_text1 is not UNSET:
            field_dict["additional_delivery_text1"] = additional_delivery_text1
        if additional_delivery_text2 is not UNSET:
            field_dict["additional_delivery_text2"] = additional_delivery_text2
        if additional_shipping_information is not UNSET:
            field_dict["additional_shipping_information"] = additional_shipping_information
        if address_appendix is not UNSET:
            field_dict["address_appendix"] = address_appendix
        if address_manually_edited is not UNSET:
            field_dict["address_manually_edited"] = address_manually_edited
        if is_address_manually_edited is not UNSET:
            field_dict["is_address_manually_edited"] = is_address_manually_edited
        if is_shared is not UNSET:
            field_dict["is_shared"] = is_shared
        if note is not UNSET:
            field_dict["note"] = note
        if valid_from is not UNSET:
            field_dict["valid_from"] = valid_from
        if valid_to is not UNSET:
            field_dict["valid_to"] = valid_to
        if currently_valid is not UNSET:
            field_dict["currently_valid"] = currently_valid
        if is_correspondence_address is not UNSET:
            field_dict["is_correspondence_address"] = is_correspondence_address
        if is_debitor_address is not UNSET:
            field_dict["is_debitor_address"] = is_debitor_address
        if is_main_post_office_box_address is not UNSET:
            field_dict["is_main_post_office_box_address"] = is_main_post_office_box_address
        if is_main_street_address is not UNSET:
            field_dict["is_main_street_address"] = is_main_street_address
        if is_management_address is not UNSET:
            field_dict["is_management_address"] = is_management_address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = MasterClientFullAddressType(d.pop("type"))




        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        city = d.pop("city", UNSET)

        country_code = d.pop("country_code", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        post_office_box = d.pop("post_office_box", UNSET)

        street = d.pop("street", UNSET)

        additional_correspondence_title = d.pop("additional_correspondence_title", UNSET)

        additional_delivery_text1 = d.pop("additional_delivery_text1", UNSET)

        additional_delivery_text2 = d.pop("additional_delivery_text2", UNSET)

        additional_shipping_information = d.pop("additional_shipping_information", UNSET)

        address_appendix = d.pop("address_appendix", UNSET)

        address_manually_edited = d.pop("address_manually_edited", UNSET)

        is_address_manually_edited = d.pop("is_address_manually_edited", UNSET)

        is_shared = d.pop("is_shared", UNSET)

        note = d.pop("note", UNSET)

        _valid_from = d.pop("valid_from", UNSET)
        valid_from: Union[Unset, datetime.date]
        if isinstance(_valid_from,  Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from).date()




        _valid_to = d.pop("valid_to", UNSET)
        valid_to: Union[Unset, datetime.date]
        if isinstance(_valid_to,  Unset):
            valid_to = UNSET
        else:
            valid_to = isoparse(_valid_to).date()




        currently_valid = d.pop("currently_valid", UNSET)

        is_correspondence_address = d.pop("is_correspondence_address", UNSET)

        is_debitor_address = d.pop("is_debitor_address", UNSET)

        is_main_post_office_box_address = d.pop("is_main_post_office_box_address", UNSET)

        is_main_street_address = d.pop("is_main_street_address", UNSET)

        is_management_address = d.pop("is_management_address", UNSET)

        master_client_full_address = cls(
            type_=type_,
            id=id,
            city=city,
            country_code=country_code,
            postal_code=postal_code,
            post_office_box=post_office_box,
            street=street,
            additional_correspondence_title=additional_correspondence_title,
            additional_delivery_text1=additional_delivery_text1,
            additional_delivery_text2=additional_delivery_text2,
            additional_shipping_information=additional_shipping_information,
            address_appendix=address_appendix,
            address_manually_edited=address_manually_edited,
            is_address_manually_edited=is_address_manually_edited,
            is_shared=is_shared,
            note=note,
            valid_from=valid_from,
            valid_to=valid_to,
            currently_valid=currently_valid,
            is_correspondence_address=is_correspondence_address,
            is_debitor_address=is_debitor_address,
            is_main_post_office_box_address=is_main_post_office_box_address,
            is_main_street_address=is_main_street_address,
            is_management_address=is_management_address,
        )


        master_client_full_address.additional_properties = d
        return master_client_full_address

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
