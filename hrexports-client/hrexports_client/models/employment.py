from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.cost_center import CostCenter





T = TypeVar("T", bound="Employment")



@_attrs_define
class Employment:
    """ 
        Attributes:
            date_of_joining (Union[Unset, str]): Date of commencement of employment Example: 1999-01-07.
            date_of_leaving (Union[Unset, str]): Date of termination of employment Example: 2022-01-07.
            initial_date_of_joining (Union[Unset, str]): Date of commencement of the Employee's initial employment Example:
                1999-01-07.
            job_title (Union[Unset, str]): Job title Example: Angestellter.
            job_title_of_occupational_classification_code (Union[Unset, str]): Job title of occupational classification code
                (Tätigkeitsschlüssel - Tätigkeitsbezeichnung) Example: Geschäftsführer/in.
            occupational_classification_code (Union[Unset, str]): Occupational classification code (Tätigkeitsschlüssel)
                Example: 71104.
            occupational_classification_code_employee_leasing (Union[Unset, str]): Occupational classification code for
                employee leasing (Tätigkeitsschlüssel - Arbeitnehmerüberlassung) Example: 0.
            sequential_number_of_occupational_classification_code (Union[Unset, str]): Sequential number of occupational
                classification code (Tätigkeitsschlüssel - fortlaufende Nummer) Example: 17098.
            type_of_contract (Union[Unset, str]): Type of employment contract Example: 1.
            weekly_working_hours (Union[Unset, float]): Contractual weekly working hours Example: 40.
            cost_center (Union[Unset, CostCenter]):
            highest_level_of_education (Union[Unset, str]): 6th position of the occupational_classification_code Example: 1.
            highest_level_of_professional_training (Union[Unset, str]): 7th position of the occupational_classification_code
                Example: 1.
     """

    date_of_joining: Union[Unset, str] = UNSET
    date_of_leaving: Union[Unset, str] = UNSET
    initial_date_of_joining: Union[Unset, str] = UNSET
    job_title: Union[Unset, str] = UNSET
    job_title_of_occupational_classification_code: Union[Unset, str] = UNSET
    occupational_classification_code: Union[Unset, str] = UNSET
    occupational_classification_code_employee_leasing: Union[Unset, str] = UNSET
    sequential_number_of_occupational_classification_code: Union[Unset, str] = UNSET
    type_of_contract: Union[Unset, str] = UNSET
    weekly_working_hours: Union[Unset, float] = UNSET
    cost_center: Union[Unset, 'CostCenter'] = UNSET
    highest_level_of_education: Union[Unset, str] = UNSET
    highest_level_of_professional_training: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.cost_center import CostCenter
        date_of_joining = self.date_of_joining

        date_of_leaving = self.date_of_leaving

        initial_date_of_joining = self.initial_date_of_joining

        job_title = self.job_title

        job_title_of_occupational_classification_code = self.job_title_of_occupational_classification_code

        occupational_classification_code = self.occupational_classification_code

        occupational_classification_code_employee_leasing = self.occupational_classification_code_employee_leasing

        sequential_number_of_occupational_classification_code = self.sequential_number_of_occupational_classification_code

        type_of_contract = self.type_of_contract

        weekly_working_hours = self.weekly_working_hours

        cost_center: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cost_center, Unset):
            cost_center = self.cost_center.to_dict()

        highest_level_of_education = self.highest_level_of_education

        highest_level_of_professional_training = self.highest_level_of_professional_training


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date_of_joining is not UNSET:
            field_dict["date_of_joining"] = date_of_joining
        if date_of_leaving is not UNSET:
            field_dict["date_of_leaving"] = date_of_leaving
        if initial_date_of_joining is not UNSET:
            field_dict["initial_date_of_joining"] = initial_date_of_joining
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if job_title_of_occupational_classification_code is not UNSET:
            field_dict["job_title_of_occupational_classification_code"] = job_title_of_occupational_classification_code
        if occupational_classification_code is not UNSET:
            field_dict["occupational_classification_code"] = occupational_classification_code
        if occupational_classification_code_employee_leasing is not UNSET:
            field_dict["occupational_classification_code_employee_leasing"] = occupational_classification_code_employee_leasing
        if sequential_number_of_occupational_classification_code is not UNSET:
            field_dict["sequential_number_of_occupational_classification_code"] = sequential_number_of_occupational_classification_code
        if type_of_contract is not UNSET:
            field_dict["type_of_contract"] = type_of_contract
        if weekly_working_hours is not UNSET:
            field_dict["weekly_working_hours"] = weekly_working_hours
        if cost_center is not UNSET:
            field_dict["cost_center"] = cost_center
        if highest_level_of_education is not UNSET:
            field_dict["highest_level_of_education"] = highest_level_of_education
        if highest_level_of_professional_training is not UNSET:
            field_dict["highest_level_of_professional_training"] = highest_level_of_professional_training

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cost_center import CostCenter
        d = src_dict.copy()
        date_of_joining = d.pop("date_of_joining", UNSET)

        date_of_leaving = d.pop("date_of_leaving", UNSET)

        initial_date_of_joining = d.pop("initial_date_of_joining", UNSET)

        job_title = d.pop("job_title", UNSET)

        job_title_of_occupational_classification_code = d.pop("job_title_of_occupational_classification_code", UNSET)

        occupational_classification_code = d.pop("occupational_classification_code", UNSET)

        occupational_classification_code_employee_leasing = d.pop("occupational_classification_code_employee_leasing", UNSET)

        sequential_number_of_occupational_classification_code = d.pop("sequential_number_of_occupational_classification_code", UNSET)

        type_of_contract = d.pop("type_of_contract", UNSET)

        weekly_working_hours = d.pop("weekly_working_hours", UNSET)

        _cost_center = d.pop("cost_center", UNSET)
        cost_center: Union[Unset, CostCenter]
        if isinstance(_cost_center,  Unset):
            cost_center = UNSET
        else:
            cost_center = CostCenter.from_dict(_cost_center)




        highest_level_of_education = d.pop("highest_level_of_education", UNSET)

        highest_level_of_professional_training = d.pop("highest_level_of_professional_training", UNSET)

        employment = cls(
            date_of_joining=date_of_joining,
            date_of_leaving=date_of_leaving,
            initial_date_of_joining=initial_date_of_joining,
            job_title=job_title,
            job_title_of_occupational_classification_code=job_title_of_occupational_classification_code,
            occupational_classification_code=occupational_classification_code,
            occupational_classification_code_employee_leasing=occupational_classification_code_employee_leasing,
            sequential_number_of_occupational_classification_code=sequential_number_of_occupational_classification_code,
            type_of_contract=type_of_contract,
            weekly_working_hours=weekly_working_hours,
            cost_center=cost_center,
            highest_level_of_education=highest_level_of_education,
            highest_level_of_professional_training=highest_level_of_professional_training,
        )


        employment.additional_properties = d
        return employment

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
