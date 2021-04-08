from behave import when, then
from clickbrick_cli import hello

@when('I start the program without any parameters')
def i_start_the_program_without_any_parameters(context):
    output = hello.process_arguments(['hello'])
    print(output)
    context.output = output

@then('It prints "{text}"')
def it_prints_hello_world(context, text):
    assert context.output == text