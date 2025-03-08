from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_message import ErrorMessage
from ...models.error_message_5_xx import ErrorMessage5Xx
from ...models.salary_total_values import SalaryTotalValues
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    client_id: str,
    employee_id: int,
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
        "url": "/clients/{client_id}/employees/{employee_id}/salarytotalvalues".format(client_id=client_id,employee_id=employee_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]]:
    if response.status_code == 200:
        response_200 = SalaryTotalValues.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]]:
    """ Get the employee's salary total values

     Salary (Gesamtbrutto, Auszahlungsbetrag, Nettoverdienst) of an employee can be accessed by its
    employee-id.



    If a non-mandatory field is not filled in the payroll system, the field will not be exported through
    the API. Therefore the example model might differ from the actual response.

    Args:
        client_id (str):
        employee_id (int):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
employee_id=employee_id,
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
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]]:
    """ Get the employee's salary total values

     Salary (Gesamtbrutto, Auszahlungsbetrag, Nettoverdienst) of an employee can be accessed by its
    employee-id.



    If a non-mandatory field is not filled in the payroll system, the field will not be exported through
    the API. Therefore the example model might differ from the actual response.

    Args:
        client_id (str):
        employee_id (int):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]
     """


    return sync_detailed(
        client_id=client_id,
employee_id=employee_id,
client=client,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]]:
    """ Get the employee's salary total values

     Salary (Gesamtbrutto, Auszahlungsbetrag, Nettoverdienst) of an employee can be accessed by its
    employee-id.



    If a non-mandatory field is not filled in the payroll system, the field will not be exported through
    the API. Therefore the example model might differ from the actual response.

    Args:
        client_id (str):
        employee_id (int):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
employee_id=employee_id,
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
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    payroll_accounting_month: Union[Unset, str] = UNSET,
    payroll_accounting_month_end: Union[Unset, str] = UNSET,
    payroll_recalculation_month: Union[Unset, str] = UNSET,
    payroll_recalculation_month_end: Union[Unset, str] = UNSET,

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]]:
    """ Get the employee's salary total values

     Salary (Gesamtbrutto, Auszahlungsbetrag, Nettoverdienst) of an employee can be accessed by its
    employee-id.



    If a non-mandatory field is not filled in the payroll system, the field will not be exported through
    the API. Therefore the example model might differ from the actual response.

    Args:
        client_id (str):
        employee_id (int):
        payroll_accounting_month (Union[Unset, str]):
        payroll_accounting_month_end (Union[Unset, str]):
        payroll_recalculation_month (Union[Unset, str]):
        payroll_recalculation_month_end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, SalaryTotalValues]
     """


    return (await asyncio_detailed(
        client_id=client_id,
employee_id=employee_id,
client=client,
payroll_accounting_month=payroll_accounting_month,
payroll_accounting_month_end=payroll_accounting_month_end,
payroll_recalculation_month=payroll_recalculation_month,
payroll_recalculation_month_end=payroll_recalculation_month_end,

    )).parsed
