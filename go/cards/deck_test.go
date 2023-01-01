package main

import (
	"os"
	"testing"
)

func TestNewDeck(t *testing.T) {
	d := newDeck()

	if len(d) != 52 {
		t.Errorf("Expected deck length of 52, but got %d", len(d))
	}

	if d[0] != "Ace of Spades" {
		t.Errorf("Expected first card as Ace of Spades, but got %v", d[0])
	}

	if d[len(d)-1] != "King of Diamonds" {
		t.Errorf("Expected last card as King of Diamonds, but got %v", d[len(d)-1])
	}
}

func TestSaveToFileAndNewDeckFromFile(t *testing.T) {
	os.Remove("_decktesting")
	d := newDeck()
	d.saveToFile("_decktesting")

	loadedDeck := newDeckFromFile("_decktesting")

	if len(loadedDeck) != 52 {
		t.Errorf("Expected 52 cards in deck, but got %d", len(loadedDeck))
	}

	os.Remove("_decktesting")
}

func TestDeal(t *testing.T) {
	d := newDeck()
	handSize := 5

	hand := d.deal(handSize)

	if len(hand) != handSize {
		t.Errorf("Expected hand to have %v cards, but got %v instead.", handSize, len(hand))
	}

	if len(d) != 47 {
		t.Errorf("Expected deck to have 47 remaining cards, but got %v instead.", len(d))
	}

	/* if len(remainingDeck) != (len(d) - handSize) {
		t.Errorf("Expected remaining deck to have %v cards, but got %v instead.", (len(d) - handSize), len(remainingDeck))
	} */
}

func TestShuffle(t *testing.T) {
	/* Rudimentary test for randomness. This could fail even if
	deck is being shuffled "correctly", but didn't want to go down rabbit hole
	on testing randomness atm */
	d := newDeck()

	for i := 0; i < 10; i++ {
		d.shuffle()
	}
	if d[0] == "Ace of Spades" && d[len(d)-1] == "King of Diamonds" {
		t.Errorf("First and last cards of deck are the same after initialization. shuffle() may need further inspection.")
	}
}
