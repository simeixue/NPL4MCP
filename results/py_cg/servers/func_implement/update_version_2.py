# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.PyPiPackage.update_version
# lines: 91-98
    def update_version(self, version: Version):
        # Update version in pyproject.toml
        with open(self.path / "pyproject.toml") as f:
            data = tomlkit.parse(f.read())
            data["project"]["version"] = version

        with open(self.path / "pyproject.toml", "w") as f:
            f.write(tomlkit.dumps(data))