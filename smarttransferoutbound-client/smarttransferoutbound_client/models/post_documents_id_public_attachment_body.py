from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json

from ..types import UNSET, Unset

from ..types import File, FileJsonType
from ..types import UNSET, Unset
from io import BytesIO
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="PostDocumentsIdPublicAttachmentBody")



@_attrs_define
class PostDocumentsIdPublicAttachmentBody:
    """ 
        Attributes:
            attachment (Union[File, None, Unset]): The attachment.
     """

    attachment: Union[File, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        attachment: Union[FileJsonType, None, Unset]
        if isinstance(self.attachment, Unset):
            attachment = UNSET
        elif isinstance(self.attachment, File):
            attachment = self.attachment.to_tuple()

        else:
            attachment = self.attachment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachment is not UNSET:
            field_dict["attachment"] = attachment

        return field_dict


    def to_multipart(self) -> dict[str, Any]:
        attachment: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.attachment, Unset):
            attachment = UNSET
        elif isinstance(self.attachment, File):
            attachment = self.attachment.to_tuple()
        else:
            attachment =  (None, str(self.attachment).encode(), "text/plain")



        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] =  (None, str(prop).encode(), "text/plain")

        field_dict.update({
        })
        if attachment is not UNSET:
            field_dict["attachment"] = attachment

        return field_dict


    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        def _parse_attachment(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                attachment_type_0 = File(
                     payload = BytesIO(data)
                )



                return attachment_type_0
            except: # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        attachment = _parse_attachment(d.pop("attachment", UNSET))


        post_documents_id_public_attachment_body = cls(
            attachment=attachment,
        )


        post_documents_id_public_attachment_body.additional_properties = d
        return post_documents_id_public_attachment_body

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
