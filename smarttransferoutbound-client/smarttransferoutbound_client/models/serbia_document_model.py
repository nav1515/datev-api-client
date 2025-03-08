from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.document_status import DocumentStatus
from ..models.document_type import DocumentType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
import datetime






T = TypeVar("T", bound="SerbiaDocumentModel")



@_attrs_define
class SerbiaDocumentModel:
    """ Defines the Serbia document model.

        Attributes:
            id (Union[Unset, int]): Gets or sets the identifier.
            type_ (Union[Unset, DocumentType]): List of document types supported by TRAFFIQX® API.<table style="font-size:
                12px;">  <thead style="background-color: rgba(0,0,0,0.05); border:1px solid rgba(0,0,0,0.08);">    <tr>      <td
                style="padding: 12px">Name</td>      <td style="padding: 12px">Description</td>    </tr>  </thead>  <tbody><tr
                style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px; font-weight:
                500;">Invoice</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The invoice document.</td></tr>
                <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px; font-weight:
                500;">CreditNote</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The credit note
                document.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px;
                font-weight: 500;">Order</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The order
                document.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px;
                font-weight: 500;">DeliveryNote</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The delivery
                note document.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px;
                font-weight: 500;">General</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The general
                document.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px;
                font-weight: 500;">Attachment</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The attachment
                document.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px;
                font-weight: 500;">PrivateAttachment</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The private
                attachment document.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px
                12px; font-weight: 500;">Other</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The type
                specifying that the document other than the defined ones.</td></tr>   </tbody></table>
            sub_type (Union[None, Unset, int]): Gets or sets the subtype.
            status (Union[Unset, DocumentStatus]): List of possible statuses for a document.<table style="font-size: 12px;">
                <thead style="background-color: rgba(0,0,0,0.05); border:1px solid rgba(0,0,0,0.08);">    <tr>      <td
                style="padding: 12px">Name</td>      <td style="padding: 12px">Description</td>    </tr>  </thead>  <tbody><tr
                style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px; font-weight:
                500;">Unknown</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The unknown status.</td></tr> <tr
                style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px; font-weight:
                500;">Initial</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The document is in initial
                state.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px; font-
                weight: 500;">Converting</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The document is
                currently being converted.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px
                12px 6px 12px; font-weight: 500;">Converted</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The
                document has been converted.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px
                12px 6px 12px; font-weight: 500;">Canceled</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The
                document has been cancelled.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px
                12px 6px 12px; font-weight: 500;">Held</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The
                document has been held.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px
                6px 12px; font-weight: 500;">RulesPending</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">There
                are rules pending to be applied to the document.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td
                style="padding: 6px 12px 6px 12px; font-weight: 500;">NoReceiver</td>  <td style="padding: 6px 12px 6px 12px;
                font-weight: 500;">There is no receiver found for the document.</td></tr> <tr style="border:1px solid
                rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">Temporary</td>  <td
                style="padding: 6px 12px 6px 12px; font-weight: 500;">The document is in temporary state.</td></tr> <tr
                style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px; font-weight:
                500;">Released</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The document has been
                released.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px;
                font-weight: 500;">Processing</td>  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">The document is in
                processing state.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px
                12px; font-weight: 500;">TransferInitialization</td>  <td style="padding: 6px 12px 6px 12px; font-weight:
                500;">The document transfer has been initialized.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">  <td
                style="padding: 6px 12px 6px 12px; font-weight: 500;">Transferring</td>  <td style="padding: 6px 12px 6px 12px;
                font-weight: 500;">The document is being transferred.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">
                <td style="padding: 6px 12px 6px 12px; font-weight: 500;">Prepared</td>  <td style="padding: 6px 12px 6px 12px;
                font-weight: 500;">The document has been prepared.</td></tr> <tr style="border:1px solid rgba(0,0,0,0.05);">
                <td style="padding: 6px 12px 6px 12px; font-weight: 500;">SignaturePending</td>  <td style="padding: 6px 12px
                6px 12px; font-weight: 500;">The document signatures are pending.</td></tr> <tr style="border:1px solid
                rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">Ready</td>  <td style="padding:
                6px 12px 6px 12px; font-weight: 500;">The document is ready.</td></tr> <tr style="border:1px solid
                rgba(0,0,0,0.05);">  <td style="padding: 6px 12px 6px 12px; font-weight: 500;">DeliveryBusy</td>  <td
                style="padding: 6px 12px 6px 12px; font-weight: 500;">The document delivery is busy.</td></tr>
                </tbody></table>
            reference (Union[None, Unset, str]): Gets or sets the reference.
            doc_date (Union[None, Unset, datetime.datetime]): Gets or sets the document date.
            match_field (Union[None, Unset, str]): Gets or sets the match field.
            custom_field (Union[None, Unset, str]): Gets or sets the custom field.
            invoice_id (Union[None, Unset, str]): Gets or sets the invoice identifier.
            invoice_state (Union[None, Unset, str]): Gets or sets the invoice state.
            created (Union[Unset, datetime.datetime]): Gets or sets the created.
            modified (Union[None, Unset, datetime.datetime]): Gets or sets the modified.
            comment (Union[None, Unset, str]): Gets or sets the comment.
     """

    id: Union[Unset, int] = UNSET
    type_: Union[Unset, DocumentType] = UNSET
    sub_type: Union[None, Unset, int] = UNSET
    status: Union[Unset, DocumentStatus] = UNSET
    reference: Union[None, Unset, str] = UNSET
    doc_date: Union[None, Unset, datetime.datetime] = UNSET
    match_field: Union[None, Unset, str] = UNSET
    custom_field: Union[None, Unset, str] = UNSET
    invoice_id: Union[None, Unset, str] = UNSET
    invoice_state: Union[None, Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[None, Unset, datetime.datetime] = UNSET
    comment: Union[None, Unset, str] = UNSET


    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        sub_type: Union[None, Unset, int]
        if isinstance(self.sub_type, Unset):
            sub_type = UNSET
        else:
            sub_type = self.sub_type

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        reference: Union[None, Unset, str]
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        doc_date: Union[None, Unset, str]
        if isinstance(self.doc_date, Unset):
            doc_date = UNSET
        elif isinstance(self.doc_date, datetime.datetime):
            doc_date = self.doc_date.isoformat()
        else:
            doc_date = self.doc_date

        match_field: Union[None, Unset, str]
        if isinstance(self.match_field, Unset):
            match_field = UNSET
        else:
            match_field = self.match_field

        custom_field: Union[None, Unset, str]
        if isinstance(self.custom_field, Unset):
            custom_field = UNSET
        else:
            custom_field = self.custom_field

        invoice_id: Union[None, Unset, str]
        if isinstance(self.invoice_id, Unset):
            invoice_id = UNSET
        else:
            invoice_id = self.invoice_id

        invoice_state: Union[None, Unset, str]
        if isinstance(self.invoice_state, Unset):
            invoice_state = UNSET
        else:
            invoice_state = self.invoice_state

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        modified: Union[None, Unset, str]
        if isinstance(self.modified, Unset):
            modified = UNSET
        elif isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if status is not UNSET:
            field_dict["status"] = status
        if reference is not UNSET:
            field_dict["reference"] = reference
        if doc_date is not UNSET:
            field_dict["docDate"] = doc_date
        if match_field is not UNSET:
            field_dict["matchField"] = match_field
        if custom_field is not UNSET:
            field_dict["customField"] = custom_field
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if invoice_state is not UNSET:
            field_dict["invoiceState"] = invoice_state
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DocumentType]
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = DocumentType(_type_)




        def _parse_sub_type(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sub_type = _parse_sub_type(d.pop("subType", UNSET))


        _status = d.pop("status", UNSET)
        status: Union[Unset, DocumentStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = DocumentStatus(_status)




        def _parse_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference = _parse_reference(d.pop("reference", UNSET))


        def _parse_doc_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                doc_date_type_0 = isoparse(data)



                return doc_date_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        doc_date = _parse_doc_date(d.pop("docDate", UNSET))


        def _parse_match_field(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        match_field = _parse_match_field(d.pop("matchField", UNSET))


        def _parse_custom_field(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_field = _parse_custom_field(d.pop("customField", UNSET))


        def _parse_invoice_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        invoice_id = _parse_invoice_id(d.pop("invoiceId", UNSET))


        def _parse_invoice_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        invoice_state = _parse_invoice_state(d.pop("invoiceState", UNSET))


        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        def _parse_modified(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_type_0 = isoparse(data)



                return modified_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        modified = _parse_modified(d.pop("modified", UNSET))


        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))


        serbia_document_model = cls(
            id=id,
            type_=type_,
            sub_type=sub_type,
            status=status,
            reference=reference,
            doc_date=doc_date,
            match_field=match_field,
            custom_field=custom_field,
            invoice_id=invoice_id,
            invoice_state=invoice_state,
            created=created,
            modified=modified,
            comment=comment,
        )

        return serbia_document_model

