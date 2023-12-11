# Queue-Capacity-Backend

Queue Capacity Backend is a Python/ Flask API application used by the Queue-Capacity-Visualization Frontend. The backend reads/ writes data from the OpsDash Dev Server:

| Server   | DB Connection                     |
| -------- | --------------------------------- |
| Server   | YKE0-D14GP0101.devfg.rbc.com\IN01 |
| Database | DWR60_OperationalDashboard_Dev    |
| Table    | PepperdataMonitoring              |

- Frontend: https://rbcgithub.fg.rbc.com/WR60/Queue-Capacity-Visualization
- Dev Hosted: https://queue-capacity-backend-wr60-private-dev.apps.ocp-sai-g1.saifg.rbc.com/test

# Developement

```

py .\server.py

```

Route URL for seeing test data: http://localhost:5000/test

## Example API Queries

| Example Type                    | SQL Query                                                                                              | API Route URL                                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Fixed 3 Column SQL Query        | SELECT \* FROM PepperdataMonitoring WHERE JobType=? AND JobStatus=? AND AppCode=?                      | `http://localhost:5000/api/query\<JobType>\<JobStatus>\<AppCode>`                                             |
| Fixed 3 Column SQL Query        | SELECT \* FROM PepperdataMonitoring WHERE JobType='SPARK' AND JobStatus='SUCCEEDED' AND AppCode='TGM0' | `http://localhost:5000/api/query/SPARK/SUCCEEDED/TGM0`                                                        |
| Flexible Multi-column SQL Query | SELECT \* FROM PepperdataMonitoring WHERE JobType='SPARK'                                              | `http://localhost:5000/api/query?column=JobType&value=SPARK&operator==`                                       |
| Flexible Multi-column SQL Query | SELECT \* FROM PepperdataMonitoring WHERE JobType='SPARK' AND JobDuration > 0                          | `http://localhost:5000/api/query?column=JobType&value=SPARK&operator==&column=JobDuration&value=0&operator=>` |

- Note that 'Fixed 3 Column SQL Query' must have values for `\<JobType>\<JobStatus>\<AppCode>`
- Note that 'Flexible Multi-column SQL Query' must be in sets of 3 containing: `column=<col name>&value=<val>&operator=<op>`
  - Valid operators are: =, >, <, >=, <=
