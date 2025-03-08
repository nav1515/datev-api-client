from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.forbidden_problem_details_extensions_type_0 import ForbiddenProblemDetailsExtensionsType0





T = TypeVar("T", bound="ForbiddenProblemDetails")



@_attrs_define
class ForbiddenProblemDetails:
    """ Forbidden problem details.

        Attributes:
            type_ (Union[None, Unset, str]):
            title (Union[None, Unset, str]):
            status (Union[None, Unset, int]):
            detail (Union[None, Unset, str]):
            instance (Union[None, Unset, str]):
            extensions (Union['ForbiddenProblemDetailsExtensionsType0', None, Unset]):
     """

    type_: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, int] = UNSET
    detail: Union[None, Unset, str] = UNSET
    instance: Union[None, Unset, str] = UNSET
    extensions: Union['ForbiddenProblemDetailsExtensionsType0', None, Unset] = UNSET


    def to_dict(self) -> dict[str, Any]:
        from ..models.forbidden_problem_details_extensions_type_0 import ForbiddenProblemDetailsExtensionsType0
        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: Union[None, Unset, int]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        detail: Union[None, Unset, str]
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        instance: Union[None, Unset, str]
        if isinstance(self.instance, Unset):
            instance = UNSET
        else:
            instance = self.instance

        extensions: Union[None, Unset, dict[str, Any]]
        if isinstance(self.extensions, Unset):
            extensions = UNSET
        elif isinstance(self.extensions, ForbiddenProblemDetailsExtensionsType0):
            extensions = self.extensions.to_dict()
        else:
            extensions = self.extensions


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.forbidden_problem_details_extensions_type_0 import ForbiddenProblemDetailsExtensionsType0
        d = src_dict.copy()
        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_detail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        detail = _parse_detail(d.pop("detail", UNSET))


        def _parse_instance(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instance = _parse_instance(d.pop("instance", UNSET))


        def _parse_extensions(data: object) -> Union['ForbiddenProblemDetailsExtensionsType0', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extensions_type_0 = ForbiddenProblemDetailsExtensionsType0.from_dict(data)



                return extensions_type_0
            except: # noqa: E722
                pass
            return cast(Union['ForbiddenProblemDetailsExtensionsType0', None, Unset], data)

        extensions = _parse_extensions(d.pop("extensions", UNSET))


        forbidden_problem_details = cls(
            type_=type_,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
            extensions=extensions,
        )

        return forbidden_problem_details

