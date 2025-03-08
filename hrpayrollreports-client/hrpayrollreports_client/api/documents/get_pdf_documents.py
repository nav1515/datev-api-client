from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_message import ErrorMessage
from ...models.error_message_5_xx import ErrorMessage5Xx
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    client_id: str,
    period: str,
    *,
    employee_number: Union[Unset, int] = UNSET,
    accept: str = 'application/pdf',

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Accept"] = accept



    

    params: dict[str, Any] = {}

    params["employee_number"] = employee_number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}/documents/{period}".format(client_id=client_id,period=period,),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorMessage, ErrorMessage5Xx]]:
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorMessage, ErrorMessage5Xx]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    period: str,
    *,
    client: Union[AuthenticatedClient, Client],
    employee_number: Union[Unset, int] = UNSET,
    accept: str = 'application/pdf',

) -> Response[Union[ErrorMessage, ErrorMessage5Xx]]:
    """ HR reports of one payroll period.

     Downloading HR reports of one payroll period for either all or one client's employee.

    Args:
        client_id (str):
        period (str):
        employee_number (Union[Unset, int]):
        accept (str):  Default: 'application/pdf'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
period=period,
employee_number=employee_number,
accept=accept,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    period: str,
    *,
    client: Union[AuthenticatedClient, Client],
    employee_number: Union[Unset, int] = UNSET,
    accept: str = 'application/pdf',

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx]]:
    """ HR reports of one payroll period.

     Downloading HR reports of one payroll period for either all or one client's employee.

    Args:
        client_id (str):
        period (str):
        employee_number (Union[Unset, int]):
        accept (str):  Default: 'application/pdf'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx]
     """


    return sync_detailed(
        client_id=client_id,
period=period,
client=client,
employee_number=employee_number,
accept=accept,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    period: str,
    *,
    client: Union[AuthenticatedClient, Client],
    employee_number: Union[Unset, int] = UNSET,
    accept: str = 'application/pdf',

) -> Response[Union[ErrorMessage, ErrorMessage5Xx]]:
    """ HR reports of one payroll period.

     Downloading HR reports of one payroll period for either all or one client's employee.

    Args:
        client_id (str):
        period (str):
        employee_number (Union[Unset, int]):
        accept (str):  Default: 'application/pdf'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
period=period,
employee_number=employee_number,
accept=accept,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    period: str,
    *,
    client: Union[AuthenticatedClient, Client],
    employee_number: Union[Unset, int] = UNSET,
    accept: str = 'application/pdf',

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx]]:
    """ HR reports of one payroll period.

     Downloading HR reports of one payroll period for either all or one client's employee.

    Args:
        client_id (str):
        period (str):
        employee_number (Union[Unset, int]):
        accept (str):  Default: 'application/pdf'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx]
     """


    return (await asyncio_detailed(
        client_id=client_id,
period=period,
client=client,
employee_number=employee_number,
accept=accept,

    )).parsed
