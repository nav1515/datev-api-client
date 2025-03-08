from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.find_all_is_consultant_client import FindAllIsConsultantClient
from ...models.find_all_orderby import FindAllOrderby
from ...models.find_all_status import FindAllStatus
from ...models.master_client_full import MasterClientFull
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    business_partner_id: Union[Unset, int] = UNSET,
    data_environment_number: Union[Unset, int] = UNSET,
    expand: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    status: Union[Unset, FindAllStatus] = UNSET,
    skip: Union[Unset, int] = 0,
    top: Union[Unset, int] = 100,
    orderby: Union[Unset, FindAllOrderby] = UNSET,
    is_consultant_client: Union[Unset, FindAllIsConsultantClient] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["business-partner-id"] = business_partner_id

    params["data-environment-number"] = data_environment_number

    params["expand"] = expand

    params["search-term"] = search_term

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["skip"] = skip

    params["top"] = top

    json_orderby: Union[Unset, str] = UNSET
    if not isinstance(orderby, Unset):
        json_orderby = orderby.value

    params["orderby"] = json_orderby

    json_is_consultant_client: Union[Unset, str] = UNSET
    if not isinstance(is_consultant_client, Unset):
        json_is_consultant_client = is_consultant_client.value

    params["is-consultant-client"] = json_is_consultant_client


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/master-clients",
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ProblemDetails, list['MasterClientFull']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = MasterClientFull.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404
    if response.status_code == 500:
        response_500 = ProblemDetails.from_dict(response.json())



        return response_500
    if response.status_code == 502:
        response_502 = ProblemDetails.from_dict(response.json())



        return response_502
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ProblemDetails, list['MasterClientFull']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    business_partner_id: Union[Unset, int] = UNSET,
    data_environment_number: Union[Unset, int] = UNSET,
    expand: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    status: Union[Unset, FindAllStatus] = UNSET,
    skip: Union[Unset, int] = 0,
    top: Union[Unset, int] = 100,
    orderby: Union[Unset, FindAllOrderby] = UNSET,
    is_consultant_client: Union[Unset, FindAllIsConsultantClient] = UNSET,

) -> Response[Union[ProblemDetails, list['MasterClientFull']]]:
    """ Returns a list of master clients.

     Returns a list of all master clients that can be accessed by the user.

    Args:
        business_partner_id (Union[Unset, int]):
        data_environment_number (Union[Unset, int]):
        expand (Union[Unset, str]):
        search_term (Union[Unset, str]):
        status (Union[Unset, FindAllStatus]):
        skip (Union[Unset, int]):  Default: 0.
        top (Union[Unset, int]):  Default: 100.
        orderby (Union[Unset, FindAllOrderby]):
        is_consultant_client (Union[Unset, FindAllIsConsultantClient]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, list['MasterClientFull']]]
     """


    kwargs = _get_kwargs(
        business_partner_id=business_partner_id,
data_environment_number=data_environment_number,
expand=expand,
search_term=search_term,
status=status,
skip=skip,
top=top,
orderby=orderby,
is_consultant_client=is_consultant_client,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    business_partner_id: Union[Unset, int] = UNSET,
    data_environment_number: Union[Unset, int] = UNSET,
    expand: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    status: Union[Unset, FindAllStatus] = UNSET,
    skip: Union[Unset, int] = 0,
    top: Union[Unset, int] = 100,
    orderby: Union[Unset, FindAllOrderby] = UNSET,
    is_consultant_client: Union[Unset, FindAllIsConsultantClient] = UNSET,

) -> Optional[Union[ProblemDetails, list['MasterClientFull']]]:
    """ Returns a list of master clients.

     Returns a list of all master clients that can be accessed by the user.

    Args:
        business_partner_id (Union[Unset, int]):
        data_environment_number (Union[Unset, int]):
        expand (Union[Unset, str]):
        search_term (Union[Unset, str]):
        status (Union[Unset, FindAllStatus]):
        skip (Union[Unset, int]):  Default: 0.
        top (Union[Unset, int]):  Default: 100.
        orderby (Union[Unset, FindAllOrderby]):
        is_consultant_client (Union[Unset, FindAllIsConsultantClient]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, list['MasterClientFull']]
     """


    return sync_detailed(
        client=client,
business_partner_id=business_partner_id,
data_environment_number=data_environment_number,
expand=expand,
search_term=search_term,
status=status,
skip=skip,
top=top,
orderby=orderby,
is_consultant_client=is_consultant_client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    business_partner_id: Union[Unset, int] = UNSET,
    data_environment_number: Union[Unset, int] = UNSET,
    expand: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    status: Union[Unset, FindAllStatus] = UNSET,
    skip: Union[Unset, int] = 0,
    top: Union[Unset, int] = 100,
    orderby: Union[Unset, FindAllOrderby] = UNSET,
    is_consultant_client: Union[Unset, FindAllIsConsultantClient] = UNSET,

) -> Response[Union[ProblemDetails, list['MasterClientFull']]]:
    """ Returns a list of master clients.

     Returns a list of all master clients that can be accessed by the user.

    Args:
        business_partner_id (Union[Unset, int]):
        data_environment_number (Union[Unset, int]):
        expand (Union[Unset, str]):
        search_term (Union[Unset, str]):
        status (Union[Unset, FindAllStatus]):
        skip (Union[Unset, int]):  Default: 0.
        top (Union[Unset, int]):  Default: 100.
        orderby (Union[Unset, FindAllOrderby]):
        is_consultant_client (Union[Unset, FindAllIsConsultantClient]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, list['MasterClientFull']]]
     """


    kwargs = _get_kwargs(
        business_partner_id=business_partner_id,
data_environment_number=data_environment_number,
expand=expand,
search_term=search_term,
status=status,
skip=skip,
top=top,
orderby=orderby,
is_consultant_client=is_consultant_client,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    business_partner_id: Union[Unset, int] = UNSET,
    data_environment_number: Union[Unset, int] = UNSET,
    expand: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
    status: Union[Unset, FindAllStatus] = UNSET,
    skip: Union[Unset, int] = 0,
    top: Union[Unset, int] = 100,
    orderby: Union[Unset, FindAllOrderby] = UNSET,
    is_consultant_client: Union[Unset, FindAllIsConsultantClient] = UNSET,

) -> Optional[Union[ProblemDetails, list['MasterClientFull']]]:
    """ Returns a list of master clients.

     Returns a list of all master clients that can be accessed by the user.

    Args:
        business_partner_id (Union[Unset, int]):
        data_environment_number (Union[Unset, int]):
        expand (Union[Unset, str]):
        search_term (Union[Unset, str]):
        status (Union[Unset, FindAllStatus]):
        skip (Union[Unset, int]):  Default: 0.
        top (Union[Unset, int]):  Default: 100.
        orderby (Union[Unset, FindAllOrderby]):
        is_consultant_client (Union[Unset, FindAllIsConsultantClient]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, list['MasterClientFull']]
     """


    return (await asyncio_detailed(
        client=client,
business_partner_id=business_partner_id,
data_environment_number=data_environment_number,
expand=expand,
search_term=search_term,
status=status,
skip=skip,
top=top,
orderby=orderby,
is_consultant_client=is_consultant_client,

    )).parsed
