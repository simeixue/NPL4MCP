# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.NpmPackage.update_version
# lines: 70-76
    def update_version(self, version: Version):
        with open(self.path / "package.json", "r+") as f:
            data = json.load(f)
            data["version"] = version
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()