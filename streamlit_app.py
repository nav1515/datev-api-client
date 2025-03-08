import streamlit as st
import requests
from datetime import datetime
import pandas as pd
from urllib.parse import urlencode
import hashlib
import base64
import os
import importlib
import inspect
import json
# Configure the base URL for the FastAPI backend
BASE_URL = "https://{api_name}.api.datev.de/platform-sandbox/v2"

# OAuth2 Configuration
AUTH_URL = "https://login.datev.de/openidsandbox/authorize"  
TOKEN_URL = "https://sandbox-api.datev.de/token"   
CLIENT_ID = st.secrets["oauth"]["client_id"]      
CLIENT_SECRET = st.secrets["oauth"]["client_secret"]
COOKIE_SECRET = st.secrets["oauth"]["cookie_secret"]
REDIRECT_URI = "http://localhost:8501"  

def generate_code_verifier():
    """Generate a code verifier for PKCE"""
    return COOKIE_SECRET

def generate_code_challenge(code_verifier):
    """Generate a code challenge for PKCE"""
    sha256_hash = hashlib.sha256(code_verifier.encode('ascii')).digest()
    return base64.urlsafe_b64encode(sha256_hash).decode('ascii').rstrip('=')

def init_session_state():
    """Initialize session state variables"""
    if "access_token" not in st.session_state:
        st.session_state.access_token = None
    if "state" not in st.session_state:
        st.session_state.state = "01234567890123456789"
    if "code_verifier" not in st.session_state:
        st.session_state.code_verifier = None
    if "current_client" not in st.session_state:
        st.session_state.current_client = None
    if "current_endpoint" not in st.session_state:
        st.session_state.current_endpoint = None

def login():
    """Handle OAuth2 login flow"""
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)
    st.session_state.code_verifier = code_verifier
    
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "state": st.session_state.state,
        "scope": "openid profile email accounting:documents accounting:clients:read accounting:dxso-jobs datev:accounting:clients datev:accounting:extf-files-import datev:hr:payrolldataupload datev:hr:payrolldatareport datev:hr:payrolldataexport datev:hr:eau datev:my-tax:documents datev:tax:taxdeclaration datev:hr:documents:upload",
        "code_challenge": code_challenge,
        "code_challenge_method": "S256"
    }
    auth_url = f"{AUTH_URL}?{urlencode(params)}"
    
    st.markdown(f"""
        <a href="{auth_url}" target="_self">
            <button style="background-color:#4CAF50;color:white;padding:10px 24px;border:none;border-radius:4px;cursor:pointer;">
                Login with DATEV
            </button>
        </a>
    """, unsafe_allow_html=True)

def handle_callback():
    """Handle OAuth2 callback and token exchange"""
    query_params = st.query_params
    
    if "code" in query_params and "state" in query_params:
        if query_params["state"] != st.session_state.state:
            st.error("Invalid state parameter")
            return
        
        try:
            auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
            auth_bytes = auth_string.encode('ascii')
            base64_auth = base64.b64encode(auth_bytes).decode('ascii')
            
            response = requests.post(
                TOKEN_URL,
                headers={
                    "X-DATEV-Client-Id": CLIENT_ID,
                    "content-type": "application/x-www-form-urlencoded",
                    "Authorization": f"Basic {base64_auth}"
                },
                data={
                    "grant_type": "authorization_code",
                    "code": query_params["code"],   
                    "redirect_uri": REDIRECT_URI,
                    "code_verifier": st.session_state.code_verifier
                }
            )
            
            if response.status_code == 200:
                token_data = response.json()
                st.session_state['access_token'] = token_data["access_token"]
                st.query_params.clear()
                st.success("Successfully logged in!")
                st.rerun()
            else:
                st.error("Failed to obtain access token")
                st.write(response.json())
        except Exception as e:
            st.error(f"Error during token exchange: {str(e)}")

def authenticated_request(method, url, **kwargs):
    """Make authenticated requests to the API"""
    if not st.session_state.access_token:
        st.error("Please log in first")
        return None
    
    headers = {
        "Authorization": f"Bearer {st.session_state.access_token}",
        "X-Datev-Client-ID": CLIENT_ID,
        "accept": "application/json;charset=UTF-8",
    }
    if "headers" in kwargs:
        headers.update(kwargs["headers"])
    kwargs["headers"] = headers
    
    response = requests.request(method, url, **kwargs)
    
    if response.status_code == 401:
        st.error("Session expired. Please log in again")
        st.session_state.access_token = None
        st.rerun()
    
    return response

def get_available_clients():
    """Get all available client folders"""
    clients = []
    for item in os.listdir():
        if os.path.isdir(item) and item.endswith('-client'):
            clients.append(item.rstrip('-client'))
    return clients

