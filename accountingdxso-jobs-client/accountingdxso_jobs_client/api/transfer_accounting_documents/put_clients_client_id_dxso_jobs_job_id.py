from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ready import Ready
from typing import cast



def _get_kwargs(
    client_id: str,
    job_id: str,
    *,
    body: Ready,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/clients/{client_id}/dxso-jobs/{job_id}".format(client_id=client_id,job_id=job_id,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/merge-patch+json"

    _kwargs["headers"] = headers
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
    body: Ready,

) -> Response[Any]:
    r""" Finalizes the data transfer (dxso-job). After this step, the data execution starts in the DATEV
    applications.

     \"The next step after the attachment of all files to a data transfer (dxso-job) is the finalization
    of the data transfer (dxso-job). Then, the execution of the data starts in DATEV Unternehmen online.

    **Note:** The \\"content type\\" header must be \\"application/merge-patch+json\\".\"

    Args:
        client_id (str):
        job_id (str):
        body (Ready):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,
body=body,

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
    body: Ready,

) -> Response[Any]:
    r""" Finalizes the data transfer (dxso-job). After this step, the data execution starts in the DATEV
    applications.

     \"The next step after the attachment of all files to a data transfer (dxso-job) is the finalization
    of the data transfer (dxso-job). Then, the execution of the data starts in DATEV Unternehmen online.

    **Note:** The \\"content type\\" header must be \\"application/merge-patch+json\\".\"

    Args:
        client_id (str):
        job_id (str):
        body (Ready):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

