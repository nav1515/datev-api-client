from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.master_client_full import MasterClientFull
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from typing import Union
from uuid import UUID



def _get_kwargs(
    master_client_id: UUID,
    *,
    expand: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["if-none-match"] = if_none_match



    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/master-clients/{master_client_id}/consultant-client".format(master_client_id=master_client_id,),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, MasterClientFull, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = MasterClientFull.from_dict(response.json())



        return response_200
    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304
    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404
    if response.status_code == 500:
        response_500 = ProblemDetails.from_dict(response.json())



        return response_500
    if response.status_code == 502:
        response_502 = ProblemDetails.from_dict(response.json())



        return response_502
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, MasterClientFull, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    master_client_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,

) -> Response[Union[Any, MasterClientFull, ProblemDetails]]:
    """ Retrieve the consultant client for a specific master client.

     Returns the consultant client for a specific master client. The user must have access to the master
    client as well as the consultant client. The consultant client is retrieved by resolving the
    assigned establishment of the master client. If a consultant client is assigned to the
    establishment, the consultant client is returned. Otherwise, the consultant client of the
    organization containing the establishment is returned, or, if neither is present, nothing is
    returned.

    Args:
        master_client_id (UUID):
        expand (Union[Unset, str]):
        if_none_match (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MasterClientFull, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        master_client_id=master_client_id,
expand=expand,
if_none_match=if_none_match,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    master_client_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, MasterClientFull, ProblemDetails]]:
    """ Retrieve the consultant client for a specific master client.

     Returns the consultant client for a specific master client. The user must have access to the master
    client as well as the consultant client. The consultant client is retrieved by resolving the
    assigned establishment of the master client. If a consultant client is assigned to the
    establishment, the consultant client is returned. Otherwise, the consultant client of the
    organization containing the establishment is returned, or, if neither is present, nothing is
    returned.

    Args:
        master_client_id (UUID):
        expand (Union[Unset, str]):
        if_none_match (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MasterClientFull, ProblemDetails]
     """


    return sync_detailed(
        master_client_id=master_client_id,
client=client,
expand=expand,
if_none_match=if_none_match,

    ).parsed

async def asyncio_detailed(
    master_client_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,

) -> Response[Union[Any, MasterClientFull, ProblemDetails]]:
    """ Retrieve the consultant client for a specific master client.

     Returns the consultant client for a specific master client. The user must have access to the master
    client as well as the consultant client. The consultant client is retrieved by resolving the
    assigned establishment of the master client. If a consultant client is assigned to the
    establishment, the consultant client is returned. Otherwise, the consultant client of the
    organization containing the establishment is returned, or, if neither is present, nothing is
    returned.

    Args:
        master_client_id (UUID):
        expand (Union[Unset, str]):
        if_none_match (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MasterClientFull, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        master_client_id=master_client_id,
expand=expand,
if_none_match=if_none_match,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    master_client_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, str] = UNSET,
    if_none_match: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, MasterClientFull, ProblemDetails]]:
    """ Retrieve the consultant client for a specific master client.

     Returns the consultant client for a specific master client. The user must have access to the master
    client as well as the consultant client. The consultant client is retrieved by resolving the
    assigned establishment of the master client. If a consultant client is assigned to the
    establishment, the consultant client is returned. Otherwise, the consultant client of the
    organization containing the establishment is returned, or, if neither is present, nothing is
    returned.

    Args:
        master_client_id (UUID):
        expand (Union[Unset, str]):
        if_none_match (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MasterClientFull, ProblemDetails]
     """


    return (await asyncio_detailed(
        master_client_id=master_client_id,
client=client,
expand=expand,
if_none_match=if_none_match,

    )).parsed
