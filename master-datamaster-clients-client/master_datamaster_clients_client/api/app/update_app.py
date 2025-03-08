from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.app_update import AppUpdate
from ...models.problem_details import ProblemDetails
from typing import cast



def _get_kwargs(
    *,
    body: AppUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/apps",
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 500:
        response_500 = ProblemDetails.from_dict(response.json())



        return response_500
    if response.status_code == 503:
        response_503 = ProblemDetails.from_dict(response.json())



        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AppUpdate,

) -> Response[Union[Any, ProblemDetails]]:
    """ Update meta data about API consumer access, e.g. the schema of the returned master clients (contexts
    & bricks). Currently only available in sandbox.

    Args:
        body (AppUpdate): Data to set for the API Consumer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: AppUpdate,

) -> Optional[Union[Any, ProblemDetails]]:
    """ Update meta data about API consumer access, e.g. the schema of the returned master clients (contexts
    & bricks). Currently only available in sandbox.

    Args:
        body (AppUpdate): Data to set for the API Consumer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AppUpdate,

) -> Response[Union[Any, ProblemDetails]]:
    """ Update meta data about API consumer access, e.g. the schema of the returned master clients (contexts
    & bricks). Currently only available in sandbox.

    Args:
        body (AppUpdate): Data to set for the API Consumer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AppUpdate,

) -> Optional[Union[Any, ProblemDetails]]:
    """ Update meta data about API consumer access, e.g. the schema of the returned master clients (contexts
    & bricks). Currently only available in sandbox.

    Args:
        body (AppUpdate): Data to set for the API Consumer.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
