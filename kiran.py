from io import BytesIO
from gzip import GzipFile
import json


# @task()
def compress_string_to_bytes(input_str):
    print("compress string to byte executing")
    bio = BytesIO()
    bio.write(input_str)
    bio.seek(0)
    stream = BytesIO()
    compressor = GzipFile(fileobj=stream, mode="w")
    while True:  # until EOF
        chunk = bio.read(8192)
        if not chunk:  # EOF?
            compressor.close()
            return stream.getvalue()
        compressor.write(chunk)


# @task()
def createorupdate_gatewaytag():

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

    inputRequest = compress_string_to_bytes(body.encode())
    print("line 47")
    print(inputRequest)
    # url = f"{self.tenant}/v1/api/gatewaytag{inputRequest}"

    # with self.client.post(
    #     url,
    #     headers=create_header,
    #     name="create or update gatewaytag",
    #     catch_response=True,
    # ) as createorupdategatewaytag_resp:
    #     if (
    #         createorupdategatewaytag_resp.status_code == 201
    #         or createorupdategatewaytag_resp.status_code == 200
    #         or createorupdategatewaytag_resp.status_code == 207
    #     ):
    #         createorupdategatewaytag_resp.success()
    #     elif createorupdategatewaytag_resp.status_code == 503:
    #         logger.info("Invalid host, quitting the test")
    #         self.parent.environment.runner.quit()
    #     else:
    #         createorupdategatewaytag_resp.failure(
    #             f"Unable to update: {0}".format(createorupdategatewaytag_resp.text)
    # )


createorupdate_gatewaytag()
