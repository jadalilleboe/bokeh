import {display} from "./_util"

import {ColumnDataSource} from "@bokehjs/models"
import {DataTable, TableColumn} from "@bokehjs/models/widgets/tables"
import {offset} from "@bokehjs/core/dom"

describe("DataTable", () => {

  it("should allow sorting a non-selectable table", async () => {
    const source = new ColumnDataSource({data: {foo: [10, 20, 30, 40], bar: [3.4, 1.2, 0, -10]}})

    const foo_col = new TableColumn({field: "foo", title: "Foo", width: 200})
    const bar_col = new TableColumn({field: "bar", title: "Bar", width: 200})
    const columns = [foo_col, bar_col]

    const table = new DataTable({source, columns, sortable: true, selectable: false})
    const {view} = await display(table, [600, 400])

    const el = view.shadow_el.querySelectorAll(".slick-header-column")[2]
    const {left, top} = offset(el)
    const ev = new MouseEvent("click", {clientX: left + 5, clientY: top + 5, bubbles: true})
    el.dispatchEvent(ev)

    await view.ready
  })
})
