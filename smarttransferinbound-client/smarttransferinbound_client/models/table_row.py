from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.table_cell import TableCell





T = TypeVar("T", bound="TableRow")



@_attrs_define
class TableRow:
    """ 
        Attributes:
            cells (Union[None, Unset, list['TableCell']]):
     """

    cells: Union[None, Unset, list['TableCell']] = UNSET


    def to_dict(self) -> dict[str, Any]:
        from ..models.table_cell import TableCell
        cells: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.cells, Unset):
            cells = UNSET
        elif isinstance(self.cells, list):
            cells = []
            for cells_type_0_item_data in self.cells:
                cells_type_0_item = cells_type_0_item_data.to_dict()
                cells.append(cells_type_0_item)


        else:
            cells = self.cells


        field_dict: dict[str, Any] = {}
        field_dict.update({
        })
        if cells is not UNSET:
            field_dict["cells"] = cells

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.table_cell import TableCell
        d = src_dict.copy()
        def _parse_cells(data: object) -> Union[None, Unset, list['TableCell']]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cells_type_0 = []
                _cells_type_0 = data
                for cells_type_0_item_data in (_cells_type_0):
                    cells_type_0_item = TableCell.from_dict(cells_type_0_item_data)



                    cells_type_0.append(cells_type_0_item)

                return cells_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list['TableCell']], data)

        cells = _parse_cells(d.pop("cells", UNSET))


        table_row = cls(
            cells=cells,
        )

        return table_row

