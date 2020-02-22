
<?php

//Index file for PHP math add function microservice //

header("Access-Control-Allow-Origin: *");		//implement CORS
header("Content-type: application/json");		//set content type as JSON
require('functions.inc.php');								//import add function file

//set default values
$output = array(
	"error" => false,
	"string" => "",
	"answer" => 0
);

//get x and y header values
$x = $_REQUEST['x'];
$y = $_REQUEST['y'];

//call add function on x and y values
$answer=add($x,$y);

//convert resultant value to a String
$output['string']=$x."+".$y."=".$answer;
$output['answer']=$answer;

//output value as json object
echo json_encode($output);
exit();
