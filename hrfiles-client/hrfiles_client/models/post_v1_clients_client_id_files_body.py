from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json

from ..types import UNSET, Unset

from ..models.post_v1_clients_client_id_files_body_import_file_type import PostV1ClientsClientIdFilesBodyImportFileType
from ..models.post_v1_clients_client_id_files_body_target_system import PostV1ClientsClientIdFilesBodyTargetSystem
from ..types import File, FileJsonType
from ..types import UNSET, Unset
from io import BytesIO
from typing import Union






T = TypeVar("T", bound="PostV1ClientsClientIdFilesBody")



@_attrs_define
class PostV1ClientsClientIdFilesBody:
    r""" 
        Attributes:
            file (File): File (max. size 3 MB) which will be imported into the
                payroll system. Filename of the file can only have a maximum size
                of 50 characters. File has to be UTF-8 encoded.
                CAUTION: the file name may not contain the following characters:
                < (less than), > (greater than),: (colon), “ (double quote), / (forward slash), \ (backslash), | (vertical bar
                or pipe), ? (question mark), * (asterisk)
            file_provider (str): Name of system uploading the file (max. size 50).
                 Example: Company XY.
            import_file_type (PostV1ClientsClientIdFilesBodyImportFileType): Identifies type of import file. Import file can
                be of type current (Bewegungsdaten as bwd) or master data (Stammdaten as psd).
            creation_time (str): States the time when file was created in the file provider's system.
                Example according to ISO8601.
                 Example: 2019-09-14T10:40:52.000+02:00.
            target_system (PostV1ClientsClientIdFilesBodyTargetSystem): Target payroll system (lodas or lug) into which the
                file will be imported.
                Example: "lodas"
            payroll_accounting_month (str): Payroll accounting month.
                Example according to ISO8601
                 Example: 2019-09-30.
            mail_address (Union[Unset, str]): With this e-mail-address (max. length 100) the user of the payroll system will
                be informed whenever a new file has been sent and is available to be imported.
                 Example: example@datev.de.
     """

    file: File
    file_provider: str
    import_file_type: PostV1ClientsClientIdFilesBodyImportFileType
    creation_time: str
    target_system: PostV1ClientsClientIdFilesBodyTargetSystem
    payroll_accounting_month: str
    mail_address: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()


        file_provider = self.file_provider

        import_file_type = self.import_file_type.value

        creation_time = self.creation_time

        target_system = self.target_system.value

        payroll_accounting_month = self.payroll_accounting_month

        mail_address = self.mail_address


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file": file,
            "file_provider": file_provider,
            "import_file_type": import_file_type,
            "creation_time": creation_time,
            "target_system": target_system,
            "payroll_accounting_month": payroll_accounting_month,
        })
        if mail_address is not UNSET:
            field_dict["mail_address"] = mail_address

        return field_dict


    def to_multipart(self) -> dict[str, Any]:
        file = self.file.to_tuple()


        file_provider =  (None, str(self.file_provider).encode(), "text/plain")


        import_file_type = (None, str(self.import_file_type.value).encode(), "text/plain")

        creation_time =  (None, str(self.creation_time).encode(), "text/plain")


        target_system = (None, str(self.target_system.value).encode(), "text/plain")

        payroll_accounting_month =  (None, str(self.payroll_accounting_month).encode(), "text/plain")


        mail_address = self.mail_address if isinstance(self.mail_address, Unset) else (None, str(self.mail_address).encode(), "text/plain")



        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] =  (None, str(prop).encode(), "text/plain")

        field_dict.update({
            "file": file,
            "file_provider": file_provider,
            "import_file_type": import_file_type,
            "creation_time": creation_time,
            "target_system": target_system,
            "payroll_accounting_month": payroll_accounting_month,
        })
        if mail_address is not UNSET:
            field_dict["mail_address"] = mail_address

        return field_dict


    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        file = File(
             payload = BytesIO(d.pop("file"))
        )




        file_provider = d.pop("file_provider")

        import_file_type = PostV1ClientsClientIdFilesBodyImportFileType(d.pop("import_file_type"))




        creation_time = d.pop("creation_time")

        target_system = PostV1ClientsClientIdFilesBodyTargetSystem(d.pop("target_system"))




        payroll_accounting_month = d.pop("payroll_accounting_month")

        mail_address = d.pop("mail_address", UNSET)

        post_v1_clients_client_id_files_body = cls(
            file=file,
            file_provider=file_provider,
            import_file_type=import_file_type,
            creation_time=creation_time,
            target_system=target_system,
            payroll_accounting_month=payroll_accounting_month,
            mail_address=mail_address,
        )


        post_v1_clients_client_id_files_body.additional_properties = d
        return post_v1_clients_client_id_files_body

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
