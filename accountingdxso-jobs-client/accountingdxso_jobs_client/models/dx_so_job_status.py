from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="DXSoJobStatus")



@_attrs_define
class DXSoJobStatus:
    """ 
        Attributes:
            id (Union[Unset, str]): ID of the data transfer (dxso-job)
            status (Union[Unset, int]): status values:   0: data transfer (dxso-job) is still open and has yet not been
                finalized    1: processing of the data transfer (dxso-job) has been started and is still in progress    2: data
                transfer (dxso-job) has been processed successfully    3: data transfer (dxso-job) has not been processed -
                critical errors occurred that have to be checked    4: data transfer (dxso-job) has been processed partially -
                errors occurred that have to be checked    5: data transfer (dxso-job) has been successfully cancelled in Belege
                online    6: data transfer (dxso-job) has not been cancelled in Belege online because the requirements were not
                fulfilled
     """

    id: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        dx_so_job_status = cls(
            id=id,
            status=status,
        )


        dx_so_job_status.additional_properties = d
        return dx_so_job_status

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
