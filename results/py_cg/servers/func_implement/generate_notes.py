# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.generate_notes
# lines: 163-175
def generate_notes(directory: Path, git_hash: GitHash) -> int:
    # Detect package type
    path = directory.resolve(strict=True)
    version = gen_version()

    click.echo(f"# Release : v{version}")
    click.echo("")
    click.echo("## Updated packages")
    for package in find_changed_packages(path, git_hash):
        name = package.package_name()
        click.echo(f"- {name}@{version}")

    return 0