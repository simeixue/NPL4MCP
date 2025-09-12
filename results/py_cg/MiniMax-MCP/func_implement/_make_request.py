# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/client.py
# module: minimax_mcp.client
# qname: minimax_mcp.client.MinimaxAPIClient._make_request
# lines: 25-87
    def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        **kwargs
    ) -> Dict[str, Any]:
        """Make an HTTP request to the Minimax API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            API response data as dictionary
            
        Raises:
            MinimaxAuthError: If authentication fails
            MinimaxRequestError: If the request fails
        """
        url = f"{self.api_host}{endpoint}"
        
        # Set Content-Type based on whether files are being uploaded
        files = kwargs.get('files')
        if not files:
            self.session.headers['Content-Type'] = 'application/json'
        else:
            # Remove Content-Type header for multipart/form-data
            # requests library will set it automatically with the correct boundary
            self.session.headers.pop('Content-Type', None)
        
        try:
            response = self.session.request(method, url, **kwargs)
            
            # Check for other HTTP errors
            response.raise_for_status()
            
            data = response.json()
            
            # Check API-specific error codes
            base_resp = data.get("base_resp", {})
            if base_resp.get("status_code") != 0:
                match base_resp.get("status_code"):
                    case 1004:
                        raise MinimaxAuthError(
                            f"API Error: {base_resp.get('status_msg')}, please check your API key and API host."
                            f"Trace-Id: {response.headers.get('Trace-Id')}"
                        )
                    case 2038:
                        raise MinimaxRequestError(
                            f"API Error: {base_resp.get('status_msg')}, should complete real-name verification on the open-platform(https://platform.minimaxi.com/user-center/basic-information)."
                            f"Trace-Id: {response.headers.get('Trace-Id')}"
                        )
                    case _:
                        raise MinimaxRequestError(
                            f"API Error: {base_resp.get('status_code')}-{base_resp.get('status_msg')} "
                            f"Trace-Id: {response.headers.get('Trace-Id')}"
                        )
                
            return data
            
        except requests.exceptions.RequestException as e:
            raise MinimaxRequestError(f"Request failed: {str(e)}")