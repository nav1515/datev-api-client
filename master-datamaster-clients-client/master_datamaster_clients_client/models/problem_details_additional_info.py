from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.problem_details_additional_info_value import ProblemDetailsAdditionalInfoValue





T = TypeVar("T", bound="ProblemDetailsAdditionalInfo")



@_attrs_define
class ProblemDetailsAdditionalInfo:
    """ Additional information for the given violation type.

        Attributes:
            key (Union[Unset, str]):
            value (Union[Unset, ProblemDetailsAdditionalInfoValue]):
     """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, 'ProblemDetailsAdditionalInfoValue'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.problem_details_additional_info_value import ProblemDetailsAdditionalInfoValue
        key = self.key

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.problem_details_additional_info_value import ProblemDetailsAdditionalInfoValue
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, ProblemDetailsAdditionalInfoValue]
        if isinstance(_value,  Unset):
            value = UNSET
        else:
            value = ProblemDetailsAdditionalInfoValue.from_dict(_value)




        problem_details_additional_info = cls(
            key=key,
            value=value,
        )


        problem_details_additional_info.additional_properties = d
        return problem_details_additional_info

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
