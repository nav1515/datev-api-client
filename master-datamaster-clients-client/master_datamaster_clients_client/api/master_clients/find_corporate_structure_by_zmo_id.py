from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.corporate_structure import CorporateStructure
from ...models.problem_details import ProblemDetails
from typing import cast
from uuid import UUID



def _get_kwargs(
    master_client_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/master-clients/{master_client_id}/corporate-structure".format(master_client_id=master_client_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[CorporateStructure, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = CorporateStructure.from_dict(response.json())



        return response_200
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[CorporateStructure, ProblemDetails]]:
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

) -> Response[Union[CorporateStructure, ProblemDetails]]:
    """ Retrieve a corporate structure for a specific master client.

     Returns a corporate structure for a specific master client which the user has access to.

    Args:
        master_client_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CorporateStructure, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        master_client_id=master_client_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    master_client_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[CorporateStructure, ProblemDetails]]:
    """ Retrieve a corporate structure for a specific master client.

     Returns a corporate structure for a specific master client which the user has access to.

    Args:
        master_client_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CorporateStructure, ProblemDetails]
     """


    return sync_detailed(
        master_client_id=master_client_id,
client=client,

    ).parsed

async def asyncio_detailed(
    master_client_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Response[Union[CorporateStructure, ProblemDetails]]:
    """ Retrieve a corporate structure for a specific master client.

     Returns a corporate structure for a specific master client which the user has access to.

    Args:
        master_client_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CorporateStructure, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        master_client_id=master_client_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    master_client_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[CorporateStructure, ProblemDetails]]:
    """ Retrieve a corporate structure for a specific master client.

     Returns a corporate structure for a specific master client which the user has access to.

    Args:
        master_client_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CorporateStructure, ProblemDetails]
     """


    return (await asyncio_detailed(
        master_client_id=master_client_id,
client=client,

    )).parsed
