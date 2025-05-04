// Echo : Prints its command-line arguments
package main

import (
	"fmt"
	"flag"
	"strings"
)
var n = flag.Bool("n",false,"omit trailing newline")
var sep = flag.String("s"," ","separator")

func main() {
	flag.Parse()
	fmt.Printf("n=%t , s=%q \n",*n,*sep)
	fmt.Print(strings.Join(flag.Args(),*sep))
	if !*n {
		fmt.Println()
		fmt.Println()
		fmt.Println()
	}
}