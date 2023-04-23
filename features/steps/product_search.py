from behave import *

@given("User is on homepage")
def step_impl(context):
    # Implementation goes here
    pass

@when('User enters Ipad in the search bar')
def step_impl(context, item):
    # Implementation goes here
    pass

@when('User enters Iphone in the search bar')
def step_impl(context, item):
    # Implementation goes here
    pass

@then('User should see Iphone product in the results')
def step_impl(context, item):
    # Implementation goes here
    pass

@then('User should see Ipad product in the results')
def step_impl(context, item):
    # Implementation goes here
    pass

@given('User searched for an Iphone')
def step_impl(context, item):
    # Implementation goes here
    pass

@given('User searched for an Ipad')
def step_impl(context, item):
    # Implementation goes here
    pass

@when("User opens first search result")
def step_impl(context):
    # Implementation goes here
    pass

@then('User should see product detail of Iphone')
def step_impl(context, item):
    # Implementation goes here
    pass

@then('User should see product detail of Ipad')
def step_impl(context, item):
    # Implementation goes here
    pass

@when(u'User enters Ipod in the search bar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User enters Ipod in the search bar')


@then(u'User should see Ipod product in the results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User should see Ipod product in the results')


@given(u'User searched for an Ipod')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User searched for an Ipod')


@then(u'User should see product detail of Ipod')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User should see product detail of Ipod')