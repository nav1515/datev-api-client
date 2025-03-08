from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dx_so_job_creation_info_import_type import DXSoJobCreationInfoImportType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime






T = TypeVar("T", bound="DXSoJobCreationInfo")



@_attrs_define
class DXSoJobCreationInfo:
    """ 
        Attributes:
            import_type (Union[Unset, DXSoJobCreationInfoImportType]): Type of transferred data: accountsPayableLedgerImport
                for incoming invoices, accountsReceivableLedgerImport for outgoing invoices, cashLedgerImport for cash entries.
                This parameter shall be used. It is mandatory when the parameter 'accounting_month' is used.
            accounting_month (Union[Unset, datetime.date]): Accounting month (data format: YYYY-MM) of the transferred data.
                This parameter shall be used. It is mandatory when the parameter 'import_type' is used.
     """

    import_type: Union[Unset, DXSoJobCreationInfoImportType] = UNSET
    accounting_month: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        import_type: Union[Unset, str] = UNSET
        if not isinstance(self.import_type, Unset):
            import_type = self.import_type.value


        accounting_month: Union[Unset, str] = UNSET
        if not isinstance(self.accounting_month, Unset):
            accounting_month = self.accounting_month.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if import_type is not UNSET:
            field_dict["import_type"] = import_type
        if accounting_month is not UNSET:
            field_dict["accounting_month"] = accounting_month

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _import_type = d.pop("import_type", UNSET)
        import_type: Union[Unset, DXSoJobCreationInfoImportType]
        if isinstance(_import_type,  Unset):
            import_type = UNSET
        else:
            import_type = DXSoJobCreationInfoImportType(_import_type)




        _accounting_month = d.pop("accounting_month", UNSET)
        accounting_month: Union[Unset, datetime.date]
        if isinstance(_accounting_month,  Unset):
            accounting_month = UNSET
        else:
            accounting_month = isoparse(_accounting_month).date()




        dx_so_job_creation_info = cls(
            import_type=import_type,
            accounting_month=accounting_month,
        )


        dx_so_job_creation_info.additional_properties = d
        return dx_so_job_creation_info

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
