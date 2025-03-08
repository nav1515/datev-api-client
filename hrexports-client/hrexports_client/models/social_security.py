from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="SocialSecurity")



@_attrs_define
class SocialSecurity:
    """ 
        Attributes:
            contribution_class_health_insurance (Union[Unset, str]): Contribution class to health insurance Example: 0.
            contribution_class_pension_insurance (Union[Unset, str]): Contribution class to pension insurance Example: 0.
            contribution_class_unemployment_insurance (Union[Unset, str]): Contribution class to unemployment insurance
                Example: 0.
            contribution_class_long_term_care_insurance (Union[Unset, str]): Contribution class to long term care insurance
                Example: 0.
            person_group_key (Union[Unset, str]): Person group key (Personengruppenschlüssel) Example: 101.
            is_ignore_additional_contribution_to_long_term_care_insurance_for_childless (Union[Unset, str]): Contribution to
                long term care insurance if childless Example: 1.
            health_insurance_company_number (Union[Unset, str]): Company number of health insurer Example: 12345678.
     """

    contribution_class_health_insurance: Union[Unset, str] = UNSET
    contribution_class_pension_insurance: Union[Unset, str] = UNSET
    contribution_class_unemployment_insurance: Union[Unset, str] = UNSET
    contribution_class_long_term_care_insurance: Union[Unset, str] = UNSET
    person_group_key: Union[Unset, str] = UNSET
    is_ignore_additional_contribution_to_long_term_care_insurance_for_childless: Union[Unset, str] = UNSET
    health_insurance_company_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        contribution_class_health_insurance = self.contribution_class_health_insurance

        contribution_class_pension_insurance = self.contribution_class_pension_insurance

        contribution_class_unemployment_insurance = self.contribution_class_unemployment_insurance

        contribution_class_long_term_care_insurance = self.contribution_class_long_term_care_insurance

        person_group_key = self.person_group_key

        is_ignore_additional_contribution_to_long_term_care_insurance_for_childless = self.is_ignore_additional_contribution_to_long_term_care_insurance_for_childless

        health_insurance_company_number = self.health_insurance_company_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if contribution_class_health_insurance is not UNSET:
            field_dict["contribution_class_health_insurance"] = contribution_class_health_insurance
        if contribution_class_pension_insurance is not UNSET:
            field_dict["contribution_class_pension_insurance"] = contribution_class_pension_insurance
        if contribution_class_unemployment_insurance is not UNSET:
            field_dict["contribution_class_unemployment_insurance"] = contribution_class_unemployment_insurance
        if contribution_class_long_term_care_insurance is not UNSET:
            field_dict["contribution_class_long_term_care_insurance"] = contribution_class_long_term_care_insurance
        if person_group_key is not UNSET:
            field_dict["person_group_key"] = person_group_key
        if is_ignore_additional_contribution_to_long_term_care_insurance_for_childless is not UNSET:
            field_dict["is_ignore_additional_contribution_to_long_term_care_insurance_for_childless"] = is_ignore_additional_contribution_to_long_term_care_insurance_for_childless
        if health_insurance_company_number is not UNSET:
            field_dict["health_insurance_company_number"] = health_insurance_company_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        contribution_class_health_insurance = d.pop("contribution_class_health_insurance", UNSET)

        contribution_class_pension_insurance = d.pop("contribution_class_pension_insurance", UNSET)

        contribution_class_unemployment_insurance = d.pop("contribution_class_unemployment_insurance", UNSET)

        contribution_class_long_term_care_insurance = d.pop("contribution_class_long_term_care_insurance", UNSET)

        person_group_key = d.pop("person_group_key", UNSET)

        is_ignore_additional_contribution_to_long_term_care_insurance_for_childless = d.pop("is_ignore_additional_contribution_to_long_term_care_insurance_for_childless", UNSET)

        health_insurance_company_number = d.pop("health_insurance_company_number", UNSET)

        social_security = cls(
            contribution_class_health_insurance=contribution_class_health_insurance,
            contribution_class_pension_insurance=contribution_class_pension_insurance,
            contribution_class_unemployment_insurance=contribution_class_unemployment_insurance,
            contribution_class_long_term_care_insurance=contribution_class_long_term_care_insurance,
            person_group_key=person_group_key,
            is_ignore_additional_contribution_to_long_term_care_insurance_for_childless=is_ignore_additional_contribution_to_long_term_care_insurance_for_childless,
            health_insurance_company_number=health_insurance_company_number,
        )


        social_security.additional_properties = d
        return social_security

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
