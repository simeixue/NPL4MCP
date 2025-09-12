# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.payments
# lines: 37-118
async def payments(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage payment operations using Square API

    Args:
        operation: The operation to perform. Valid operations:
            Payments:
                - list_payments
                - create_payment
                - get_payment
                - update_payment
                - cancel_payment
            Refunds:
                - refund_payment
                - list_refunds
                - get_refund
            Disputes:
                - list_disputes
                - retrieve_dispute
                - accept_dispute
                - create_dispute_evidence
            Gift Cards:
                - create_gift_card
                - link_customer_to_gift_card
                - retrieve_gift_card
                - list_gift_cards
            Bank Accounts:
                - list_bank_accounts
                - get_bank_account
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            # Payments
            case "list_payments":
                result = square_client.payments.list_payments(**params)
            case "create_payment":
                result = square_client.payments.create_payment(params)
            case "get_payment":
                result = square_client.payments.get_payment(**params)
            case "update_payment":
                result = square_client.payments.update_payment(**params)
            case "cancel_payment":
                result = square_client.payments.cancel_payment(**params)
            # Refunds
            case "refund_payment":
                result = square_client.refunds.refund_payment(params)
            case "list_refunds":
                result = square_client.refunds.list_payment_refunds(**params)
            case "get_refund":
                result = square_client.refunds.get_payment_refund(**params)
            # Disputes
            case "list_disputes":
                result = square_client.disputes.list_disputes(**params)
            case "retrieve_dispute":
                result = square_client.disputes.retrieve_dispute(**params)
            case "accept_dispute":
                result = square_client.disputes.accept_dispute(**params)
            case "create_dispute_evidence":
                result = square_client.disputes.create_dispute_evidence(**params)
            # Gift Cards
            case "create_gift_card":
                result = square_client.gift_cards.create_gift_card(params)
            case "link_customer_to_gift_card":
                result = square_client.gift_cards.link_customer_to_gift_card(**params)
            case "retrieve_gift_card":
                result = square_client.gift_cards.retrieve_gift_card(**params)
            case "list_gift_cards":
                result = square_client.gift_cards.list_gift_cards(**params)
            # Bank Accounts
            case "list_bank_accounts":
                result = square_client.bank_accounts.list_bank_accounts(**params)
            case "get_bank_account":
                result = square_client.bank_accounts.get_bank_account(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))