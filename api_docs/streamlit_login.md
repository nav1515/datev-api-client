# st.login - Streamlit Docs
Learn more in [User authentication and information](https://docs.streamlit.io/develop/concepts/connections/authentication).



* Function signature[source]:  st.login(provider=None) 
* Function signature[source]: Parameters
* Function signature[source]:           provider          (str or None)         
  *                 The name of your provider configuration to use for login.If provider is None (default), Streamlit will use all settingsin the [auth] dictionary within your app's secrets.toml file.Otherwise, use an [auth.{provider}] dictionary for the namedprovider, as shown in the examples that follow. When you pass a stringto provider, Streamlit will use redirect_uri andcookie_secret, while ignoring any other values in the [auth]dictionary.      


#### Examples

> **Example 1: Use an unnamed default identity provider**
> 
> If you do not specify a name for your provider, specify all settings within the \[auth\] dictionary of your secrets.toml file. The following example configures Google as the default provider. For information about using OIDC with Google, see [Google Identity](https://developers.google.com/identity/openid-connect/openid-connect).
> 
> .streamlit/secrets.toml:
> 
> ```
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"

```

> 
> Your app code:
> 
> ```
import streamlit as st

if not st.experimental_user.is_logged_in:
    if st.button("Log in"):
        st.login()
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.experimental_user.name}!")

```

> 
> **Example 2: Use a named identity provider**
> 
> If you specify a name for your provider, save the shared settings in the \[auth\] dictionary of your secrets.toml file, and save the other settings in an \[auth.{provider}\] dictionary, where {provider} is the name of your provider. The following example configures Microsoft as the provider. The example uses provider="microsoft", but you can use any name. This name is internal to Streamlit and is used to match the login command to its configuration. For information about using OIDC with Microsoft, see [Microsoft Entra ID](https://learn.microsoft.com/en-us/power-pages/security/authentication/openid-settings). To configure your {tenant} value in server\_metadata\_url, see [Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc#find-your-apps-openid-configuration-document-uri).
> 
> .streamlit/secrets.toml:
> 
> ```
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.microsoft]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration"

```

> 
> Your app code:
> 
> ```
import streamlit as st

if not st.experimental_user.is_logged_in:
    st.login("microsoft")
else:
    st.write(f"Hello, {st.experimental_user.name}!")

```

> 
> **Example 3: Use multiple, named providers**
> 
> If you want to give your users a choice of authentication methods, configure multiple providers and give them each a unique name. The following example lets users choose between Okta and Microsoft to log in. Always check with your identity provider to understand the structure of their identity tokens because the returned fields may differ. Remember to set {tenant} and {subdomain} in server\_metadata\_url for Microsoft and Okta, respectively.
> 
> ```
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.microsoft]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration"

[auth.okta]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{subdomain}.okta.com/.well-known/openid-configuration"

```

> 
> Your app code:
> 
> ```
import streamlit as st

if not st.experimental_user.is_logged_in:
    st.header("Log in:")
    if st.button("Microsoft"):
        st.login("microsoft")
    if st.button("Okta"):
        st.login("okta")
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.experimental_user.name}!")

```

> 
> **Example 4: Change the default connection settings**
> 
> prompt="select\_account" may be treated differently by some providers when a user is already logged into their account. If a user is logged into their Google or Microsoft account from a previous session, the provider will prompt them to select the account they want to use, even if it's the only one. However, if the user is logged into their Okta or Auth0 account from a previous session, the account will automatically be selected. st.logout() does not clear a user's related cookies. To force users to log in every time, use prompt="login" as described in Auth0's [Customize Signup and Login Prompts](https://auth0.com/docs/customize/login-pages/universal-login/customize-signup-and-login-prompts).
> 
> .streamlit/secrets.toml:
> 
> ```
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.auth0]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{account}.{region}.auth0.com/.well-known/openid-configuration"
client_kwargs = { "prompt" = "login" }

```

> 
> Your app code:
> 
> ```
import streamlit as st
if st.button("Log in"):
    st.login("auth0")
if st.experimental_user.is_logged_in:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.experimental_user.name}!)

```


[Previous: Authentication & user info](https://docs.streamlit.io/develop/api-reference/user)
[Next: st.logout](https://docs.streamlit.io/develop/api-reference/user/st.logout)

_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io/) are full of helpful information and Streamlit experts.