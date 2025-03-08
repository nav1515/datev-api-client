from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.serbia_document_model import SerbiaDocumentModel
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime



def _get_kwargs(
    *,
    modified: Union[None, Unset, datetime.datetime] = UNSET,
    match_field: Union[None, Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key



    

    params: dict[str, Any] = {}

    json_modified: Union[None, Unset, str]
    if isinstance(modified, Unset):
        json_modified = UNSET
    elif isinstance(modified, datetime.datetime):
        json_modified = modified.isoformat()
    else:
        json_modified = modified
    params["modified"] = json_modified

    json_match_field: Union[None, Unset, str]
    if isinstance(match_field, Unset):
        json_match_field = UNSET
    else:
        json_match_field = match_field
    params["matchField"] = json_match_field


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Gov/Serbia/Documents/Received",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[list['SerbiaDocumentModel']]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = SerbiaDocumentModel.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list['SerbiaDocumentModel']]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    modified: Union[None, Unset, datetime.datetime] = UNSET,
    match_field: Union[None, Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[list['SerbiaDocumentModel']]:
    """ Returns the received documents.

    Args:
        modified (Union[None, Unset, datetime.datetime]):
        match_field (Union[None, Unset, str]):
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['SerbiaDocumentModel']]
     """


    kwargs = _get_kwargs(
        modified=modified,
match_field=match_field,
x_api_key=x_api_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    modified: Union[None, Unset, datetime.datetime] = UNSET,
    match_field: Union[None, Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[list['SerbiaDocumentModel']]:
    """ Returns the received documents.

    Args:
        modified (Union[None, Unset, datetime.datetime]):
        match_field (Union[None, Unset, str]):
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['SerbiaDocumentModel']
     """


    return sync_detailed(
        client=client,
modified=modified,
match_field=match_field,
x_api_key=x_api_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    modified: Union[None, Unset, datetime.datetime] = UNSET,
    match_field: Union[None, Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[list['SerbiaDocumentModel']]:
    """ Returns the received documents.

    Args:
        modified (Union[None, Unset, datetime.datetime]):
        match_field (Union[None, Unset, str]):
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['SerbiaDocumentModel']]
     """


    kwargs = _get_kwargs(
        modified=modified,
match_field=match_field,
x_api_key=x_api_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    modified: Union[None, Unset, datetime.datetime] = UNSET,
    match_field: Union[None, Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[list['SerbiaDocumentModel']]:
    """ Returns the received documents.

    Args:
        modified (Union[None, Unset, datetime.datetime]):
        match_field (Union[None, Unset, str]):
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['SerbiaDocumentModel']
     """


    return (await asyncio_detailed(
        client=client,
modified=modified,
match_field=match_field,
x_api_key=x_api_key,

    )).parsed
