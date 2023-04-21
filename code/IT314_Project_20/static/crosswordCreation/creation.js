let formfield = document.getElementById('formfield');

function add() {
	console.log("Clicked");
	let newField = document.createElement('input');
	newField.setAttribute('type', 'text');
	newField.setAttribute('name', 'text');
	newField.setAttribute('class', 'text');
	newField.setAttribute('siz', 50);
	newField.setAttribute('placeholder', 'Optional Field');
	formfield.appendChild(newField);
}

function remove() {
	let input_tags = formfield.getElementsByTagName('input');

	if (input_tags.length > 2) {
		formfield.removeChild(input_tags[(input_tags.length) - 1]);
	}
}