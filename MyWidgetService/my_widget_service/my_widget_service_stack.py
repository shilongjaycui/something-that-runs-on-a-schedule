"""CDK stack for my_widget_service."""
from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from constructs import Construct


class MyWidgetServiceStack(Stack):
    """CDK stack for my_widget_service."""

    # pylint: disable-next=useless-parent-delegation
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        """Construct my_widget_service's CDK stack."""
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MyWidgetServiceQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
