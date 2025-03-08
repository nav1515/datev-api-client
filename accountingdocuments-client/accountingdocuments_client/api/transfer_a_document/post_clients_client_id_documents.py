from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.document import Document
from ...models.post_clients_client_id_documents_body import PostClientsClientIdDocumentsBody
from typing import cast



def _get_kwargs(
    client_id: str,
    *,
    body: PostClientsClientIdDocumentsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/clients/{client_id}/documents".format(client_id=client_id,),
    }

    _body = body.to_multipart()


    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, Document]]:
    if response.status_code == 201:
        response_201 = Document.from_dict(response.json())



        return response_201
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, Document]]:
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
    body: PostClientsClientIdDocumentsBody,

) -> Response[Union[Any, Document]]:
    r""" Transfers a document

     A new accounting document will be transferred to Belege online in DATEV Unternehmen online. Each
    accounting document is transferred in a multipart object as a single file with optional metadata
    (document type and note). The content-type indicated in the multipart object has to correspond to
    the file. The accepted content-types and the accepted file size are determined by Belege online.
    Exception: ZIP files are not supported.

    It is recommended that the user chooses the document type for each accounting document, as the
    document type affects further processing by DATEV. The chosen document type has to be existent at
    the given client. Please check the list of document types for a given client. The user should also
    have the possibility to choose “no document type”.

    If the value of the document_type is empty, then the parameter will be ignored and will not be
    returned in the response. In this case, and if the parameter document_type is not used, the term
    “ohne Belegtyp” (without document type) is displayed in the DATEV applications.

    **Please note:**
    It is recommended that file names are encoded in UTF8. Unicode characters have to be precomposed
    characters; in other words, each special character, such as an umlaut (ä, ü, ö), has to be a single
    code point. Decomposed characters are not supported. This applies to both the file name and the
    metadata. There exists a white list for signs that may be used in file names. Unallowed signs will
    be replaced by underscore.
    These signs may be used: Space &()+-._ 0-9A-Za-
    zÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ

    Large files require more storage space and can slow down load times within DATEV Unternehmen online
    and the DATEV Rechnungswesen-Programm. We recommend that the user is informed whenever the file size
    exceeds 500 kB.

    **Example:Document has been imported successfully:**


    ```json
    HTTP/1.1 201 Processed
    Content-Encoding: gzip
    Transfer-Encoding: chunked

    {
    \"files\":[{
    \"name\":\"Test-File.pdf\",
    \"size\":\"123456\"
    }],
    \"document_type\":\"Rechnungseingang\",
    \"note\":\"Beleg von Beispiel GmbH\"
    }

    ```

    Args:
        client_id (str):
        body (PostClientsClientIdDocumentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Document]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: AuthenticatedClient,
    body: PostClientsClientIdDocumentsBody,

) -> Optional[Union[Any, Document]]:
    r""" Transfers a document

     A new accounting document will be transferred to Belege online in DATEV Unternehmen online. Each
    accounting document is transferred in a multipart object as a single file with optional metadata
    (document type and note). The content-type indicated in the multipart object has to correspond to
    the file. The accepted content-types and the accepted file size are determined by Belege online.
    Exception: ZIP files are not supported.

    It is recommended that the user chooses the document type for each accounting document, as the
    document type affects further processing by DATEV. The chosen document type has to be existent at
    the given client. Please check the list of document types for a given client. The user should also
    have the possibility to choose “no document type”.

    If the value of the document_type is empty, then the parameter will be ignored and will not be
    returned in the response. In this case, and if the parameter document_type is not used, the term
    “ohne Belegtyp” (without document type) is displayed in the DATEV applications.

    **Please note:**
    It is recommended that file names are encoded in UTF8. Unicode characters have to be precomposed
    characters; in other words, each special character, such as an umlaut (ä, ü, ö), has to be a single
    code point. Decomposed characters are not supported. This applies to both the file name and the
    metadata. There exists a white list for signs that may be used in file names. Unallowed signs will
    be replaced by underscore.
    These signs may be used: Space &()+-._ 0-9A-Za-
    zÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ

    Large files require more storage space and can slow down load times within DATEV Unternehmen online
    and the DATEV Rechnungswesen-Programm. We recommend that the user is informed whenever the file size
    exceeds 500 kB.

    **Example:Document has been imported successfully:**


    ```json
    HTTP/1.1 201 Processed
    Content-Encoding: gzip
    Transfer-Encoding: chunked

    {
    \"files\":[{
    \"name\":\"Test-File.pdf\",
    \"size\":\"123456\"
    }],
    \"document_type\":\"Rechnungseingang\",
    \"note\":\"Beleg von Beispiel GmbH\"
    }

    ```

    Args:
        client_id (str):
        body (PostClientsClientIdDocumentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Document]
     """


    return sync_detailed(
        client_id=client_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,
    body: PostClientsClientIdDocumentsBody,

) -> Response[Union[Any, Document]]:
    r""" Transfers a document

     A new accounting document will be transferred to Belege online in DATEV Unternehmen online. Each
    accounting document is transferred in a multipart object as a single file with optional metadata
    (document type and note). The content-type indicated in the multipart object has to correspond to
    the file. The accepted content-types and the accepted file size are determined by Belege online.
    Exception: ZIP files are not supported.

    It is recommended that the user chooses the document type for each accounting document, as the
    document type affects further processing by DATEV. The chosen document type has to be existent at
    the given client. Please check the list of document types for a given client. The user should also
    have the possibility to choose “no document type”.

    If the value of the document_type is empty, then the parameter will be ignored and will not be
    returned in the response. In this case, and if the parameter document_type is not used, the term
    “ohne Belegtyp” (without document type) is displayed in the DATEV applications.

    **Please note:**
    It is recommended that file names are encoded in UTF8. Unicode characters have to be precomposed
    characters; in other words, each special character, such as an umlaut (ä, ü, ö), has to be a single
    code point. Decomposed characters are not supported. This applies to both the file name and the
    metadata. There exists a white list for signs that may be used in file names. Unallowed signs will
    be replaced by underscore.
    These signs may be used: Space &()+-._ 0-9A-Za-
    zÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ

    Large files require more storage space and can slow down load times within DATEV Unternehmen online
    and the DATEV Rechnungswesen-Programm. We recommend that the user is informed whenever the file size
    exceeds 500 kB.

    **Example:Document has been imported successfully:**


    ```json
    HTTP/1.1 201 Processed
    Content-Encoding: gzip
    Transfer-Encoding: chunked

    {
    \"files\":[{
    \"name\":\"Test-File.pdf\",
    \"size\":\"123456\"
    }],
    \"document_type\":\"Rechnungseingang\",
    \"note\":\"Beleg von Beispiel GmbH\"
    }

    ```

    Args:
        client_id (str):
        body (PostClientsClientIdDocumentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Document]]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: AuthenticatedClient,
    body: PostClientsClientIdDocumentsBody,

) -> Optional[Union[Any, Document]]:
    r""" Transfers a document

     A new accounting document will be transferred to Belege online in DATEV Unternehmen online. Each
    accounting document is transferred in a multipart object as a single file with optional metadata
    (document type and note). The content-type indicated in the multipart object has to correspond to
    the file. The accepted content-types and the accepted file size are determined by Belege online.
    Exception: ZIP files are not supported.

    It is recommended that the user chooses the document type for each accounting document, as the
    document type affects further processing by DATEV. The chosen document type has to be existent at
    the given client. Please check the list of document types for a given client. The user should also
    have the possibility to choose “no document type”.

    If the value of the document_type is empty, then the parameter will be ignored and will not be
    returned in the response. In this case, and if the parameter document_type is not used, the term
    “ohne Belegtyp” (without document type) is displayed in the DATEV applications.

    **Please note:**
    It is recommended that file names are encoded in UTF8. Unicode characters have to be precomposed
    characters; in other words, each special character, such as an umlaut (ä, ü, ö), has to be a single
    code point. Decomposed characters are not supported. This applies to both the file name and the
    metadata. There exists a white list for signs that may be used in file names. Unallowed signs will
    be replaced by underscore.
    These signs may be used: Space &()+-._ 0-9A-Za-
    zÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ

    Large files require more storage space and can slow down load times within DATEV Unternehmen online
    and the DATEV Rechnungswesen-Programm. We recommend that the user is informed whenever the file size
    exceeds 500 kB.

    **Example:Document has been imported successfully:**


    ```json
    HTTP/1.1 201 Processed
    Content-Encoding: gzip
    Transfer-Encoding: chunked

    {
    \"files\":[{
    \"name\":\"Test-File.pdf\",
    \"size\":\"123456\"
    }],
    \"document_type\":\"Rechnungseingang\",
    \"note\":\"Beleg von Beispiel GmbH\"
    }

    ```

    Args:
        client_id (str):
        body (PostClientsClientIdDocumentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Document]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,
body=body,

    )).parsed
