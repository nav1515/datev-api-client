from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    client_id: str,
    job_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/clients/{client_id}/dxso-jobs/{job_id}".format(client_id=client_id,job_id=job_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 503:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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

) -> Response[Any]:
    """ Cancels a data transfer (dxso-job) that has not been finalized yet.

     A data transfer (dxso-job) can be cancelled. This is only possible as long as the data transfer
    (dxso-job) has not been finalized. A data transfer (dxso-job) that has not yet been finalized has
    the status 0. All data concerning the cancelled data transfer (dxso-job) is deleted after
    cancellation.

    After deleting a data transfer (dxso-job), no file uploads and no protocol entry requests are
    possible because all data and protocol entries have been removed for this data transfer (dxso-job).

    Possible reasons for the cancellation of a data transfer (dxso-job):

    - The information returned after creating a data transfer (dxso-job) is not suitable for the
    configuration of the third-party solution.
    - The validation of the data in accordance to the DATEV XML-Schnittstelle online has returned an
    error.
    - The user has cancelled the data transfer (dxso-job).

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    client_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any]:
    """ Cancels a data transfer (dxso-job) that has not been finalized yet.

     A data transfer (dxso-job) can be cancelled. This is only possible as long as the data transfer
    (dxso-job) has not been finalized. A data transfer (dxso-job) that has not yet been finalized has
    the status 0. All data concerning the cancelled data transfer (dxso-job) is deleted after
    cancellation.

    After deleting a data transfer (dxso-job), no file uploads and no protocol entry requests are
    possible because all data and protocol entries have been removed for this data transfer (dxso-job).

    Possible reasons for the cancellation of a data transfer (dxso-job):

    - The information returned after creating a data transfer (dxso-job) is not suitable for the
    configuration of the third-party solution.
    - The validation of the data in accordance to the DATEV XML-Schnittstelle online has returned an
    error.
    - The user has cancelled the data transfer (dxso-job).

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

