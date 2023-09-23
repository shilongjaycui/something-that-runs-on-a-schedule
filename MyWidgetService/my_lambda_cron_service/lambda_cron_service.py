"""The source file to define the Lambda cron service."""
from aws_cdk import aws_lambda as lambda_
from aws_cdk import Duration
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from constructs import Construct


class LambdaCronService(Construct):
    """Lambda cron job service class."""

    # pylint: disable-next=invalid-name, redefined-builtin
    def __init__(self, scope: Construct, id: str):
        """Create a Lambda function that gets triggered by an event."""
        super().__init__(scope, id)

        lambdaFn = lambda_.Function(
            self,
            "MessageHandler",
            code=lambda_.Code.from_asset("lambda"),
            handler="message.handler",
            timeout=Duration.seconds(300),
            runtime=lambda_.Runtime.PYTHON_3_7,
        )

        rule = events.Rule(
            self, "Rule",
            schedule=events.Schedule.cron(
                minute='0',
                hour='18',
                month='*',
                week_day='MON-FRI',
                year='*'),
        )
        rule.add_target(targets.LambdaFunction(lambdaFn))
        