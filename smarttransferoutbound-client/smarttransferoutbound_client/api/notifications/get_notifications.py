from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.notification_model_i_enumerable_o_data_value import NotificationModelIEnumerableODataValue
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

) -> dict[str, Any]:
    

    

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
        "url": "/Notifications",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[NotificationModelIEnumerableODataValue]:
    if response.status_code == 200:
        response_200 = NotificationModelIEnumerableODataValue.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[NotificationModelIEnumerableODataValue]:
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

) -> Response[NotificationModelIEnumerableODataValue]:
    r""" Retrieves notifications.

     <div style=\"display:flex; flex-direction:row; align-items:center;font-size:14px;border-radius: 4px;
    padding: 4px; background-color: rgb(157,181,205,0.3)\">  <div style=\"border-radius: 4px; padding:
    4px; background-color: #000000; margin-right:12px;color: white;\">ODATA</div>   <div>This API call
    supports querying and filtering using OData. Following table provides description and examples of
    possible options:</div></div><div style=\"display:flex; flex-direction:row; align-items:center;font-
    size:14px;margin-left:0px;margin-top:12px\">  <div style=\"width:100%; margin-top:-4px\"><table
    style=\"width:100%;border-radius:4px\"> <thead style=\"background-color: rgba(0,0,0,0.05); border:
    1px solid rgba(0,0,0,0.08);\">     <tr>         <td style=\"padding: 12px\">Option</td>         <td
    style=\"padding: 12px\">Description</td>         <td style=\"padding: 12px\">Example</td>
    <td style=\"padding: 12px\">Documentation</td>     </tr> </thead> <tbody><tr style=\"border: 1px
    solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-right:12px;\">$select</td>
    <td style=\"padding-left:12px;padding-right:12px;\">Limits the properties returned in the
    result.</td>    <td style=\"padding-left:12px;padding-right:12px;\">/Notifications$select=id</td>
    <td style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#select\" target=\"_blank\">Documentation🡥</a></td></tr><tr
    style=\"border: 1px solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-
    right:12px;\">$filter</td>    <td style=\"padding-left:12px;padding-right:12px;\">Restricts the set
    of items returned.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$filter=id gt 445566</td>    <td style=\"padding-left:12px;padding-
    right:12px;\"><a href=\"https://docs.microsoft.com/en-us/odata/webapi/first-odata-api#filter\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$orderby</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Specifies the order in which items are returned.</td>    <td
    style=\"padding-left:12px;padding-right:12px;\">/Notifications$orderby=id desc</td>    <td
    style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#orderby\" target=\"_blank\">Documentation🡥</a></td></tr><tr
    style=\"border: 1px solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-
    right:12px;\">$top</td>    <td style=\"padding-left:12px;padding-right:12px;\">Limits the number of
    items returned from a collection.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$top=50</td>    <td style=\"padding-left:12px;padding-right:12px;\"><a
    href=\"https://docs.microsoft.com/en-us/odata/client/query-options#top\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$skip</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Excludes the specified number of items of the queried collection
    from the result.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$skip=25</td>    <td style=\"padding-left:12px;padding-right:12px;\"><a
    href=\"https://docs.microsoft.com/en-us/odata/webapi/first-odata-api#skip\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$count</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Indicates whether the total count of items within a collection are
    returned in the result.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$count=true</td>    <td style=\"padding-left:12px;padding-
    right:12px;\"><a href=\"https://docs.microsoft.com/en-us/odata/client/query-options#count\"
    target=\"_blank\">Documentation🡥</a></td></tr></tbody></table>  </div></div>

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationModelIEnumerableODataValue]
     """


    kwargs = _get_kwargs(
        select=select,
filter_=filter_,
orderby=orderby,
top=top,
skip=skip,
count=count,

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

) -> Optional[NotificationModelIEnumerableODataValue]:
    r""" Retrieves notifications.

     <div style=\"display:flex; flex-direction:row; align-items:center;font-size:14px;border-radius: 4px;
    padding: 4px; background-color: rgb(157,181,205,0.3)\">  <div style=\"border-radius: 4px; padding:
    4px; background-color: #000000; margin-right:12px;color: white;\">ODATA</div>   <div>This API call
    supports querying and filtering using OData. Following table provides description and examples of
    possible options:</div></div><div style=\"display:flex; flex-direction:row; align-items:center;font-
    size:14px;margin-left:0px;margin-top:12px\">  <div style=\"width:100%; margin-top:-4px\"><table
    style=\"width:100%;border-radius:4px\"> <thead style=\"background-color: rgba(0,0,0,0.05); border:
    1px solid rgba(0,0,0,0.08);\">     <tr>         <td style=\"padding: 12px\">Option</td>         <td
    style=\"padding: 12px\">Description</td>         <td style=\"padding: 12px\">Example</td>
    <td style=\"padding: 12px\">Documentation</td>     </tr> </thead> <tbody><tr style=\"border: 1px
    solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-right:12px;\">$select</td>
    <td style=\"padding-left:12px;padding-right:12px;\">Limits the properties returned in the
    result.</td>    <td style=\"padding-left:12px;padding-right:12px;\">/Notifications$select=id</td>
    <td style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#select\" target=\"_blank\">Documentation🡥</a></td></tr><tr
    style=\"border: 1px solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-
    right:12px;\">$filter</td>    <td style=\"padding-left:12px;padding-right:12px;\">Restricts the set
    of items returned.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$filter=id gt 445566</td>    <td style=\"padding-left:12px;padding-
    right:12px;\"><a href=\"https://docs.microsoft.com/en-us/odata/webapi/first-odata-api#filter\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$orderby</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Specifies the order in which items are returned.</td>    <td
    style=\"padding-left:12px;padding-right:12px;\">/Notifications$orderby=id desc</td>    <td
    style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#orderby\" target=\"_blank\">Documentation🡥</a></td></tr><tr
    style=\"border: 1px solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-
    right:12px;\">$top</td>    <td style=\"padding-left:12px;padding-right:12px;\">Limits the number of
    items returned from a collection.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$top=50</td>    <td style=\"padding-left:12px;padding-right:12px;\"><a
    href=\"https://docs.microsoft.com/en-us/odata/client/query-options#top\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$skip</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Excludes the specified number of items of the queried collection
    from the result.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$skip=25</td>    <td style=\"padding-left:12px;padding-right:12px;\"><a
    href=\"https://docs.microsoft.com/en-us/odata/webapi/first-odata-api#skip\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$count</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Indicates whether the total count of items within a collection are
    returned in the result.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$count=true</td>    <td style=\"padding-left:12px;padding-
    right:12px;\"><a href=\"https://docs.microsoft.com/en-us/odata/client/query-options#count\"
    target=\"_blank\">Documentation🡥</a></td></tr></tbody></table>  </div></div>

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationModelIEnumerableODataValue
     """


    return sync_detailed(
        client=client,
select=select,
filter_=filter_,
orderby=orderby,
top=top,
skip=skip,
count=count,

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

) -> Response[NotificationModelIEnumerableODataValue]:
    r""" Retrieves notifications.

     <div style=\"display:flex; flex-direction:row; align-items:center;font-size:14px;border-radius: 4px;
    padding: 4px; background-color: rgb(157,181,205,0.3)\">  <div style=\"border-radius: 4px; padding:
    4px; background-color: #000000; margin-right:12px;color: white;\">ODATA</div>   <div>This API call
    supports querying and filtering using OData. Following table provides description and examples of
    possible options:</div></div><div style=\"display:flex; flex-direction:row; align-items:center;font-
    size:14px;margin-left:0px;margin-top:12px\">  <div style=\"width:100%; margin-top:-4px\"><table
    style=\"width:100%;border-radius:4px\"> <thead style=\"background-color: rgba(0,0,0,0.05); border:
    1px solid rgba(0,0,0,0.08);\">     <tr>         <td style=\"padding: 12px\">Option</td>         <td
    style=\"padding: 12px\">Description</td>         <td style=\"padding: 12px\">Example</td>
    <td style=\"padding: 12px\">Documentation</td>     </tr> </thead> <tbody><tr style=\"border: 1px
    solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-right:12px;\">$select</td>
    <td style=\"padding-left:12px;padding-right:12px;\">Limits the properties returned in the
    result.</td>    <td style=\"padding-left:12px;padding-right:12px;\">/Notifications$select=id</td>
    <td style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#select\" target=\"_blank\">Documentation🡥</a></td></tr><tr
    style=\"border: 1px solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-
    right:12px;\">$filter</td>    <td style=\"padding-left:12px;padding-right:12px;\">Restricts the set
    of items returned.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$filter=id gt 445566</td>    <td style=\"padding-left:12px;padding-
    right:12px;\"><a href=\"https://docs.microsoft.com/en-us/odata/webapi/first-odata-api#filter\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$orderby</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Specifies the order in which items are returned.</td>    <td
    style=\"padding-left:12px;padding-right:12px;\">/Notifications$orderby=id desc</td>    <td
    style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#orderby\" target=\"_blank\">Documentation🡥</a></td></tr><tr
    style=\"border: 1px solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-
    right:12px;\">$top</td>    <td style=\"padding-left:12px;padding-right:12px;\">Limits the number of
    items returned from a collection.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$top=50</td>    <td style=\"padding-left:12px;padding-right:12px;\"><a
    href=\"https://docs.microsoft.com/en-us/odata/client/query-options#top\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$skip</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Excludes the specified number of items of the queried collection
    from the result.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$skip=25</td>    <td style=\"padding-left:12px;padding-right:12px;\"><a
    href=\"https://docs.microsoft.com/en-us/odata/webapi/first-odata-api#skip\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$count</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Indicates whether the total count of items within a collection are
    returned in the result.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$count=true</td>    <td style=\"padding-left:12px;padding-
    right:12px;\"><a href=\"https://docs.microsoft.com/en-us/odata/client/query-options#count\"
    target=\"_blank\">Documentation🡥</a></td></tr></tbody></table>  </div></div>

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationModelIEnumerableODataValue]
     """


    kwargs = _get_kwargs(
        select=select,
filter_=filter_,
orderby=orderby,
top=top,
skip=skip,
count=count,

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

) -> Optional[NotificationModelIEnumerableODataValue]:
    r""" Retrieves notifications.

     <div style=\"display:flex; flex-direction:row; align-items:center;font-size:14px;border-radius: 4px;
    padding: 4px; background-color: rgb(157,181,205,0.3)\">  <div style=\"border-radius: 4px; padding:
    4px; background-color: #000000; margin-right:12px;color: white;\">ODATA</div>   <div>This API call
    supports querying and filtering using OData. Following table provides description and examples of
    possible options:</div></div><div style=\"display:flex; flex-direction:row; align-items:center;font-
    size:14px;margin-left:0px;margin-top:12px\">  <div style=\"width:100%; margin-top:-4px\"><table
    style=\"width:100%;border-radius:4px\"> <thead style=\"background-color: rgba(0,0,0,0.05); border:
    1px solid rgba(0,0,0,0.08);\">     <tr>         <td style=\"padding: 12px\">Option</td>         <td
    style=\"padding: 12px\">Description</td>         <td style=\"padding: 12px\">Example</td>
    <td style=\"padding: 12px\">Documentation</td>     </tr> </thead> <tbody><tr style=\"border: 1px
    solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-right:12px;\">$select</td>
    <td style=\"padding-left:12px;padding-right:12px;\">Limits the properties returned in the
    result.</td>    <td style=\"padding-left:12px;padding-right:12px;\">/Notifications$select=id</td>
    <td style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#select\" target=\"_blank\">Documentation🡥</a></td></tr><tr
    style=\"border: 1px solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-
    right:12px;\">$filter</td>    <td style=\"padding-left:12px;padding-right:12px;\">Restricts the set
    of items returned.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$filter=id gt 445566</td>    <td style=\"padding-left:12px;padding-
    right:12px;\"><a href=\"https://docs.microsoft.com/en-us/odata/webapi/first-odata-api#filter\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$orderby</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Specifies the order in which items are returned.</td>    <td
    style=\"padding-left:12px;padding-right:12px;\">/Notifications$orderby=id desc</td>    <td
    style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#orderby\" target=\"_blank\">Documentation🡥</a></td></tr><tr
    style=\"border: 1px solid rgba(0,0,0,0.08);\">    <td style=\"padding-left:12px;padding-
    right:12px;\">$top</td>    <td style=\"padding-left:12px;padding-right:12px;\">Limits the number of
    items returned from a collection.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$top=50</td>    <td style=\"padding-left:12px;padding-right:12px;\"><a
    href=\"https://docs.microsoft.com/en-us/odata/client/query-options#top\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$skip</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Excludes the specified number of items of the queried collection
    from the result.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$skip=25</td>    <td style=\"padding-left:12px;padding-right:12px;\"><a
    href=\"https://docs.microsoft.com/en-us/odata/webapi/first-odata-api#skip\"
    target=\"_blank\">Documentation🡥</a></td></tr><tr style=\"border: 1px solid rgba(0,0,0,0.08);\">
    <td style=\"padding-left:12px;padding-right:12px;\">$count</td>    <td style=\"padding-
    left:12px;padding-right:12px;\">Indicates whether the total count of items within a collection are
    returned in the result.</td>    <td style=\"padding-left:12px;padding-
    right:12px;\">/Notifications$count=true</td>    <td style=\"padding-left:12px;padding-
    right:12px;\"><a href=\"https://docs.microsoft.com/en-us/odata/client/query-options#count\"
    target=\"_blank\">Documentation🡥</a></td></tr></tbody></table>  </div></div>

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationModelIEnumerableODataValue
     """


    return (await asyncio_detailed(
        client=client,
select=select,
filter_=filter_,
orderby=orderby,
top=top,
skip=skip,
count=count,

    )).parsed
