---
title: API Example
tags: example
---

# Addin Function Reference

### xlGetData

`xlGetData(Database, Query, [Trigger], [IfNull], [Transpose])`{: style='color: #2980B9'}
: Returns records from a database located anywhere in space according to the provided query. Records
  are arranged in a table and the table can be transposed. Use the `Trigger` argument to force execution
  order in Excel.

    - <span style='color: #2980B9; background: #f0f0f0'>Database</span>: a reference to a database created in space.
    - Query: a query to filter the data from space. Only SELECT query are supported. If you need to manipulate
        data, please use the [xlExecute](#xlExecute) function.
    - Trigger: optional dummy argument to enforce calculation order.
    - IfNull: optional replacement value for NULL fields
    - Transpose: an optional bool to avoid computational inefficiencies related to compute a transpose
      table that can be created transposed.

    **Returns**: an array of data with columns as fields and records as rows. Unless column headings are specified,
      the first row is interpreted as column names.

### xlExecute

`xlExecute(Database, Query, [Trigger])`{: style='color: #2980B9'}
: Execute a non-SELECT query in a database located anywhere in space. Use the `Trigger` argument to force execution
  order in Excel.

    - <span style='color: #2980B9; background: #f0f0f0'>Database</span>: a reference to a database created in space.
    - Query: a query to manipulate the data in space. Only non-SELECT query are supported. If you need to filter
        data, please use the [xlGetData](#xlGetData) function.
    - Trigger: optional dummy argument to enforce calculation order.

    **Returns**: number of records affected, if available.
