from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.document_metadata_dto import DocumentMetadataDto
from ...models.error_message import ErrorMessage
from ...models.error_message_5_xx import ErrorMessage5Xx
from ...models.get_document_metadata_document_types import GetDocumentMetadataDocumentTypes
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    client_id: str,
    *,
    document_types: GetDocumentMetadataDocumentTypes,
    period: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_document_types = document_types.value
    params["document_types"] = json_document_types

    params["period"] = period

    params["timestamp"] = timestamp


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}/documents-metadata".format(client_id=client_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]]:
    if response.status_code == 200:
        response_200 = DocumentMetadataDto.from_dict(response.json())



        return response_200
    if response.status_code == 400:
        response_400 = ErrorMessage.from_dict(response.json())



        return response_400
    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())



        return response_401
    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())



        return response_403
    if response.status_code == 500:
        response_500 = ErrorMessage5Xx.from_dict(response.json())



        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    document_types: GetDocumentMetadataDocumentTypes,
    period: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,

) -> Response[Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]]:
    """ List of metadata for all available documents.

     Returns the  metadata (document types, period, timestamp) for all available documents. At least one
    of the query parameters 'period' or 'timestamp' have to be set, both are also possible.

    Args:
        client_id (str):
        document_types (GetDocumentMetadataDocumentTypes):
        period (Union[Unset, str]):
        timestamp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
document_types=document_types,
period=period,
timestamp=timestamp,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    document_types: GetDocumentMetadataDocumentTypes,
    period: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,

) -> Optional[Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]]:
    """ List of metadata for all available documents.

     Returns the  metadata (document types, period, timestamp) for all available documents. At least one
    of the query parameters 'period' or 'timestamp' have to be set, both are also possible.

    Args:
        client_id (str):
        document_types (GetDocumentMetadataDocumentTypes):
        period (Union[Unset, str]):
        timestamp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]
     """


    return sync_detailed(
        client_id=client_id,
client=client,
document_types=document_types,
period=period,
timestamp=timestamp,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    document_types: GetDocumentMetadataDocumentTypes,
    period: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,

) -> Response[Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]]:
    """ List of metadata for all available documents.

     Returns the  metadata (document types, period, timestamp) for all available documents. At least one
    of the query parameters 'period' or 'timestamp' have to be set, both are also possible.

    Args:
        client_id (str):
        document_types (GetDocumentMetadataDocumentTypes):
        period (Union[Unset, str]):
        timestamp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
document_types=document_types,
period=period,
timestamp=timestamp,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    document_types: GetDocumentMetadataDocumentTypes,
    period: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,

) -> Optional[Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]]:
    """ List of metadata for all available documents.

     Returns the  metadata (document types, period, timestamp) for all available documents. At least one
    of the query parameters 'period' or 'timestamp' have to be set, both are also possible.

    Args:
        client_id (str):
        document_types (GetDocumentMetadataDocumentTypes):
        period (Union[Unset, str]):
        timestamp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DocumentMetadataDto, ErrorMessage, ErrorMessage5Xx]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,
document_types=document_types,
period=period,
timestamp=timestamp,

    )).parsed
