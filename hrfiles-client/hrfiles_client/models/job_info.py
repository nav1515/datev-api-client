from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.job_info_state import JobInfoState
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="JobInfo")



@_attrs_define
class JobInfo:
    """ Each JobInfo-Object is returned with its most current state. An JobInfo-Object is mapped to a single file.

        Attributes:
            job_id (str): Id which identifies requested job and therefore a file's current state. The Id is represented as
                an UUID in the format 8-4-4-4-12.
                 Example: abc12345-abcd-abcd-tt33-12345aedgf55.
            state (JobInfoState): State of the file. A file has the initial state uploaded. After it has been imported
                successfully into the payroll system, the state changes to 'imported'.
                Via the context menu in the payroll system, the state can be changed to either corrupted (if a file is not valid
                for an import) or to 'deleted' (if it should be deleted completely).
                If a file contains the state 'uploaded' for longer than 60 days or the file contains the state 'corrupted' or
                'imported' for longer than 365 days, the file will be deleted automatically and the state 'auto-deleted' will be
                set.
            timestamp (Union[Unset, str]): States the time (according to ISO8601) when the state has been set in the
                service.
                 Example: 2019-09-14T10:40:52+2:00.
     """

    job_id: str
    state: JobInfoState
    timestamp: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        state = self.state.value

        timestamp = self.timestamp


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "job_id": job_id,
            "state": state,
        })
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("job_id")

        state = JobInfoState(d.pop("state"))




        timestamp = d.pop("timestamp", UNSET)

        job_info = cls(
            job_id=job_id,
            state=state,
            timestamp=timestamp,
        )


        job_info.additional_properties = d
        return job_info

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
