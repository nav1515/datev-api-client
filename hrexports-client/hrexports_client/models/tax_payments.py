from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="TaxPayments")



@_attrs_define
class TaxPayments:
    """ 
        Attributes:
            personnel_number (Union[Unset, int]): Employee's personnel number in the payroll system Example: 10.
            company_personnel_number (Union[Unset, str]): Company personnel number (Betriebliche Personalnummer) Example:
                10.
            accounting_month (Union[Unset, str]): Accounting month (Abrechnungsmonat) Example: 2020-01.
            month_of_recalculation (Union[Unset, str]): Month of recalculation (Nachberechnungsmonat) Example: 2020-01.
            current_gross_tax (Union[Unset, float]): Current gross tax (Steuer-Brutto) Example: 2000.
            flat_rate_church_tax (Union[Unset, float]): Flat rate church tax (Pauschale Kirchensteuer) Example: 50.1.
            flat_rate_solidarity_tax (Union[Unset, float]): Flat rate solidarity tax (Pauschale Solidaritätszuschlag)
                Example: 80.
            flat_rate_wage_tax (Union[Unset, float]): Flat rate wage tax (Pauschale Lohnsteuer) Example: 120.12.
            flat_rate_taxed_payments (Union[Unset, float]): Sum of other_payments_taxed_at_flat_rate,
                payment_taxed_at_a_flat_rate_when_low_paid_employed and payment_taxed_at_a_flat_rate_when_short_term_employed
                (Pauschal versteuerte Bezüge) Example: 125.16.
            solidarity_tax (Union[Unset, float]): Solidarity Tax (Solidaritätszuschlag) Example: 20.
            wage_tax (Union[Unset, float]): Wage tax (Lohnsteuer) Example: 130.
            other_payments_taxed_at_flat_rate (Union[Unset, float]): Other payments taxed at flat rate (Sonstige pauschal
                besteuerte Bezüge) Example: 123.45.
            payment_taxed_at_a_flat_rate_when_low_paid_employed (Union[Unset, float]): Payment taxed at a flat rate when low
                paid employed (Pauschal versteuerte Bezüge geringfügig beschäftigt) Example: 123.45.
            payment_taxed_at_a_flat_rate_when_short_term_employed (Union[Unset, float]): Payment taxed at a flat rate when
                short term employed (Pauschal versteuerte Bezüge kurzfristig beschäftigt) Example: 123.45.
            wage_tax_non_recurring_payment (Union[Unset, float]): Wage tax non recurring payment (Lohnsteuer Einmalbezug)
                Example: 180.
            wage_tax_monthly (Union[Unset, float]): Wage tax monthly (Lohnsteuer laufend) Example: 200.
            church_tax_non_recurring_payment (Union[Unset, float]): Church tax non recurring payment (Kirchensteuer
                Einmalbezug) Example: 80.
            church_tax (Union[Unset, float]): Church tax (Kirchensteuer) Example: 45.
            church_tax_monthly (Union[Unset, float]): Church tax monthly (Kirchensteuer laufend) Example: 50.
            tax_relevant_days (Union[Unset, float]): Number of days relevant for tax Example: 28.
            gross_tax_non_recurring_payment (Union[Unset, float]): Gross tax non recurring payments (Steuerbrutto
                Einmalbezug) Example: 1000.5.
            tax_deductions (Union[Unset, float]): Tax deductions Example: 750.88.
            solidarity_tax_monthly (Union[Unset, float]): Solidarity tax monthly (Solidatitätszuschlag laufend) Example:
                125.83.
            solidarity_tax_non_recurring_payment (Union[Unset, float]): Solidarity tax non recurring payments
                (Solidatitätszuschlag Einmalbezug) Example: 65.83.
     """

    personnel_number: Union[Unset, int] = UNSET
    company_personnel_number: Union[Unset, str] = UNSET
    accounting_month: Union[Unset, str] = UNSET
    month_of_recalculation: Union[Unset, str] = UNSET
    current_gross_tax: Union[Unset, float] = UNSET
    flat_rate_church_tax: Union[Unset, float] = UNSET
    flat_rate_solidarity_tax: Union[Unset, float] = UNSET
    flat_rate_wage_tax: Union[Unset, float] = UNSET
    flat_rate_taxed_payments: Union[Unset, float] = UNSET
    solidarity_tax: Union[Unset, float] = UNSET
    wage_tax: Union[Unset, float] = UNSET
    other_payments_taxed_at_flat_rate: Union[Unset, float] = UNSET
    payment_taxed_at_a_flat_rate_when_low_paid_employed: Union[Unset, float] = UNSET
    payment_taxed_at_a_flat_rate_when_short_term_employed: Union[Unset, float] = UNSET
    wage_tax_non_recurring_payment: Union[Unset, float] = UNSET
    wage_tax_monthly: Union[Unset, float] = UNSET
    church_tax_non_recurring_payment: Union[Unset, float] = UNSET
    church_tax: Union[Unset, float] = UNSET
    church_tax_monthly: Union[Unset, float] = UNSET
    tax_relevant_days: Union[Unset, float] = UNSET
    gross_tax_non_recurring_payment: Union[Unset, float] = UNSET
    tax_deductions: Union[Unset, float] = UNSET
    solidarity_tax_monthly: Union[Unset, float] = UNSET
    solidarity_tax_non_recurring_payment: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        personnel_number = self.personnel_number

        company_personnel_number = self.company_personnel_number

        accounting_month = self.accounting_month

        month_of_recalculation = self.month_of_recalculation

        current_gross_tax = self.current_gross_tax

        flat_rate_church_tax = self.flat_rate_church_tax

        flat_rate_solidarity_tax = self.flat_rate_solidarity_tax

        flat_rate_wage_tax = self.flat_rate_wage_tax

        flat_rate_taxed_payments = self.flat_rate_taxed_payments

        solidarity_tax = self.solidarity_tax

        wage_tax = self.wage_tax

        other_payments_taxed_at_flat_rate = self.other_payments_taxed_at_flat_rate

        payment_taxed_at_a_flat_rate_when_low_paid_employed = self.payment_taxed_at_a_flat_rate_when_low_paid_employed

        payment_taxed_at_a_flat_rate_when_short_term_employed = self.payment_taxed_at_a_flat_rate_when_short_term_employed

        wage_tax_non_recurring_payment = self.wage_tax_non_recurring_payment

        wage_tax_monthly = self.wage_tax_monthly

        church_tax_non_recurring_payment = self.church_tax_non_recurring_payment

        church_tax = self.church_tax

        church_tax_monthly = self.church_tax_monthly

        tax_relevant_days = self.tax_relevant_days

        gross_tax_non_recurring_payment = self.gross_tax_non_recurring_payment

        tax_deductions = self.tax_deductions

        solidarity_tax_monthly = self.solidarity_tax_monthly

        solidarity_tax_non_recurring_payment = self.solidarity_tax_non_recurring_payment


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
        if current_gross_tax is not UNSET:
            field_dict["current_gross_tax"] = current_gross_tax
        if flat_rate_church_tax is not UNSET:
            field_dict["flat_rate_church_tax"] = flat_rate_church_tax
        if flat_rate_solidarity_tax is not UNSET:
            field_dict["flat_rate_solidarity_tax"] = flat_rate_solidarity_tax
        if flat_rate_wage_tax is not UNSET:
            field_dict["flat_rate_wage_tax"] = flat_rate_wage_tax
        if flat_rate_taxed_payments is not UNSET:
            field_dict["flat_rate_taxed_payments"] = flat_rate_taxed_payments
        if solidarity_tax is not UNSET:
            field_dict["solidarity_tax"] = solidarity_tax
        if wage_tax is not UNSET:
            field_dict["wage_tax"] = wage_tax
        if other_payments_taxed_at_flat_rate is not UNSET:
            field_dict["other_payments_taxed_at_flat_rate"] = other_payments_taxed_at_flat_rate
        if payment_taxed_at_a_flat_rate_when_low_paid_employed is not UNSET:
            field_dict["payment_taxed_at_a_flat_rate_when_low_paid_employed"] = payment_taxed_at_a_flat_rate_when_low_paid_employed
        if payment_taxed_at_a_flat_rate_when_short_term_employed is not UNSET:
            field_dict["payment_taxed_at_a_flat_rate_when_short_term_employed"] = payment_taxed_at_a_flat_rate_when_short_term_employed
        if wage_tax_non_recurring_payment is not UNSET:
            field_dict["wage_tax_non_recurring_payment"] = wage_tax_non_recurring_payment
        if wage_tax_monthly is not UNSET:
            field_dict["wage_tax_monthly"] = wage_tax_monthly
        if church_tax_non_recurring_payment is not UNSET:
            field_dict["church_tax_non_recurring_payment"] = church_tax_non_recurring_payment
        if church_tax is not UNSET:
            field_dict["church_tax"] = church_tax
        if church_tax_monthly is not UNSET:
            field_dict["church_tax_monthly"] = church_tax_monthly
        if tax_relevant_days is not UNSET:
            field_dict["tax_relevant_days"] = tax_relevant_days
        if gross_tax_non_recurring_payment is not UNSET:
            field_dict["gross_tax_non_recurring_payment"] = gross_tax_non_recurring_payment
        if tax_deductions is not UNSET:
            field_dict["tax_deductions"] = tax_deductions
        if solidarity_tax_monthly is not UNSET:
            field_dict["solidarity_tax_monthly"] = solidarity_tax_monthly
        if solidarity_tax_non_recurring_payment is not UNSET:
            field_dict["solidarity_tax_non_recurring_payment"] = solidarity_tax_non_recurring_payment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        personnel_number = d.pop("personnel_number", UNSET)

        company_personnel_number = d.pop("company_personnel_number", UNSET)

        accounting_month = d.pop("accounting_month", UNSET)

        month_of_recalculation = d.pop("month_of_recalculation", UNSET)

        current_gross_tax = d.pop("current_gross_tax", UNSET)

        flat_rate_church_tax = d.pop("flat_rate_church_tax", UNSET)

        flat_rate_solidarity_tax = d.pop("flat_rate_solidarity_tax", UNSET)

        flat_rate_wage_tax = d.pop("flat_rate_wage_tax", UNSET)

        flat_rate_taxed_payments = d.pop("flat_rate_taxed_payments", UNSET)

        solidarity_tax = d.pop("solidarity_tax", UNSET)

        wage_tax = d.pop("wage_tax", UNSET)

        other_payments_taxed_at_flat_rate = d.pop("other_payments_taxed_at_flat_rate", UNSET)

        payment_taxed_at_a_flat_rate_when_low_paid_employed = d.pop("payment_taxed_at_a_flat_rate_when_low_paid_employed", UNSET)

        payment_taxed_at_a_flat_rate_when_short_term_employed = d.pop("payment_taxed_at_a_flat_rate_when_short_term_employed", UNSET)

        wage_tax_non_recurring_payment = d.pop("wage_tax_non_recurring_payment", UNSET)

        wage_tax_monthly = d.pop("wage_tax_monthly", UNSET)

        church_tax_non_recurring_payment = d.pop("church_tax_non_recurring_payment", UNSET)

        church_tax = d.pop("church_tax", UNSET)

        church_tax_monthly = d.pop("church_tax_monthly", UNSET)

        tax_relevant_days = d.pop("tax_relevant_days", UNSET)

        gross_tax_non_recurring_payment = d.pop("gross_tax_non_recurring_payment", UNSET)

        tax_deductions = d.pop("tax_deductions", UNSET)

        solidarity_tax_monthly = d.pop("solidarity_tax_monthly", UNSET)

        solidarity_tax_non_recurring_payment = d.pop("solidarity_tax_non_recurring_payment", UNSET)

        tax_payments = cls(
            personnel_number=personnel_number,
            company_personnel_number=company_personnel_number,
            accounting_month=accounting_month,
            month_of_recalculation=month_of_recalculation,
            current_gross_tax=current_gross_tax,
            flat_rate_church_tax=flat_rate_church_tax,
            flat_rate_solidarity_tax=flat_rate_solidarity_tax,
            flat_rate_wage_tax=flat_rate_wage_tax,
            flat_rate_taxed_payments=flat_rate_taxed_payments,
            solidarity_tax=solidarity_tax,
            wage_tax=wage_tax,
            other_payments_taxed_at_flat_rate=other_payments_taxed_at_flat_rate,
            payment_taxed_at_a_flat_rate_when_low_paid_employed=payment_taxed_at_a_flat_rate_when_low_paid_employed,
            payment_taxed_at_a_flat_rate_when_short_term_employed=payment_taxed_at_a_flat_rate_when_short_term_employed,
            wage_tax_non_recurring_payment=wage_tax_non_recurring_payment,
            wage_tax_monthly=wage_tax_monthly,
            church_tax_non_recurring_payment=church_tax_non_recurring_payment,
            church_tax=church_tax,
            church_tax_monthly=church_tax_monthly,
            tax_relevant_days=tax_relevant_days,
            gross_tax_non_recurring_payment=gross_tax_non_recurring_payment,
            tax_deductions=tax_deductions,
            solidarity_tax_monthly=solidarity_tax_monthly,
            solidarity_tax_non_recurring_payment=solidarity_tax_non_recurring_payment,
        )


        tax_payments.additional_properties = d
        return tax_payments

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
