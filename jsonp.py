import json

body = json.dumps(
    {
        "gateway": "chctest109",
        "gatewayId": "c10532a4-1c6f-4bc9-b8bd-2151877c9090",
        "version": 0,
        "created": "2022-06-13T18:51:44.140Z",
        "tags": [
            {
                "id": "chctest109.tag001",
                "tagName": "tag001",
                "description": " a tag",
                "engineeringUnits": "degcs",
                "rangeHigh": 1000,
                "rangeLow": 5,
                "scanFrequency": 12,
                "scanUnits": "s",
            }
        ],
    }
)

print(type(body.encode()))
