"""CDK stack for my_lambda_cron_service."""
from aws_cdk import Stack
from constructs import Construct

from . import lambda_cron_service


class MyLambdaCronStack(Stack):
    """CDK stack for my_lambda_cron_service."""

    # pylint: disable-next=useless-parent-delegation
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        """Construct my_lambda_cron_service's CDK stack."""
        super().__init__(scope, construct_id, **kwargs)

        lambda_cron_service.LambdaCronService(self, "CronJob")
