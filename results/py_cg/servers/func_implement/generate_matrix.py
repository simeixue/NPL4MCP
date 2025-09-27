# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.generate_matrix
# lines: 192-206
def generate_matrix(directory: Path, git_hash: GitHash, pypi: bool, npm: bool) -> int:
    # Detect package type
    path = directory.resolve(strict=True)
    version = gen_version()

    changes = []
    for package in find_changed_packages(path, git_hash):
        pkg = package.path.relative_to(path)
        if npm and isinstance(package, NpmPackage):
            changes.append(str(pkg))
        if pypi and isinstance(package, PyPiPackage):
            changes.append(str(pkg))

    click.echo(json.dumps(changes))
    return 0