def get_client_endpoints(client_name):
    """Get all available endpoints for a specific client"""
    try:
        # Convert folder name to module name format
        folder_name = f"{client_name}-client"  # e.g., "accounting-clients-client"
        
        # # Add the folder to Python path if it's not already there
        # import sys
        folder_path = os.path.abspath(folder_name)
        # if folder_path not in sys.path:
        #     sys.path.append(folder_path)
        
        module_name = folder_name.replace('-', '_')  # e.g., "accounting_clients_client"
        
        import_module = importlib.import_module(f"{folder_name}.{module_name}")

        # # Import the api module
        module_api = os.path.join(folder_path, f"{module_name}/api")  # e.g., "accounting_clients_client.api"
        
        endpoints = {}
        for item in os.listdir(module_api):
            full_path = os.path.join(module_api, item)
            if os.path.isdir(full_path) and not item.startswith('__'):
                # st.write(f"Found API group: {item}")
                for subitem in os.listdir(full_path):
                    subfull_path = os.path.join(full_path, subitem)
                    if os.path.isfile(subfull_path) and subitem.endswith('.py') and not subitem.startswith('__'):
                        # st.write(f"Found API endpoint in group {item}: {subitem}")
                        # submodule_name = f"{module_api}/{item}/{subitem}"
                        if item not in endpoints:
                            endpoints[item] = []
                        endpoints[item].append(subitem)
                        # st.write(f"Endpoint path: {subfull_path}")
                        # submodule = importlib.import_module(f"{module_api}.{item}.{subitem}")
                        # st.write(f"Submodule contents: {dir(submodule)}")
        # st.write(f"Endpoints: {endpoints}")
        return import_module, endpoints

        # # Import the api module dynamically
        # api_module = importlib.import_module(module_api)
        
        # # Get the actual path of the api package
        # api_path = os.path.dirname(api_module.__file__)
        # st.write(f"API path: {api_path}")
        
        # # List all subdirectories (they contain the actual API modules)
        # endpoints = {}
        # for item in os.listdir(api_path):
        #     item_path = os.path.join(api_path, item)
        #     if os.path.isdir(item_path) and not item.startswith('__'):
        #         st.write(f"Found API module: {item}")
        #         try:
        #             # Import the submodule
        #             submodule = importlib.import_module(f"{module_path}.{item}")
        #             st.write(f"Submodule contents: {dir(submodule)}")
                    
        #             # Look for functions like get_clients, sync_detailed, etc.
        #             for name, obj in inspect.getmembers(submodule):
        #                 if inspect.isfunction(obj) and not name.startswith('_'):
        #                     # Get the function's parameters
        #                     params = inspect.signature(obj).parameters
        #                     required_params = {
        #                         name: param.annotation 
        #                         for name, param in params.items() 
        #                         if param.default == inspect.Parameter.empty 
        #                         and name not in ['self', 'client']  # Exclude self and client params
        #                     }
        #                     if required_params:  # Only add if it has parameters
        #                         endpoints[f"{item}.{name}"] = required_params
        #         except ImportError as e:
        #             st.write(f"Error importing {item}: {str(e)}")
        #             continue
        
        return endpoints
    except ImportError as e:
        st.error(f"Could not import {module_path}: {str(e)}")
        st.info(f"Make sure you have installed the package with: pip install -e ./{folder_name}")
        return {}

def handle_endpoint_call(client_name, endpoint_name, params):
    """Handle the API call for the selected endpoint"""
    try:
        # Split endpoint name into class and method
        class_name, method_name = endpoint_name.split('.')
        
        # Import the client module
        client_module = importlib.import_module(f"{client_name}_client.client")
        api_class = getattr(client_module, class_name)
        
        # Create client instance with authentication
        client_instance = api_class(
            host=BASE_URL.format(api_name=client_name),
            headers={
                "Authorization": f"Bearer {st.session_state.access_token}",
                "X-Datev-Client-ID": CLIENT_ID
            }
        )
        
        # Call the method with provided parameters
        method = getattr(client_instance, method_name)
        response = method(**params)
        
        # Display response
        st.json(response)
        
    except Exception as e:
        st.error(f"Error calling endpoint: {str(e)}")

