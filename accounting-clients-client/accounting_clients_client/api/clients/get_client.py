from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.client import Client
from ...models.problem_details import ProblemDetails
from typing import cast



def _get_kwargs(
    client_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}".format(client_id=client_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, Client, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = Client.from_dict(response.json())



        return response_200
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, Client, ProblemDetails]]:
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

) -> Response[Union[Any, Client, ProblemDetails]]:
    """ Retrieve a specific client.

     Returns a specific client which the user has access to. In addition, this item also provides the
    available services for data transfer to the DATEV data center. The client ID is a technical object
    for the communication between the third-party solution and the DATEV data center. The ID is not to
    be displayed to the end user. Please note: A data transfer to the DATEV data center is only possible
    if the user has access to the client. The third-party solution must ensure this by checking if the
    client number and consultant number exists in the list of clients.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Client, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, Client, ProblemDetails]]:
    """ Retrieve a specific client.

     Returns a specific client which the user has access to. In addition, this item also provides the
    available services for data transfer to the DATEV data center. The client ID is a technical object
    for the communication between the third-party solution and the DATEV data center. The ID is not to
    be displayed to the end user. Please note: A data transfer to the DATEV data center is only possible
    if the user has access to the client. The third-party solution must ensure this by checking if the
    client number and consultant number exists in the list of clients.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Client, ProblemDetails]
     """


    return sync_detailed(
        client_id=client_id,
client=client,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[Any, Client, ProblemDetails]]:
    """ Retrieve a specific client.

     Returns a specific client which the user has access to. In addition, this item also provides the
    available services for data transfer to the DATEV data center. The client ID is a technical object
    for the communication between the third-party solution and the DATEV data center. The ID is not to
    be displayed to the end user. Please note: A data transfer to the DATEV data center is only possible
    if the user has access to the client. The third-party solution must ensure this by checking if the
    client number and consultant number exists in the list of clients.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Client, ProblemDetails]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[Any, Client, ProblemDetails]]:
    """ Retrieve a specific client.

     Returns a specific client which the user has access to. In addition, this item also provides the
    available services for data transfer to the DATEV data center. The client ID is a technical object
    for the communication between the third-party solution and the DATEV data center. The ID is not to
    be displayed to the end user. Please note: A data transfer to the DATEV data center is only possible
    if the user has access to the client. The third-party solution must ensure this by checking if the
    client number and consultant number exists in the list of clients.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Client, ProblemDetails]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,

    )).parsed
