from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.job_result import JobResult
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.validation_details import ValidationDetails





T = TypeVar("T", bound="Job")



@_attrs_define
class Job:
    """ 
        Attributes:
            id (Union[Unset, str]): Identifies the job Example: 5656-zyxv-trew-ijkl.
            filename (Union[Unset, str]): Name of the file Example: EXTF_AusgangsrechnungenMaerz.CSV.
            fiscal_year_begin (Union[Unset, datetime.date]): First day of fiscal year
            client_application_display_name (Union[Unset, str]): Name of the system uploading the file Example: Test_Office.
            client_application_vendor (Union[Unset, str]): Vendor of the system uploading the file Example: Test_StartUp.
            client_application_version (Union[Unset, str]): Version of the system uploading the file Example: T_1.23.
            data_category_id (Union[Unset, int]): Data category ID. As an example, data_category_id 21 means "accounting
                records" Example: 21.
            date_from (Union[Unset, datetime.date]): Accounting sequence date from
            date_to (Union[Unset, datetime.date]): Accounting sequence date to
            label (Union[Unset, str]): Description of accounting sequence. Labels that exceed a lenght of 250 characters are
                truncated to 250 characters followed by three dots. Example: AR 2020/03.
            number_of_accounting_records (Union[Unset, int]): Number of accounting records Example: 127.
            reference_id (Union[Unset, str]): User defined ID Example: TO_2020_4713.
            result (Union[Unset, JobResult]): Status of the job Example: failed.
            timestamp (Union[Unset, datetime.datetime]): Timestamp when the service received the file (automatically
                created) Example: 2020-04-13T17:55:42Z.
            validation_details (Union[Unset, ValidationDetails]):
     """

    id: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    fiscal_year_begin: Union[Unset, datetime.date] = UNSET
    client_application_display_name: Union[Unset, str] = UNSET
    client_application_vendor: Union[Unset, str] = UNSET
    client_application_version: Union[Unset, str] = UNSET
    data_category_id: Union[Unset, int] = UNSET
    date_from: Union[Unset, datetime.date] = UNSET
    date_to: Union[Unset, datetime.date] = UNSET
    label: Union[Unset, str] = UNSET
    number_of_accounting_records: Union[Unset, int] = UNSET
    reference_id: Union[Unset, str] = UNSET
    result: Union[Unset, JobResult] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    validation_details: Union[Unset, 'ValidationDetails'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.validation_details import ValidationDetails
        id = self.id

        filename = self.filename

        fiscal_year_begin: Union[Unset, str] = UNSET
        if not isinstance(self.fiscal_year_begin, Unset):
            fiscal_year_begin = self.fiscal_year_begin.isoformat()

        client_application_display_name = self.client_application_display_name

        client_application_vendor = self.client_application_vendor

        client_application_version = self.client_application_version

        data_category_id = self.data_category_id

        date_from: Union[Unset, str] = UNSET
        if not isinstance(self.date_from, Unset):
            date_from = self.date_from.isoformat()

        date_to: Union[Unset, str] = UNSET
        if not isinstance(self.date_to, Unset):
            date_to = self.date_to.isoformat()

        label = self.label

        number_of_accounting_records = self.number_of_accounting_records

        reference_id = self.reference_id

        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value


        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        validation_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.validation_details, Unset):
            validation_details = self.validation_details.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if filename is not UNSET:
            field_dict["filename"] = filename
        if fiscal_year_begin is not UNSET:
            field_dict["fiscal_year_begin"] = fiscal_year_begin
        if client_application_display_name is not UNSET:
            field_dict["client_application_display_name"] = client_application_display_name
        if client_application_vendor is not UNSET:
            field_dict["client_application_vendor"] = client_application_vendor
        if client_application_version is not UNSET:
            field_dict["client_application_version"] = client_application_version
        if data_category_id is not UNSET:
            field_dict["data_category_id"] = data_category_id
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if label is not UNSET:
            field_dict["label"] = label
        if number_of_accounting_records is not UNSET:
            field_dict["number_of_accounting_records"] = number_of_accounting_records
        if reference_id is not UNSET:
            field_dict["reference_id"] = reference_id
        if result is not UNSET:
            field_dict["result"] = result
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if validation_details is not UNSET:
            field_dict["validation_details"] = validation_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.validation_details import ValidationDetails
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        filename = d.pop("filename", UNSET)

        _fiscal_year_begin = d.pop("fiscal_year_begin", UNSET)
        fiscal_year_begin: Union[Unset, datetime.date]
        if isinstance(_fiscal_year_begin,  Unset):
            fiscal_year_begin = UNSET
        else:
            fiscal_year_begin = isoparse(_fiscal_year_begin).date()




        client_application_display_name = d.pop("client_application_display_name", UNSET)

        client_application_vendor = d.pop("client_application_vendor", UNSET)

        client_application_version = d.pop("client_application_version", UNSET)

        data_category_id = d.pop("data_category_id", UNSET)

        _date_from = d.pop("date_from", UNSET)
        date_from: Union[Unset, datetime.date]
        if isinstance(_date_from,  Unset):
            date_from = UNSET
        else:
            date_from = isoparse(_date_from).date()




        _date_to = d.pop("date_to", UNSET)
        date_to: Union[Unset, datetime.date]
        if isinstance(_date_to,  Unset):
            date_to = UNSET
        else:
            date_to = isoparse(_date_to).date()




        label = d.pop("label", UNSET)

        number_of_accounting_records = d.pop("number_of_accounting_records", UNSET)

        reference_id = d.pop("reference_id", UNSET)

        _result = d.pop("result", UNSET)
        result: Union[Unset, JobResult]
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = JobResult(_result)




        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp,  Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)




        _validation_details = d.pop("validation_details", UNSET)
        validation_details: Union[Unset, ValidationDetails]
        if isinstance(_validation_details,  Unset):
            validation_details = UNSET
        else:
            validation_details = ValidationDetails.from_dict(_validation_details)




        job = cls(
            id=id,
            filename=filename,
            fiscal_year_begin=fiscal_year_begin,
            client_application_display_name=client_application_display_name,
            client_application_vendor=client_application_vendor,
            client_application_version=client_application_version,
            data_category_id=data_category_id,
            date_from=date_from,
            date_to=date_to,
            label=label,
            number_of_accounting_records=number_of_accounting_records,
            reference_id=reference_id,
            result=result,
            timestamp=timestamp,
            validation_details=validation_details,
        )


        job.additional_properties = d
        return job

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
