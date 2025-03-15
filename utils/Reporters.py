from behave_html_formatter.html import HTMLFormatter


class Reporters():
    """
    Reporters class for adding screenshots to HTMLFormatter in Behave.

    Attributes:
        context (object): The Behave context object containing the runner and formatters.

    Copyright (c) 2025 Rithesh B
    """

    def __init__(self, context):
        self.context = context

    def add_screenshot_to_HTMLFormatter(self, screenshot_data, caption="Screenshot"):
        """
        Adds a screenshot to the HTMLFormatter in the Behave report.

        Parameters:
            screenshot_data (bytes): The screenshot data in bytes format.
            caption (str): The caption for the screenshot. Default is "Screenshot".

        Example:
            screenshot_data = context.driver.get_screenshot_as_base64()
            reporters = Reporters(context)
            reporters.add_screenshot_to_HTMLFormatter(screenshot_data, "Test Screenshot")
        """
        for formatter in self.context._runner.formatters:
            if "html" in formatter.name and hasattr(formatter, 'embedding') and isinstance(formatter, HTMLFormatter):
                formatter.embedding(mime_type="image/png", data=screenshot_data, caption=caption)
                print("Screenshot added ----- ")