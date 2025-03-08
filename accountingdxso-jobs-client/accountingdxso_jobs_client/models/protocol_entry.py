from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="ProtocolEntry")



@_attrs_define
class ProtocolEntry:
    """ 
        Attributes:
            time (Union[Unset, datetime.datetime]): import time  in accordance with ISO8601 'YYYY-MM-DDThh:mm:ss±hh:mm'
            text (Union[Unset, str]): further information about the protocol entry
            context (Union[Unset, str]): context of the protocol entry
            type_ (Union[Unset, str]): type of the protocol entry: information, warning, error
            filename (Union[Unset, str]): name of the file that is imported
     """

    time: Union[Unset, datetime.datetime] = UNSET
    text: Union[Unset, str] = UNSET
    context: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        text = self.text

        context = self.context

        type_ = self.type_

        filename = self.filename


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if time is not UNSET:
            field_dict["time"] = time
        if text is not UNSET:
            field_dict["text"] = text
        if context is not UNSET:
            field_dict["context"] = context
        if type_ is not UNSET:
            field_dict["type"] = type_
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = isoparse(_time)




        text = d.pop("text", UNSET)

        context = d.pop("context", UNSET)

        type_ = d.pop("type", UNSET)

        filename = d.pop("filename", UNSET)

        protocol_entry = cls(
            time=time,
            text=text,
            context=context,
            type_=type_,
            filename=filename,
        )


        protocol_entry.additional_properties = d
        return protocol_entry

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
