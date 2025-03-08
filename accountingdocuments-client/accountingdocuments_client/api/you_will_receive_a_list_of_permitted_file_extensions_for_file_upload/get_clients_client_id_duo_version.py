from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.duo_version import DuoVersion
from typing import cast



def _get_kwargs(
    client_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}/duo-version".format(client_id=client_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, list['DuoVersion']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = DuoVersion.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, list['DuoVersion']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, list['DuoVersion']]]:
    """ Returns a list of permitted file extensions for file upload

     Returns a list of permitted file extensions for file upload for a given client. The content of the
    list depends on the Datev-status of the client. There is a difference between DuoNext and DuoNow.
    For details please look at the example.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['DuoVersion']]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, list['DuoVersion']]]:
    """ Returns a list of permitted file extensions for file upload

     Returns a list of permitted file extensions for file upload for a given client. The content of the
    list depends on the Datev-status of the client. There is a difference between DuoNext and DuoNow.
    For details please look at the example.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['DuoVersion']]
     """


    return sync_detailed(
        client_id=client_id,
client=client,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, list['DuoVersion']]]:
    """ Returns a list of permitted file extensions for file upload

     Returns a list of permitted file extensions for file upload for a given client. The content of the
    list depends on the Datev-status of the client. There is a difference between DuoNext and DuoNow.
    For details please look at the example.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['DuoVersion']]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, list['DuoVersion']]]:
    """ Returns a list of permitted file extensions for file upload

     Returns a list of permitted file extensions for file upload for a given client. The content of the
    list depends on the Datev-status of the client. There is a difference between DuoNext and DuoNow.
    For details please look at the example.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['DuoVersion']]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,

    )).parsed
