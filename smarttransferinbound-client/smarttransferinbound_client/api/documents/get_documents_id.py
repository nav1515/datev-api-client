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
    id: int,
    *,
    type_: Union[None, Unset, str] = 'pdf',
    x_api_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key



    

    params: dict[str, Any] = {}

    json_type_: Union[None, Unset, str]
    if isinstance(type_, Unset):
        json_type_ = UNSET
    else:
        json_type_ = type_
    params["type"] = json_type_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Documents/{id}".format(id=id,),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, InboxDocumentModelIEnumerableODataValue]]:
    if response.status_code == 200:
        response_200 = InboxDocumentModelIEnumerableODataValue.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, InboxDocumentModelIEnumerableODataValue]]:
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
    type_: Union[None, Unset, str] = 'pdf',
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[Union[Any, InboxDocumentModelIEnumerableODataValue]]:
    """ Gets the document.

    Args:
        id (int): The document identifier.
        type_ (Union[None, Unset, str]): The type. Default: 'pdf'.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InboxDocumentModelIEnumerableODataValue]]
     """


    kwargs = _get_kwargs(
        id=id,
type_=type_,
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
    type_: Union[None, Unset, str] = 'pdf',
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, InboxDocumentModelIEnumerableODataValue]]:
    """ Gets the document.

    Args:
        id (int): The document identifier.
        type_ (Union[None, Unset, str]): The type. Default: 'pdf'.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, InboxDocumentModelIEnumerableODataValue]
     """


    return sync_detailed(
        id=id,
client=client,
type_=type_,
x_api_key=x_api_key,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[None, Unset, str] = 'pdf',
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[Union[Any, InboxDocumentModelIEnumerableODataValue]]:
    """ Gets the document.

    Args:
        id (int): The document identifier.
        type_ (Union[None, Unset, str]): The type. Default: 'pdf'.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, InboxDocumentModelIEnumerableODataValue]]
     """


    kwargs = _get_kwargs(
        id=id,
type_=type_,
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
    type_: Union[None, Unset, str] = 'pdf',
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, InboxDocumentModelIEnumerableODataValue]]:
    """ Gets the document.

    Args:
        id (int): The document identifier.
        type_ (Union[None, Unset, str]): The type. Default: 'pdf'.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, InboxDocumentModelIEnumerableODataValue]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
type_=type_,
x_api_key=x_api_key,

    )).parsed
