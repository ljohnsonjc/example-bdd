from pytest_bdd import given, when, then

@given('I have entered 50 into the calculator')
def step_i_have_entered_50(calculator):
    calculator.enter(50)

@given('I have entered 70 into the calculator')
def step_i_have_entered_70(calculator):
    calculator.enter(70)

@when('I press add')
def step_i_press_add(calculator):
    calculator.add()

@then('the result should be 120 on the screen')
def step_result_is_120(calculator):
    assert calculator.result() == 120