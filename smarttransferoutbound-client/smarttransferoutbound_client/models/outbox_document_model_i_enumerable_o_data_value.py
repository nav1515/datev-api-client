from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.outbox_document_model import OutboxDocumentModel





T = TypeVar("T", bound="OutboxDocumentModelIEnumerableODataValue")



@_attrs_define
class OutboxDocumentModelIEnumerableODataValue:
    """ 
        Attributes:
            value (Union[None, Unset, list['OutboxDocumentModel']]):
     """

    value: Union[None, Unset, list['OutboxDocumentModel']] = UNSET


    def to_dict(self) -> dict[str, Any]:
        from ..models.outbox_document_model import OutboxDocumentModel
        value: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = []
            for value_type_0_item_data in self.value:
                value_type_0_item = value_type_0_item_data.to_dict()
                value.append(value_type_0_item)


        else:
            value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.outbox_document_model import OutboxDocumentModel
        d = src_dict.copy()
        def _parse_value(data: object) -> Union[None, Unset, list['OutboxDocumentModel']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = []
                _value_type_0 = data
                for value_type_0_item_data in (_value_type_0):
                    value_type_0_item = OutboxDocumentModel.from_dict(value_type_0_item_data)



                    value_type_0.append(value_type_0_item)

                return value_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['OutboxDocumentModel']], data)

        value = _parse_value(d.pop("value", UNSET))


        outbox_document_model_i_enumerable_o_data_value = cls(
            value=value,
        )

        return outbox_document_model_i_enumerable_o_data_value

