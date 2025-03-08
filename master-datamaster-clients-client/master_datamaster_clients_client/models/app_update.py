from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.brick_context import BrickContext





T = TypeVar("T", bound="AppUpdate")



@_attrs_define
class AppUpdate:
    """ Data to set for the API Consumer.

        Attributes:
            brick_contexts (Union[Unset, list['BrickContext']]): Listing of context and bricks which define the schema of
                the returned master clients.
     """

    brick_contexts: Union[Unset, list['BrickContext']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.brick_context import BrickContext
        brick_contexts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.brick_contexts, Unset):
            brick_contexts = []
            for brick_contexts_item_data in self.brick_contexts:
                brick_contexts_item = brick_contexts_item_data.to_dict()
                brick_contexts.append(brick_contexts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if brick_contexts is not UNSET:
            field_dict["brick_contexts"] = brick_contexts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.brick_context import BrickContext
        d = src_dict.copy()
        brick_contexts = []
        _brick_contexts = d.pop("brick_contexts", UNSET)
        for brick_contexts_item_data in (_brick_contexts or []):
            brick_contexts_item = BrickContext.from_dict(brick_contexts_item_data)



            brick_contexts.append(brick_contexts_item)


        app_update = cls(
            brick_contexts=brick_contexts,
        )


        app_update.additional_properties = d
        return app_update

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
