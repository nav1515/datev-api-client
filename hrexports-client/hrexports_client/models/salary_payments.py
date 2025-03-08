from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.gross_payments_lug import GrossPaymentsLug
  from ..models.gross_payments_lodas import GrossPaymentsLodas
  from ..models.net_payments import NetPayments





T = TypeVar("T", bound="SalaryPayments")



@_attrs_define
class SalaryPayments:
    """ 
        Attributes:
            personnel_number (Union[Unset, int]): Employee's personnel number in the payroll system Example: 10.
            company_personnel_number (Union[Unset, str]): Company personnel number (Betriebliche Personalnummer) Example:
                10.
            accounting_month (Union[Unset, str]): Accounting month (Abrechnungsmonat) Example: 2020-01.
            month_of_recalculation (Union[Unset, str]): Month of recalculation (Nachberechnungsmonat) Example: 2020-01.
            gross_payments_lodas (Union[Unset, list['GrossPaymentsLodas']]): Gross Payments represent 'Lohnarten' with
                wage_type_number up until 8999 for LODAS
            gross_payments_lug (Union[Unset, list['GrossPaymentsLug']]): Gross Payments represent 'Lohnarten' with
                wage_type_number up until 8999 for LuG
            net_payments (Union[Unset, list['NetPayments']]): Net Payments represent 'Nettobezüge' and 'Nettoabzüge' with
                wage_type_number equal to or greater than 9000
     """

    personnel_number: Union[Unset, int] = UNSET
    company_personnel_number: Union[Unset, str] = UNSET
    accounting_month: Union[Unset, str] = UNSET
    month_of_recalculation: Union[Unset, str] = UNSET
    gross_payments_lodas: Union[Unset, list['GrossPaymentsLodas']] = UNSET
    gross_payments_lug: Union[Unset, list['GrossPaymentsLug']] = UNSET
    net_payments: Union[Unset, list['NetPayments']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> dict[str, Any]:
        from ..models.gross_payments_lug import GrossPaymentsLug
        from ..models.gross_payments_lodas import GrossPaymentsLodas
        from ..models.net_payments import NetPayments
        personnel_number = self.personnel_number

        company_personnel_number = self.company_personnel_number

        accounting_month = self.accounting_month

        month_of_recalculation = self.month_of_recalculation

        gross_payments_lodas: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.gross_payments_lodas, Unset):
            gross_payments_lodas = []
            for gross_payments_lodas_item_data in self.gross_payments_lodas:
                gross_payments_lodas_item = gross_payments_lodas_item_data.to_dict()
                gross_payments_lodas.append(gross_payments_lodas_item)



        gross_payments_lug: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.gross_payments_lug, Unset):
            gross_payments_lug = []
            for gross_payments_lug_item_data in self.gross_payments_lug:
                gross_payments_lug_item = gross_payments_lug_item_data.to_dict()
                gross_payments_lug.append(gross_payments_lug_item)



        net_payments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.net_payments, Unset):
            net_payments = []
            for net_payments_item_data in self.net_payments:
                net_payments_item = net_payments_item_data.to_dict()
                net_payments.append(net_payments_item)




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
        if gross_payments_lodas is not UNSET:
            field_dict["gross_payments_lodas"] = gross_payments_lodas
        if gross_payments_lug is not UNSET:
            field_dict["gross_payments_lug"] = gross_payments_lug
        if net_payments is not UNSET:
            field_dict["net_payments"] = net_payments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gross_payments_lug import GrossPaymentsLug
        from ..models.gross_payments_lodas import GrossPaymentsLodas
        from ..models.net_payments import NetPayments
        d = src_dict.copy()
        personnel_number = d.pop("personnel_number", UNSET)

        company_personnel_number = d.pop("company_personnel_number", UNSET)

        accounting_month = d.pop("accounting_month", UNSET)

        month_of_recalculation = d.pop("month_of_recalculation", UNSET)

        gross_payments_lodas = []
        _gross_payments_lodas = d.pop("gross_payments_lodas", UNSET)
        for gross_payments_lodas_item_data in (_gross_payments_lodas or []):
            gross_payments_lodas_item = GrossPaymentsLodas.from_dict(gross_payments_lodas_item_data)



            gross_payments_lodas.append(gross_payments_lodas_item)


        gross_payments_lug = []
        _gross_payments_lug = d.pop("gross_payments_lug", UNSET)
        for gross_payments_lug_item_data in (_gross_payments_lug or []):
            gross_payments_lug_item = GrossPaymentsLug.from_dict(gross_payments_lug_item_data)



            gross_payments_lug.append(gross_payments_lug_item)


        net_payments = []
        _net_payments = d.pop("net_payments", UNSET)
        for net_payments_item_data in (_net_payments or []):
            net_payments_item = NetPayments.from_dict(net_payments_item_data)



            net_payments.append(net_payments_item)


        salary_payments = cls(
            personnel_number=personnel_number,
            company_personnel_number=company_personnel_number,
            accounting_month=accounting_month,
            month_of_recalculation=month_of_recalculation,
            gross_payments_lodas=gross_payments_lodas,
            gross_payments_lug=gross_payments_lug,
            net_payments=net_payments,
        )


        salary_payments.additional_properties = d
        return salary_payments

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
