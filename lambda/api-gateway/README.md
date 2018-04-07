## Testing

With Cognito Token

````
curl -X POST -H 'Authorization: <PASTE-YOUR-COGNITO-TOKEN>' -H "Content-Type: application/json" -H "Content-Type: application/json" -d '{"KEY1": "VALUE1","KEY2": "VALUE2"}' "https://API-GATEWAY-URL-WITH-ENDPOINT"
````

With API Key

````
curl -X POST -H "x-api-key: <YOUR-API-KEY>" -H "Content-Type: application/json" -d '{"KEY1": "VALUE1"}' "https://<YOUR-API-GATEWAY-URL>/<WITH-API-GATEWAY-ENDPOINT>"
````

