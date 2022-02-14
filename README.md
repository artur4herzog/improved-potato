# improved-potato

## Start mysql
```bash
docker-compose up -d
```
Starts mysql and creates database and table in it.

## Install pyasn
```bash
pip install pyasn
```

## Get latest RIB database
Utils from pyasn package.
```bash
pyasn_util_download.py --latest
pyasn_util_convert.py --single <Downloaded RIB File> <ipasn_db_file_name>
```

## Run script
Mysql password will be prompted. Root password can be found in docker-compose.yaml, or for user "asn" in docker-entrypoint-initdb.d/00-asn.sql.
```bash
./getprefix.py  -f <ipasn_db_file_name> -a <ASN>
```
Example:
```bash
./getprefix.py -f rib.dat -a 25537 39494 48287 5537
./getprefix.py -h
```