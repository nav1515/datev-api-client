from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="UserModel")



@_attrs_define
class UserModel:
    """ Contains information related to a user.

        Attributes:
            id (Union[Unset, int]): Gets or sets the user identifier.
            client_id (Union[Unset, int]): Gets or sets the client identifier to which the user belongs.
            first_name (Union[None, Unset, str]): Gets or sets the first name of the user.
            last_name (Union[None, Unset, str]): Gets or sets the last name of the user.
            email (Union[None, Unset, str]): Gets or sets the email of the user.
     """

    id: Union[Unset, int] = UNSET
    client_id: Union[Unset, int] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET


    def to_dict(self) -> dict[str, Any]:
        id = self.id

        client_id = self.client_id

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        client_id = d.pop("clientId", UNSET)

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))


        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))


        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))


        user_model = cls(
            id=id,
            client_id=client_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        return user_model

