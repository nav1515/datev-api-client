from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.org_info_data_environment import OrgInfoDataEnvironment
  from ..models.org_info_business_partner import OrgInfoBusinessPartner





T = TypeVar("T", bound="OrgInfo")



@_attrs_define
class OrgInfo:
    """ Information about the current user's organization.

        Attributes:
            business_partner (Union[Unset, OrgInfoBusinessPartner]): Information about a business partner in the current
                users context.
            data_environments (Union[Unset, list['OrgInfoDataEnvironment']]):
     """

    business_partner: Union[Unset, 'OrgInfoBusinessPartner'] = UNSET
    data_environments: Union[Unset, list['OrgInfoDataEnvironment']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.org_info_data_environment import OrgInfoDataEnvironment
        from ..models.org_info_business_partner import OrgInfoBusinessPartner
        business_partner: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.business_partner, Unset):
            business_partner = self.business_partner.to_dict()

        data_environments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_environments, Unset):
            data_environments = []
            for data_environments_item_data in self.data_environments:
                data_environments_item = data_environments_item_data.to_dict()
                data_environments.append(data_environments_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if business_partner is not UNSET:
            field_dict["business_partner"] = business_partner
        if data_environments is not UNSET:
            field_dict["data_environments"] = data_environments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.org_info_data_environment import OrgInfoDataEnvironment
        from ..models.org_info_business_partner import OrgInfoBusinessPartner
        d = src_dict.copy()
        _business_partner = d.pop("business_partner", UNSET)
        business_partner: Union[Unset, OrgInfoBusinessPartner]
        if isinstance(_business_partner,  Unset):
            business_partner = UNSET
        else:
            business_partner = OrgInfoBusinessPartner.from_dict(_business_partner)




        data_environments = []
        _data_environments = d.pop("data_environments", UNSET)
        for data_environments_item_data in (_data_environments or []):
            data_environments_item = OrgInfoDataEnvironment.from_dict(data_environments_item_data)



            data_environments.append(data_environments_item)


        org_info = cls(
            business_partner=business_partner,
            data_environments=data_environments,
        )


        org_info.additional_properties = d
        return org_info

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
