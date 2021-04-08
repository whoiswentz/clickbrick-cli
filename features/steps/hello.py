from behave import when, then
from clickbrick_cli import hello


@when('I start the program without any parameters')
def i_start_the_program_without_any_parameters(context):
    output = hello.process_arguments(['hello'])
    context.output = output


@when('I start the program passing a name')
def i_start_the_program_passing_a_name(context):
    output = hello.process_arguments(['hello', '--name', 'name'])
    context.output = output


@then('It prints "{text}"')
def it_prints_hello_world(context, text):
    print(context.output, text)
    assert context.output == text
