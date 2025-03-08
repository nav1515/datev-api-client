from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.notification_state import NotificationState
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="NotificationModel")



@_attrs_define
class NotificationModel:
    """ 
        Attributes:
            id (Union[Unset, int]):
            client_id (Union[None, Unset, int]):
            state (Union[Unset, NotificationState]): <table style="font-size: 12px;">  <thead style="background-color:
                rgba(0,0,0,0.05); border:1px solid rgba(0,0,0,0.08);">    <tr>      <td style="padding: 12px">Name</td>      <td
                style="padding: 12px">Description</td>    </tr>  </thead>  <tbody>  </tbody></table>
            language (Union[None, Unset, str]):
            receiver_email (Union[None, Unset, str]):
            return_address (Union[None, Unset, str]):
            sender_email (Union[None, Unset, str]):
            country (Union[None, Unset, str]):
            type_ (Union[None, Unset, str]):
            document_id (Union[None, Unset, int]): Corresponds to the "MessageId" which is unknown to the outside world.
            created (Union[Unset, datetime.datetime]):
     """

    id: Union[Unset, int] = UNSET
    client_id: Union[None, Unset, int] = UNSET
    state: Union[Unset, NotificationState] = UNSET
    language: Union[None, Unset, str] = UNSET
    receiver_email: Union[None, Unset, str] = UNSET
    return_address: Union[None, Unset, str] = UNSET
    sender_email: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    document_id: Union[None, Unset, int] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET


    def to_dict(self) -> dict[str, Any]:
        id = self.id

        client_id: Union[None, Unset, int]
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        state: Union[Unset, int] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value


        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        receiver_email: Union[None, Unset, str]
        if isinstance(self.receiver_email, Unset):
            receiver_email = UNSET
        else:
            receiver_email = self.receiver_email

        return_address: Union[None, Unset, str]
        if isinstance(self.return_address, Unset):
            return_address = UNSET
        else:
            return_address = self.return_address

        sender_email: Union[None, Unset, str]
        if isinstance(self.sender_email, Unset):
            sender_email = UNSET
        else:
            sender_email = self.sender_email

        country: Union[None, Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        document_id: Union[None, Unset, int]
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if state is not UNSET:
            field_dict["state"] = state
        if language is not UNSET:
            field_dict["language"] = language
        if receiver_email is not UNSET:
            field_dict["receiverEmail"] = receiver_email
        if return_address is not UNSET:
            field_dict["returnAddress"] = return_address
        if sender_email is not UNSET:
            field_dict["senderEmail"] = sender_email
        if country is not UNSET:
            field_dict["country"] = country
        if type_ is not UNSET:
            field_dict["type"] = type_
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        def _parse_client_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        client_id = _parse_client_id(d.pop("clientId", UNSET))


        _state = d.pop("state", UNSET)
        state: Union[Unset, NotificationState]
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = NotificationState(_state)




        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("language", UNSET))


        def _parse_receiver_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        receiver_email = _parse_receiver_email(d.pop("receiverEmail", UNSET))


        def _parse_return_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        return_address = _parse_return_address(d.pop("returnAddress", UNSET))


        def _parse_sender_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sender_email = _parse_sender_email(d.pop("senderEmail", UNSET))


        def _parse_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country = _parse_country(d.pop("country", UNSET))


        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_document_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        document_id = _parse_document_id(d.pop("documentId", UNSET))


        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        notification_model = cls(
            id=id,
            client_id=client_id,
            state=state,
            language=language,
            receiver_email=receiver_email,
            return_address=return_address,
            sender_email=sender_email,
            country=country,
            type_=type_,
            document_id=document_id,
            created=created,
        )

        return notification_model

