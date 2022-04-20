# Phone Book data

## 2020-2022

The file "institutional_affiliation_20" was produced by applying a filter (grep)
on the much larger file "institutional_affiliation", selecting years 19-23.
There seems to be inconsistency in the orignal DB source with regards to what
years are recorded (i.e. there are gaps which don't make sense). The procedure
for building such filtered file is trivial so seems OK for maintenance.

## 2022-

A new set of data files was prepared in April 2022 by B.Johnson, and is kept
in the folder ```capture20220417```. Small inconsistencies (like a few missing institutions)
were fixed by hand. A pair of companion scripts has been developed to parse these
input data files and convert them into YAML format for easy integration with the rest of the
site data. Regarding affiliation, "primary institutions" for individuals associated with more
than institution, were recorded in a separate file used by the parser for unambiguous
mapping.

