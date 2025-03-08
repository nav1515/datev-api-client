from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.affected_element import AffectedElement





T = TypeVar("T", bound="ValidationDetails")



@_attrs_define
class ValidationDetails:
    """ 
        Attributes:
            type_ (Union[Unset, str]): A URI reference [RFC3986](https://tools.ietf.org/html/rfc3986) that identifies the
                problem type. This specification encourages that, when
                dereferenced, a human-readable documentation for the
                problem type (e.g., using HTML [W3C.REC-html5-20141028]) is provided.  When
                this member is not present, its value is assumed to be "about:blank".
                 Example: http://www.datev.de/hilfe/1008834.
            title (Union[Unset, str]): A short, human-readable summary of the problem
                type. It SHOULD NOT change from occurrence to occurrence of the
                problem, except for purposes of localization (e.g., using
                proactive content negotiation; see [RFC7231](https://tools.ietf.org/html/rfc7231#section-3.4), Section 3.4).
                 Example: Invalid EXTF-header.
            detail (Union[Unset, str]): A human-readable explanation specific to this occurrence of the problem.
                 Example: Fields with error.
            affected_elements (Union[Unset, list['AffectedElement']]):
     """

    type_: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    affected_elements: Union[Unset, list['AffectedElement']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.affected_element import AffectedElement
        type_ = self.type_

        title = self.title

        detail = self.detail

        affected_elements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_elements, Unset):
            affected_elements = []
            for affected_elements_item_data in self.affected_elements:
                affected_elements_item = affected_elements_item_data.to_dict()
                affected_elements.append(affected_elements_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if detail is not UNSET:
            field_dict["detail"] = detail
        if affected_elements is not UNSET:
            field_dict["affected_elements"] = affected_elements

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.affected_element import AffectedElement
        d = src_dict.copy()
        type_ = d.pop("type", UNSET)

        title = d.pop("title", UNSET)

        detail = d.pop("detail", UNSET)

        affected_elements = []
        _affected_elements = d.pop("affected_elements", UNSET)
        for affected_elements_item_data in (_affected_elements or []):
            affected_elements_item = AffectedElement.from_dict(affected_elements_item_data)



            affected_elements.append(affected_elements_item)


        validation_details = cls(
            type_=type_,
            title=title,
            detail=detail,
            affected_elements=affected_elements,
        )


        validation_details.additional_properties = d
        return validation_details

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
