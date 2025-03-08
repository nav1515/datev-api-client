from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.employment import Employment
  from ..models.personal_data import PersonalData
  from ..models.social_security import SocialSecurity
  from ..models.taxes import Taxes





T = TypeVar("T", bound="MasterData")



@_attrs_define
class MasterData:
    """ 
        Attributes:
            social_security (Union[Unset, SocialSecurity]):
            employment (Union[Unset, Employment]):
            taxes (Union[Unset, Taxes]):
            personnel_number (Union[Unset, int]): Employee's personnel number in the payroll system Example: 10.
            company_personnel_number (Union[Unset, str]): Company personnel number (Betriebliche Personalnummer) Example:
                10.
            accounting_month (Union[Unset, str]): Accounting month (Abrechnungsmonat) Example: 2020-01.
            month_of_recalculation (Union[Unset, str]): Month of recalculation (Nachberechnungsmonat) Example: 2020-01.
            personal_data (Union[Unset, PersonalData]):
     """

    social_security: Union[Unset, 'SocialSecurity'] = UNSET
    employment: Union[Unset, 'Employment'] = UNSET
    taxes: Union[Unset, 'Taxes'] = UNSET
    personnel_number: Union[Unset, int] = UNSET
    company_personnel_number: Union[Unset, str] = UNSET
    accounting_month: Union[Unset, str] = UNSET
    month_of_recalculation: Union[Unset, str] = UNSET
    personal_data: Union[Unset, 'PersonalData'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.employment import Employment
        from ..models.personal_data import PersonalData
        from ..models.social_security import SocialSecurity
        from ..models.taxes import Taxes
        social_security: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.social_security, Unset):
            social_security = self.social_security.to_dict()

        employment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.employment, Unset):
            employment = self.employment.to_dict()

        taxes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = self.taxes.to_dict()

        personnel_number = self.personnel_number

        company_personnel_number = self.company_personnel_number

        accounting_month = self.accounting_month

        month_of_recalculation = self.month_of_recalculation

        personal_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.personal_data, Unset):
            personal_data = self.personal_data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if social_security is not UNSET:
            field_dict["social_security"] = social_security
        if employment is not UNSET:
            field_dict["employment"] = employment
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if personnel_number is not UNSET:
            field_dict["personnel_number"] = personnel_number
        if company_personnel_number is not UNSET:
            field_dict["company_personnel_number"] = company_personnel_number
        if accounting_month is not UNSET:
            field_dict["accounting_month"] = accounting_month
        if month_of_recalculation is not UNSET:
            field_dict["month_of_recalculation"] = month_of_recalculation
        if personal_data is not UNSET:
            field_dict["personal_data"] = personal_data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.employment import Employment
        from ..models.personal_data import PersonalData
        from ..models.social_security import SocialSecurity
        from ..models.taxes import Taxes
        d = src_dict.copy()
        _social_security = d.pop("social_security", UNSET)
        social_security: Union[Unset, SocialSecurity]
        if isinstance(_social_security,  Unset):
            social_security = UNSET
        else:
            social_security = SocialSecurity.from_dict(_social_security)




        _employment = d.pop("employment", UNSET)
        employment: Union[Unset, Employment]
        if isinstance(_employment,  Unset):
            employment = UNSET
        else:
            employment = Employment.from_dict(_employment)




        _taxes = d.pop("taxes", UNSET)
        taxes: Union[Unset, Taxes]
        if isinstance(_taxes,  Unset):
            taxes = UNSET
        else:
            taxes = Taxes.from_dict(_taxes)




        personnel_number = d.pop("personnel_number", UNSET)

        company_personnel_number = d.pop("company_personnel_number", UNSET)

        accounting_month = d.pop("accounting_month", UNSET)

        month_of_recalculation = d.pop("month_of_recalculation", UNSET)

        _personal_data = d.pop("personal_data", UNSET)
        personal_data: Union[Unset, PersonalData]
        if isinstance(_personal_data,  Unset):
            personal_data = UNSET
        else:
            personal_data = PersonalData.from_dict(_personal_data)




        master_data = cls(
            social_security=social_security,
            employment=employment,
            taxes=taxes,
            personnel_number=personnel_number,
            company_personnel_number=company_personnel_number,
            accounting_month=accounting_month,
            month_of_recalculation=month_of_recalculation,
            personal_data=personal_data,
        )


        master_data.additional_properties = d
        return master_data

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
