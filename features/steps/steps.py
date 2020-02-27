from behave import *

@given('I have 2 dollars')
def step_given_have_2(context):
    context.dollars = 2

@when('I earn {amount} dollars')
def step_when_earn(context, amount):
    context.dollars += int(amount)

@then('I should have {x} dollars')
def step_then_i_have(context, x):
	assert context.dollars == int(x)
