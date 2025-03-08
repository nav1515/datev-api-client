from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.client import Client
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients",
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, list['Client']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = Client.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, list['Client']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, list['Client']]]:
    r""" Returns a list of clients that are accessible for the user.

     Returns a list of all clients to which the user has access. The user is only familiar with the
    client name, the client number, and the consultant number. For all subsequent requests concerning
    data transfer to DATEV, the ID of the client is necessary. The ID is a technical object for the
    communication between the third-party solution and the DATEV data center. The ID is not to be
    displayed to the end user.

    **Please note:** Data transfer to the DATEV data center is only possible if the user has access to
    the client. The third-party solution must ensure this by checking that the client number and
    consultant number exists in the list of clients.

    **Example: The user has access to one client**

        [{
            \"client_number\": 1,
            \"consultant_number\": 455148,
            \"id\": \"455148-1\",
            \"name\": \"Muster GmbH 1\"
        }]




    **Example: The user has access to two clients**


        [{
            \"client_number\":1,
            \"consultant_number\":455148,
            \"id\":\"455148-1\",
            \"name\":\"Muster GmbH 1\"},
          {
            \"client_number\":2,
            \"consultant_number\":455148,
            \"id\":\"455148-2\",
            \"name\":\"Muster GmbH 2\"

          }]

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['Client']]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, list['Client']]]:
    r""" Returns a list of clients that are accessible for the user.

     Returns a list of all clients to which the user has access. The user is only familiar with the
    client name, the client number, and the consultant number. For all subsequent requests concerning
    data transfer to DATEV, the ID of the client is necessary. The ID is a technical object for the
    communication between the third-party solution and the DATEV data center. The ID is not to be
    displayed to the end user.

    **Please note:** Data transfer to the DATEV data center is only possible if the user has access to
    the client. The third-party solution must ensure this by checking that the client number and
    consultant number exists in the list of clients.

    **Example: The user has access to one client**

        [{
            \"client_number\": 1,
            \"consultant_number\": 455148,
            \"id\": \"455148-1\",
            \"name\": \"Muster GmbH 1\"
        }]




    **Example: The user has access to two clients**


        [{
            \"client_number\":1,
            \"consultant_number\":455148,
            \"id\":\"455148-1\",
            \"name\":\"Muster GmbH 1\"},
          {
            \"client_number\":2,
            \"consultant_number\":455148,
            \"id\":\"455148-2\",
            \"name\":\"Muster GmbH 2\"

          }]

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['Client']]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, list['Client']]]:
    r""" Returns a list of clients that are accessible for the user.

     Returns a list of all clients to which the user has access. The user is only familiar with the
    client name, the client number, and the consultant number. For all subsequent requests concerning
    data transfer to DATEV, the ID of the client is necessary. The ID is a technical object for the
    communication between the third-party solution and the DATEV data center. The ID is not to be
    displayed to the end user.

    **Please note:** Data transfer to the DATEV data center is only possible if the user has access to
    the client. The third-party solution must ensure this by checking that the client number and
    consultant number exists in the list of clients.

    **Example: The user has access to one client**

        [{
            \"client_number\": 1,
            \"consultant_number\": 455148,
            \"id\": \"455148-1\",
            \"name\": \"Muster GmbH 1\"
        }]




    **Example: The user has access to two clients**


        [{
            \"client_number\":1,
            \"consultant_number\":455148,
            \"id\":\"455148-1\",
            \"name\":\"Muster GmbH 1\"},
          {
            \"client_number\":2,
            \"consultant_number\":455148,
            \"id\":\"455148-2\",
            \"name\":\"Muster GmbH 2\"

          }]

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['Client']]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, list['Client']]]:
    r""" Returns a list of clients that are accessible for the user.

     Returns a list of all clients to which the user has access. The user is only familiar with the
    client name, the client number, and the consultant number. For all subsequent requests concerning
    data transfer to DATEV, the ID of the client is necessary. The ID is a technical object for the
    communication between the third-party solution and the DATEV data center. The ID is not to be
    displayed to the end user.

    **Please note:** Data transfer to the DATEV data center is only possible if the user has access to
    the client. The third-party solution must ensure this by checking that the client number and
    consultant number exists in the list of clients.

    **Example: The user has access to one client**

        [{
            \"client_number\": 1,
            \"consultant_number\": 455148,
            \"id\": \"455148-1\",
            \"name\": \"Muster GmbH 1\"
        }]




    **Example: The user has access to two clients**


        [{
            \"client_number\":1,
            \"consultant_number\":455148,
            \"id\":\"455148-1\",
            \"name\":\"Muster GmbH 1\"},
          {
            \"client_number\":2,
            \"consultant_number\":455148,
            \"id\":\"455148-2\",
            \"name\":\"Muster GmbH 2\"

          }]

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['Client']]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
