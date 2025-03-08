from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.document_type import DocumentType
from typing import cast



def _get_kwargs(
    client_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}/document-types".format(client_id=client_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, list['DocumentType']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = DocumentType.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, list['DocumentType']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, list['DocumentType']]]:
    r""" Returns a list of document types for a given client.

     Returns a list of document types for a given client. The user is normally only familiar with the
    name of the document type. The document type is determined by the properties category and
    debit_credit_identifier. Further processing in DATEV Unternehmen online depends on these properties.
    For example, a document type with the category “invoice_received” is processed as an incoming
    invoice.

    The document type in DATEV applications is called “Belegtyp”. A client can have a lot of different
    document types. There are document types with special restrictions – document types with the
    category “personnel_documents” and “travel_expense_documents”. This means that the user’s DATEV
    authentication method needs to be configured with special rights.

    **Please note:** If the returned list is empty then the client has no document types. Normally, a
    client has at least four document types.


     **Get list of document types**



    ```json
    HTTP/1.1 200 OK
    Content-Encoding: gzip
    Transfer-Encoding: chunked

    [
    {
    \"name\":\"Rechnungseingang\",
    \"category\":\"invoices_received\",
    \"debit_credit_identifier\":\"debit\"
    },
    {
    \"name\":\"Rechnungsausgang\",
    \"category\":\"outgoing_invoices\",
    \"debit_credit_identifier\":\"credit\"
    },
    {
    \"name\":\"Kasse\",
    \"category\":\"other_documents\"
    },
    {
    \"name\":\"Sonstige\",
    \"category\":\"other_documents\"
    }
    ]

    ```

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['DocumentType']]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, list['DocumentType']]]:
    r""" Returns a list of document types for a given client.

     Returns a list of document types for a given client. The user is normally only familiar with the
    name of the document type. The document type is determined by the properties category and
    debit_credit_identifier. Further processing in DATEV Unternehmen online depends on these properties.
    For example, a document type with the category “invoice_received” is processed as an incoming
    invoice.

    The document type in DATEV applications is called “Belegtyp”. A client can have a lot of different
    document types. There are document types with special restrictions – document types with the
    category “personnel_documents” and “travel_expense_documents”. This means that the user’s DATEV
    authentication method needs to be configured with special rights.

    **Please note:** If the returned list is empty then the client has no document types. Normally, a
    client has at least four document types.


     **Get list of document types**



    ```json
    HTTP/1.1 200 OK
    Content-Encoding: gzip
    Transfer-Encoding: chunked

    [
    {
    \"name\":\"Rechnungseingang\",
    \"category\":\"invoices_received\",
    \"debit_credit_identifier\":\"debit\"
    },
    {
    \"name\":\"Rechnungsausgang\",
    \"category\":\"outgoing_invoices\",
    \"debit_credit_identifier\":\"credit\"
    },
    {
    \"name\":\"Kasse\",
    \"category\":\"other_documents\"
    },
    {
    \"name\":\"Sonstige\",
    \"category\":\"other_documents\"
    }
    ]

    ```

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['DocumentType']]
     """


    return sync_detailed(
        client_id=client_id,
client=client,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, list['DocumentType']]]:
    r""" Returns a list of document types for a given client.

     Returns a list of document types for a given client. The user is normally only familiar with the
    name of the document type. The document type is determined by the properties category and
    debit_credit_identifier. Further processing in DATEV Unternehmen online depends on these properties.
    For example, a document type with the category “invoice_received” is processed as an incoming
    invoice.

    The document type in DATEV applications is called “Belegtyp”. A client can have a lot of different
    document types. There are document types with special restrictions – document types with the
    category “personnel_documents” and “travel_expense_documents”. This means that the user’s DATEV
    authentication method needs to be configured with special rights.

    **Please note:** If the returned list is empty then the client has no document types. Normally, a
    client has at least four document types.


     **Get list of document types**



    ```json
    HTTP/1.1 200 OK
    Content-Encoding: gzip
    Transfer-Encoding: chunked

    [
    {
    \"name\":\"Rechnungseingang\",
    \"category\":\"invoices_received\",
    \"debit_credit_identifier\":\"debit\"
    },
    {
    \"name\":\"Rechnungsausgang\",
    \"category\":\"outgoing_invoices\",
    \"debit_credit_identifier\":\"credit\"
    },
    {
    \"name\":\"Kasse\",
    \"category\":\"other_documents\"
    },
    {
    \"name\":\"Sonstige\",
    \"category\":\"other_documents\"
    }
    ]

    ```

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['DocumentType']]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, list['DocumentType']]]:
    r""" Returns a list of document types for a given client.

     Returns a list of document types for a given client. The user is normally only familiar with the
    name of the document type. The document type is determined by the properties category and
    debit_credit_identifier. Further processing in DATEV Unternehmen online depends on these properties.
    For example, a document type with the category “invoice_received” is processed as an incoming
    invoice.

    The document type in DATEV applications is called “Belegtyp”. A client can have a lot of different
    document types. There are document types with special restrictions – document types with the
    category “personnel_documents” and “travel_expense_documents”. This means that the user’s DATEV
    authentication method needs to be configured with special rights.

    **Please note:** If the returned list is empty then the client has no document types. Normally, a
    client has at least four document types.


     **Get list of document types**



    ```json
    HTTP/1.1 200 OK
    Content-Encoding: gzip
    Transfer-Encoding: chunked

    [
    {
    \"name\":\"Rechnungseingang\",
    \"category\":\"invoices_received\",
    \"debit_credit_identifier\":\"debit\"
    },
    {
    \"name\":\"Rechnungsausgang\",
    \"category\":\"outgoing_invoices\",
    \"debit_credit_identifier\":\"credit\"
    },
    {
    \"name\":\"Kasse\",
    \"category\":\"other_documents\"
    },
    {
    \"name\":\"Sonstige\",
    \"category\":\"other_documents\"
    }
    ]

    ```

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['DocumentType']]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,

    )).parsed
