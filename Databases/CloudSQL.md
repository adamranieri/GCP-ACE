# Cloud SQL
- Relational Database
- default snapshot backup of 7 days
- Manual scaling
- RDBMS
    - MySQL
    - Postgres

```bash
gcloud sql intances patch mysqldb

gcloud sql backups create --instance mysqldb

gcloud sql export sql mysqldb gs://mybucket/data.sql --database=mysql
gcloud sql export csv mysqldb gs://mybucket/data.csv --database=mysql

gcloud sql import sql mysqldb gs://mybucket/data.sql --database=mysql
```