from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.additional_message_severity import AdditionalMessageSeverity
from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="AdditionalMessage")



@_attrs_define
class AdditionalMessage:
    """ 
        Attributes:
            id (str): Unique ID
            severity (AdditionalMessageSeverity):
            description (Union[Unset, str]):
            help_uri (Union[Unset, str]):
            path (Union[Unset, str]): Path to affected resource
            affected_fields (Union[Unset, list[str]]): Paths of affected properties
     """

    id: str
    severity: AdditionalMessageSeverity
    description: Union[Unset, str] = UNSET
    help_uri: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    affected_fields: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id = self.id

        severity = self.severity.value

        description = self.description

        help_uri = self.help_uri

        path = self.path

        affected_fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.affected_fields, Unset):
            affected_fields = self.affected_fields




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "severity": severity,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if help_uri is not UNSET:
            field_dict["help_uri"] = help_uri
        if path is not UNSET:
            field_dict["path"] = path
        if affected_fields is not UNSET:
            field_dict["affected_fields"] = affected_fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        severity = AdditionalMessageSeverity(d.pop("severity"))




        description = d.pop("description", UNSET)

        help_uri = d.pop("help_uri", UNSET)

        path = d.pop("path", UNSET)

        affected_fields = cast(list[str], d.pop("affected_fields", UNSET))


        additional_message = cls(
            id=id,
            severity=severity,
            description=description,
            help_uri=help_uri,
            path=path,
            affected_fields=affected_fields,
        )


        additional_message.additional_properties = d
        return additional_message

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
