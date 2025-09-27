# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.PyPiPackage.package_name
# lines: 83-89
    def package_name(self) -> str:
        with open(self.path / "pyproject.toml") as f:
            toml_data = tomlkit.parse(f.read())
            name = toml_data.get("project", {}).get("name")
            if not name:
                raise Exception("No name in pyproject.toml project section")
            return str(name)