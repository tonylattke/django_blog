/* Append value to the form
 * @form : Form
 * @name : Attribute name
 * @value: Attribute value
 */
function appendInfoForm (form, name, value) {
	var aux = document.createElement("input");
	aux.setAttribute("name", name);
	aux.setAttribute("value", value);
	aux.setAttribute("type", "hidden");
	form.append(aux);
}