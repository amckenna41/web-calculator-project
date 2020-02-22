
// Main power function for power microservice for web calculator //

package com.example.demo;

//import neccessary springboot classes and dependancies
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

//Main class that controls the rest api of the microservice
//CORS integration
@RestController
@CrossOrigin(origins = "*")   //implement cors
public class Power implements ErrorController {			//class implements the errorcontroller class used for error handling

   //constant PATH to store the error path
   private static final String PATH = "/error";

   //method to get the x and y parameters from the URL
   @RequestMapping("/")
   public String power(@RequestParam(value = "x", required =false) String x, @RequestParam(value ="y" , required = false) String y) {

       //validation carried out if x and y variables are empty
     if (x == "" || y == "") {
      int power_value = 0;
      return String.format("%d", power_value);

     }

       //convert string x and y values to double data type
       //double type needed for the Math.pow method
       double x_double = Double.parseDouble(x);
       double y_double = Double.parseDouble(y);

       //calculate the power value of x^y using the Math class, convert this value to an integer
  	   int power_value = (int)Math.pow(x_double,y_double);

  	   //return power_value as a formatted string
  	   return String.format("%d", power_value);


      }
    //method for handling errors
   	@RequestMapping(value = "/error")
   	public String error()  {
   		return "Error, check parameter values are present and are whole numbers";
   	}

   	//method inherited from errorcontroller class for error handling
	@Override
	public String getErrorPath() {
		return PATH;
	}
}
