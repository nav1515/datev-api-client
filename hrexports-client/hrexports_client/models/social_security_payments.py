from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.health_insurance import HealthInsurance
  from ..models.unemployment_insurance import UnemploymentInsurance
  from ..models.long_term_care_insurance import LongTermCareInsurance
  from ..models.pension_insurance import PensionInsurance





T = TypeVar("T", bound="SocialSecurityPayments")



@_attrs_define
class SocialSecurityPayments:
    """ 
        Attributes:
            personnel_number (Union[Unset, int]): Employee's personnel number in the payroll system Example: 10.
            company_personnel_number (Union[Unset, str]): Company personnel number (Betriebliche Personalnummer) Example:
                10.
            accounting_month (Union[Unset, str]): Accounting month (Abrechnungsmonat) Example: 2020-01.
            month_of_recalculation (Union[Unset, str]): Month of recalculation (Nachberechnungsmonat) Example: 2020-01.
            health_insurance (Union[Unset, HealthInsurance]):
            unemployment_insurance (Union[Unset, UnemploymentInsurance]):
            long_term_care_insurance (Union[Unset, LongTermCareInsurance]):
            pension_insurance (Union[Unset, PensionInsurance]):
            current_payments_to_social_security_employers_contribution (Union[Unset, float]): Current payments as employer's
                contribution to social security (Arbeitgeberaufwand zur Sozialversicherung aus laufenden Bezügen (KV, PV, AV,
                RV)) Example: 886.19.
            other_payments_to_social_security_employers_contribution (Union[Unset, float]): Other payments as employer's
                contribution to social security (Arbeitgeberaufwand zur Sozialversicherung aus Einmalbezügen (KV, PV, AV, RV))
            allocation1 (Union[Unset, float]): Sickness allocation U1 (Umlage U1 - Krankheitsumlage) Example: 125.16.
            allocation2 (Union[Unset, float]): Maternity allocation U2 (Umlage U2 - Mutterschaftsumlage) Example: 19.67.
            monthly_allocation_to_insolvency_benefit (Union[Unset, float]): Monthly allocation to insolvency benefit
                (Monatliche Insolvenzgeldumlage)
            allocation_insolvency (Union[Unset, float]): Sum of monthly and annual allocation to insolvency benefit
            social_security_days (Union[Unset, float]): Number of days relevant for social security Example: 25.
            annual_allocation_to_insolvency_benefit (Union[Unset, float]): Annual allocation to insolvency benefit
                (Jährliche Insolvenzgeldumlage)
            social_security_deductions (Union[Unset, float]): Social security deductions Example: 500.
     """

    personnel_number: Union[Unset, int] = UNSET
    company_personnel_number: Union[Unset, str] = UNSET
    accounting_month: Union[Unset, str] = UNSET
    month_of_recalculation: Union[Unset, str] = UNSET
    health_insurance: Union[Unset, 'HealthInsurance'] = UNSET
    unemployment_insurance: Union[Unset, 'UnemploymentInsurance'] = UNSET
    long_term_care_insurance: Union[Unset, 'LongTermCareInsurance'] = UNSET
    pension_insurance: Union[Unset, 'PensionInsurance'] = UNSET
    current_payments_to_social_security_employers_contribution: Union[Unset, float] = UNSET
    other_payments_to_social_security_employers_contribution: Union[Unset, float] = UNSET
    allocation1: Union[Unset, float] = UNSET
    allocation2: Union[Unset, float] = UNSET
    monthly_allocation_to_insolvency_benefit: Union[Unset, float] = UNSET
    allocation_insolvency: Union[Unset, float] = UNSET
    social_security_days: Union[Unset, float] = UNSET
    annual_allocation_to_insolvency_benefit: Union[Unset, float] = UNSET
    social_security_deductions: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.health_insurance import HealthInsurance
        from ..models.unemployment_insurance import UnemploymentInsurance
        from ..models.long_term_care_insurance import LongTermCareInsurance
        from ..models.pension_insurance import PensionInsurance
        personnel_number = self.personnel_number

        company_personnel_number = self.company_personnel_number

        accounting_month = self.accounting_month

        month_of_recalculation = self.month_of_recalculation

        health_insurance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.health_insurance, Unset):
            health_insurance = self.health_insurance.to_dict()

        unemployment_insurance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.unemployment_insurance, Unset):
            unemployment_insurance = self.unemployment_insurance.to_dict()

        long_term_care_insurance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.long_term_care_insurance, Unset):
            long_term_care_insurance = self.long_term_care_insurance.to_dict()

        pension_insurance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pension_insurance, Unset):
            pension_insurance = self.pension_insurance.to_dict()

        current_payments_to_social_security_employers_contribution = self.current_payments_to_social_security_employers_contribution

        other_payments_to_social_security_employers_contribution = self.other_payments_to_social_security_employers_contribution

        allocation1 = self.allocation1

        allocation2 = self.allocation2

        monthly_allocation_to_insolvency_benefit = self.monthly_allocation_to_insolvency_benefit

        allocation_insolvency = self.allocation_insolvency

        social_security_days = self.social_security_days

        annual_allocation_to_insolvency_benefit = self.annual_allocation_to_insolvency_benefit

        social_security_deductions = self.social_security_deductions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if personnel_number is not UNSET:
            field_dict["personnel_number"] = personnel_number
        if company_personnel_number is not UNSET:
            field_dict["company_personnel_number"] = company_personnel_number
        if accounting_month is not UNSET:
            field_dict["accounting_month"] = accounting_month
        if month_of_recalculation is not UNSET:
            field_dict["month_of_recalculation"] = month_of_recalculation
        if health_insurance is not UNSET:
            field_dict["health_insurance"] = health_insurance
        if unemployment_insurance is not UNSET:
            field_dict["unemployment_insurance"] = unemployment_insurance
        if long_term_care_insurance is not UNSET:
            field_dict["long_term_care_insurance"] = long_term_care_insurance
        if pension_insurance is not UNSET:
            field_dict["pension_insurance"] = pension_insurance
        if current_payments_to_social_security_employers_contribution is not UNSET:
            field_dict["current_payments_to_social_security_employers_contribution"] = current_payments_to_social_security_employers_contribution
        if other_payments_to_social_security_employers_contribution is not UNSET:
            field_dict["other_payments_to_social_security_employers_contribution"] = other_payments_to_social_security_employers_contribution
        if allocation1 is not UNSET:
            field_dict["allocation1"] = allocation1
        if allocation2 is not UNSET:
            field_dict["allocation2"] = allocation2
        if monthly_allocation_to_insolvency_benefit is not UNSET:
            field_dict["monthly_allocation_to_insolvency_benefit"] = monthly_allocation_to_insolvency_benefit
        if allocation_insolvency is not UNSET:
            field_dict["allocation_insolvency"] = allocation_insolvency
        if social_security_days is not UNSET:
            field_dict["social_security_days"] = social_security_days
        if annual_allocation_to_insolvency_benefit is not UNSET:
            field_dict["annual_allocation_to_insolvency_benefit"] = annual_allocation_to_insolvency_benefit
        if social_security_deductions is not UNSET:
            field_dict["social_security_deductions"] = social_security_deductions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.health_insurance import HealthInsurance
        from ..models.unemployment_insurance import UnemploymentInsurance
        from ..models.long_term_care_insurance import LongTermCareInsurance
        from ..models.pension_insurance import PensionInsurance
        d = src_dict.copy()
        personnel_number = d.pop("personnel_number", UNSET)

        company_personnel_number = d.pop("company_personnel_number", UNSET)

        accounting_month = d.pop("accounting_month", UNSET)

        month_of_recalculation = d.pop("month_of_recalculation", UNSET)

        _health_insurance = d.pop("health_insurance", UNSET)
        health_insurance: Union[Unset, HealthInsurance]
        if isinstance(_health_insurance,  Unset):
            health_insurance = UNSET
        else:
            health_insurance = HealthInsurance.from_dict(_health_insurance)




        _unemployment_insurance = d.pop("unemployment_insurance", UNSET)
        unemployment_insurance: Union[Unset, UnemploymentInsurance]
        if isinstance(_unemployment_insurance,  Unset):
            unemployment_insurance = UNSET
        else:
            unemployment_insurance = UnemploymentInsurance.from_dict(_unemployment_insurance)




        _long_term_care_insurance = d.pop("long_term_care_insurance", UNSET)
        long_term_care_insurance: Union[Unset, LongTermCareInsurance]
        if isinstance(_long_term_care_insurance,  Unset):
            long_term_care_insurance = UNSET
        else:
            long_term_care_insurance = LongTermCareInsurance.from_dict(_long_term_care_insurance)




        _pension_insurance = d.pop("pension_insurance", UNSET)
        pension_insurance: Union[Unset, PensionInsurance]
        if isinstance(_pension_insurance,  Unset):
            pension_insurance = UNSET
        else:
            pension_insurance = PensionInsurance.from_dict(_pension_insurance)




        current_payments_to_social_security_employers_contribution = d.pop("current_payments_to_social_security_employers_contribution", UNSET)

        other_payments_to_social_security_employers_contribution = d.pop("other_payments_to_social_security_employers_contribution", UNSET)

        allocation1 = d.pop("allocation1", UNSET)

        allocation2 = d.pop("allocation2", UNSET)

        monthly_allocation_to_insolvency_benefit = d.pop("monthly_allocation_to_insolvency_benefit", UNSET)

        allocation_insolvency = d.pop("allocation_insolvency", UNSET)

        social_security_days = d.pop("social_security_days", UNSET)

        annual_allocation_to_insolvency_benefit = d.pop("annual_allocation_to_insolvency_benefit", UNSET)

        social_security_deductions = d.pop("social_security_deductions", UNSET)

        social_security_payments = cls(
            personnel_number=personnel_number,
            company_personnel_number=company_personnel_number,
            accounting_month=accounting_month,
            month_of_recalculation=month_of_recalculation,
            health_insurance=health_insurance,
            unemployment_insurance=unemployment_insurance,
            long_term_care_insurance=long_term_care_insurance,
            pension_insurance=pension_insurance,
            current_payments_to_social_security_employers_contribution=current_payments_to_social_security_employers_contribution,
            other_payments_to_social_security_employers_contribution=other_payments_to_social_security_employers_contribution,
            allocation1=allocation1,
            allocation2=allocation2,
            monthly_allocation_to_insolvency_benefit=monthly_allocation_to_insolvency_benefit,
            allocation_insolvency=allocation_insolvency,
            social_security_days=social_security_days,
            annual_allocation_to_insolvency_benefit=annual_allocation_to_insolvency_benefit,
            social_security_deductions=social_security_deductions,
        )


        social_security_payments.additional_properties = d
        return social_security_payments

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
