from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem_details import ProblemDetails
from ...types import File, FileJsonType
from ...types import UNSET, Unset
from io import BytesIO
from typing import cast
from typing import Union



def _get_kwargs(
    client_id: str,
    *,
    body: File,
    filename: str,
    reference_id: Union[Unset, str] = UNSET,
    client_application_version: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Filename"] = filename

    if not isinstance(reference_id, Unset):
        headers["Reference-Id"] = reference_id

    if not isinstance(client_application_version, Unset):
        headers["Client-Application-Version"] = client_application_version



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/clients/{client_id}/extf-files/import".format(client_id=client_id,),
    }

    _body = body.payload

    _kwargs["content"] = _body
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 405:
        response_405 = ProblemDetails.from_dict(response.json())



        return response_405
    if response.status_code == 406:
        response_406 = ProblemDetails.from_dict(response.json())



        return response_406
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == 415:
        response_415 = ProblemDetails.from_dict(response.json())



        return response_415
    if response.status_code == 500:
        response_500 = ProblemDetails.from_dict(response.json())



        return response_500
    if response.status_code == 503:
        response_503 = cast(Any, None)
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
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    filename: str,
    reference_id: Union[Unset, str] = UNSET,
    client_application_version: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ProblemDetails]]:
    r""" Transfer a file to DATEV data center

     This endpoint accepts one file based on DATEV-Format type \"EXTF\".

    Args:
        client_id (str):
        filename (str):
        reference_id (Union[Unset, str]):
        client_application_version (Union[Unset, str]):
        body (File):  Example: file as binary stream.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
body=body,
filename=filename,
reference_id=reference_id,
client_application_version=client_application_version,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    filename: str,
    reference_id: Union[Unset, str] = UNSET,
    client_application_version: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ProblemDetails]]:
    r""" Transfer a file to DATEV data center

     This endpoint accepts one file based on DATEV-Format type \"EXTF\".

    Args:
        client_id (str):
        filename (str):
        reference_id (Union[Unset, str]):
        client_application_version (Union[Unset, str]):
        body (File):  Example: file as binary stream.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
     """


    return sync_detailed(
        client_id=client_id,
client=client,
body=body,
filename=filename,
reference_id=reference_id,
client_application_version=client_application_version,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    filename: str,
    reference_id: Union[Unset, str] = UNSET,
    client_application_version: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ProblemDetails]]:
    r""" Transfer a file to DATEV data center

     This endpoint accepts one file based on DATEV-Format type \"EXTF\".

    Args:
        client_id (str):
        filename (str):
        reference_id (Union[Unset, str]):
        client_application_version (Union[Unset, str]):
        body (File):  Example: file as binary stream.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
body=body,
filename=filename,
reference_id=reference_id,
client_application_version=client_application_version,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    filename: str,
    reference_id: Union[Unset, str] = UNSET,
    client_application_version: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ProblemDetails]]:
    r""" Transfer a file to DATEV data center

     This endpoint accepts one file based on DATEV-Format type \"EXTF\".

    Args:
        client_id (str):
        filename (str):
        reference_id (Union[Unset, str]):
        client_application_version (Union[Unset, str]):
        body (File):  Example: file as binary stream.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,
body=body,
filename=filename,
reference_id=reference_id,
client_application_version=client_application_version,

    )).parsed
