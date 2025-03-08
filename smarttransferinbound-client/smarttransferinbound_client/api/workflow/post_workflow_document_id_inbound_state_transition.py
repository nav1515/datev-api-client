from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.workflow_state import WorkflowState
from ...models.workflow_transition import WorkflowTransition
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    document_id: str,
    *,
    body: Union[
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Workflow/{document_id}/Inbound/State/Transition".format(document_id=document_id,),
    }

    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=minimal;odata.streaming=true"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=minimal;odata.streaming=false"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=minimal"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=full;odata.streaming=true"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=full;odata.streaming=false"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=full"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=none;odata.streaming=true"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=none;odata.streaming=false"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.metadata=none"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.streaming=true"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json;odata.streaming=false"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json; odata.metadata=full; odata.streaming=true"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, WorkflowTransition):
        _json_body = body.to_dict()


        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, WorkflowState]]:
    if response.status_code == 200:
        response_200 = WorkflowState.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, WorkflowState]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[Union[Any, WorkflowState]]:
    """ Sets the inbound state transition.

    Args:
        document_id (str):
        x_api_key (Union[Unset, str]):
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WorkflowState]]
     """


    kwargs = _get_kwargs(
        document_id=document_id,
body=body,
x_api_key=x_api_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, WorkflowState]]:
    """ Sets the inbound state transition.

    Args:
        document_id (str):
        x_api_key (Union[Unset, str]):
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WorkflowState]
     """


    return sync_detailed(
        document_id=document_id,
client=client,
body=body,
x_api_key=x_api_key,

    ).parsed

async def asyncio_detailed(
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[Union[Any, WorkflowState]]:
    """ Sets the inbound state transition.

    Args:
        document_id (str):
        x_api_key (Union[Unset, str]):
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WorkflowState]]
     """


    kwargs = _get_kwargs(
        document_id=document_id,
body=body,
x_api_key=x_api_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
        WorkflowTransition,
    ],
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, WorkflowState]]:
    """ Sets the inbound state transition.

    Args:
        document_id (str):
        x_api_key (Union[Unset, str]):
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.
        body (WorkflowTransition): Contains information related to workflow transition for a
            document.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WorkflowState]
     """


    return (await asyncio_detailed(
        document_id=document_id,
client=client,
body=body,
x_api_key=x_api_key,

    )).parsed
