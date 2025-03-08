from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.master_client_full import MasterClientFull
from ...models.problem_details import ProblemDetails
from ...models.search import Search
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: Search,
    expand: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/master-clients/search",
        "params": params,
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ProblemDetails, list['MasterClientFull']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = MasterClientFull.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ProblemDetails, list['MasterClientFull']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Search,
    expand: Union[Unset, str] = UNSET,

) -> Response[Union[ProblemDetails, list['MasterClientFull']]]:
    """ Returns a list of master clients. Provides extended search abilities.

     Returns a list of all master clients that can be accessed by the user. Extended search parameters
    can be provided in the request body.

    Args:
        expand (Union[Unset, str]):
        body (Search): The extended search parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, list['MasterClientFull']]]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: Search,
    expand: Union[Unset, str] = UNSET,

) -> Optional[Union[ProblemDetails, list['MasterClientFull']]]:
    """ Returns a list of master clients. Provides extended search abilities.

     Returns a list of all master clients that can be accessed by the user. Extended search parameters
    can be provided in the request body.

    Args:
        expand (Union[Unset, str]):
        body (Search): The extended search parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, list['MasterClientFull']]
     """


    return sync_detailed(
        client=client,
body=body,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Search,
    expand: Union[Unset, str] = UNSET,

) -> Response[Union[ProblemDetails, list['MasterClientFull']]]:
    """ Returns a list of master clients. Provides extended search abilities.

     Returns a list of all master clients that can be accessed by the user. Extended search parameters
    can be provided in the request body.

    Args:
        expand (Union[Unset, str]):
        body (Search): The extended search parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, list['MasterClientFull']]]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Search,
    expand: Union[Unset, str] = UNSET,

) -> Optional[Union[ProblemDetails, list['MasterClientFull']]]:
    """ Returns a list of master clients. Provides extended search abilities.

     Returns a list of all master clients that can be accessed by the user. Extended search parameters
    can be provided in the request body.

    Args:
        expand (Union[Unset, str]):
        body (Search): The extended search parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, list['MasterClientFull']]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
expand=expand,

    )).parsed
