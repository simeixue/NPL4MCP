# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.update_packages
# lines: 144-155
def update_packages(directory: Path, git_hash: GitHash) -> int:
    # Detect package type
    path = directory.resolve(strict=True)
    version = gen_version()

    for package in find_changed_packages(path, git_hash):
        name = package.package_name()
        package.update_version(version)

        click.echo(f"{name}@{version}")

    return 0