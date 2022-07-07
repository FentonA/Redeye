package escrow

type Payment struct {
	Amount   int64
	Currency string
}

func Escrow(payer string, payee string, charge Payment) bool {
	return true
}
