package main

import (
	"log"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"github.com/stripe/stripe-go"
	"github.com/stripe/stripe-go/charge"
)

type ChargeJSON struct {
	Amount       int64  `json:"amount"`
	ReceiptEmail string `json:"receiptEmail"`
}

func main() {
	err := godotenv.Load(".env")
	if err != nil {
		log.Fatalf("Error loading .env file: %v", err)
	}

	r := gin.Default()

	r.POST("api/charges", func(c *gin.Context) {
		var json ChargeJSON
		c.BindJSON(&json)

		apikey := os.Getenv("stripe_key")
		stripe.Key = apikey

		_, err := charge.New(&stripe.ChargeParams{
			Amount:       stripe.Int64(json.Amount),
			Currency:     stripe.String(string(stripe.CurrencyUSD)),
			Source:       &stripe.SourceParams{Token: stripe.String("tok_visa")},
			ReceiptEmail: stripe.String(json.ReceiptEmail)})

		if err != nil {
			c.String(http.StatusBadRequest, "Request failed")
			return
		}
		c.String(http.StatusCreated, "Successfully charged")
	})

	r.Run(":8080")
}
