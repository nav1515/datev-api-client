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

if TYPE_CHECKING:
  from ..models.notification_model import NotificationModel
  from ..models.party import Party





T = TypeVar("T", bound="DocumentInfo")



@_attrs_define
class DocumentInfo:
    """ Contains document information.

        Attributes:
            tags (Union[None, Unset, list['NotificationModel']]): Gets or sets the tags.
            private_custom_field_1 (Union[None, Unset, str]): Gets or sets the private custom field1.
            private_custom_field_2 (Union[None, Unset, str]): Gets or sets the private custom field2.
            workflow_state (Union[None, Unset, str]): Gets or sets the state of the workflow.
            public_attachment_ids (Union[None, Unset, list[int]]): Gets the public attachment ids.
            public_attachments_count (Union[Unset, int]): Gets the public attachments count.
            private_attachment_ids (Union[None, Unset, list[int]]): Gets the private attachment ids.
            private_attachments_count (Union[Unset, int]): Gets the private attachments count.
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
            sub_type (Union[None, Unset, int]): Gets or sets the type of the sub.
            amount (Union[None, Unset, float]): Gets or sets the amount.
            reference (Union[None, Unset, str]): Gets or sets the reference.
            customer_number (Union[None, Unset, str]): Gets or sets the customer number.
            doc_date (Union[None, Unset, datetime.datetime]): Gets or sets the document date.
            is_duplicate (Union[Unset, bool]): Gets or sets a value indicating whether this instance is duplicate.
            match_field (Union[None, Unset, str]): Gets or sets the match field.
            custom_field (Union[None, Unset, str]): Gets or sets the custom field.
            created (Union[Unset, datetime.datetime]): Gets or sets the created.
            ready_for_api (Union[None, Unset, datetime.datetime]): Gets or sets the ready for API.
            archived (Union[Unset, bool]): Gets or sets a value indicating whether this
                B4.TraffiqxApi.Models.Base.DocumentBase is archived.
            error_text (Union[None, Unset, str]): Gets or sets the error text.
            sender (Union[Unset, Party]):
            receiver (Union[Unset, Party]):
     """

    tags: Union[None, Unset, list['NotificationModel']] = UNSET
    private_custom_field_1: Union[None, Unset, str] = UNSET
    private_custom_field_2: Union[None, Unset, str] = UNSET
    workflow_state: Union[None, Unset, str] = UNSET
    public_attachment_ids: Union[None, Unset, list[int]] = UNSET
    public_attachments_count: Union[Unset, int] = UNSET
    private_attachment_ids: Union[None, Unset, list[int]] = UNSET
    private_attachments_count: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    type_: Union[Unset, DocumentType] = UNSET
    status: Union[Unset, DocumentStatus] = UNSET
    sub_type: Union[None, Unset, int] = UNSET
    amount: Union[None, Unset, float] = UNSET
    reference: Union[None, Unset, str] = UNSET
    customer_number: Union[None, Unset, str] = UNSET
    doc_date: Union[None, Unset, datetime.datetime] = UNSET
    is_duplicate: Union[Unset, bool] = UNSET
    match_field: Union[None, Unset, str] = UNSET
    custom_field: Union[None, Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    ready_for_api: Union[None, Unset, datetime.datetime] = UNSET
    archived: Union[Unset, bool] = UNSET
    error_text: Union[None, Unset, str] = UNSET
    sender: Union[Unset, 'Party'] = UNSET
    receiver: Union[Unset, 'Party'] = UNSET


    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_model import NotificationModel
        from ..models.party import Party
        tags: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)


        else:
            tags = self.tags

        private_custom_field_1: Union[None, Unset, str]
        if isinstance(self.private_custom_field_1, Unset):
            private_custom_field_1 = UNSET
        else:
            private_custom_field_1 = self.private_custom_field_1

        private_custom_field_2: Union[None, Unset, str]
        if isinstance(self.private_custom_field_2, Unset):
            private_custom_field_2 = UNSET
        else:
            private_custom_field_2 = self.private_custom_field_2

        workflow_state: Union[None, Unset, str]
        if isinstance(self.workflow_state, Unset):
            workflow_state = UNSET
        else:
            workflow_state = self.workflow_state

        public_attachment_ids: Union[None, Unset, list[int]]
        if isinstance(self.public_attachment_ids, Unset):
            public_attachment_ids = UNSET
        elif isinstance(self.public_attachment_ids, list):
            public_attachment_ids = self.public_attachment_ids


        else:
            public_attachment_ids = self.public_attachment_ids

        public_attachments_count = self.public_attachments_count

        private_attachment_ids: Union[None, Unset, list[int]]
        if isinstance(self.private_attachment_ids, Unset):
            private_attachment_ids = UNSET
        elif isinstance(self.private_attachment_ids, list):
            private_attachment_ids = self.private_attachment_ids


        else:
            private_attachment_ids = self.private_attachment_ids

        private_attachments_count = self.private_attachments_count

        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        sub_type: Union[None, Unset, int]
        if isinstance(self.sub_type, Unset):
            sub_type = UNSET
        else:
            sub_type = self.sub_type

        amount: Union[None, Unset, float]
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        reference: Union[None, Unset, str]
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        customer_number: Union[None, Unset, str]
        if isinstance(self.customer_number, Unset):
            customer_number = UNSET
        else:
            customer_number = self.customer_number

        doc_date: Union[None, Unset, str]
        if isinstance(self.doc_date, Unset):
            doc_date = UNSET
        elif isinstance(self.doc_date, datetime.datetime):
            doc_date = self.doc_date.isoformat()
        else:
            doc_date = self.doc_date

        is_duplicate = self.is_duplicate

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

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        ready_for_api: Union[None, Unset, str]
        if isinstance(self.ready_for_api, Unset):
            ready_for_api = UNSET
        elif isinstance(self.ready_for_api, datetime.datetime):
            ready_for_api = self.ready_for_api.isoformat()
        else:
            ready_for_api = self.ready_for_api

        archived = self.archived

        error_text: Union[None, Unset, str]
        if isinstance(self.error_text, Unset):
            error_text = UNSET
        else:
            error_text = self.error_text

        sender: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        receiver: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.receiver, Unset):
            receiver = self.receiver.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if tags is not UNSET:
            field_dict["tags"] = tags
        if private_custom_field_1 is not UNSET:
            field_dict["privateCustomField1"] = private_custom_field_1
        if private_custom_field_2 is not UNSET:
            field_dict["privateCustomField2"] = private_custom_field_2
        if workflow_state is not UNSET:
            field_dict["workflowState"] = workflow_state
        if public_attachment_ids is not UNSET:
            field_dict["publicAttachmentIds"] = public_attachment_ids
        if public_attachments_count is not UNSET:
            field_dict["publicAttachmentsCount"] = public_attachments_count
        if private_attachment_ids is not UNSET:
            field_dict["privateAttachmentIds"] = private_attachment_ids
        if private_attachments_count is not UNSET:
            field_dict["privateAttachmentsCount"] = private_attachments_count
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if reference is not UNSET:
            field_dict["reference"] = reference
        if customer_number is not UNSET:
            field_dict["customerNumber"] = customer_number
        if doc_date is not UNSET:
            field_dict["docDate"] = doc_date
        if is_duplicate is not UNSET:
            field_dict["isDuplicate"] = is_duplicate
        if match_field is not UNSET:
            field_dict["matchField"] = match_field
        if custom_field is not UNSET:
            field_dict["customField"] = custom_field
        if created is not UNSET:
            field_dict["created"] = created
        if ready_for_api is not UNSET:
            field_dict["readyForAPI"] = ready_for_api
        if archived is not UNSET:
            field_dict["archived"] = archived
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if sender is not UNSET:
            field_dict["sender"] = sender
        if receiver is not UNSET:
            field_dict["receiver"] = receiver

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.notification_model import NotificationModel
        from ..models.party import Party
        d = src_dict.copy()
        def _parse_tags(data: object) -> Union[None, Unset, list['NotificationModel']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in (_tags_type_0):
                    tags_type_0_item = NotificationModel.from_dict(tags_type_0_item_data)



                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['NotificationModel']], data)

        tags = _parse_tags(d.pop("tags", UNSET))


        def _parse_private_custom_field_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        private_custom_field_1 = _parse_private_custom_field_1(d.pop("privateCustomField1", UNSET))


        def _parse_private_custom_field_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        private_custom_field_2 = _parse_private_custom_field_2(d.pop("privateCustomField2", UNSET))


        def _parse_workflow_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        workflow_state = _parse_workflow_state(d.pop("workflowState", UNSET))


        def _parse_public_attachment_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                public_attachment_ids_type_0 = cast(list[int], data)

                return public_attachment_ids_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        public_attachment_ids = _parse_public_attachment_ids(d.pop("publicAttachmentIds", UNSET))


        public_attachments_count = d.pop("publicAttachmentsCount", UNSET)

        def _parse_private_attachment_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                private_attachment_ids_type_0 = cast(list[int], data)

                return private_attachment_ids_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        private_attachment_ids = _parse_private_attachment_ids(d.pop("privateAttachmentIds", UNSET))


        private_attachments_count = d.pop("privateAttachmentsCount", UNSET)

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DocumentType]
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = DocumentType(_type_)




        _status = d.pop("status", UNSET)
        status: Union[Unset, DocumentStatus]
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = DocumentStatus(_status)




        def _parse_sub_type(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sub_type = _parse_sub_type(d.pop("subType", UNSET))


        def _parse_amount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        amount = _parse_amount(d.pop("amount", UNSET))


        def _parse_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference = _parse_reference(d.pop("reference", UNSET))


        def _parse_customer_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        customer_number = _parse_customer_number(d.pop("customerNumber", UNSET))


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


        is_duplicate = d.pop("isDuplicate", UNSET)

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


        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created,  Unset):
            created = UNSET
        else:
            created = isoparse(_created)




        def _parse_ready_for_api(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ready_for_api_type_0 = isoparse(data)



                return ready_for_api_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        ready_for_api = _parse_ready_for_api(d.pop("readyForAPI", UNSET))


        archived = d.pop("archived", UNSET)

        def _parse_error_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error_text = _parse_error_text(d.pop("errorText", UNSET))


        _sender = d.pop("sender", UNSET)
        sender: Union[Unset, Party]
        if isinstance(_sender,  Unset):
            sender = UNSET
        else:
            sender = Party.from_dict(_sender)




        _receiver = d.pop("receiver", UNSET)
        receiver: Union[Unset, Party]
        if isinstance(_receiver,  Unset):
            receiver = UNSET
        else:
            receiver = Party.from_dict(_receiver)




        document_info = cls(
            tags=tags,
            private_custom_field_1=private_custom_field_1,
            private_custom_field_2=private_custom_field_2,
            workflow_state=workflow_state,
            public_attachment_ids=public_attachment_ids,
            public_attachments_count=public_attachments_count,
            private_attachment_ids=private_attachment_ids,
            private_attachments_count=private_attachments_count,
            id=id,
            type_=type_,
            status=status,
            sub_type=sub_type,
            amount=amount,
            reference=reference,
            customer_number=customer_number,
            doc_date=doc_date,
            is_duplicate=is_duplicate,
            match_field=match_field,
            custom_field=custom_field,
            created=created,
            ready_for_api=ready_for_api,
            archived=archived,
            error_text=error_text,
            sender=sender,
            receiver=receiver,
        )

        return document_info

