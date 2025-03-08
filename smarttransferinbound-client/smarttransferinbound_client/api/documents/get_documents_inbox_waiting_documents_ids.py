from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.inbox_document_model_i_enumerable_o_data_value import InboxDocumentModelIEnumerableODataValue
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    x_api_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Documents/Inbox/WaitingDocuments/Ids",
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[InboxDocumentModelIEnumerableODataValue]:
    if response.status_code == 200:
        response_200 = InboxDocumentModelIEnumerableODataValue.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[InboxDocumentModelIEnumerableODataValue]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[InboxDocumentModelIEnumerableODataValue]:
    """ Gets the Ids of waiting documents in inbox.

    Args:
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InboxDocumentModelIEnumerableODataValue]
     """


    kwargs = _get_kwargs(
        x_api_key=x_api_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[InboxDocumentModelIEnumerableODataValue]:
    """ Gets the Ids of waiting documents in inbox.

    Args:
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InboxDocumentModelIEnumerableODataValue
     """


    return sync_detailed(
        client=client,
x_api_key=x_api_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[InboxDocumentModelIEnumerableODataValue]:
    """ Gets the Ids of waiting documents in inbox.

    Args:
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InboxDocumentModelIEnumerableODataValue]
     """


    kwargs = _get_kwargs(
        x_api_key=x_api_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[InboxDocumentModelIEnumerableODataValue]:
    """ Gets the Ids of waiting documents in inbox.

    Args:
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InboxDocumentModelIEnumerableODataValue
     """


    return (await asyncio_detailed(
        client=client,
x_api_key=x_api_key,

    )).parsed
