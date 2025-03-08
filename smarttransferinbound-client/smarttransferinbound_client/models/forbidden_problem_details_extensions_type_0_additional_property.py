from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ForbiddenProblemDetailsExtensionsType0AdditionalProperty")



@_attrs_define
class ForbiddenProblemDetailsExtensionsType0AdditionalProperty:
    """ 
     """



    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        forbidden_problem_details_extensions_type_0_additional_property = cls(
        )

        return forbidden_problem_details_extensions_type_0_additional_property

