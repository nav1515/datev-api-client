from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="WorkflowState")



@_attrs_define
class WorkflowState:
    """ Contains information related to workflow state.

        Attributes:
            workflow (Union[None, Unset, str]): Gets or sets the workflow name.
            state (Union[None, Unset, str]): Gets or sets the workflow state.
     """

    workflow: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET


    def to_dict(self) -> dict[str, Any]:
        workflow: Union[None, Unset, str]
        if isinstance(self.workflow, Unset):
            workflow = UNSET
        else:
            workflow = self.workflow

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        def _parse_workflow(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        workflow = _parse_workflow(d.pop("workflow", UNSET))


        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))


        workflow_state = cls(
            workflow=workflow,
            state=state,
        )

        return workflow_state

