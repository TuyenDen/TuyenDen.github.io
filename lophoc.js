function saveData(){
	var firstname = document.getElementBuId("firstname").value;
	var lastname = document.getElementBuId("lastname").value;
	sessionStorage.firstname = firstName;
	sessionStorage.lastname = lastName;
}

function init() {
	var regForm = document.getElementBuId("registerForm")
	regForm.onsubmit = saveData;
}

window.onload = init;