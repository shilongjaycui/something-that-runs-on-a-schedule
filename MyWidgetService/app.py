"""Main entry point for the application."""
import aws_cdk as cdk

from my_lambda_cron_service.my_lambda_cron_stack import MyLambdaCronStack

app = cdk.App()
MyLambdaCronStack(
    app,
    "MyLambdaCronStack",
)

app.synth()
