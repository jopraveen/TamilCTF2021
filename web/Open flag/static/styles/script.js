'use strict';

window.addEventListener('load', windowLoaded, false);

function windowLoaded() {
	var 
		tabs = document.querySelectorAll('.cd-tabs')[0],
		login = document.querySelectorAll('a[data-content=\'login\']')[0],
		signup = document.querySelectorAll('a[data-content=\'signup\']')[0],
		tabContentWrapper = document.querySelectorAll('ul.cd-tabs-content')[0],
		currentContent = document.querySelectorAll('li.selected')[0];

	login.addEventListener('click', clicked, false);
	signup.addEventListener('click', clicked, false);

	function clicked(event) {
		event.preventDefault();
    
		var selectedItem = event.currentTarget;
		if (selectedItem.className === 'selected') {
      // ...       
		} else {
			var selectedTab = selectedItem.getAttribute('data-content'),
				selectedContent = document.querySelectorAll('li[data-content=\'' + selectedTab + '\']')[0];

			if (selectedItem == login) {
				signup.className = '';
				login.className = 'selected';
			} else {
				login.className = '';
				signup.className = 'selected';
			}

			currentContent.className = '';
			currentContent = selectedContent;
			selectedContent.className = 'selected';

		}
	}

	var inputs = document.querySelectorAll('input');
	for (var i = 0; i < inputs.length; i++) {
		inputs[i].addEventListener('focus', inputFocused, false);
	}

	function inputFocused(event) {
		var label = document.querySelectorAll('label[for=\''+ this.name +'\']')[0];
		label.className = 'focused';
	}
}	
