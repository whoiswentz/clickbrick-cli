Feature: Hello World
    Scenario: The program greets the world
        When I start the program without any parameters
        Then It prints "hello world"

    Scenario: The Program Should Greet Us
        When I start the program passing a name
        Then It prints "hello name"