@1

package "ocp-get" {

  version     = "HEAD"

  description = "Client for the OCaml PAckage Manager (OPAM)"

  sources     = [
      "https://github.com/OCamlPro/ocp-get.git"
  ]

  patches = [
      "files://files/ocp-get.install"
  ]

  make = [
      "ocp-get config -ocp -rstrict ocp-get > depends.ocp";
      "ocp-build ocp-get ocp-get-server"
  ]

  depends =
    "mancoosi-cudf, mancoosi-dose, ocaml-extlib, ocaml-arg, ocaml-graph"
}