from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.client_basics import ClientBasics
from typing import cast



def _get_kwargs(
    client_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/clients/{client_id}".format(client_id=client_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, ClientBasics]]:
    if response.status_code == 200:
        response_200 = ClientBasics.from_dict(response.json())



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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, ClientBasics]]:
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

) -> Response[Union[Any, ClientBasics]]:
    r""" Returns a list of basic data about a given client.

     Returns a list of basic data about a given client. With this information, the third-party solution
    can check whether the configuration of the client is suitable and prepared for data transfer: a
    client for the application Belege online and a matching fiscal year for the editing form
    \\"extended\\" , for the application Rechnungseingangsbuch online for transferring accounts payable
    data, for the application Rechnungsausgangsbuch online for transferring accounts receivable data,
    and/or for the application Kassenbuch online for transferring cash entries are necessary.

    **Please note:** If a matching fiscal year is not present, but there is a previous fiscal year that
    meets certain requirements, DATEV will automatically generate the subsequent matching fiscal year.
    This will be done within the operation \\"create a data transfer (dxso-job)\\" . This function is
    not available for the application Kassenbuch online.

    **Example: No data import possible**

    The requirements for processing data are not fulfilled.

    ```json
    HTTP/1.1 200 OK
    Content-Type:application/json

    {\"client_number\":102,\"consultant_number\":455148,
    \"id\":\"455148-102\",\"name\":\"Muster GmbH 3\",
    \"is_document_management_available\":\"false\",
    \"basic_accounting_information\":[]}
    ```

    **Example: Automatic generation of new fiscal year in a complex scenario**

    The requirements for processing data are fulfilled for
    - Cash ledger data for 2015, 2016, and 2017
    - Incoming invoice data for 2015, 2016, and 2017 (automatic generation of the fiscal year 2017 is
    possible)
    - Outgoing invoice data for 2015, 2016, and 2017 (automatic generation of the fiscal year 2017 is
    possible)

    ```json
    HTTP/1.1 200 OK
    Content-Type:application/json

    {\"client_number\":4,\"consultant_number\":455148,
    \"id\":\"455148-4\",\"name\":\"Muster GmbH 4\",
    \"is_document_management_available\":\"true\",
    \"basic_accounting_information\":[
    {\"fiscal_year_start\":\"2015-01-01\",
    \"fiscal_year_end\":\"2015-12-31\",
    \"account_length\":4,
    \"ledgers\":
    {\"is_accounts_payable_ledger_available\":\"true\",
    \"is_accounts_receivable_ledger_available\":\"true\",
    \"is_cash_ledger_available\":\"true\"}
    },
    {\"fiscal_year_start\":\"2016-01-01\",
    \"fiscal_year_end\":\"2016-12-31\",
    \"account_length\":4,
    \"ledgers\":{
    \"is_accounts_payable_ledger_available\":\"true\",
    \"is_accounts_receivable_ledger_available\":\"true\",
    \"is_cash_ledger_available\":\"true\"}
    },
    {\"fiscal_year_start\":\"2017-01-01\",
    \"fiscal_year_end\":\"2017-12-31\",
    \"account_length\":4,
    \"ledgers\":{
    \"is_accounts_payable_ledger_available\":\"false\",
    \"is_accounts_receivable_ledger_available\":\"false\",
    \"is_cash_ledger_available\":\"true\"}
    }]}
    ```

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClientBasics]]
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

) -> Optional[Union[Any, ClientBasics]]:
    r""" Returns a list of basic data about a given client.

     Returns a list of basic data about a given client. With this information, the third-party solution
    can check whether the configuration of the client is suitable and prepared for data transfer: a
    client for the application Belege online and a matching fiscal year for the editing form
    \\"extended\\" , for the application Rechnungseingangsbuch online for transferring accounts payable
    data, for the application Rechnungsausgangsbuch online for transferring accounts receivable data,
    and/or for the application Kassenbuch online for transferring cash entries are necessary.

    **Please note:** If a matching fiscal year is not present, but there is a previous fiscal year that
    meets certain requirements, DATEV will automatically generate the subsequent matching fiscal year.
    This will be done within the operation \\"create a data transfer (dxso-job)\\" . This function is
    not available for the application Kassenbuch online.

    **Example: No data import possible**

    The requirements for processing data are not fulfilled.

    ```json
    HTTP/1.1 200 OK
    Content-Type:application/json

    {\"client_number\":102,\"consultant_number\":455148,
    \"id\":\"455148-102\",\"name\":\"Muster GmbH 3\",
    \"is_document_management_available\":\"false\",
    \"basic_accounting_information\":[]}
    ```

    **Example: Automatic generation of new fiscal year in a complex scenario**

    The requirements for processing data are fulfilled for
    - Cash ledger data for 2015, 2016, and 2017
    - Incoming invoice data for 2015, 2016, and 2017 (automatic generation of the fiscal year 2017 is
    possible)
    - Outgoing invoice data for 2015, 2016, and 2017 (automatic generation of the fiscal year 2017 is
    possible)

    ```json
    HTTP/1.1 200 OK
    Content-Type:application/json

    {\"client_number\":4,\"consultant_number\":455148,
    \"id\":\"455148-4\",\"name\":\"Muster GmbH 4\",
    \"is_document_management_available\":\"true\",
    \"basic_accounting_information\":[
    {\"fiscal_year_start\":\"2015-01-01\",
    \"fiscal_year_end\":\"2015-12-31\",
    \"account_length\":4,
    \"ledgers\":
    {\"is_accounts_payable_ledger_available\":\"true\",
    \"is_accounts_receivable_ledger_available\":\"true\",
    \"is_cash_ledger_available\":\"true\"}
    },
    {\"fiscal_year_start\":\"2016-01-01\",
    \"fiscal_year_end\":\"2016-12-31\",
    \"account_length\":4,
    \"ledgers\":{
    \"is_accounts_payable_ledger_available\":\"true\",
    \"is_accounts_receivable_ledger_available\":\"true\",
    \"is_cash_ledger_available\":\"true\"}
    },
    {\"fiscal_year_start\":\"2017-01-01\",
    \"fiscal_year_end\":\"2017-12-31\",
    \"account_length\":4,
    \"ledgers\":{
    \"is_accounts_payable_ledger_available\":\"false\",
    \"is_accounts_receivable_ledger_available\":\"false\",
    \"is_cash_ledger_available\":\"true\"}
    }]}
    ```

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClientBasics]
     """


    return sync_detailed(
        client_id=client_id,
client=client,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, ClientBasics]]:
    r""" Returns a list of basic data about a given client.

     Returns a list of basic data about a given client. With this information, the third-party solution
    can check whether the configuration of the client is suitable and prepared for data transfer: a
    client for the application Belege online and a matching fiscal year for the editing form
    \\"extended\\" , for the application Rechnungseingangsbuch online for transferring accounts payable
    data, for the application Rechnungsausgangsbuch online for transferring accounts receivable data,
    and/or for the application Kassenbuch online for transferring cash entries are necessary.

    **Please note:** If a matching fiscal year is not present, but there is a previous fiscal year that
    meets certain requirements, DATEV will automatically generate the subsequent matching fiscal year.
    This will be done within the operation \\"create a data transfer (dxso-job)\\" . This function is
    not available for the application Kassenbuch online.

    **Example: No data import possible**

    The requirements for processing data are not fulfilled.

    ```json
    HTTP/1.1 200 OK
    Content-Type:application/json

    {\"client_number\":102,\"consultant_number\":455148,
    \"id\":\"455148-102\",\"name\":\"Muster GmbH 3\",
    \"is_document_management_available\":\"false\",
    \"basic_accounting_information\":[]}
    ```

    **Example: Automatic generation of new fiscal year in a complex scenario**

    The requirements for processing data are fulfilled for
    - Cash ledger data for 2015, 2016, and 2017
    - Incoming invoice data for 2015, 2016, and 2017 (automatic generation of the fiscal year 2017 is
    possible)
    - Outgoing invoice data for 2015, 2016, and 2017 (automatic generation of the fiscal year 2017 is
    possible)

    ```json
    HTTP/1.1 200 OK
    Content-Type:application/json

    {\"client_number\":4,\"consultant_number\":455148,
    \"id\":\"455148-4\",\"name\":\"Muster GmbH 4\",
    \"is_document_management_available\":\"true\",
    \"basic_accounting_information\":[
    {\"fiscal_year_start\":\"2015-01-01\",
    \"fiscal_year_end\":\"2015-12-31\",
    \"account_length\":4,
    \"ledgers\":
    {\"is_accounts_payable_ledger_available\":\"true\",
    \"is_accounts_receivable_ledger_available\":\"true\",
    \"is_cash_ledger_available\":\"true\"}
    },
    {\"fiscal_year_start\":\"2016-01-01\",
    \"fiscal_year_end\":\"2016-12-31\",
    \"account_length\":4,
    \"ledgers\":{
    \"is_accounts_payable_ledger_available\":\"true\",
    \"is_accounts_receivable_ledger_available\":\"true\",
    \"is_cash_ledger_available\":\"true\"}
    },
    {\"fiscal_year_start\":\"2017-01-01\",
    \"fiscal_year_end\":\"2017-12-31\",
    \"account_length\":4,
    \"ledgers\":{
    \"is_accounts_payable_ledger_available\":\"false\",
    \"is_accounts_receivable_ledger_available\":\"false\",
    \"is_cash_ledger_available\":\"true\"}
    }]}
    ```

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClientBasics]]
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

) -> Optional[Union[Any, ClientBasics]]:
    r""" Returns a list of basic data about a given client.

     Returns a list of basic data about a given client. With this information, the third-party solution
    can check whether the configuration of the client is suitable and prepared for data transfer: a
    client for the application Belege online and a matching fiscal year for the editing form
    \\"extended\\" , for the application Rechnungseingangsbuch online for transferring accounts payable
    data, for the application Rechnungsausgangsbuch online for transferring accounts receivable data,
    and/or for the application Kassenbuch online for transferring cash entries are necessary.

    **Please note:** If a matching fiscal year is not present, but there is a previous fiscal year that
    meets certain requirements, DATEV will automatically generate the subsequent matching fiscal year.
    This will be done within the operation \\"create a data transfer (dxso-job)\\" . This function is
    not available for the application Kassenbuch online.

    **Example: No data import possible**

    The requirements for processing data are not fulfilled.

    ```json
    HTTP/1.1 200 OK
    Content-Type:application/json

    {\"client_number\":102,\"consultant_number\":455148,
    \"id\":\"455148-102\",\"name\":\"Muster GmbH 3\",
    \"is_document_management_available\":\"false\",
    \"basic_accounting_information\":[]}
    ```

    **Example: Automatic generation of new fiscal year in a complex scenario**

    The requirements for processing data are fulfilled for
    - Cash ledger data for 2015, 2016, and 2017
    - Incoming invoice data for 2015, 2016, and 2017 (automatic generation of the fiscal year 2017 is
    possible)
    - Outgoing invoice data for 2015, 2016, and 2017 (automatic generation of the fiscal year 2017 is
    possible)

    ```json
    HTTP/1.1 200 OK
    Content-Type:application/json

    {\"client_number\":4,\"consultant_number\":455148,
    \"id\":\"455148-4\",\"name\":\"Muster GmbH 4\",
    \"is_document_management_available\":\"true\",
    \"basic_accounting_information\":[
    {\"fiscal_year_start\":\"2015-01-01\",
    \"fiscal_year_end\":\"2015-12-31\",
    \"account_length\":4,
    \"ledgers\":
    {\"is_accounts_payable_ledger_available\":\"true\",
    \"is_accounts_receivable_ledger_available\":\"true\",
    \"is_cash_ledger_available\":\"true\"}
    },
    {\"fiscal_year_start\":\"2016-01-01\",
    \"fiscal_year_end\":\"2016-12-31\",
    \"account_length\":4,
    \"ledgers\":{
    \"is_accounts_payable_ledger_available\":\"true\",
    \"is_accounts_receivable_ledger_available\":\"true\",
    \"is_cash_ledger_available\":\"true\"}
    },
    {\"fiscal_year_start\":\"2017-01-01\",
    \"fiscal_year_end\":\"2017-12-31\",
    \"account_length\":4,
    \"ledgers\":{
    \"is_accounts_payable_ledger_available\":\"false\",
    \"is_accounts_receivable_ledger_available\":\"false\",
    \"is_cash_ledger_available\":\"true\"}
    }]}
    ```

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClientBasics]
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,

    )).parsed
