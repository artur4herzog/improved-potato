#!/usr/local/bin/python3

import argparse
import pyasn
import mysql.connector as mysql
from getpass import getpass

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", required=True, help="Input file. Mandatory parameter")
parser.add_argument("-a", "--asn", required=True, type=int, nargs='+', help="asn list. Mandatory parameter")
parser.add_argument("-H", "--host", default="127.0.0.1", help="Mysql host. Default: 127.0.0.1")
parser.add_argument("-P", "--port", default=3306, help="Mysql port. Default: 3306")
parser.add_argument("-u", "--user", default="root", help="Mysql user. Default: root")
parser.add_argument("-d", "--database", default="asn", help="Mysql database. Default: asn")

args = parser.parse_args()
 
asndb = pyasn.pyasn(args.file);

record = []
for asn in args.asn:
  prefixes = asndb.get_as_prefixes_effective(asn)
  if prefixes is not None:
    for prefix in prefixes:
      record.append((asn, prefix))
#      print("%d\t%s"%(asn, prefix))

password=getpass("Mysql password for user " + args.user + ":")
db = mysql.connect(
    host = args.host,
    user = args.user,
    passwd = password,
    database = args.database
)
cursor = db.cursor()
query = "INSERT INTO prefixes (asn, prefix) VALUES (%s, %s)"
cursor.executemany(query, record)
db.commit()
db.close()
