package main

import (
	"log"

	"github.com/joho/godotenv" 
)

func main() {
	err := godotenv.Load(".env")
	if err != nil {
		log.Fatalf("Error loading .env file")
	}
	// strip.key
	// c, _ := customer.Get("cus")
}
