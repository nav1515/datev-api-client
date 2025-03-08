from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dx_so_job_status import DXSoJobStatus
from typing import cast



def _get_kwargs(
    client_id: str,
    job_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}/dxso-jobs/{job_id}".format(client_id=client_id,job_id=job_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, DXSoJobStatus]]:
    if response.status_code == 200:
        response_200 = DXSoJobStatus.from_dict(response.json())



        return response_200
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, DXSoJobStatus]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, DXSoJobStatus]]:
    r""" Returns the status of a data transfer (dxso-job).

     The processing of a data transfer (dxso-job) has different stages. The third-party solution has to
    check the status of a data transfer (dxso-job) and has to provide the information to the user, as
    this information is not available permanently in DATEV Unternehmen online. The status is a part of
    the protocol entries in DATEV Unternehmen online that are kept only a limited time (about two
    months).

    **Note:** Data transfers (dxso-jobs) are processed asynchronously.

    **Example: The data transfer has been processed partially:**
    ```json
    HTTP/1.1 200 OK
    Content-Encoding: gzip
    Transfer-Encoding:chunked

    {
    \"id\":<id>,
    \"status\":4
    }

    ```

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DXSoJobStatus]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, DXSoJobStatus]]:
    r""" Returns the status of a data transfer (dxso-job).

     The processing of a data transfer (dxso-job) has different stages. The third-party solution has to
    check the status of a data transfer (dxso-job) and has to provide the information to the user, as
    this information is not available permanently in DATEV Unternehmen online. The status is a part of
    the protocol entries in DATEV Unternehmen online that are kept only a limited time (about two
    months).

    **Note:** Data transfers (dxso-jobs) are processed asynchronously.

    **Example: The data transfer has been processed partially:**
    ```json
    HTTP/1.1 200 OK
    Content-Encoding: gzip
    Transfer-Encoding:chunked

    {
    \"id\":<id>,
    \"status\":4
    }

    ```

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DXSoJobStatus]
     """


    return sync_detailed(
        client_id=client_id,
job_id=job_id,
client=client,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, DXSoJobStatus]]:
    r""" Returns the status of a data transfer (dxso-job).

     The processing of a data transfer (dxso-job) has different stages. The third-party solution has to
    check the status of a data transfer (dxso-job) and has to provide the information to the user, as
    this information is not available permanently in DATEV Unternehmen online. The status is a part of
    the protocol entries in DATEV Unternehmen online that are kept only a limited time (about two
    months).

    **Note:** Data transfers (dxso-jobs) are processed asynchronously.

    **Example: The data transfer has been processed partially:**
    ```json
    HTTP/1.1 200 OK
    Content-Encoding: gzip
    Transfer-Encoding:chunked

    {
    \"id\":<id>,
    \"status\":4
    }

    ```

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DXSoJobStatus]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, DXSoJobStatus]]:
    r""" Returns the status of a data transfer (dxso-job).

     The processing of a data transfer (dxso-job) has different stages. The third-party solution has to
    check the status of a data transfer (dxso-job) and has to provide the information to the user, as
    this information is not available permanently in DATEV Unternehmen online. The status is a part of
    the protocol entries in DATEV Unternehmen online that are kept only a limited time (about two
    months).

    **Note:** Data transfers (dxso-jobs) are processed asynchronously.

    **Example: The data transfer has been processed partially:**
    ```json
    HTTP/1.1 200 OK
    Content-Encoding: gzip
    Transfer-Encoding:chunked

    {
    \"id\":<id>,
    \"status\":4
    }

    ```

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DXSoJobStatus]
     """


    return (await asyncio_detailed(
        client_id=client_id,
job_id=job_id,
client=client,

    )).parsed
