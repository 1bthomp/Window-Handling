from behave import given, when, then

@given('Open sign in page')
def home_page_for_target(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.original_window

@when('Click on Target terms and conditions link')
def click_target_tc_link(self):
    context.app.sign_in_page.click_TCLINK()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.sign_in_page.verify_terms_and_conditions_page()

@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.app.sign_in_page.switch_to_original_window()
