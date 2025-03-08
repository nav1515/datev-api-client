from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dx_so_job_creation_info import DXSoJobCreationInfo
from typing import cast



def _get_kwargs(
    client_id: str,
    *,
    body: DXSoJobCreationInfo,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/clients/{client_id}/dxso-jobs".format(client_id=client_id,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

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
    *,
    client: AuthenticatedClient,
    body: DXSoJobCreationInfo,

) -> Response[Any]:
    r""" A data transfer (dxso-job) is created and the ID of the data transfer (dxso-job) is returned.

     A data transfer (dxso-job) is created and the ID for this data transfer (dxso-job) is returned if
    the requirements are fulfilled.

    The transferred data has to be in the format DATEV XML-Schnittstelle online version 4.0 or higher.
    The transferred data can only be processed if the configuration of the client is suitable for data
    processing: a client for the application Belege online in DATEV Unternehmen online and a matching
    fiscal year for the editing form \"extended\" , for the application Rechnungseingangsbuch online for
    transferring accounts payable data, for the application Rechnungsausgangsbuch online for
    transferring accounts receivable data, and/or for the application Kassenbuch online for transferring
    cash entries are necessary.

    Therefore, it is recommended to determine the data by creating the data transfer and set the
    parameters import_type (type of data) and accounting_month. If the parameters are set and a matching
    fiscal year is not present, but there is a previous fiscal year that meets certain requirements,
    DATEV will automatically generate the subsequent matching fiscal year. This function is not
    available for the application Kassenbuch online.

    It is recommended that the transferred data is in the format **DATEV LedgerImport-Package**: <table>
    <thead> <tr> <th>Data type</th> <th>Extension in document.xml of DATEV LedgerImport-Packages</th>
    <th>Element in the data file of the DATEV LedgerImport-Packages</th> <th>Value for API parameter
    'import_type'</th> <th>Automatic generation of the next fiscal year</th> </tr> </thead> <tbody> <tr>
    <td>Incoming invoices</td> <td>xsi:type='accountsPayableLedger'</td> <td>accountsPayableLedger</td>
    <td>'import_type': 'accountsPayableLedgerImport'</td> <td>possible </td> </tr> <tr> <td>Outgoing
    invoices</td> <td>xsi:type='accountsReceivableLedger'</td> <td>accountsReceivableLedger</td>
    <td>'import_type': 'accountsReceivableLedgerImport'</td> <td>possible</td> </tr> <tr> <td>Cash
    entries</td> <td>xsi:type='cashLedger'</td> <td>cashLedger</td> <td>'import_type':
    'cashLedgerImport' </td> <td>not supported</td> </tr> </tbody> </table>


    Alternatively, invoices can be in the format **DATEV Invoice-Package**:

     <table> <thead> <tr> <th>Data type</th> <th>Extension in document.xml of DATEV Invoice-
    Packages</th> <th>Element in the data file of the DATEV Invoice-Packages</th> <th>Value for API
    parameter 'import_type'</th> <th>Automatic generation of the next fiscal year</th> </tr> </thead>
    <tbody> <tr> <td>Incoming invoices</td> <td>xsi:type'invoice' with property 'Incoming' as
    'InvoiceType'</td> <td>invoice</td> <td>'import_type': 'accountsPayableLedgerImport'</td>
    <td>possible </td> </tr> <tr> <td>Outgoing invoices</td> <td>xsi:type='invoice' with property
    'Outgoing' as 'InvoiceType' </td> <td>invoice</td> <td>'import_type':
    'accountsReceivableLedgerImport'</td> <td>possible</td> </tr> </tbody> </table>


    **Notes:**
    The third-party solution ensures that for each variant of data (accounts payable data, accounts
    receivable data, and cash entries) and for each accounting period/month an own data transfer (dxso-
    job) is created.

    The \"content type\" header must be \"application/json\".

    **Remember:** When working with Kassenbuch online, the cash data must be supplied in the correct
    order so as to avoid a negative cash balance. Data transfers (dxso-job) cannot be processed in
    parallel. Kassenbuch online cannot be edited during import and vice versa. A new data transfer
    (dxso-job) can only be started when the previous data transfer (dxso-job) for cash data has been
    completed.

    **Example: DATEV accountsReceivableLedgerImport-Package**


    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/ HTTP/1.1
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {
    \"import_type\":\"accountsReceivableLedgerImport\",
    \"accounting_month\":\"2017-01\"
    }
    ```


    The third-party solution has to analyze the returned information. The name of the correct ledger
    folder is part of the information in document.xml of the DATEV accountsReceivableLedgerImport-
    Package.


    **Example: DATEV accountsPayableLedgerImport-Package**

    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/ HTTP/1.1
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {
    \"import_type\":\"accountsPayableLedgerImport\",
    \"accounting_month\":\"2017-01\"
    }
    ```


    The third-party solution has to analyze the returned information. The name of the correct ledger
    folder is part of the information in document.xml of the DATEV accountsPayableLedgerImport-Package.

    **Example: DATEV cashLedgerImport-Package**

    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {
    \"import_type\":\"cashLedgerImport\",
    \"accounting_month\":\"2017-01\"
    }
    ```

    The third-party solution has to analyze the returned information. The name of the correct cash
    ledger is part of the information in document.xml of the DATEV cashLedgerImport-Package.

    **Example: DATEV invoice-Package with incoming invoices to one period**

    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {
    \"import_type\":\"accountsPayableLedgerImport\",
    \"accounting_month\":\"2017-01\"
    }
    ```

    The third-party solution has to analyze the returned information. Please note that in this case the
    name of the ledger folder is not a part of the information in document.xml.

    **Example: Creation of a data transfer (dxso-jobs) without parameters**

    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {

    }
    ```

    The third-party solution has to check and receive further information on its own (fiscal year,
    account_length, ledger_folder_names, etc.). During the processing of invoice data, the automatic
    generation of the subsequent fiscal year will also be performed by the DATEV solution.

    Args:
        client_id (str):
        body (DXSoJobCreationInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,
    body: DXSoJobCreationInfo,

) -> Response[Any]:
    r""" A data transfer (dxso-job) is created and the ID of the data transfer (dxso-job) is returned.

     A data transfer (dxso-job) is created and the ID for this data transfer (dxso-job) is returned if
    the requirements are fulfilled.

    The transferred data has to be in the format DATEV XML-Schnittstelle online version 4.0 or higher.
    The transferred data can only be processed if the configuration of the client is suitable for data
    processing: a client for the application Belege online in DATEV Unternehmen online and a matching
    fiscal year for the editing form \"extended\" , for the application Rechnungseingangsbuch online for
    transferring accounts payable data, for the application Rechnungsausgangsbuch online for
    transferring accounts receivable data, and/or for the application Kassenbuch online for transferring
    cash entries are necessary.

    Therefore, it is recommended to determine the data by creating the data transfer and set the
    parameters import_type (type of data) and accounting_month. If the parameters are set and a matching
    fiscal year is not present, but there is a previous fiscal year that meets certain requirements,
    DATEV will automatically generate the subsequent matching fiscal year. This function is not
    available for the application Kassenbuch online.

    It is recommended that the transferred data is in the format **DATEV LedgerImport-Package**: <table>
    <thead> <tr> <th>Data type</th> <th>Extension in document.xml of DATEV LedgerImport-Packages</th>
    <th>Element in the data file of the DATEV LedgerImport-Packages</th> <th>Value for API parameter
    'import_type'</th> <th>Automatic generation of the next fiscal year</th> </tr> </thead> <tbody> <tr>
    <td>Incoming invoices</td> <td>xsi:type='accountsPayableLedger'</td> <td>accountsPayableLedger</td>
    <td>'import_type': 'accountsPayableLedgerImport'</td> <td>possible </td> </tr> <tr> <td>Outgoing
    invoices</td> <td>xsi:type='accountsReceivableLedger'</td> <td>accountsReceivableLedger</td>
    <td>'import_type': 'accountsReceivableLedgerImport'</td> <td>possible</td> </tr> <tr> <td>Cash
    entries</td> <td>xsi:type='cashLedger'</td> <td>cashLedger</td> <td>'import_type':
    'cashLedgerImport' </td> <td>not supported</td> </tr> </tbody> </table>


    Alternatively, invoices can be in the format **DATEV Invoice-Package**:

     <table> <thead> <tr> <th>Data type</th> <th>Extension in document.xml of DATEV Invoice-
    Packages</th> <th>Element in the data file of the DATEV Invoice-Packages</th> <th>Value for API
    parameter 'import_type'</th> <th>Automatic generation of the next fiscal year</th> </tr> </thead>
    <tbody> <tr> <td>Incoming invoices</td> <td>xsi:type'invoice' with property 'Incoming' as
    'InvoiceType'</td> <td>invoice</td> <td>'import_type': 'accountsPayableLedgerImport'</td>
    <td>possible </td> </tr> <tr> <td>Outgoing invoices</td> <td>xsi:type='invoice' with property
    'Outgoing' as 'InvoiceType' </td> <td>invoice</td> <td>'import_type':
    'accountsReceivableLedgerImport'</td> <td>possible</td> </tr> </tbody> </table>


    **Notes:**
    The third-party solution ensures that for each variant of data (accounts payable data, accounts
    receivable data, and cash entries) and for each accounting period/month an own data transfer (dxso-
    job) is created.

    The \"content type\" header must be \"application/json\".

    **Remember:** When working with Kassenbuch online, the cash data must be supplied in the correct
    order so as to avoid a negative cash balance. Data transfers (dxso-job) cannot be processed in
    parallel. Kassenbuch online cannot be edited during import and vice versa. A new data transfer
    (dxso-job) can only be started when the previous data transfer (dxso-job) for cash data has been
    completed.

    **Example: DATEV accountsReceivableLedgerImport-Package**


    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/ HTTP/1.1
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {
    \"import_type\":\"accountsReceivableLedgerImport\",
    \"accounting_month\":\"2017-01\"
    }
    ```


    The third-party solution has to analyze the returned information. The name of the correct ledger
    folder is part of the information in document.xml of the DATEV accountsReceivableLedgerImport-
    Package.


    **Example: DATEV accountsPayableLedgerImport-Package**

    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/ HTTP/1.1
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {
    \"import_type\":\"accountsPayableLedgerImport\",
    \"accounting_month\":\"2017-01\"
    }
    ```


    The third-party solution has to analyze the returned information. The name of the correct ledger
    folder is part of the information in document.xml of the DATEV accountsPayableLedgerImport-Package.

    **Example: DATEV cashLedgerImport-Package**

    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {
    \"import_type\":\"cashLedgerImport\",
    \"accounting_month\":\"2017-01\"
    }
    ```

    The third-party solution has to analyze the returned information. The name of the correct cash
    ledger is part of the information in document.xml of the DATEV cashLedgerImport-Package.

    **Example: DATEV invoice-Package with incoming invoices to one period**

    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {
    \"import_type\":\"accountsPayableLedgerImport\",
    \"accounting_month\":\"2017-01\"
    }
    ```

    The third-party solution has to analyze the returned information. Please note that in this case the
    name of the ledger folder is not a part of the information in document.xml.

    **Example: Creation of a data transfer (dxso-jobs) without parameters**

    ```json
    POST /accounting/v1/clients/{client-id}/dxso-jobs/
    Content-Type: application/json;charset=UTF-8
    Authorization: bearer <access_token>
    Content-Length: <length>
    Host: <resourceServer>

    {

    }
    ```

    The third-party solution has to check and receive further information on its own (fiscal year,
    account_length, ledger_folder_names, etc.). During the processing of invoice data, the automatic
    generation of the subsequent fiscal year will also be performed by the DATEV solution.

    Args:
        client_id (str):
        body (DXSoJobCreationInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        client_id=client_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

