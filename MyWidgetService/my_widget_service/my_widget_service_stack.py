"""CDK stack for my_widget_service."""
from aws_cdk import Stack  # Duration,; aws_sqs as sqs,
from constructs import Construct
from . import widget_service


class MyWidgetServiceStack(Stack):
    """CDK stack for my_widget_service."""

    # pylint: disable-next=useless-parent-delegation
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        """Construct my_widget_service's CDK stack."""
        super().__init__(scope, construct_id, **kwargs)

        widget_service.WidgetService(self, "Widgets")
