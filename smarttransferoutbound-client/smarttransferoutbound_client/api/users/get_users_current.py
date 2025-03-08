from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user_model import UserModel
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    select: Union[Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key



    

    params: dict[str, Any] = {}

    params["$select"] = select


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Users/Current",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[UserModel]:
    if response.status_code == 200:
        response_200 = UserModel.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[UserModel]:
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
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[UserModel]:
    r""" Gets the currently logged in user.

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
    result.</td>    <td style=\"padding-left:12px;padding-right:12px;\">/Users/Current$select=id</td>
    <td style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#select\"
    target=\"_blank\">Documentation🡥</a></td></tr></tbody></table>  </div></div>

    Args:
        select (Union[Unset, str]): Limits the properties returned in the result.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserModel]
     """


    kwargs = _get_kwargs(
        select=select,
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
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[UserModel]:
    r""" Gets the currently logged in user.

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
    result.</td>    <td style=\"padding-left:12px;padding-right:12px;\">/Users/Current$select=id</td>
    <td style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#select\"
    target=\"_blank\">Documentation🡥</a></td></tr></tbody></table>  </div></div>

    Args:
        select (Union[Unset, str]): Limits the properties returned in the result.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserModel
     """


    return sync_detailed(
        client=client,
select=select,
x_api_key=x_api_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    select: Union[Unset, str] = UNSET,
    x_api_key: Union[Unset, str] = UNSET,

) -> Response[UserModel]:
    r""" Gets the currently logged in user.

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
    result.</td>    <td style=\"padding-left:12px;padding-right:12px;\">/Users/Current$select=id</td>
    <td style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#select\"
    target=\"_blank\">Documentation🡥</a></td></tr></tbody></table>  </div></div>

    Args:
        select (Union[Unset, str]): Limits the properties returned in the result.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserModel]
     """


    kwargs = _get_kwargs(
        select=select,
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
    x_api_key: Union[Unset, str] = UNSET,

) -> Optional[UserModel]:
    r""" Gets the currently logged in user.

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
    result.</td>    <td style=\"padding-left:12px;padding-right:12px;\">/Users/Current$select=id</td>
    <td style=\"padding-left:12px;padding-right:12px;\"><a href=\"https://docs.microsoft.com/en-
    us/odata/webapi/first-odata-api#select\"
    target=\"_blank\">Documentation🡥</a></td></tr></tbody></table>  </div></div>

    Args:
        select (Union[Unset, str]): Limits the properties returned in the result.
        x_api_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserModel
     """


    return (await asyncio_detailed(
        client=client,
select=select,
x_api_key=x_api_key,

    )).parsed
