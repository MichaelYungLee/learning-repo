Go Notes

Hello, World
  Five questions
  1. How do we run the code in our project?
    Go CLI
    - go build: compiles a bunch of go source code files
    - go run: compiles and executes one or two files
    - go fmt: Formats all the code in each file in the current directory
    - go install: compiles and "installs" a package
    - go get: downloads raw source code of someone else's package
    - go test: runs any tests associated with the current project
  2. What does 'package main' mean?
    - Package == Project == Workspace
    - Collection of common source code files
    - Every file in the package must declare the name of the package at the very top
    - Two types of packages: executable and reusable
        - Executable: generates a file we can run
        - Reusable: code used as 'helpers'. Good place to put reusable logic
    - Name of package determines the type of package
        - "main" means executable; any other name will be reusable
    - An executable package must have a function named "main" in it as well
  3. What does 'import "fmt"' mean?
    - fmt is a std lib package that helps with print formatting
  4. What's that 'func' thing?
    - Short for function
  5. How is the main.go file organized?
    - Package declaration
    - Import other packages that we need
    - Declare functions, tell Go to do things
