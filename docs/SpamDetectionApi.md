# cloudmersive_spam_api_client.SpamDetectionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spam_detect_text_string_advanced_post**](SpamDetectionApi.md#spam_detect_text_string_advanced_post) | **POST** /spam/detect/text-string/advanced | Perform advanced AI spam detection and classification against input text string.  Analyzes input content as well as embedded URLs with AI deep learnign to detect spam, phishing and other unsafe content.  Uses 25-100 API calls depending on model selected.
[**spam_detect_text_string_post**](SpamDetectionApi.md#spam_detect_text_string_post) | **POST** /spam/detect/text-string | Perform AI spam detection and classification against input text string.  Analyzes input content as well as embedded URLs with AI deep learnign to detect spam, phishing and other unsafe content.  Uses 25-75 API calls depending on model selected.


# **spam_detect_text_string_advanced_post**
> SpamDetectionAdvancedResponse spam_detect_text_string_advanced_post(body=body)

Perform advanced AI spam detection and classification against input text string.  Analyzes input content as well as embedded URLs with AI deep learnign to detect spam, phishing and other unsafe content.  Uses 25-100 API calls depending on model selected.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_spam_api_client
from cloudmersive_spam_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_spam_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_spam_api_client.SpamDetectionApi(cloudmersive_spam_api_client.ApiClient(configuration))
body = cloudmersive_spam_api_client.SpamDetectionAdvancedRequest() # SpamDetectionAdvancedRequest | Spam detection request (optional)

try:
    # Perform advanced AI spam detection and classification against input text string.  Analyzes input content as well as embedded URLs with AI deep learnign to detect spam, phishing and other unsafe content.  Uses 25-100 API calls depending on model selected.
    api_response = api_instance.spam_detect_text_string_advanced_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpamDetectionApi->spam_detect_text_string_advanced_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpamDetectionAdvancedRequest**](SpamDetectionAdvancedRequest.md)| Spam detection request | [optional] 

### Return type

[**SpamDetectionAdvancedResponse**](SpamDetectionAdvancedResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spam_detect_text_string_post**
> SpamDetectionResponse spam_detect_text_string_post(body=body)

Perform AI spam detection and classification against input text string.  Analyzes input content as well as embedded URLs with AI deep learnign to detect spam, phishing and other unsafe content.  Uses 25-75 API calls depending on model selected.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_spam_api_client
from cloudmersive_spam_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_spam_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_spam_api_client.SpamDetectionApi(cloudmersive_spam_api_client.ApiClient(configuration))
body = cloudmersive_spam_api_client.SpamDetectionRequest() # SpamDetectionRequest | Spam detection request (optional)

try:
    # Perform AI spam detection and classification against input text string.  Analyzes input content as well as embedded URLs with AI deep learnign to detect spam, phishing and other unsafe content.  Uses 25-75 API calls depending on model selected.
    api_response = api_instance.spam_detect_text_string_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpamDetectionApi->spam_detect_text_string_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpamDetectionRequest**](SpamDetectionRequest.md)| Spam detection request | [optional] 

### Return type

[**SpamDetectionResponse**](SpamDetectionResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

