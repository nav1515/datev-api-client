from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_client_full_communication_type import MasterClientFullCommunicationType
from ..types import UNSET, Unset
from typing import Union
from uuid import UUID






T = TypeVar("T", bound="MasterClientFullCommunication")



@_attrs_define
class MasterClientFullCommunication:
    """ (Angaben zu Kommunikation) Communication specific data.

        Attributes:
            type_ (MasterClientFullCommunicationType): (Verbindungsart) Indicates the type of communication medium to which
                a certain number/address relates. Example: phone.
            id (Union[Unset, UUID]): GUID - internal ID of a communication link. Example:
                20b9d6d9-117b-4555-b0b0-3659eb0279d9.
            data_content (Union[Unset, str]): (Inhalt) Indicates the number (e.g. telephone number) or address (e.g. e-mail
                address) of the communication medium concerned. Example: +49 8721 123456.
            number_standardized (Union[Unset, str]): (Nummer normiert) Indicates the telephone number/fax number without
                special characters (purely as a sequence of digits). Example: 00498721123456.
            note (Union[Unset, str]): (Notiz) Field for notes about the communication link. Example: ab 9 Uhr.
            is_main_communication (Union[Unset, bool]): (Standardverbindung) Indicates the standard communication link for
                each means of communication. If communication_type is 'other', then this property may not be set to 'true'.
                Apart from this, exactly one of the communication links for the means of communication must be marked as 'true'.
                Example: True.
            is_management_phone (Union[Unset, bool]): (Geschäftsleitungsverbindung) Indicates the management phone. Only
                relevant if the communication type is 'phone' and the associated addressee is of the type 'legal_person'.
                Exactly one telephone line of the corresponding addressee must be marked as 'true'. Example: True.
     """

    type_: MasterClientFullCommunicationType
    id: Union[Unset, UUID] = UNSET
    data_content: Union[Unset, str] = UNSET
    number_standardized: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    is_main_communication: Union[Unset, bool] = UNSET
    is_management_phone: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        data_content = self.data_content

        number_standardized = self.number_standardized

        note = self.note

        is_main_communication = self.is_main_communication

        is_management_phone = self.is_management_phone


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if data_content is not UNSET:
            field_dict["data_content"] = data_content
        if number_standardized is not UNSET:
            field_dict["number_standardized"] = number_standardized
        if note is not UNSET:
            field_dict["note"] = note
        if is_main_communication is not UNSET:
            field_dict["is_main_communication"] = is_main_communication
        if is_management_phone is not UNSET:
            field_dict["is_management_phone"] = is_management_phone

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = MasterClientFullCommunicationType(d.pop("type"))




        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        data_content = d.pop("data_content", UNSET)

        number_standardized = d.pop("number_standardized", UNSET)

        note = d.pop("note", UNSET)

        is_main_communication = d.pop("is_main_communication", UNSET)

        is_management_phone = d.pop("is_management_phone", UNSET)

        master_client_full_communication = cls(
            type_=type_,
            id=id,
            data_content=data_content,
            number_standardized=number_standardized,
            note=note,
            is_main_communication=is_main_communication,
            is_management_phone=is_management_phone,
        )


        master_client_full_communication.additional_properties = d
        return master_client_full_communication

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
