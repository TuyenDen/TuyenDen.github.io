function calculateAge(yearBorn) {
	var currentTime = new Date();
	var currentYear = currentTime.getFullYear();
	return currentYear - yearBorn;
	
}

var name = prompt("Enter your name: ")			

var yearBorn = prompt("Enter the year you were born: ");
var age;
age = calculateAge (yearBorn);
console.log(name + " is " + age + " years old") ;
var message = "";
if (age < 18) {
	message += "You are";
	var i=0;
	while (i<5){
		message += "very";
		i++;
	}
	message += "young";
	if ((age>5) && (agea<10)){
		message = "You are a kid";
	}
} else if (age<50){
	message = "You are quite young";

} else{
	message = "You are over 50 years old";

}
console.log(message)

var gender = prompt("Are you male or female? (male/female)")
switch (gender) {
	case "male" :
		console.log("You are a man");
		break;
	case "female" :
		console.log("You are a woman");
		break;
	default:
		console.log("Wrong gender input, undefine");

}

var isClose = confirm("Do you want to close current tab?")
message = "" ;
if (isClose === true) {
	console.log("Bye bye")
} else {
	console.log("Thank you for staying with me")
}




