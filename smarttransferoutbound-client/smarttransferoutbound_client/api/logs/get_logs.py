from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.log_model_i_enumerable_o_data_value import LogModelIEnumerableODataValue
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    select: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    orderby: Union[Unset, str] = UNSET,
    top: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
    count: Union[Unset, bool] = False,
    x_api_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key



    

    params: dict[str, Any] = {}

    params["$select"] = select

    params["$filter"] = filter_

    params["$orderby"] = orderby

    params["$top"] = top

    params["$skip"] = skip

    params["$count"] = count


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Logs",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[LogModelIEnumerableODataValue]:
    if response.status_code == 200:
        response_200 = LogModelIEnumerableODataValue.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[LogModelIEnumerableODataValue]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    select: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    orderby: Union[Unset, str] = UNSET,
    top: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
    count: Union[Unset, bool] = False,
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[LogModelIEnumerableODataValue]:
    """ Retrieves logs.

    Args:
        select (Union[Unset, str]): Limits the properties returned in the result.
        filter_ (Union[Unset, str]): Restricts the set of items returned.
        orderby (Union[Unset, str]): Specifies the order in which items are returned.
        top (Union[Unset, int]): Limits the number of items returned from a collection. Default:
            100.
        skip (Union[Unset, int]): Excludes the specified number of items of the queried collection
            from the result. Default: 0.
        count (Union[Unset, bool]): Indicates whether the total count of items within a collection
            are returned in the result. Default: False.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogModelIEnumerableODataValue]
     """


    kwargs = _get_kwargs(
        select=select,
filter_=filter_,
orderby=orderby,
top=top,
skip=skip,
count=count,
x_api_key=x_api_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    select: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    orderby: Union[Unset, str] = UNSET,
    top: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
    count: Union[Unset, bool] = False,
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[LogModelIEnumerableODataValue]:
    """ Retrieves logs.

    Args:
        select (Union[Unset, str]): Limits the properties returned in the result.
        filter_ (Union[Unset, str]): Restricts the set of items returned.
        orderby (Union[Unset, str]): Specifies the order in which items are returned.
        top (Union[Unset, int]): Limits the number of items returned from a collection. Default:
            100.
        skip (Union[Unset, int]): Excludes the specified number of items of the queried collection
            from the result. Default: 0.
        count (Union[Unset, bool]): Indicates whether the total count of items within a collection
            are returned in the result. Default: False.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogModelIEnumerableODataValue
     """


    return sync_detailed(
        client=client,
select=select,
filter_=filter_,
orderby=orderby,
top=top,
skip=skip,
count=count,
x_api_key=x_api_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    select: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    orderby: Union[Unset, str] = UNSET,
    top: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
    count: Union[Unset, bool] = False,
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[LogModelIEnumerableODataValue]:
    """ Retrieves logs.

    Args:
        select (Union[Unset, str]): Limits the properties returned in the result.
        filter_ (Union[Unset, str]): Restricts the set of items returned.
        orderby (Union[Unset, str]): Specifies the order in which items are returned.
        top (Union[Unset, int]): Limits the number of items returned from a collection. Default:
            100.
        skip (Union[Unset, int]): Excludes the specified number of items of the queried collection
            from the result. Default: 0.
        count (Union[Unset, bool]): Indicates whether the total count of items within a collection
            are returned in the result. Default: False.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogModelIEnumerableODataValue]
     """


    kwargs = _get_kwargs(
        select=select,
filter_=filter_,
orderby=orderby,
top=top,
skip=skip,
count=count,
x_api_key=x_api_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    select: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    orderby: Union[Unset, str] = UNSET,
    top: Union[Unset, int] = 100,
    skip: Union[Unset, int] = 0,
    count: Union[Unset, bool] = False,
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[LogModelIEnumerableODataValue]:
    """ Retrieves logs.

    Args:
        select (Union[Unset, str]): Limits the properties returned in the result.
        filter_ (Union[Unset, str]): Restricts the set of items returned.
        orderby (Union[Unset, str]): Specifies the order in which items are returned.
        top (Union[Unset, int]): Limits the number of items returned from a collection. Default:
            100.
        skip (Union[Unset, int]): Excludes the specified number of items of the queried collection
            from the result. Default: 0.
        count (Union[Unset, bool]): Indicates whether the total count of items within a collection
            are returned in the result. Default: False.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogModelIEnumerableODataValue
     """


    return (await asyncio_detailed(
        client=client,
select=select,
filter_=filter_,
orderby=orderby,
top=top,
skip=skip,
count=count,
x_api_key=x_api_key,

    )).parsed
