# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/tests/test_mcp_server.py
# module: tests.test_mcp_server
# qname: tests.test_mcp_server.setup_test_database
# lines: 23-81
async def setup_test_database():
    """Set up test database and tables before running tests."""
    client = create_clickhouse_client()

    # Test database and table names
    test_db = "test_mcp_db"
    test_table = "test_table"
    test_table2 = "another_test_table"

    # Create test database
    client.command(f"CREATE DATABASE IF NOT EXISTS {test_db}")

    # Drop tables if they exist
    client.command(f"DROP TABLE IF EXISTS {test_db}.{test_table}")
    client.command(f"DROP TABLE IF EXISTS {test_db}.{test_table2}")

    # Create first test table with comments
    client.command(f"""
        CREATE TABLE {test_db}.{test_table} (
            id UInt32 COMMENT 'Primary identifier',
            name String COMMENT 'User name field',
            age UInt8 COMMENT 'User age',
            created_at DateTime DEFAULT now() COMMENT 'Record creation timestamp'
        ) ENGINE = MergeTree()
        ORDER BY id
        COMMENT 'Test table for MCP server testing'
    """)

    # Create second test table
    client.command(f"""
        CREATE TABLE {test_db}.{test_table2} (
            event_id UInt64,
            event_type String,
            timestamp DateTime
        ) ENGINE = MergeTree()
        ORDER BY (event_type, timestamp)
        COMMENT 'Event tracking table'
    """)

    # Insert test data
    client.command(f"""
        INSERT INTO {test_db}.{test_table} (id, name, age) VALUES
        (1, 'Alice', 30),
        (2, 'Bob', 25),
        (3, 'Charlie', 35),
        (4, 'Diana', 28)
    """)

    client.command(f"""
        INSERT INTO {test_db}.{test_table2} (event_id, event_type, timestamp) VALUES
        (1001, 'login', '2024-01-01 10:00:00'),
        (1002, 'logout', '2024-01-01 11:00:00'),
        (1003, 'login', '2024-01-01 12:00:00')
    """)

    yield test_db, test_table, test_table2

    # Cleanup after tests
    client.command(f"DROP DATABASE IF EXISTS {test_db}")