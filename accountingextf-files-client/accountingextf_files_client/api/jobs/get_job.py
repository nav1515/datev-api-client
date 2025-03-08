from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.job import Job
from ...models.problem_details import ProblemDetails
from typing import cast



def _get_kwargs(
    client_id: str,
    job_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}/extf-files/jobs/{job_id}".format(client_id=client_id,job_id=job_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, Job, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = Job.from_dict(response.json())



        return response_200
    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



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
    if response.status_code == 500:
        response_500 = ProblemDetails.from_dict(response.json())



        return response_500
    if response.status_code == 503:
        response_503 = ProblemDetails.from_dict(response.json())



        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, Job, ProblemDetails]]:
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
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, Job, ProblemDetails]]:
    """ Retrieves state of a designated job.

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Job, ProblemDetails]]
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
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, Job, ProblemDetails]]:
    """ Retrieves state of a designated job.

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Job, ProblemDetails]
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
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, Job, ProblemDetails]]:
    """ Retrieves state of a designated job.

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Job, ProblemDetails]]
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
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, Job, ProblemDetails]]:
    """ Retrieves state of a designated job.

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Job, ProblemDetails]
     """


    return (await asyncio_detailed(
        client_id=client_id,
job_id=job_id,
client=client,

    )).parsed
