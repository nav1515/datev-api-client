from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.protocol_entry import ProtocolEntry
from typing import cast



def _get_kwargs(
    client_id: str,
    job_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}/dxso-jobs/{job_id}/protocol-entries".format(client_id=client_id,job_id=job_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, list['ProtocolEntry']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ProtocolEntry.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, list['ProtocolEntry']]]:
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
    client: AuthenticatedClient,

) -> Response[Union[Any, list['ProtocolEntry']]]:
    r""" Returns protocol entries of a data transfer (dxso-job).

     The processing of a data transfer (dxso-job) has to be checked as it is executed asynchronously. To
    do this, the third-party solution should provide the protocol entries (from Belege online in DATEV
    Unternehmen online) to the user. The protocol entries contain detailed information about the
    processing in DATEV Unternehmen online. The entries are kept only a limited time (about two months)
    in DATEV Unternehmen online, so the third-party solution has to store this information. The protocol
    entries are prepared for the display for the user. DATEV will change the messages from time to time.

    **Note:** Data transfers (dxso-jobs) are processed asynchronously.

    **Example: One protocol entry of a data transfer:**
    ```json
        HTTP/1.1 200 OK
        Content-Encoding: gzip
        Transfer-Encoding: chunked

        [
          {
            \"text\":\"wurde empfangen!\",
            \"type\":\"information\",
            \"filename\":\"document.xml\",
            \"time\":\"2017-02-07T14:12:57+01:00\"
          }
        ]

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ProtocolEntry']]]
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
    client: AuthenticatedClient,

) -> Optional[Union[Any, list['ProtocolEntry']]]:
    r""" Returns protocol entries of a data transfer (dxso-job).

     The processing of a data transfer (dxso-job) has to be checked as it is executed asynchronously. To
    do this, the third-party solution should provide the protocol entries (from Belege online in DATEV
    Unternehmen online) to the user. The protocol entries contain detailed information about the
    processing in DATEV Unternehmen online. The entries are kept only a limited time (about two months)
    in DATEV Unternehmen online, so the third-party solution has to store this information. The protocol
    entries are prepared for the display for the user. DATEV will change the messages from time to time.

    **Note:** Data transfers (dxso-jobs) are processed asynchronously.

    **Example: One protocol entry of a data transfer:**
    ```json
        HTTP/1.1 200 OK
        Content-Encoding: gzip
        Transfer-Encoding: chunked

        [
          {
            \"text\":\"wurde empfangen!\",
            \"type\":\"information\",
            \"filename\":\"document.xml\",
            \"time\":\"2017-02-07T14:12:57+01:00\"
          }
        ]

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ProtocolEntry']]
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
    client: AuthenticatedClient,

) -> Response[Union[Any, list['ProtocolEntry']]]:
    r""" Returns protocol entries of a data transfer (dxso-job).

     The processing of a data transfer (dxso-job) has to be checked as it is executed asynchronously. To
    do this, the third-party solution should provide the protocol entries (from Belege online in DATEV
    Unternehmen online) to the user. The protocol entries contain detailed information about the
    processing in DATEV Unternehmen online. The entries are kept only a limited time (about two months)
    in DATEV Unternehmen online, so the third-party solution has to store this information. The protocol
    entries are prepared for the display for the user. DATEV will change the messages from time to time.

    **Note:** Data transfers (dxso-jobs) are processed asynchronously.

    **Example: One protocol entry of a data transfer:**
    ```json
        HTTP/1.1 200 OK
        Content-Encoding: gzip
        Transfer-Encoding: chunked

        [
          {
            \"text\":\"wurde empfangen!\",
            \"type\":\"information\",
            \"filename\":\"document.xml\",
            \"time\":\"2017-02-07T14:12:57+01:00\"
          }
        ]

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ProtocolEntry']]]
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
    client: AuthenticatedClient,

) -> Optional[Union[Any, list['ProtocolEntry']]]:
    r""" Returns protocol entries of a data transfer (dxso-job).

     The processing of a data transfer (dxso-job) has to be checked as it is executed asynchronously. To
    do this, the third-party solution should provide the protocol entries (from Belege online in DATEV
    Unternehmen online) to the user. The protocol entries contain detailed information about the
    processing in DATEV Unternehmen online. The entries are kept only a limited time (about two months)
    in DATEV Unternehmen online, so the third-party solution has to store this information. The protocol
    entries are prepared for the display for the user. DATEV will change the messages from time to time.

    **Note:** Data transfers (dxso-jobs) are processed asynchronously.

    **Example: One protocol entry of a data transfer:**
    ```json
        HTTP/1.1 200 OK
        Content-Encoding: gzip
        Transfer-Encoding: chunked

        [
          {
            \"text\":\"wurde empfangen!\",
            \"type\":\"information\",
            \"filename\":\"document.xml\",
            \"time\":\"2017-02-07T14:12:57+01:00\"
          }
        ]

    Args:
        client_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ProtocolEntry']]
     """


    return (await asyncio_detailed(
        client_id=client_id,
job_id=job_id,
client=client,

    )).parsed
