from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.client import Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    filter_: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    top: Union[Unset, int] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["skip"] = skip

    params["top"] = top


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ProblemDetails, list['Client']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Client.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ProblemDetails, list['Client']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    top: Union[Unset, int] = UNSET,

) -> Response[Union[Any, ProblemDetails, list['Client']]]:
    """ Returns a list of clients.

     Returns a list of all clients which can be accessed by the user. In addition, this list also
    provides the available services for the data transfer to the DATEV data center. For all subsequent
    requests concerning a data transfer to DATEV, the ID of the client is necessary. The ID is a
    technical object for the communication between the third-party solution and the DATEV data center.
    The ID is not to be displayed to the end user. Please note: Data transfer to the DATEV data center
    is only possible if the user has access to the client. The third-party solution must ensure this by
    checking if the client number and consultant number exists in the list of clients.

    Args:
        filter_ (Union[Unset, str]):
        skip (Union[Unset, int]):
        top (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, list['Client']]]
     """


    kwargs = _get_kwargs(
        filter_=filter_,
skip=skip,
top=top,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    top: Union[Unset, int] = UNSET,

) -> Optional[Union[Any, ProblemDetails, list['Client']]]:
    """ Returns a list of clients.

     Returns a list of all clients which can be accessed by the user. In addition, this list also
    provides the available services for the data transfer to the DATEV data center. For all subsequent
    requests concerning a data transfer to DATEV, the ID of the client is necessary. The ID is a
    technical object for the communication between the third-party solution and the DATEV data center.
    The ID is not to be displayed to the end user. Please note: Data transfer to the DATEV data center
    is only possible if the user has access to the client. The third-party solution must ensure this by
    checking if the client number and consultant number exists in the list of clients.

    Args:
        filter_ (Union[Unset, str]):
        skip (Union[Unset, int]):
        top (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, list['Client']]
     """


    return sync_detailed(
        client=client,
filter_=filter_,
skip=skip,
top=top,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    top: Union[Unset, int] = UNSET,

) -> Response[Union[Any, ProblemDetails, list['Client']]]:
    """ Returns a list of clients.

     Returns a list of all clients which can be accessed by the user. In addition, this list also
    provides the available services for the data transfer to the DATEV data center. For all subsequent
    requests concerning a data transfer to DATEV, the ID of the client is necessary. The ID is a
    technical object for the communication between the third-party solution and the DATEV data center.
    The ID is not to be displayed to the end user. Please note: Data transfer to the DATEV data center
    is only possible if the user has access to the client. The third-party solution must ensure this by
    checking if the client number and consultant number exists in the list of clients.

    Args:
        filter_ (Union[Unset, str]):
        skip (Union[Unset, int]):
        top (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, list['Client']]]
     """


    kwargs = _get_kwargs(
        filter_=filter_,
skip=skip,
top=top,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, str] = UNSET,
    skip: Union[Unset, int] = UNSET,
    top: Union[Unset, int] = UNSET,

) -> Optional[Union[Any, ProblemDetails, list['Client']]]:
    """ Returns a list of clients.

     Returns a list of all clients which can be accessed by the user. In addition, this list also
    provides the available services for the data transfer to the DATEV data center. For all subsequent
    requests concerning a data transfer to DATEV, the ID of the client is necessary. The ID is a
    technical object for the communication between the third-party solution and the DATEV data center.
    The ID is not to be displayed to the end user. Please note: Data transfer to the DATEV data center
    is only possible if the user has access to the client. The third-party solution must ensure this by
    checking if the client number and consultant number exists in the list of clients.

    Args:
        filter_ (Union[Unset, str]):
        skip (Union[Unset, int]):
        top (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, list['Client']]
     """


    return (await asyncio_detailed(
        client=client,
filter_=filter_,
skip=skip,
top=top,

    )).parsed
