
//Main file for divide microservice for web calculator in Golang //

package main
//package handler

//import go dependancies

import (
	"fmt"
	"log"
	"net/http"
	"strings"
	"encoding/json"
	"strconv"


)

//main function for go microservice
func main()	{

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {

	//get header values
	x, ok := r.URL.Query()["x"]
	y, ok := r.URL.Query()["y"]


	//if statement utilised if x or y parameter is missing to return default values
	if !ok || len(y[0]) < 1 || len(x[0]) < 1 {
		//create struct variable type to create json object
		type Divvalues struct {
				DefaultValue1     int
				DefaultValue2  	 int
				Answer   				 int
			}
			//create instance of struct type
			group := Divvalues{
				DefaultValue1:    0,
				DefaultValue2:   	0,
				Answer: 		0,
			}
			b, err := json.Marshal(group)
			if err != nil {
				fmt.Println(w, "Error")
				return
			}
			s:= string(b)
			fmt.Fprintf(w,s)

			return
		}

		//format string header correctly
		string_x := strings.Join(x, "")
		string_y := strings.Join(y, "")

		//convert string header to int
	 	int_val1, err := strconv.Atoi(string_x)

		//if errror when converting to int then print error
		if err != nil {
			fmt.Println(w, "Error")
		}

		//convert string header to int
		int_val2, err := strconv.Atoi(string_y)

		//if error when converting to int then print error
		if err != nil {
			fmt.Println(w, "Error")
		}

		//call divide function and assign to div_value
		div_value := divide(int_val1,int_val2)

		fmt.Println("Div value =  ", div_value)

		//create struct variable type to create json object
		type Divvalues struct {
				Value1     int
				Value2  	 int
				Answer   	 int
			}

			//create instance of struct type
			group := Divvalues{
				Value1:     int_val1,
				Value2:   	int_val2,
				Answer: 		div_value,
			}

			//use json marshall to group the 3 elements into json object
			b, err := json.Marshal(group)

			//if error in json marshall then print error
			if err != nil {
				fmt.Println("error:", err)
			}

			//convert json object to string
			s:= string(b)

			//print string to screen
			fmt.Fprintf(w,s)


	})

	//set http port listener to port 8080
	log.Fatal(http.ListenAndServe(":8080", nil))
}


//divide function carries out divide of 2 ints and returns an int
func divide(x , y int) int {

				 //if denominsator bigger than numerator return 0
				 if x < y  || y == 0 {
					 return 0
				 }

         div_value  := x / y

         return div_value

}
