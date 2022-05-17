from storages.backends.azure_storage import AzureStorage

account_name = 'djangoproject2'
key = 'drDJxEtrc2RS1ygEnUf+mbV8ImYtoml1U7ibVKgYmDEYVuYeRe9W95UMYiu1iWYFrkmwEhAd079g+AStMZ7WmQ=='


class AzureMediaStorage(AzureStorage):
    account_name = account_name
    account_key = key
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = account_name
    account_key = key
    azure_container = 'static'
    expiration_secs = None
