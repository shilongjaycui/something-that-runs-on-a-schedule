"""The source file to define the widget service."""
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_lambda as lambda_)


class WidgetService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        bucket = s3.Bucket(self, "WidgetStore")

        handler = lambda_.Function(
            self, 'HelloHandler',
            runtime=lambda_.Runtime.PYTHON_3_7,
            code=lambda_.Code.from_asset('lambda'),
            handler='hello.handler',
        )

        bucket.grant_read_write(handler)

        api = apigateway.RestApi(
            self,
            "widgets-api",
            rest_api_name="Widget Service",
            description="This service serves widgets.",
        )

        get_widgets_integration = apigateway.LambdaIntegration(
            handler,
            request_templates={"application/json": '{ "statusCode": "200" }'},
        )

        api.root.add_method("GET", get_widgets_integration)   # GET /