def main():
    init_session_state()
    st.title("DATEV API Integration Dashboard")
    
    # Handle authentication
    if not st.session_state.access_token:
        login()
        handle_callback()
        return

    # Logout button
    if st.sidebar.button("Logout"):
        st.session_state.access_token = None
        st.rerun()
    
    # Get available clients
    clients = get_available_clients()
    
    # Create sidebar navigation
    st.sidebar.header("Available APIs")
    
    # Create buttons for each client
    for client in clients:
        if st.sidebar.button(client.title()):
            st.session_state.current_client = client
            st.session_state.current_endpoint = None
            st.rerun()
    
    # Display endpoints for selected client
    if st.session_state.get('current_client'):
        st.header(f"{st.session_state.current_client.title()} API")

        # Get available endpoints
        import_module, endpoints = get_client_endpoints(st.session_state.current_client)
        
        # Create dropdown for endpoints
        for endpoint_group in endpoints.keys():
            st.markdown(f"#### {endpoint_group}")
            endpoint_key = f"endpoint_selector_{endpoint_group}"
            selected_endpoint = st.selectbox(
                "Select Endpoint",
                options=endpoints[endpoint_group],
                format_func=lambda x: x.split('.')[0],
                key=endpoint_key,
                index=None
            )
        
            if selected_endpoint:
                # Get the base module name and import the specific module right after selection
                base_module = import_module.__name__
                clients_module = importlib.import_module(f"{base_module}.api.{endpoint_group}.{selected_endpoint.split('.')[0]}")
                
                # Get the function signature and prepare inputs
                signature = inspect.signature(clients_module.sync_detailed)
                inputs = {}
                
                # Show required parameters first
                if len(signature.parameters.items()) > 1:
                    st.markdown(f"##### Required Parameters:")
                for param_name, param in signature.parameters.items():
                    if param_name != 'client' and param.default == inspect.Parameter.empty:
                        param_type = param.annotation.__name__ if param.annotation != inspect.Parameter.empty else "any"
                        
                        if param_type == 'bool':
                            inputs[param_name] = st.checkbox(
                                param_name, 
                                key=f"{endpoint_key}_{param_name}"
                            )
                        elif param_type in ['int', 'float']:
                            inputs[param_name] = st.number_input(
                                param_name,
                                key=f"{endpoint_key}_{param_name}"
                            )
                        else:
                            inputs[param_name] = st.text_input(
                                param_name,
                                key=f"{endpoint_key}_{param_name}"
                            )

                # Optional parameters in expander
                with st.expander("Optional Parameters"):
                    for param_name, param in signature.parameters.items():
                        if param_name != 'client' and param.default != inspect.Parameter.empty:
                            param_type = param.annotation.__name__ if param.annotation != inspect.Parameter.empty else "any"
                            st.write(f"##### Optional: {param_name} ({param_type})")
                            
                            # Check if default is an Unset object
                            is_unset = str(param.default).find('Unset object at') != -1
                            
                            if param_type == 'bool':
                                inputs[param_name] = st.checkbox(
                                    param_name,
                                    value=False if is_unset else param.default,
                                    key=f"{endpoint_key}_{param_name}"
                                )
                            elif param_type in ['int', 'float']:
                                inputs[param_name] = st.number_input(
                                    param_name,
                                    value=0 if is_unset else param.default,
                                    key=f"{endpoint_key}_{param_name}"
                                )
                            else:  # For string and other types
                                inputs[param_name] = st.text_input(
                                    param_name,
                                    value="" if is_unset else str(param.default),
                                    key=f"{endpoint_key}_{param_name}"
                                )
                            
                            # Only add to inputs if value is provided
                            if inputs[param_name] in ["", 0, False] and is_unset:
                                del inputs[param_name]

                # Execute button after parameters
                if st.button("Execute", key=f"execute_button_{endpoint_group}"):
                    client = import_module.AuthenticatedClient(
                        base_url="https://accounting-clients.api.datev.de/platform-sandbox/v2",
                        token=st.session_state.access_token,
                        headers={
                            "x-datev-client-id": "2dc1ae73bb210ebaa3df04c703ec779d"
                        }
                    )
                    with client as client:
                        try:
                            my_data = clients_module.sync_detailed(client=client, **inputs)
                            
                            # Status code with color
                            if my_data.status_code < 300:  # Success
                                st.success(f"Status Code: {my_data.status_code}")
                            elif my_data.status_code < 400:  # Redirect
                                st.warning(f"Status Code: {my_data.status_code}")
                            else:  # Error
                                st.error(f"Status Code: {my_data.status_code}")
                            
                            # Pretty print JSON response
                            try:
                                # Convert bytes to string and parse JSON
                                json_response = json.loads(my_data.content.decode('utf-8'))
                                # Convert back to string with pretty printing
                                pretty_json = json.dumps(json_response, indent=4, sort_keys=True)
                                # Display using st.code() for better formatting
                                st.code(pretty_json, language="json")
                            except Exception as e:
                                st.error(f"Error parsing response: {str(e)}")
                        except Exception as e:
                            st.error(f"Error executing endpoint: {str(e)}")

                
    else:
        # Add a message when no client is selected
        st.info("Please select an API from the sidebar to begin.")

if __name__ == "__main__":
    st.set_page_config(
        page_title="DATEV API Integration",
        page_icon="📊",
        layout="wide"
    )
    main() 