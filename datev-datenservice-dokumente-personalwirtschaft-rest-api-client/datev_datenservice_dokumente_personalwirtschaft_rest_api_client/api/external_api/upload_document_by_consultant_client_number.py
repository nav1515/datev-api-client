from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_message import ErrorMessage
from ...models.upload_document_by_consultant_client_number_body import UploadDocumentByConsultantClientNumberBody
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    consultantnumber_clientnumber: str,
    *,
    body: UploadDocumentByConsultantClientNumberBody,
    client_application: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(client_application, Unset):
        headers["Client-Application"] = client_application



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/clients/{consultantnumber_clientnumber}/documents/upload".format(consultantnumber_clientnumber=consultantnumber_clientnumber,),
    }

    _body = body.to_multipart()


    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ErrorMessage]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = ErrorMessage.from_dict(response.json())



        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = ErrorMessage.from_dict(response.json())



        return response_403
    if response.status_code == 404:
        response_404 = ErrorMessage.from_dict(response.json())



        return response_404
    if response.status_code == 422:
        response_422 = ErrorMessage.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ErrorMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    consultantnumber_clientnumber: str,
    *,
    client: AuthenticatedClient,
    body: UploadDocumentByConsultantClientNumberBody,
    client_application: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ErrorMessage]]:
    """ Upload of a single document to DATEV Personalakte. This operation supports a resource in the form of
    clients/{consultantnumber-clientnumber} and the usage of long time authentication tokens.

    Args:
        consultantnumber_clientnumber (str): Consultant and client number separated by a hyphen.
            Example: 402248-17100.
        client_application (Union[Unset, str]):
        body (UploadDocumentByConsultantClientNumberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
     """


    kwargs = _get_kwargs(
        consultantnumber_clientnumber=consultantnumber_clientnumber,
body=body,
client_application=client_application,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    consultantnumber_clientnumber: str,
    *,
    client: AuthenticatedClient,
    body: UploadDocumentByConsultantClientNumberBody,
    client_application: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ErrorMessage]]:
    """ Upload of a single document to DATEV Personalakte. This operation supports a resource in the form of
    clients/{consultantnumber-clientnumber} and the usage of long time authentication tokens.

    Args:
        consultantnumber_clientnumber (str): Consultant and client number separated by a hyphen.
            Example: 402248-17100.
        client_application (Union[Unset, str]):
        body (UploadDocumentByConsultantClientNumberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
     """


    return sync_detailed(
        consultantnumber_clientnumber=consultantnumber_clientnumber,
client=client,
body=body,
client_application=client_application,

    ).parsed

async def asyncio_detailed(
    consultantnumber_clientnumber: str,
    *,
    client: AuthenticatedClient,
    body: UploadDocumentByConsultantClientNumberBody,
    client_application: Union[Unset, str] = UNSET,

) -> Response[Union[Any, ErrorMessage]]:
    """ Upload of a single document to DATEV Personalakte. This operation supports a resource in the form of
    clients/{consultantnumber-clientnumber} and the usage of long time authentication tokens.

    Args:
        consultantnumber_clientnumber (str): Consultant and client number separated by a hyphen.
            Example: 402248-17100.
        client_application (Union[Unset, str]):
        body (UploadDocumentByConsultantClientNumberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorMessage]]
     """


    kwargs = _get_kwargs(
        consultantnumber_clientnumber=consultantnumber_clientnumber,
body=body,
client_application=client_application,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    consultantnumber_clientnumber: str,
    *,
    client: AuthenticatedClient,
    body: UploadDocumentByConsultantClientNumberBody,
    client_application: Union[Unset, str] = UNSET,

) -> Optional[Union[Any, ErrorMessage]]:
    """ Upload of a single document to DATEV Personalakte. This operation supports a resource in the form of
    clients/{consultantnumber-clientnumber} and the usage of long time authentication tokens.

    Args:
        consultantnumber_clientnumber (str): Consultant and client number separated by a hyphen.
            Example: 402248-17100.
        client_application (Union[Unset, str]):
        body (UploadDocumentByConsultantClientNumberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ErrorMessage]
     """


    return (await asyncio_detailed(
        consultantnumber_clientnumber=consultantnumber_clientnumber,
client=client,
body=body,
client_application=client_application,

    )).parsed
