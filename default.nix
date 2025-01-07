with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "development";
  buildInputs = [
    pkg-config
    python312
    pylint
  ];
}
