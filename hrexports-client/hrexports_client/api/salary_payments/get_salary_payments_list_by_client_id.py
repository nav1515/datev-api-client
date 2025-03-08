from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_message import ErrorMessage
from ...models.error_message_5_xx import ErrorMessage5Xx
from ...models.salary_payments import SalaryPayments
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    client_id: str,
    *,
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["payroll_accounting_month"] = payroll_accounting_month

    params["payroll_accounting_month_end"] = payroll_accounting_month_end

    params["payroll_recalculation_month"] = payroll_recalculation_month

    params["payroll_recalculation_month_end"] = payroll_recalculation_month_end


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}/employees/salarypayments".format(client_id=client_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = SalaryPayments.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ErrorMessage.from_dict(response.json())



        return response_400
    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())



        return response_403
    if response.status_code == 404:
        response_404 = ErrorMessage.from_dict(response.json())



        return response_404
    if response.status_code == 500:
        response_500 = ErrorMessage5Xx.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]]:
    """ Get the employee's salary payments

     Salary components (Lohnarten, Nettobezüge, Nettoabzüge) of all employees of an client can be
    accessed by the client's client-id.



    If a non-mandatory field is not filled in the payroll system, the field will not be exported through
    the API. Therefore the example model might differ from the actual response.



    | Property | Values |
    | ----| -----|
    |  |   |
    | **tax_and_social_security_treatment_of_wage_type** | 0 = keine SV-Verteilung, kein Gesamt-Brutto,
    1 = Bezüge steuer- u. sv-pflichtig, 2 = Bezüge nur steuerpflichtig, 3 = Bezüge nur sv-pflichtig, 4 =
    Bezüge steuer- u. sv-frei, 5 = Bez. steuer- u. sv-pfl., kein Gesamt-Brutto, 6 = Bez. steuer- u. sv-
    pfl., Verst.ü.Jahrestab., 7 = Bezüge nur steuerpfl., Verst.ü.Jahrestab., 9 = steuer- u.sv-
    pfl.,k.Ges.bto, Jahrestabelle, 10 = nur steuerpfl., k.Ges.bto, Jahrestabelle, 11 = Abwälzung pausch.
    Steuer, nur Gesamtbrutto, 12 = Steuer: Fünftelregelung, sv-pfl. sonstiger Bezug, 13 = AG-Ant. ZVK
    Umlage (öff. Dienst), 14 = Sachzuwend p .St/SV-frei, 17 = AG-Ant. ZVK Umlage (öff. Dienst) Verst.
    Jahrestab., 18 = Bez. steuer- u. sv-pfl., Verst.ü.Monatstab., 19 = Bezüge steuerfrei, sv-pflichtig,
    21 = Weihnachtsgratifikation, einmaliges Entgelt, 22 = Fahrtkost. Ausw.Lohnkto u. LStB, steuer- u.
    sv-frei, 23 = steuer- u. sv-freie Verpflegungszusch. bei Auswärtstätigkeit, 24 = Bezüge n.
    Doppelbesteuerungsabk., lfd.Bezug, 25 = Bezüge n. Doppelbest.abk., einmal. Entgelt, 26 = Bezüge n.
    Auslandstätigkeiterlass, lfd.Bezug, 27 = Bez. n.Auslandstätigk.erlass, einmal.Entgelt, 28 = Bezüge
    steuer- u. sv-pfl., Jahrestabelle, 29 = Bezüge nur sv-pflichtig, kein Gesamt-Brutto, 30 =
    Versorgungsbezüge, Verst. ü. Monatstabelle, 31 = Versorgungsbezüge, Verst. ü. Jahrestabelle, 32 =
    AG-Anteil Vermögensbildung, laufender Bezug, 33 = AG-Anteil Vermögensbildung, einmal. Entgelt, 34 =
    AVV ST pausch SV mtl, 35 = AVV ST pausch SV frei, 36 = AVV ST pausch SV jhrl, 38 = Zusatzrente
    Unterstützungskasse, steuer- und sv.frei, 41 = Erholungsbeihilfe p .St/SV-frei, 42 = Firmenrabatt,
    monatlich, 43 = Firmenrabatt, jährlich, 44 = AG-Leist. doppelte Haushaltsführung, 45 = Zuschüsse
    Mutterschaftsgeld, 46 = Verdienstausf.entschäd. n.Bundesseuchenges., 47 = pauschal versteuerte
    Fahrtkosten, 48 = pauschal versteuerte Bezüge, 25%, sv-frei, 49 = Sachzuwendung pausch.
    Versteuerung, sv-jhrl.., 50 = Abfindung, steuerpflichtig, sv-frei, 51 = Nachtzuschlag, 25%
    steuerfrei, 52 = Sonntagszuschlag, 50% steuerfrei, 53 = Feiertagszuschlag, 125% steuerfrei, 54 =
    Feiertagszuschlag, 150% steuerfrei, 55 = Nachtzuschlag/Kern, 40% steuerfrei, 56 = Sonntags-
    u.Nachtzu./Kern, 90% steuerfrei, 57 = Feiertags- u.Nachtzu./Kern, 165% steuerfrei, 58 = Feiertags-
    u. Nachtzu./Kern, 190% steuerfr., 59 = Sonntags- u. Nachtzuschlag, 75% steuerfrei, 60 = Feiertags-
    u. Nachtzuschlag, 150% steuerfr., 61 = Feiertags- u. Nachtzuschlag, 175% steuerfr., 71 = ausgez.
    Wertguthaben, st.-pfl. mehrj. Bezug, 72 = ausgez. Wertguthaben, st.-pfl. jhrl. Bezug, 73 = ausgez.
    Wertguthaben, steuerfreier Bezug, 74 = ST/SV/Umlage jhrl., 75 = st.pfl. Monatstabelle; sv-pfl.
    monatsbez. BBG bzw. VB-Max, 76 = st.pfl. Jahrestabelle; sv-pfl. monatsbez. BBG bzw. VB-Max, 77 =
    st.pfl. mehrjährig; sv-frei, 78 = st-pfl. über Jahrestabelle/sv-frei, 79 = st-pfl. monatlich/sv-
    frei, k. Ges. Brutto, 80 = Besondere Pauschalierung/SV lfd., 81 = Besondere Pauschalierung/SV jhrl.,
    82 = Besondere Pauschalierung/SV frei, 83 = Bezüge nur steuerpfl., k. Ges. Brutto, 84 = Bezüge
    steuer- u. sv-frei, k. Ges. Brutto, 85 = Bezüge EBZ st-frei, sv-pfl., k. Ges.Brutto, 86 = AVV ST
    pausch SV mtl., k. Ges. Brutto, 87 = AVV ST pausch SV frei, k. Ges. Brutto, 88 = AVV ST pausch SV
    jhrl., k. Ges. Brutto, 89 = Bezüge lfd st-frei, sv-pfl., k. Ges.Brutto, 90 = st-pfl. jährlich/sv-
    frei, k. Ges. Brutto, 91 = st-pfl. mehrjährig/sv-frei, k. Ges. Brutto, 92 = Versorgbez. st-pfl.
    monatlich / sv-frei   |
    | **social_security_treatment_of_wage_type** | F = Frei, L = Laufender Bezug, P = Pauschal, E =
    Einmalbezug, A = Abfindung, M = Mehrjähriger Bezug |
    | **tax_treatment_of_wage_type** | L = Laufender Bezug, F = Frei, P = Pauschal, S = Sonstiger Bezug,
    M = mehrjähriger Bezug, W = Störfall West, O = Störfall Ost |
    | **component_gross_payment** | Ist Bestandteil des Gesamtbruttos Ja/Nein |

    Args:
        client_id (str):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]]:
    """ Get the employee's salary payments

     Salary components (Lohnarten, Nettobezüge, Nettoabzüge) of all employees of an client can be
    accessed by the client's client-id.



    If a non-mandatory field is not filled in the payroll system, the field will not be exported through
    the API. Therefore the example model might differ from the actual response.



    | Property | Values |
    | ----| -----|
    |  |   |
    | **tax_and_social_security_treatment_of_wage_type** | 0 = keine SV-Verteilung, kein Gesamt-Brutto,
    1 = Bezüge steuer- u. sv-pflichtig, 2 = Bezüge nur steuerpflichtig, 3 = Bezüge nur sv-pflichtig, 4 =
    Bezüge steuer- u. sv-frei, 5 = Bez. steuer- u. sv-pfl., kein Gesamt-Brutto, 6 = Bez. steuer- u. sv-
    pfl., Verst.ü.Jahrestab., 7 = Bezüge nur steuerpfl., Verst.ü.Jahrestab., 9 = steuer- u.sv-
    pfl.,k.Ges.bto, Jahrestabelle, 10 = nur steuerpfl., k.Ges.bto, Jahrestabelle, 11 = Abwälzung pausch.
    Steuer, nur Gesamtbrutto, 12 = Steuer: Fünftelregelung, sv-pfl. sonstiger Bezug, 13 = AG-Ant. ZVK
    Umlage (öff. Dienst), 14 = Sachzuwend p .St/SV-frei, 17 = AG-Ant. ZVK Umlage (öff. Dienst) Verst.
    Jahrestab., 18 = Bez. steuer- u. sv-pfl., Verst.ü.Monatstab., 19 = Bezüge steuerfrei, sv-pflichtig,
    21 = Weihnachtsgratifikation, einmaliges Entgelt, 22 = Fahrtkost. Ausw.Lohnkto u. LStB, steuer- u.
    sv-frei, 23 = steuer- u. sv-freie Verpflegungszusch. bei Auswärtstätigkeit, 24 = Bezüge n.
    Doppelbesteuerungsabk., lfd.Bezug, 25 = Bezüge n. Doppelbest.abk., einmal. Entgelt, 26 = Bezüge n.
    Auslandstätigkeiterlass, lfd.Bezug, 27 = Bez. n.Auslandstätigk.erlass, einmal.Entgelt, 28 = Bezüge
    steuer- u. sv-pfl., Jahrestabelle, 29 = Bezüge nur sv-pflichtig, kein Gesamt-Brutto, 30 =
    Versorgungsbezüge, Verst. ü. Monatstabelle, 31 = Versorgungsbezüge, Verst. ü. Jahrestabelle, 32 =
    AG-Anteil Vermögensbildung, laufender Bezug, 33 = AG-Anteil Vermögensbildung, einmal. Entgelt, 34 =
    AVV ST pausch SV mtl, 35 = AVV ST pausch SV frei, 36 = AVV ST pausch SV jhrl, 38 = Zusatzrente
    Unterstützungskasse, steuer- und sv.frei, 41 = Erholungsbeihilfe p .St/SV-frei, 42 = Firmenrabatt,
    monatlich, 43 = Firmenrabatt, jährlich, 44 = AG-Leist. doppelte Haushaltsführung, 45 = Zuschüsse
    Mutterschaftsgeld, 46 = Verdienstausf.entschäd. n.Bundesseuchenges., 47 = pauschal versteuerte
    Fahrtkosten, 48 = pauschal versteuerte Bezüge, 25%, sv-frei, 49 = Sachzuwendung pausch.
    Versteuerung, sv-jhrl.., 50 = Abfindung, steuerpflichtig, sv-frei, 51 = Nachtzuschlag, 25%
    steuerfrei, 52 = Sonntagszuschlag, 50% steuerfrei, 53 = Feiertagszuschlag, 125% steuerfrei, 54 =
    Feiertagszuschlag, 150% steuerfrei, 55 = Nachtzuschlag/Kern, 40% steuerfrei, 56 = Sonntags-
    u.Nachtzu./Kern, 90% steuerfrei, 57 = Feiertags- u.Nachtzu./Kern, 165% steuerfrei, 58 = Feiertags-
    u. Nachtzu./Kern, 190% steuerfr., 59 = Sonntags- u. Nachtzuschlag, 75% steuerfrei, 60 = Feiertags-
    u. Nachtzuschlag, 150% steuerfr., 61 = Feiertags- u. Nachtzuschlag, 175% steuerfr., 71 = ausgez.
    Wertguthaben, st.-pfl. mehrj. Bezug, 72 = ausgez. Wertguthaben, st.-pfl. jhrl. Bezug, 73 = ausgez.
    Wertguthaben, steuerfreier Bezug, 74 = ST/SV/Umlage jhrl., 75 = st.pfl. Monatstabelle; sv-pfl.
    monatsbez. BBG bzw. VB-Max, 76 = st.pfl. Jahrestabelle; sv-pfl. monatsbez. BBG bzw. VB-Max, 77 =
    st.pfl. mehrjährig; sv-frei, 78 = st-pfl. über Jahrestabelle/sv-frei, 79 = st-pfl. monatlich/sv-
    frei, k. Ges. Brutto, 80 = Besondere Pauschalierung/SV lfd., 81 = Besondere Pauschalierung/SV jhrl.,
    82 = Besondere Pauschalierung/SV frei, 83 = Bezüge nur steuerpfl., k. Ges. Brutto, 84 = Bezüge
    steuer- u. sv-frei, k. Ges. Brutto, 85 = Bezüge EBZ st-frei, sv-pfl., k. Ges.Brutto, 86 = AVV ST
    pausch SV mtl., k. Ges. Brutto, 87 = AVV ST pausch SV frei, k. Ges. Brutto, 88 = AVV ST pausch SV
    jhrl., k. Ges. Brutto, 89 = Bezüge lfd st-frei, sv-pfl., k. Ges.Brutto, 90 = st-pfl. jährlich/sv-
    frei, k. Ges. Brutto, 91 = st-pfl. mehrjährig/sv-frei, k. Ges. Brutto, 92 = Versorgbez. st-pfl.
    monatlich / sv-frei   |
    | **social_security_treatment_of_wage_type** | F = Frei, L = Laufender Bezug, P = Pauschal, E =
    Einmalbezug, A = Abfindung, M = Mehrjähriger Bezug |
    | **tax_treatment_of_wage_type** | L = Laufender Bezug, F = Frei, P = Pauschal, S = Sonstiger Bezug,
    M = mehrjähriger Bezug, W = Störfall West, O = Störfall Ost |
    | **component_gross_payment** | Ist Bestandteil des Gesamtbruttos Ja/Nein |

    Args:
        client_id (str):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]
     """


    return sync_detailed(
        client_id=client_id,
client=client,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]]:
    """ Get the employee's salary payments

     Salary components (Lohnarten, Nettobezüge, Nettoabzüge) of all employees of an client can be
    accessed by the client's client-id.



    If a non-mandatory field is not filled in the payroll system, the field will not be exported through
    the API. Therefore the example model might differ from the actual response.



    | Property | Values |
    | ----| -----|
    |  |   |
    | **tax_and_social_security_treatment_of_wage_type** | 0 = keine SV-Verteilung, kein Gesamt-Brutto,
    1 = Bezüge steuer- u. sv-pflichtig, 2 = Bezüge nur steuerpflichtig, 3 = Bezüge nur sv-pflichtig, 4 =
    Bezüge steuer- u. sv-frei, 5 = Bez. steuer- u. sv-pfl., kein Gesamt-Brutto, 6 = Bez. steuer- u. sv-
    pfl., Verst.ü.Jahrestab., 7 = Bezüge nur steuerpfl., Verst.ü.Jahrestab., 9 = steuer- u.sv-
    pfl.,k.Ges.bto, Jahrestabelle, 10 = nur steuerpfl., k.Ges.bto, Jahrestabelle, 11 = Abwälzung pausch.
    Steuer, nur Gesamtbrutto, 12 = Steuer: Fünftelregelung, sv-pfl. sonstiger Bezug, 13 = AG-Ant. ZVK
    Umlage (öff. Dienst), 14 = Sachzuwend p .St/SV-frei, 17 = AG-Ant. ZVK Umlage (öff. Dienst) Verst.
    Jahrestab., 18 = Bez. steuer- u. sv-pfl., Verst.ü.Monatstab., 19 = Bezüge steuerfrei, sv-pflichtig,
    21 = Weihnachtsgratifikation, einmaliges Entgelt, 22 = Fahrtkost. Ausw.Lohnkto u. LStB, steuer- u.
    sv-frei, 23 = steuer- u. sv-freie Verpflegungszusch. bei Auswärtstätigkeit, 24 = Bezüge n.
    Doppelbesteuerungsabk., lfd.Bezug, 25 = Bezüge n. Doppelbest.abk., einmal. Entgelt, 26 = Bezüge n.
    Auslandstätigkeiterlass, lfd.Bezug, 27 = Bez. n.Auslandstätigk.erlass, einmal.Entgelt, 28 = Bezüge
    steuer- u. sv-pfl., Jahrestabelle, 29 = Bezüge nur sv-pflichtig, kein Gesamt-Brutto, 30 =
    Versorgungsbezüge, Verst. ü. Monatstabelle, 31 = Versorgungsbezüge, Verst. ü. Jahrestabelle, 32 =
    AG-Anteil Vermögensbildung, laufender Bezug, 33 = AG-Anteil Vermögensbildung, einmal. Entgelt, 34 =
    AVV ST pausch SV mtl, 35 = AVV ST pausch SV frei, 36 = AVV ST pausch SV jhrl, 38 = Zusatzrente
    Unterstützungskasse, steuer- und sv.frei, 41 = Erholungsbeihilfe p .St/SV-frei, 42 = Firmenrabatt,
    monatlich, 43 = Firmenrabatt, jährlich, 44 = AG-Leist. doppelte Haushaltsführung, 45 = Zuschüsse
    Mutterschaftsgeld, 46 = Verdienstausf.entschäd. n.Bundesseuchenges., 47 = pauschal versteuerte
    Fahrtkosten, 48 = pauschal versteuerte Bezüge, 25%, sv-frei, 49 = Sachzuwendung pausch.
    Versteuerung, sv-jhrl.., 50 = Abfindung, steuerpflichtig, sv-frei, 51 = Nachtzuschlag, 25%
    steuerfrei, 52 = Sonntagszuschlag, 50% steuerfrei, 53 = Feiertagszuschlag, 125% steuerfrei, 54 =
    Feiertagszuschlag, 150% steuerfrei, 55 = Nachtzuschlag/Kern, 40% steuerfrei, 56 = Sonntags-
    u.Nachtzu./Kern, 90% steuerfrei, 57 = Feiertags- u.Nachtzu./Kern, 165% steuerfrei, 58 = Feiertags-
    u. Nachtzu./Kern, 190% steuerfr., 59 = Sonntags- u. Nachtzuschlag, 75% steuerfrei, 60 = Feiertags-
    u. Nachtzuschlag, 150% steuerfr., 61 = Feiertags- u. Nachtzuschlag, 175% steuerfr., 71 = ausgez.
    Wertguthaben, st.-pfl. mehrj. Bezug, 72 = ausgez. Wertguthaben, st.-pfl. jhrl. Bezug, 73 = ausgez.
    Wertguthaben, steuerfreier Bezug, 74 = ST/SV/Umlage jhrl., 75 = st.pfl. Monatstabelle; sv-pfl.
    monatsbez. BBG bzw. VB-Max, 76 = st.pfl. Jahrestabelle; sv-pfl. monatsbez. BBG bzw. VB-Max, 77 =
    st.pfl. mehrjährig; sv-frei, 78 = st-pfl. über Jahrestabelle/sv-frei, 79 = st-pfl. monatlich/sv-
    frei, k. Ges. Brutto, 80 = Besondere Pauschalierung/SV lfd., 81 = Besondere Pauschalierung/SV jhrl.,
    82 = Besondere Pauschalierung/SV frei, 83 = Bezüge nur steuerpfl., k. Ges. Brutto, 84 = Bezüge
    steuer- u. sv-frei, k. Ges. Brutto, 85 = Bezüge EBZ st-frei, sv-pfl., k. Ges.Brutto, 86 = AVV ST
    pausch SV mtl., k. Ges. Brutto, 87 = AVV ST pausch SV frei, k. Ges. Brutto, 88 = AVV ST pausch SV
    jhrl., k. Ges. Brutto, 89 = Bezüge lfd st-frei, sv-pfl., k. Ges.Brutto, 90 = st-pfl. jährlich/sv-
    frei, k. Ges. Brutto, 91 = st-pfl. mehrjährig/sv-frei, k. Ges. Brutto, 92 = Versorgbez. st-pfl.
    monatlich / sv-frei   |
    | **social_security_treatment_of_wage_type** | F = Frei, L = Laufender Bezug, P = Pauschal, E =
    Einmalbezug, A = Abfindung, M = Mehrjähriger Bezug |
    | **tax_treatment_of_wage_type** | L = Laufender Bezug, F = Frei, P = Pauschal, S = Sonstiger Bezug,
    M = mehrjähriger Bezug, W = Störfall West, O = Störfall Ost |
    | **component_gross_payment** | Ist Bestandteil des Gesamtbruttos Ja/Nein |

    Args:
        client_id (str):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]]:
    """ Get the employee's salary payments

     Salary components (Lohnarten, Nettobezüge, Nettoabzüge) of all employees of an client can be
    accessed by the client's client-id.



    If a non-mandatory field is not filled in the payroll system, the field will not be exported through
    the API. Therefore the example model might differ from the actual response.



    | Property | Values |
    | ----| -----|
    |  |   |
    | **tax_and_social_security_treatment_of_wage_type** | 0 = keine SV-Verteilung, kein Gesamt-Brutto,
    1 = Bezüge steuer- u. sv-pflichtig, 2 = Bezüge nur steuerpflichtig, 3 = Bezüge nur sv-pflichtig, 4 =
    Bezüge steuer- u. sv-frei, 5 = Bez. steuer- u. sv-pfl., kein Gesamt-Brutto, 6 = Bez. steuer- u. sv-
    pfl., Verst.ü.Jahrestab., 7 = Bezüge nur steuerpfl., Verst.ü.Jahrestab., 9 = steuer- u.sv-
    pfl.,k.Ges.bto, Jahrestabelle, 10 = nur steuerpfl., k.Ges.bto, Jahrestabelle, 11 = Abwälzung pausch.
    Steuer, nur Gesamtbrutto, 12 = Steuer: Fünftelregelung, sv-pfl. sonstiger Bezug, 13 = AG-Ant. ZVK
    Umlage (öff. Dienst), 14 = Sachzuwend p .St/SV-frei, 17 = AG-Ant. ZVK Umlage (öff. Dienst) Verst.
    Jahrestab., 18 = Bez. steuer- u. sv-pfl., Verst.ü.Monatstab., 19 = Bezüge steuerfrei, sv-pflichtig,
    21 = Weihnachtsgratifikation, einmaliges Entgelt, 22 = Fahrtkost. Ausw.Lohnkto u. LStB, steuer- u.
    sv-frei, 23 = steuer- u. sv-freie Verpflegungszusch. bei Auswärtstätigkeit, 24 = Bezüge n.
    Doppelbesteuerungsabk., lfd.Bezug, 25 = Bezüge n. Doppelbest.abk., einmal. Entgelt, 26 = Bezüge n.
    Auslandstätigkeiterlass, lfd.Bezug, 27 = Bez. n.Auslandstätigk.erlass, einmal.Entgelt, 28 = Bezüge
    steuer- u. sv-pfl., Jahrestabelle, 29 = Bezüge nur sv-pflichtig, kein Gesamt-Brutto, 30 =
    Versorgungsbezüge, Verst. ü. Monatstabelle, 31 = Versorgungsbezüge, Verst. ü. Jahrestabelle, 32 =
    AG-Anteil Vermögensbildung, laufender Bezug, 33 = AG-Anteil Vermögensbildung, einmal. Entgelt, 34 =
    AVV ST pausch SV mtl, 35 = AVV ST pausch SV frei, 36 = AVV ST pausch SV jhrl, 38 = Zusatzrente
    Unterstützungskasse, steuer- und sv.frei, 41 = Erholungsbeihilfe p .St/SV-frei, 42 = Firmenrabatt,
    monatlich, 43 = Firmenrabatt, jährlich, 44 = AG-Leist. doppelte Haushaltsführung, 45 = Zuschüsse
    Mutterschaftsgeld, 46 = Verdienstausf.entschäd. n.Bundesseuchenges., 47 = pauschal versteuerte
    Fahrtkosten, 48 = pauschal versteuerte Bezüge, 25%, sv-frei, 49 = Sachzuwendung pausch.
    Versteuerung, sv-jhrl.., 50 = Abfindung, steuerpflichtig, sv-frei, 51 = Nachtzuschlag, 25%
    steuerfrei, 52 = Sonntagszuschlag, 50% steuerfrei, 53 = Feiertagszuschlag, 125% steuerfrei, 54 =
    Feiertagszuschlag, 150% steuerfrei, 55 = Nachtzuschlag/Kern, 40% steuerfrei, 56 = Sonntags-
    u.Nachtzu./Kern, 90% steuerfrei, 57 = Feiertags- u.Nachtzu./Kern, 165% steuerfrei, 58 = Feiertags-
    u. Nachtzu./Kern, 190% steuerfr., 59 = Sonntags- u. Nachtzuschlag, 75% steuerfrei, 60 = Feiertags-
    u. Nachtzuschlag, 150% steuerfr., 61 = Feiertags- u. Nachtzuschlag, 175% steuerfr., 71 = ausgez.
    Wertguthaben, st.-pfl. mehrj. Bezug, 72 = ausgez. Wertguthaben, st.-pfl. jhrl. Bezug, 73 = ausgez.
    Wertguthaben, steuerfreier Bezug, 74 = ST/SV/Umlage jhrl., 75 = st.pfl. Monatstabelle; sv-pfl.
    monatsbez. BBG bzw. VB-Max, 76 = st.pfl. Jahrestabelle; sv-pfl. monatsbez. BBG bzw. VB-Max, 77 =
    st.pfl. mehrjährig; sv-frei, 78 = st-pfl. über Jahrestabelle/sv-frei, 79 = st-pfl. monatlich/sv-
    frei, k. Ges. Brutto, 80 = Besondere Pauschalierung/SV lfd., 81 = Besondere Pauschalierung/SV jhrl.,
    82 = Besondere Pauschalierung/SV frei, 83 = Bezüge nur steuerpfl., k. Ges. Brutto, 84 = Bezüge
    steuer- u. sv-frei, k. Ges. Brutto, 85 = Bezüge EBZ st-frei, sv-pfl., k. Ges.Brutto, 86 = AVV ST
    pausch SV mtl., k. Ges. Brutto, 87 = AVV ST pausch SV frei, k. Ges. Brutto, 88 = AVV ST pausch SV
    jhrl., k. Ges. Brutto, 89 = Bezüge lfd st-frei, sv-pfl., k. Ges.Brutto, 90 = st-pfl. jährlich/sv-
    frei, k. Ges. Brutto, 91 = st-pfl. mehrjährig/sv-frei, k. Ges. Brutto, 92 = Versorgbez. st-pfl.
    monatlich / sv-frei   |
    | **social_security_treatment_of_wage_type** | F = Frei, L = Laufender Bezug, P = Pauschal, E =
    Einmalbezug, A = Abfindung, M = Mehrjähriger Bezug |
    | **tax_treatment_of_wage_type** | L = Laufender Bezug, F = Frei, P = Pauschal, S = Sonstiger Bezug,
    M = mehrjähriger Bezug, W = Störfall West, O = Störfall Ost |
    | **component_gross_payment** | Ist Bestandteil des Gesamtbruttos Ja/Nein |

    Args:
        client_id (str):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, list['SalaryPayments']]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    )).parsed
