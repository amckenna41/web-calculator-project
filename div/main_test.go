
//Testing for divide function in Golang //
package main

//import testing dependancy
import ("testing")

//tests to test the result from the function with expected value
func TestDivide(t *testing.T) {

	if divide(10, 5) != 2 {
		t.Error("Expected 10 / 5 to equal 2")
		return
		}

	if divide(100, 20) != 5 {
		t.Error("Expected 100 / 20 to equal 5")
		return
			}

	if divide(30, 5) != 6 {
		t.Error("Expected 30 / 5 to equal 6")
		return
			}

	if divide(50, 5) != 10 {
		t.Error("Expected 30 / 5 to equal 6")
		return
}
	}

//tests to test the result from the function with expected value from struct
func TestDiv_struct(t *testing.T) {

	//struct to hold x and y parameter and result
	tables := []struct {
		x int
		y int
		result int
	}
	{
		{10, 5, 2},
		{40, 5, 8},
		{78, 2, 39},
		{120, 2, 60},
	}

	//loop through struct, testing if the x and y parameter produce the correct result
	for _, table := range tables {
		result := divide(table.x, table.y)
		if result != table.result {
			t.Errorf("Division of (%d+%d) was incorrect, got: %d, want: %d.", table.x, table.y, result, table.result)
		}
	}
}
