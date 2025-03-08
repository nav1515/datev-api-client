from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.problem_details_additional_info import ProblemDetailsAdditionalInfo





T = TypeVar("T", bound="ProblemDetailsViolationDetails")



@_attrs_define
class ProblemDetailsViolationDetails:
    """ Additional details in case of validation failures (when reason is set to `VALIDATION_FAILED`).

        Attributes:
            description (Union[Unset, str]): A description for the violation.
            affected_field (Union[Unset, str]): The affected field in form of a JSON path.
            type_ (Union[Unset, str]): The violation type. The following violation types are possible:
                | Violation type | Description or cause |
                | ----------- | -------------------- |
                | MISSING_PROPERTY |  A required property is missing. |
                | INVALID_PROPERTY |  A property is invalid in the context that it's used in. |
                | INVALID_ENUMERATION |  A property contains a value that is not one of the allowed enumeration values. |
                | OUT_OF_RANGE |  An integer is out of the allowed range (either too small or large). |
                | INVALID_LENGTH |  A string has an invalid length (either too small or large). |
                | INVALID_PATTERN |  A string does not conform the the required pattern (regular expression). |
            additional_info (Union[Unset, list['ProblemDetailsAdditionalInfo']]): Additional information for the given
                violation type.
     """

    description: Union[Unset, str] = UNSET
    affected_field: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_info: Union[Unset, list['ProblemDetailsAdditionalInfo']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.problem_details_additional_info import ProblemDetailsAdditionalInfo
        description = self.description

        affected_field = self.affected_field

        type_ = self.type_

        additional_info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.additional_info, Unset):
            additional_info = []
            for additional_info_item_data in self.additional_info:
                additional_info_item = additional_info_item_data.to_dict()
                additional_info.append(additional_info_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if affected_field is not UNSET:
            field_dict["affected_field"] = affected_field
        if type_ is not UNSET:
            field_dict["type"] = type_
        if additional_info is not UNSET:
            field_dict["additional_info"] = additional_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.problem_details_additional_info import ProblemDetailsAdditionalInfo
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        affected_field = d.pop("affected_field", UNSET)

        type_ = d.pop("type", UNSET)

        additional_info = []
        _additional_info = d.pop("additional_info", UNSET)
        for additional_info_item_data in (_additional_info or []):
            additional_info_item = ProblemDetailsAdditionalInfo.from_dict(additional_info_item_data)



            additional_info.append(additional_info_item)


        problem_details_violation_details = cls(
            description=description,
            affected_field=affected_field,
            type_=type_,
            additional_info=additional_info,
        )


        problem_details_violation_details.additional_properties = d
        return problem_details_violation_details

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
