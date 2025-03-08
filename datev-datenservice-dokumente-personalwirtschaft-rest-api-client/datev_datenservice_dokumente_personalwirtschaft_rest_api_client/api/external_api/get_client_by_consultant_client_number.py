from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.client import Client
from ...models.error_message import ErrorMessage
from typing import cast



def _get_kwargs(
    consultantnumber_clientnumber: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{consultantnumber_clientnumber}".format(consultantnumber_clientnumber=consultantnumber_clientnumber,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, Client, ErrorMessage]]:
    if response.status_code == 200:
        response_200 = Client.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())



        return response_403
    if response.status_code == 404:
        response_404 = ErrorMessage.from_dict(response.json())



        return response_404
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == 500:
        response_500 = ErrorMessage.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, Client, ErrorMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    consultantnumber_clientnumber: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, Client, ErrorMessage]]:
    """ Gets the client specified by consultant number and client number. This operation supports the usage
    of long time authentication tokens.

    Args:
        consultantnumber_clientnumber (str): Consultant and client number separated by a hyphen.
            Example: 402248-17100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Client, ErrorMessage]]
     """


    kwargs = _get_kwargs(
        consultantnumber_clientnumber=consultantnumber_clientnumber,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    consultantnumber_clientnumber: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, Client, ErrorMessage]]:
    """ Gets the client specified by consultant number and client number. This operation supports the usage
    of long time authentication tokens.

    Args:
        consultantnumber_clientnumber (str): Consultant and client number separated by a hyphen.
            Example: 402248-17100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Client, ErrorMessage]
     """


    return sync_detailed(
        consultantnumber_clientnumber=consultantnumber_clientnumber,
client=client,

    ).parsed

async def asyncio_detailed(
    consultantnumber_clientnumber: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, Client, ErrorMessage]]:
    """ Gets the client specified by consultant number and client number. This operation supports the usage
    of long time authentication tokens.

    Args:
        consultantnumber_clientnumber (str): Consultant and client number separated by a hyphen.
            Example: 402248-17100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Client, ErrorMessage]]
     """


    kwargs = _get_kwargs(
        consultantnumber_clientnumber=consultantnumber_clientnumber,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    consultantnumber_clientnumber: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, Client, ErrorMessage]]:
    """ Gets the client specified by consultant number and client number. This operation supports the usage
    of long time authentication tokens.

    Args:
        consultantnumber_clientnumber (str): Consultant and client number separated by a hyphen.
            Example: 402248-17100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Client, ErrorMessage]
     """


    return (await asyncio_detailed(
        consultantnumber_clientnumber=consultantnumber_clientnumber,
client=client,

    )).parsed
