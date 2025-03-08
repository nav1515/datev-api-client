from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="WorkflowTransition")



@_attrs_define
class WorkflowTransition:
    """ Contains information related to workflow transition for a document.

        Attributes:
            document_id (Union[Unset, int]): Gets or sets the document identifier.
            workflow (Union[None, Unset, str]): Gets or sets the workflow.
            transition (Union[None, Unset, str]): Gets or sets the transition.
     """

    document_id: Union[Unset, int] = UNSET
    workflow: Union[None, Unset, str] = UNSET
    transition: Union[None, Unset, str] = UNSET


    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        workflow: Union[None, Unset, str]
        if isinstance(self.workflow, Unset):
            workflow = UNSET
        else:
            workflow = self.workflow

        transition: Union[None, Unset, str]
        if isinstance(self.transition, Unset):
            transition = UNSET
        else:
            transition = self.transition


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if transition is not UNSET:
            field_dict["transition"] = transition

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        document_id = d.pop("documentId", UNSET)

        def _parse_workflow(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        workflow = _parse_workflow(d.pop("workflow", UNSET))


        def _parse_transition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        transition = _parse_transition(d.pop("transition", UNSET))


        workflow_transition = cls(
            document_id=document_id,
            workflow=workflow,
            transition=transition,
        )

        return workflow_transition

