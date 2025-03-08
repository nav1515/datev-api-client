from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="Metadata")



@_attrs_define
class Metadata:
    """ 
        Attributes:
            document_type (Union[Unset, str]): Name of the document type
            note (Union[Unset, str]): Note pertaining to the document for the tax consultant.
            category (Union[Unset, str]): First level of the document repository of Belege online. As soon as one of the
                repository levels is used, all three levels has to be entered.
            folder (Union[Unset, str]): Second level of the document repository of Belege online. As soon as one of the
                repository levels is used, all three levels has to be entered.
            register (Union[Unset, str]): Third level of the document repository of Belege online. As soon as one of the
                repository levels is used, all three levels has to be entered.
     """

    document_type: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    folder: Union[Unset, str] = UNSET
    register: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        document_type = self.document_type

        note = self.note

        category = self.category

        folder = self.folder

        register = self.register


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if note is not UNSET:
            field_dict["note"] = note
        if category is not UNSET:
            field_dict["category"] = category
        if folder is not UNSET:
            field_dict["folder"] = folder
        if register is not UNSET:
            field_dict["register"] = register

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        document_type = d.pop("document_type", UNSET)

        note = d.pop("note", UNSET)

        category = d.pop("category", UNSET)

        folder = d.pop("folder", UNSET)

        register = d.pop("register", UNSET)

        metadata = cls(
            document_type=document_type,
            note=note,
            category=category,
            folder=folder,
            register=register,
        )


        metadata.additional_properties = d
        return metadata

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
