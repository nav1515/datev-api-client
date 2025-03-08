from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.employee_address import EmployeeAddress





T = TypeVar("T", bound="PersonalData")



@_attrs_define
class PersonalData:
    """ 
        Attributes:
            social_security_number (Union[Unset, str]): Employee's social security number Example: 12190367M006.
            personnel_number (Union[Unset, int]): Employee's personnel number in the payroll system Example: 10.
            first_name (Union[Unset, str]): Employee's first name Example: Maximilian.
            surname (Union[Unset, str]): Employee's surname Example: Muster.
            sex (Union[Unset, str]): Employee's gender Example: 0.
            nationality (Union[Unset, str]): Employee's nationality Example: A.
            date_of_birth (Union[Unset, str]): Employee's date of birth Example: 15.02.1980.
            academic_title (Union[Unset, str]): Employee's academic title Example: Prof., Dr. med., Dipl.-Ing. (FH).
            name_prefix (Union[Unset, str]): Employee's name prefix Example: auf dem, am.
            title_of_nobility (Union[Unset, str]): Employee's title of nobility Example: Fürst, Baron.
            company_personnel_number (Union[Unset, str]): Company personnel number (Betriebliche Personalnummer) Example:
                10.
            address (Union[Unset, EmployeeAddress]):
     """

    social_security_number: Union[Unset, str] = UNSET
    personnel_number: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    sex: Union[Unset, str] = UNSET
    nationality: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, str] = UNSET
    academic_title: Union[Unset, str] = UNSET
    name_prefix: Union[Unset, str] = UNSET
    title_of_nobility: Union[Unset, str] = UNSET
    company_personnel_number: Union[Unset, str] = UNSET
    address: Union[Unset, 'EmployeeAddress'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.employee_address import EmployeeAddress
        social_security_number = self.social_security_number

        personnel_number = self.personnel_number

        first_name = self.first_name

        surname = self.surname

        sex = self.sex

        nationality = self.nationality

        date_of_birth = self.date_of_birth

        academic_title = self.academic_title

        name_prefix = self.name_prefix

        title_of_nobility = self.title_of_nobility

        company_personnel_number = self.company_personnel_number

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if social_security_number is not UNSET:
            field_dict["social_security_number"] = social_security_number
        if personnel_number is not UNSET:
            field_dict["personnel_number"] = personnel_number
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if surname is not UNSET:
            field_dict["surname"] = surname
        if sex is not UNSET:
            field_dict["sex"] = sex
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if academic_title is not UNSET:
            field_dict["academic_title"] = academic_title
        if name_prefix is not UNSET:
            field_dict["name_prefix"] = name_prefix
        if title_of_nobility is not UNSET:
            field_dict["title_of_nobility"] = title_of_nobility
        if company_personnel_number is not UNSET:
            field_dict["company_personnel_number"] = company_personnel_number
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.employee_address import EmployeeAddress
        d = src_dict.copy()
        social_security_number = d.pop("social_security_number", UNSET)

        personnel_number = d.pop("personnel_number", UNSET)

        first_name = d.pop("first_name", UNSET)

        surname = d.pop("surname", UNSET)

        sex = d.pop("sex", UNSET)

        nationality = d.pop("nationality", UNSET)

        date_of_birth = d.pop("date_of_birth", UNSET)

        academic_title = d.pop("academic_title", UNSET)

        name_prefix = d.pop("name_prefix", UNSET)

        title_of_nobility = d.pop("title_of_nobility", UNSET)

        company_personnel_number = d.pop("company_personnel_number", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, EmployeeAddress]
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = EmployeeAddress.from_dict(_address)




        personal_data = cls(
            social_security_number=social_security_number,
            personnel_number=personnel_number,
            first_name=first_name,
            surname=surname,
            sex=sex,
            nationality=nationality,
            date_of_birth=date_of_birth,
            academic_title=academic_title,
            name_prefix=name_prefix,
            title_of_nobility=title_of_nobility,
            company_personnel_number=company_personnel_number,
            address=address,
        )


        personal_data.additional_properties = d
        return personal_data

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
