from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_message import ErrorMessage
from ...models.error_message_5_xx import ErrorMessage5Xx
from ...models.job_info import JobInfo
from typing import cast



def _get_kwargs(
    client_id: str,
    job_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/clients/{client_id}/jobs/{job_id}".format(client_id=client_id,job_id=job_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    if response.status_code == 200:
        response_200 = JobInfo.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    """ get the file's state

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    """ get the file's state

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, JobInfo]
     """


    return sync_detailed(
        client_id=client_id,
job_id=job_id,
client=client,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    """ get the file's state

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    """ get the file's state

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, JobInfo]
     """


    return (await asyncio_detailed(
        client_id=client_id,
job_id=job_id,
client=client,

    )).parsed
