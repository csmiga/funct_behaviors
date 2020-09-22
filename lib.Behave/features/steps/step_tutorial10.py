# File: features/steps/step_tutorial10.py
#
# Tutorial 10: User-defined Data Type
# https://jenisys.github.io/behave.example/tutorials/tutorial10.html
#
# Goal: Show how user-defined data types can be used in step parameters.
#
# First you need to provide the type converter for Number and register it:

# ----------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ----------------------------------------------------------------------------
from behave import register_type

def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)
# -- REGISTER: User-defined type converter (parse_type).
register_type(Number=parse_number)

# Now you can use Number as type in step parameters for the step definitions:

# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, equal_to
from calculator import Calculator

@given('I have a calculator')
def step_impl(context):
    context.calculator = Calculator()

@when('I add "{x:Number}" and "{y:Number}"')
def step_impl(context, x, y):
    assert isinstance(x, int)
    assert isinstance(y, int)
    context.calculator.add2(x, y)

@then('the calculator returns "{expected:Number}"')
def step_impl(context, expected):
    assert isinstance(expected, int)
    assert_that(context.calculator.result, equal_to(expected))