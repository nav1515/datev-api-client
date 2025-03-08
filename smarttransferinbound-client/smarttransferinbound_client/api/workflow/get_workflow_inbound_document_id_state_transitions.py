from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.workflow_transition import WorkflowTransition
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    document_id: int,
    *,
    x_api_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Workflow/Inbound/{document_id}/State/Transitions".format(document_id=document_id,),
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, list['WorkflowTransition']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = WorkflowTransition.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, list['WorkflowTransition']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    document_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[Union[Any, list['WorkflowTransition']]]:
    """ Gets the inbound workflow state transitions.

    Args:
        document_id (int): The document identifier.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['WorkflowTransition']]]
     """


    kwargs = _get_kwargs(
        document_id=document_id,
x_api_key=x_api_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    document_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, list['WorkflowTransition']]]:
    """ Gets the inbound workflow state transitions.

    Args:
        document_id (int): The document identifier.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['WorkflowTransition']]
     """


    return sync_detailed(
        document_id=document_id,
client=client,
x_api_key=x_api_key,

    ).parsed

async def asyncio_detailed(
    document_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[Union[Any, list['WorkflowTransition']]]:
    """ Gets the inbound workflow state transitions.

    Args:
        document_id (int): The document identifier.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['WorkflowTransition']]]
     """


    kwargs = _get_kwargs(
        document_id=document_id,
x_api_key=x_api_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    document_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, list['WorkflowTransition']]]:
    """ Gets the inbound workflow state transitions.

    Args:
        document_id (int): The document identifier.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['WorkflowTransition']]
     """


    return (await asyncio_detailed(
        document_id=document_id,
client=client,
x_api_key=x_api_key,

    )).parsed
