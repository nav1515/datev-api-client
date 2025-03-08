from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_message import ErrorMessage
from ...models.error_message_5_xx import ErrorMessage5Xx
from ...models.job_info import JobInfo
from ...models.post_v1_clients_client_id_files_body import PostV1ClientsClientIdFilesBody
from typing import cast



def _get_kwargs(
    client_id: str,
    *,
    body: PostV1ClientsClientIdFilesBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/clients/{client_id}/files".format(client_id=client_id,),
    }

    _body = body.to_multipart()


    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    if response.status_code == 201:
        response_201 = JobInfo.from_dict(response.json())



        return response_201
    if response.status_code == 400:
        response_400 = ErrorMessage.from_dict(response.json())



        return response_400
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
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
    body: PostV1ClientsClientIdFilesBody,

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    """ Adds a file with its file information

     A file can be sent with its file information (required parameters). It can then be processed in the
    payroll system.

    Args:
        client_id (str):
        body (PostV1ClientsClientIdFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostV1ClientsClientIdFilesBody,

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    """ Adds a file with its file information

     A file can be sent with its file information (required parameters). It can then be processed in the
    payroll system.

    Args:
        client_id (str):
        body (PostV1ClientsClientIdFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, JobInfo]
     """


    return sync_detailed(
        client_id=client_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostV1ClientsClientIdFilesBody,

) -> Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    """ Adds a file with its file information

     A file can be sent with its file information (required parameters). It can then be processed in the
    payroll system.

    Args:
        client_id (str):
        body (PostV1ClientsClientIdFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostV1ClientsClientIdFilesBody,

) -> Optional[Union[ErrorMessage, ErrorMessage5Xx, JobInfo]]:
    """ Adds a file with its file information

     A file can be sent with its file information (required parameters). It can then be processed in the
    payroll system.

    Args:
        client_id (str):
        body (PostV1ClientsClientIdFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorMessage, ErrorMessage5Xx, JobInfo]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,
body=body,

    )).parsed
