
ocaml-leveldb: OCaml bindings for Google's LevelDB
===================================================
Copyright (c) 2011-2014 Mauricio Fernandez <mfp@acm.org>

These bindings expose nearly the full LevelDB C++ API, including:

* iterators
* snapshots
* batch updates
* support for custom comparators

Blocking functions release the OCaml runtime system, allowing to:

* run them in parallel with other OCaml code
* perform multiple LevelDB operations in parallel

Requirements
------------

* OCaml >= 3.12.0
* GCC with C++ frontend (g++)
* omake to build
* oUnit for the unit tests
* LevelDB (including dev package libleveldb-dev or similar)
* Snappy (including dev package libsnappy-dev or similar)

Building
--------
Just 

   $ omake

should do. It will build both LevelDB and the OCaml bindings.

You can then install (via ocamlfind) with

   $ omake install

API documentation
-----------------
Refer to src/levelDB.mli.

