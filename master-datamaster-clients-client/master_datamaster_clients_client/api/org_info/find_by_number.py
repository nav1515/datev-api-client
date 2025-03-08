from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.data_environment import DataEnvironment
from ...models.find_by_number_expand import FindByNumberExpand
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    number: int,
    *,
    expand: Union[Unset, FindByNumberExpand] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_expand: Union[Unset, str] = UNSET
    if not isinstance(expand, Unset):
        json_expand = expand.value

    params["expand"] = json_expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/data-environments/{number}".format(number=number,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[DataEnvironment, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = DataEnvironment.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[DataEnvironment, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    number: int,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, FindByNumberExpand] = UNSET,

) -> Response[Union[DataEnvironment, ProblemDetails]]:
    """ Returns a data environment.

     Returns a specific data environment which the user has access to.

    Args:
        number (int):
        expand (Union[Unset, FindByNumberExpand]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataEnvironment, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        number=number,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    number: int,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, FindByNumberExpand] = UNSET,

) -> Optional[Union[DataEnvironment, ProblemDetails]]:
    """ Returns a data environment.

     Returns a specific data environment which the user has access to.

    Args:
        number (int):
        expand (Union[Unset, FindByNumberExpand]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataEnvironment, ProblemDetails]
     """


    return sync_detailed(
        number=number,
client=client,
expand=expand,

    ).parsed

async def asyncio_detailed(
    number: int,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, FindByNumberExpand] = UNSET,

) -> Response[Union[DataEnvironment, ProblemDetails]]:
    """ Returns a data environment.

     Returns a specific data environment which the user has access to.

    Args:
        number (int):
        expand (Union[Unset, FindByNumberExpand]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataEnvironment, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        number=number,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    number: int,
    *,
    client: AuthenticatedClient,
    expand: Union[Unset, FindByNumberExpand] = UNSET,

) -> Optional[Union[DataEnvironment, ProblemDetails]]:
    """ Returns a data environment.

     Returns a specific data environment which the user has access to.

    Args:
        number (int):
        expand (Union[Unset, FindByNumberExpand]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataEnvironment, ProblemDetails]
     """


    return (await asyncio_detailed(
        number=number,
client=client,
expand=expand,

    )).parsed
