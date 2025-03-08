from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.additional_message import AdditionalMessage





T = TypeVar("T", bound="ErrorMessage")



@_attrs_define
class ErrorMessage:
    """ 
        Attributes:
            error (Union[Unset, str]):
            error_description (Union[Unset, str]):
            error_uri (Union[Unset, str]):
            request_id (Union[Unset, str]):
            additional_messages (Union[Unset, list['AdditionalMessage']]):
     """

    error: Union[Unset, str] = UNSET
    error_description: Union[Unset, str] = UNSET
    error_uri: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    additional_messages: Union[Unset, list['AdditionalMessage']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.additional_message import AdditionalMessage
        error = self.error

        error_description = self.error_description

        error_uri = self.error_uri

        request_id = self.request_id

        additional_messages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.additional_messages, Unset):
            additional_messages = []
            for additional_messages_item_data in self.additional_messages:
                additional_messages_item = additional_messages_item_data.to_dict()
                additional_messages.append(additional_messages_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if error_uri is not UNSET:
            field_dict["error_uri"] = error_uri
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if additional_messages is not UNSET:
            field_dict["additional_messages"] = additional_messages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.additional_message import AdditionalMessage
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        error_description = d.pop("error_description", UNSET)

        error_uri = d.pop("error_uri", UNSET)

        request_id = d.pop("request_id", UNSET)

        additional_messages = []
        _additional_messages = d.pop("additional_messages", UNSET)
        for additional_messages_item_data in (_additional_messages or []):
            additional_messages_item = AdditionalMessage.from_dict(additional_messages_item_data)



            additional_messages.append(additional_messages_item)


        error_message = cls(
            error=error,
            error_description=error_description,
            error_uri=error_uri,
            request_id=request_id,
            additional_messages=additional_messages,
        )


        error_message.additional_properties = d
        return error_message

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
