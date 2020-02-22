<?php

//Test file for add function in web calculator  //

echo "Test Script Starting\n";
require('functions.inc.php');   //import add function file

$x=10;
$y=5;
$expect=15;

//call add function on x and y variables
$answer=add($x,$y);

//output result of add calculation and the exepected result
echo "Test Result: ".$x."+".$y."=".$answer." (expected: ".$expect.")\n";

//if result of calculation is equal to expected value test passes, if not test fails
if ($answer==$expect)
{
    echo "Test Passed\n";
    exit(0); // exit code 0 - success
}
else
{
    echo "Test Failed\n";
    exit(1); // exit code not zero - error
}

//adding more PHP tests

x=49;
$y=20;
$expect=69;

$answer=add($x,$y);

echo "Test Result: ".$x."+".$y."=".$answer." (expected: ".$expect.")\n";

if ($answer==$expect)
{
    echo "Test Passed\n";
    exit(0); // exit code 0 - success
}
else
{
    echo "Test Failed\n";
    exit(1); // exit code not zero - error
}


x=103;
$y=47;
$expect=150;

$answer=add($x,$y);

echo "Test Result: ".$x."+".$y."=".$answer." (expected: ".$expect.")\n";

if ($answer==$expect)
{
    echo "Test Passed\n";
    exit(0); // exit code 0 - success
}
else
{
    echo "Test Failed\n";
    exit(1); // exit code not zero - error
}
