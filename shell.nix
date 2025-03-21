let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.discordpy
      python-pkgs.requests
      python-pkgs.python-dotenv
    ]))
  ];
}
