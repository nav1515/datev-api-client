from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="LogModel")



@_attrs_define
class LogModel:
    """ Defines the log model.

        Attributes:
            id (Union[Unset, int]): Gets or sets the identifier.
            module (Union[None, Unset, str]): Gets or sets the module.
            severity (Union[Unset, int]): Gets or sets the severity.
            reference (Union[None, Unset, int]): Gets or sets the reference.
            reference_type (Union[None, Unset, int]): Gets or sets the type of the reference.
            user_id (Union[None, Unset, int]): Gets or sets the user identifier.
            text (Union[None, Unset, str]): Gets or sets the text.
            action (Union[None, Unset, str]): Gets or sets the action.
            action_parameters (Union[None, Unset, str]): Gets or sets the action parameters.
            sub_module (Union[None, Unset, str]): Gets or sets the sub module.
            created (Union[Unset, datetime.datetime]): Gets or sets the created.
     """

    id: Union[Unset, int] = UNSET
    module: Union[None, Unset, str] = UNSET
    severity: Union[Unset, int] = UNSET
    reference: Union[None, Unset, int] = UNSET
    reference_type: Union[None, Unset, int] = UNSET
    user_id: Union[None, Unset, int] = UNSET
    text: Union[None, Unset, str] = UNSET
    action: Union[None, Unset, str] = UNSET
    action_parameters: Union[None, Unset, str] = UNSET
    sub_module: Union[None, Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET


    def to_dict(self) -> dict[str, Any]:
        id = self.id

        module: Union[None, Unset, str]
        if isinstance(self.module, Unset):
            module = UNSET
        else:
            module = self.module

        severity = self.severity

        reference: Union[None, Unset, int]
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        reference_type: Union[None, Unset, int]
        if isinstance(self.reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = self.reference_type

        user_id: Union[None, Unset, int]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        text: Union[None, Unset, str]
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        action: Union[None, Unset, str]
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        action_parameters: Union[None, Unset, str]
        if isinstance(self.action_parameters, Unset):
            action_parameters = UNSET
        else:
            action_parameters = self.action_parameters

        sub_module: Union[None, Unset, str]
        if isinstance(self.sub_module, Unset):
            sub_module = UNSET
        else:
            sub_module = self.sub_module

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if module is not UNSET:
            field_dict["module"] = module
        if severity is not UNSET:
            field_dict["severity"] = severity
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if text is not UNSET:
            field_dict["text"] = text
        if action is not UNSET:
            field_dict["action"] = action
        if action_parameters is not UNSET:
            field_dict["actionParameters"] = action_parameters
        if sub_module is not UNSET:
            field_dict["subModule"] = sub_module
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        def _parse_module(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        module = _parse_module(d.pop("module", UNSET))


        severity = d.pop("severity", UNSET)

        def _parse_reference(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        reference = _parse_reference(d.pop("reference", UNSET))


        def _parse_reference_type(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        reference_type = _parse_reference_type(d.pop("referenceType", UNSET))


        def _parse_user_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        user_id = _parse_user_id(d.pop("userId", UNSET))


        def _parse_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text = _parse_text(d.pop("text", UNSET))


        def _parse_action(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        action = _parse_action(d.pop("action", UNSET))


        def _parse_action_parameters(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        action_parameters = _parse_action_parameters(d.pop("actionParameters", UNSET))


        def _parse_sub_module(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sub_module = _parse_sub_module(d.pop("subModule", UNSET))


        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        log_model = cls(
            id=id,
            module=module,
            severity=severity,
            reference=reference,
            reference_type=reference_type,
            user_id=user_id,
            text=text,
            action=action,
            action_parameters=action_parameters,
            sub_module=sub_module,
            created=created,
        )

        return log_model

