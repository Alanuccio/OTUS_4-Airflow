PGPASSWORD=$PSQL_PASSWORD psql -h $PSQL_HOST -p 6432 -d $PSQL_DBNAME -U $PSQL_USER -q -c "SELECT * FROM bitcoin_course" -t -P format=unaligned
