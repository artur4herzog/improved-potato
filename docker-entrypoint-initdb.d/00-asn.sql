CREATE DATABASE IF NOT EXISTS `asn`;

CREATE USER IF NOT EXISTS `asn` IDENTIFIED BY "qwerty123";

GRANT ALL ON `asn`.* TO `asn`@'%';

use asn;

CREATE TABLE IF NOT EXISTS prefixes (
    asn int UNSIGNED,
    prefix char(18),
    KEY asn_index (`asn`)
)