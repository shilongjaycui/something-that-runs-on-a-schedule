"""Unit tests of MyWedgetService."""
import aws_cdk as core
from aws_cdk import assertions

from my_widget_service.my_widget_service_stack import MyWidgetServiceStack


# example tests. To run these tests, uncomment this file along with the example
# resource in my_widget_service/my_widget_service_stack.py
def test_sqs_queue_created():
    """Test to see if an SQS queue is created."""
    app = core.App()
    stack = MyWidgetServiceStack(app, "my-widget-service")
    assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
