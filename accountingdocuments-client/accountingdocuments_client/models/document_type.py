from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.document_type_category import DocumentTypeCategory
from ..models.document_type_debit_credit_identifier import DocumentTypeDebitCreditIdentifier
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="DocumentType")



@_attrs_define
class DocumentType:
    """ 
        Attributes:
            name (Union[Unset, str]): name of the document type
            category (Union[Unset, DocumentTypeCategory]): category of the document type
            debit_credit_identifier (Union[Unset, DocumentTypeDebitCreditIdentifier]): debit/credit identifier of the
                document type
     """

    name: Union[Unset, str] = UNSET
    category: Union[Unset, DocumentTypeCategory] = UNSET
    debit_credit_identifier: Union[Unset, DocumentTypeDebitCreditIdentifier] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        name = self.name

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value


        debit_credit_identifier: Union[Unset, str] = UNSET
        if not isinstance(self.debit_credit_identifier, Unset):
            debit_credit_identifier = self.debit_credit_identifier.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if debit_credit_identifier is not UNSET:
            field_dict["debit_credit_identifier"] = debit_credit_identifier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, DocumentTypeCategory]
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = DocumentTypeCategory(_category)




        _debit_credit_identifier = d.pop("debit_credit_identifier", UNSET)
        debit_credit_identifier: Union[Unset, DocumentTypeDebitCreditIdentifier]
        if isinstance(_debit_credit_identifier,  Unset):
            debit_credit_identifier = UNSET
        else:
            debit_credit_identifier = DocumentTypeDebitCreditIdentifier(_debit_credit_identifier)




        document_type = cls(
            name=name,
            category=category,
            debit_credit_identifier=debit_credit_identifier,
        )


        document_type.additional_properties = d
        return document_type

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
