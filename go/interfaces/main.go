package main

import "fmt"

type bot interface {
	// Interface type
	getGreeting() string
}

// Concrete types
type englishBot struct{}
type spanishBot struct{}

func main() {
	eb := englishBot{}
	sb := spanishBot{}

	printGreeting(eb)
	printGreeting(sb)
}

func printGreeting(b bot) {
	fmt.Println(b.getGreeting())
}

func (englishBot) getGreeting() string {
	// TODO: custom logic for eb
	return "Hi there!"
}

func (spanishBot) getGreeting() string {
	// TODO: custom logic for sb
	return "Hola!"
}
