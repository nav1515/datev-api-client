from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.basic_accounting_information import BasicAccountingInformation





T = TypeVar("T", bound="ClientBasics")



@_attrs_define
class ClientBasics:
    """ 
        Attributes:
            client_number (Union[Unset, int]): client number
            consultant_number (Union[Unset, int]): consultant number
            id (Union[Unset, str]): client id (technical)
            name (Union[Unset, str]): client name
            is_document_management_available (Union[Unset, bool]): Belege online is existent (= true) or is nonexistent (=
                false)
            basic_accounting_information (Union[Unset, list['BasicAccountingInformation']]): Basic accounting data and array
                of existent account books. The last three fiscal years are returned.
     """

    client_number: Union[Unset, int] = UNSET
    consultant_number: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    is_document_management_available: Union[Unset, bool] = UNSET
    basic_accounting_information: Union[Unset, list['BasicAccountingInformation']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.basic_accounting_information import BasicAccountingInformation
        client_number = self.client_number

        consultant_number = self.consultant_number

        id = self.id

        name = self.name

        is_document_management_available = self.is_document_management_available

        basic_accounting_information: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.basic_accounting_information, Unset):
            basic_accounting_information = []
            for basic_accounting_information_item_data in self.basic_accounting_information:
                basic_accounting_information_item = basic_accounting_information_item_data.to_dict()
                basic_accounting_information.append(basic_accounting_information_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if client_number is not UNSET:
            field_dict["client_number"] = client_number
        if consultant_number is not UNSET:
            field_dict["consultant_number"] = consultant_number
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_document_management_available is not UNSET:
            field_dict["is_document_management_available"] = is_document_management_available
        if basic_accounting_information is not UNSET:
            field_dict["basic_accounting_information"] = basic_accounting_information

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.basic_accounting_information import BasicAccountingInformation
        d = src_dict.copy()
        client_number = d.pop("client_number", UNSET)

        consultant_number = d.pop("consultant_number", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_document_management_available = d.pop("is_document_management_available", UNSET)

        basic_accounting_information = []
        _basic_accounting_information = d.pop("basic_accounting_information", UNSET)
        for basic_accounting_information_item_data in (_basic_accounting_information or []):
            basic_accounting_information_item = BasicAccountingInformation.from_dict(basic_accounting_information_item_data)



            basic_accounting_information.append(basic_accounting_information_item)


        client_basics = cls(
            client_number=client_number,
            consultant_number=consultant_number,
            id=id,
            name=name,
            is_document_management_available=is_document_management_available,
            basic_accounting_information=basic_accounting_information,
        )


        client_basics.additional_properties = d
        return client_basics

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
