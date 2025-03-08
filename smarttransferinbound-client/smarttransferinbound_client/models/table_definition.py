from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.table_column import TableColumn





T = TypeVar("T", bound="TableDefinition")



@_attrs_define
class TableDefinition:
    """ 
        Attributes:
            name (Union[None, Unset, str]):
            columns (Union[None, Unset, list['TableColumn']]):
     """

    name: Union[None, Unset, str] = UNSET
    columns: Union[None, Unset, list['TableColumn']] = UNSET


    def to_dict(self) -> dict[str, Any]:
        from ..models.table_column import TableColumn
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        columns: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.columns, Unset):
            columns = UNSET
        elif isinstance(self.columns, list):
            columns = []
            for columns_type_0_item_data in self.columns:
                columns_type_0_item = columns_type_0_item_data.to_dict()
                columns.append(columns_type_0_item)


        else:
            columns = self.columns


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if columns is not UNSET:
            field_dict["columns"] = columns

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.table_column import TableColumn
        d = src_dict.copy()
        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_columns(data: object) -> Union[None, Unset, list['TableColumn']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                columns_type_0 = []
                _columns_type_0 = data
                for columns_type_0_item_data in (_columns_type_0):
                    columns_type_0_item = TableColumn.from_dict(columns_type_0_item_data)



                    columns_type_0.append(columns_type_0_item)

                return columns_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['TableColumn']], data)

        columns = _parse_columns(d.pop("columns", UNSET))


        table_definition = cls(
            name=name,
            columns=columns,
        )

        return table_definition

