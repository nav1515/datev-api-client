from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.forbidden_problem_details import ForbiddenProblemDetails
from ...models.log_model import LogModel
from ...models.not_found_problem_details import NotFoundProblemDetails
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    id: int,
    *,
    select: Union[Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key



    

    params: dict[str, Any] = {}

    params["$select"] = select


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Logs/{id}".format(id=id,),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]]:
    if response.status_code == 200:
        response_200 = LogModel.from_dict(response.json())



        return response_200
    if response.status_code == 403:
        response_403 = ForbiddenProblemDetails.from_dict(response.json())



        return response_403
    if response.status_code == 404:
        response_404 = NotFoundProblemDetails.from_dict(response.json())



        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    select: Union[Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]]:
    """ Gets a single log by id.

    Args:
        id (int):
        select (Union[Unset, str]): Limits the properties returned in the result.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]]
     """


    kwargs = _get_kwargs(
        id=id,
select=select,
x_api_key=x_api_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    select: Union[Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]]:
    """ Gets a single log by id.

    Args:
        id (int):
        select (Union[Unset, str]): Limits the properties returned in the result.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]
     """


    return sync_detailed(
        id=id,
client=client,
select=select,
x_api_key=x_api_key,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    select: Union[Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]]:
    """ Gets a single log by id.

    Args:
        id (int):
        select (Union[Unset, str]): Limits the properties returned in the result.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]]
     """


    kwargs = _get_kwargs(
        id=id,
select=select,
x_api_key=x_api_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    select: Union[Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]]:
    """ Gets a single log by id.

    Args:
        id (int):
        select (Union[Unset, str]): Limits the properties returned in the result.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ForbiddenProblemDetails, LogModel, NotFoundProblemDetails]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
select=select,
x_api_key=x_api_key,

    )).parsed
