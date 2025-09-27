# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.NpmPackage.package_name
# lines: 66-68
    def package_name(self) -> str:
        with open(self.path / "package.json", "r") as f:
            return json.load(f)["name"]