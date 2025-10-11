# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/bump_version.py
# module: scripts.bump_version
# qname: scripts.bump_version.main
# lines: 80-112
def main():
    parser = argparse.ArgumentParser(description="Bump version numbers in the project")
    parser.add_argument(
        "bump_type",
        nargs="?",
        choices=["major", "minor", "patch"],
        default="minor",
        help="Type of version bump (default: minor)",
    )
    args = parser.parse_args()

    # Get root directory
    root_dir = Path(__file__).parent.parent

    # Read current version from pyproject.toml
    pyproject_path = root_dir / "pyproject.toml"
    current_version = read_toml(pyproject_path)["project"]["version"]

    # Calculate new version
    new_version = bump_version(current_version, args.bump_type)

    # Update files
    update_pyproject_toml(pyproject_path, new_version)
    update_version_py(root_dir / "src" / "semgrep_mcp" / "version.py", new_version)
    update_changelog(root_dir / "CHANGELOG.md", new_version)
    update_chart_yaml(root_dir / "chart" / "semgrep-mcp" / "Chart.yaml", new_version)

    print(f"Successfully bumped version from {current_version} to {new_version}")
    print("Files updated:")
    print("- pyproject.toml")
    print("- src/semgrep_mcp/version.py")
    print("- CHANGELOG.md")
    print("- chart/semgrep-mcp/Chart.yaml")