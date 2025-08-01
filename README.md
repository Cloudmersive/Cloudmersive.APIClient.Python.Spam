# cloudmersive_spam_api_client
Easily and directly scan and block spam security threats in input.

This Python package provides a native API client for [Cloudmersive Spam Detection API](https://cloudmersive.com/spam-detection-api)

- API version: v1
- Package version: 3.0.3
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_spam_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_spam_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SpamDetectionApi* | [**spam_detect_text_string_advanced_post**](docs/SpamDetectionApi.md#spam_detect_text_string_advanced_post) | **POST** /spam/detect/text-string/advanced | Perform advanced AI spam detection and classification against input text string.  Analyzes input content as well as embedded URLs with AI deep learnign to detect spam, phishing and other unsafe content.  Uses 25-100 API calls depending on model selected.
*SpamDetectionApi* | [**spam_detect_text_string_post**](docs/SpamDetectionApi.md#spam_detect_text_string_post) | **POST** /spam/detect/text-string | Perform AI spam detection and classification against input text string.  Analyzes input content as well as embedded URLs with AI deep learnign to detect spam, phishing and other unsafe content.  Uses 25-75 API calls depending on model selected.


## Documentation For Models

 - [SpamDetectionAdvancedRequest](docs/SpamDetectionAdvancedRequest.md)
 - [SpamDetectionAdvancedResponse](docs/SpamDetectionAdvancedResponse.md)
 - [SpamDetectionRequest](docs/SpamDetectionRequest.md)
 - [SpamDetectionResponse](docs/SpamDetectionResponse.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



