set trimspool on
set trim on
set pages 0
set linesize 1000
set long 1000000
set longchunksize 1000000
set feedback off
set echo off
set verify off
set termout on

set termout off

spool sqlmon_active_&1..html

SELECT dbms_sqltune.Report_sql_monitor(SQL_ID=>'&1.', TYPE=>'active')
FROM   dual;

spool OFF

exit