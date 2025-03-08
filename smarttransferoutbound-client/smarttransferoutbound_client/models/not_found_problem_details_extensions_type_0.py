from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.not_found_problem_details_extensions_type_0_additional_property import NotFoundProblemDetailsExtensionsType0AdditionalProperty





T = TypeVar("T", bound="NotFoundProblemDetailsExtensionsType0")



@_attrs_define
class NotFoundProblemDetailsExtensionsType0:
    """ 
     """

    additional_properties: dict[str, 'NotFoundProblemDetailsExtensionsType0AdditionalProperty'] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.not_found_problem_details_extensions_type_0_additional_property import NotFoundProblemDetailsExtensionsType0AdditionalProperty
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.not_found_problem_details_extensions_type_0_additional_property import NotFoundProblemDetailsExtensionsType0AdditionalProperty
        d = src_dict.copy()
        not_found_problem_details_extensions_type_0 = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = NotFoundProblemDetailsExtensionsType0AdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        not_found_problem_details_extensions_type_0.additional_properties = additional_properties
        return not_found_problem_details_extensions_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> 'NotFoundProblemDetailsExtensionsType0AdditionalProperty':
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: 'NotFoundProblemDetailsExtensionsType0AdditionalProperty') -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
