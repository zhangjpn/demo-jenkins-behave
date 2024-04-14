

from behave import given,when,then


@given("given given")
def prepare(context):
    print('aaaa')


@when("when when")
def action(context):
    print('tack action')


@then("then then")
def expect(context):
    print("something should happen")

