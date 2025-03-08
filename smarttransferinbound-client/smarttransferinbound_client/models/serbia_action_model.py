from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="SerbiaActionModel")



@_attrs_define
class SerbiaActionModel:
    """ Defines the Serbian action model.

        Attributes:
            comment (str): The comment or reason for the target document of the action.
            id (Union[Unset, int]): The ID of the document.
     """

    comment: str
    id: Union[Unset, int] = UNSET


    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update({
            "comment": comment,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        comment = d.pop("comment")

        id = d.pop("id", UNSET)

        serbia_action_model = cls(
            comment=comment,
            id=id,
        )

        return serbia_action_model

