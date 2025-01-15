package main

import (
	"fmt"
)

func main() {
	var cubeVal int64
	var input int64

	input = 1500

	cubeVal = input * input * input

	fmt.Println("cubeVal: %d", cubeVal)
}
