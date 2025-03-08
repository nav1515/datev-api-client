from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.inbox_document_model_i_enumerable_o_data_value import InboxDocumentModelIEnumerableODataValue
from ...types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union



def _get_kwargs(
    *,
    body: Union[
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Documents/CommitInboxDownload",
    }

    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=minimal;odata.streaming=true"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=minimal;odata.streaming=false"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=minimal"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=full;odata.streaming=true"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=full;odata.streaming=false"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=full"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=none;odata.streaming=true"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=none;odata.streaming=false"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=none"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.streaming=true"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.streaming=false"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json; odata.metadata=full; odata.streaming=true"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, Union[None, list[int]]):
        _json_body: Union[None, list[int]]
        if isinstance(body, list):
            _json_body = body


        else:
            _json_body = body


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

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
    body: Union[
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[InboxDocumentModelIEnumerableODataValue]:
    """ Commits the given documents for inbox download.

    Args:
        x_api_key (Union[Unset, str]):
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InboxDocumentModelIEnumerableODataValue]
     """


    kwargs = _get_kwargs(
        body=body,
x_api_key=x_api_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[InboxDocumentModelIEnumerableODataValue]:
    """ Commits the given documents for inbox download.

    Args:
        x_api_key (Union[Unset, str]):
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InboxDocumentModelIEnumerableODataValue
     """


    return sync_detailed(
        client=client,
body=body,
x_api_key=x_api_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[InboxDocumentModelIEnumerableODataValue]:
    """ Commits the given documents for inbox download.

    Args:
        x_api_key (Union[Unset, str]):
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InboxDocumentModelIEnumerableODataValue]
     """


    kwargs = _get_kwargs(
        body=body,
x_api_key=x_api_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
        Union[None, list[int]],
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[InboxDocumentModelIEnumerableODataValue]:
    """ Commits the given documents for inbox download.

    Args:
        x_api_key (Union[Unset, str]):
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.
        body (Union[None, list[int]]): The document ids.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InboxDocumentModelIEnumerableODataValue
     """


    return (await asyncio_detailed(
        client=client,
body=body,
x_api_key=x_api_key,

    )).parsed
