from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_clients_client_id_dxso_jobs_job_id_files_body import PostClientsClientIdDxsoJobsJobIdFilesBody
from typing import cast



def _get_kwargs(
    client_id: str,
    job_id: str,
    *,
    body: PostClientsClientIdDxsoJobsJobIdFilesBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/clients/{client_id}/dxso-jobs/{job_id}/files".format(client_id=client_id,job_id=job_id,),
    }

    _body = body.to_multipart()


    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 201:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 503:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    body: PostClientsClientIdDxsoJobsJobIdFilesBody,

) -> Response[Any]:
    r""" Attaches files to a data transfer (dxso-job)

     Attaches files to a data transfer (dxso-job). Each file is transferred as a single file and not as a
    ZIP file as it is described in the documentation of DATEV XML-Schnittstelle online. The third-party
    solution ensures that only correctly validated data are transferred to the DATEV data center. The
    data format and the file size of the files have to be supported by DATEV.

    The files (including the file information) need to be transferred as data type \\"multipart/form-
    data\\" to ensure all details are transferred.

    **Please note:** It is recommended that file names be encoded in UTF8. Unicode characters have to be
    precomposed characters; that is, each special character, such as an umlaut ( &auml;, &uuml;,
    &ouml;), has to be one single code point. Decomposed characters are not supported. There exists a
    white list for signs that may be used in file names. Unallowed signs will be replaced by underscore.
    These signs may be used: Space &()+-._ 0-9A-Za-
    zÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ

    **Example: Multipart upload**
    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/{job-id}/files HTTP/1.1
    Content-Type: multipart/form-data; boundary=\"----=_Part_2_7463675.1448450513503\"
    MIME-Version: 1.0
    Authorization: Bearer <access_token>
    Content-Length: 1776
    Host: <resourceServer>

    ------=_Part_2_7463675.1448450513503
    Content-Type: text/xml; charset=Cp1252; name=AR-2015-0001.xml
    Content-Transfer-Encoding: binary
    Content-Disposition: form-data; name=\"files\"; filename=\"AR-2015-0001.xml\"
    <?xml version=\"1.0\" encoding=\"utf-8\"?>
    ...
    ```

    Args:
        client_id (str):
        job_id (str):
        body (PostClientsClientIdDxsoJobsJobIdFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    client_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient,
    body: PostClientsClientIdDxsoJobsJobIdFilesBody,

) -> Response[Any]:
    r""" Attaches files to a data transfer (dxso-job)

     Attaches files to a data transfer (dxso-job). Each file is transferred as a single file and not as a
    ZIP file as it is described in the documentation of DATEV XML-Schnittstelle online. The third-party
    solution ensures that only correctly validated data are transferred to the DATEV data center. The
    data format and the file size of the files have to be supported by DATEV.

    The files (including the file information) need to be transferred as data type \\"multipart/form-
    data\\" to ensure all details are transferred.

    **Please note:** It is recommended that file names be encoded in UTF8. Unicode characters have to be
    precomposed characters; that is, each special character, such as an umlaut ( &auml;, &uuml;,
    &ouml;), has to be one single code point. Decomposed characters are not supported. There exists a
    white list for signs that may be used in file names. Unallowed signs will be replaced by underscore.
    These signs may be used: Space &()+-._ 0-9A-Za-
    zÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ

    **Example: Multipart upload**
    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/{job-id}/files HTTP/1.1
    Content-Type: multipart/form-data; boundary=\"----=_Part_2_7463675.1448450513503\"
    MIME-Version: 1.0
    Authorization: Bearer <access_token>
    Content-Length: 1776
    Host: <resourceServer>

    ------=_Part_2_7463675.1448450513503
    Content-Type: text/xml; charset=Cp1252; name=AR-2015-0001.xml
    Content-Transfer-Encoding: binary
    Content-Disposition: form-data; name=\"files\"; filename=\"AR-2015-0001.xml\"
    <?xml version=\"1.0\" encoding=\"utf-8\"?>
    ...
    ```

    Args:
        client_id (str):
        job_id (str):
        body (PostClientsClientIdDxsoJobsJobIdFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
job_id=job_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

