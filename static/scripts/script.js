function trigger_menu(){
	console.log("a");
	var menu_icon = document.getElementById("menu-icon");
	var links = document.getElementById("links");
	var menu_opened = false;

	if (menu_opened == false){
		menu_icon.style.transform = "rotate(90deg)";
		links.style.display = "block";
		menu_opened = true;
	}else{
		menu_icon.style.transform = "rotate(0deg)";
		links.style.display = "none";
		menu_opened = false;
	}
}

function option_click(el){
  const elid = el.id;
  const boxes = document.querySelectorAll("#" + elid);

  boxes.forEach(box => {
  	box.classList.remove("gradient-border");
    box.classList.add("inactive-border");
  });
  
  el.classList.add("gradient-border");
  el.classList.remove("inactive-border");
}

var metric = true;

function units(el){
	const elid = el.id;
  const buttons = document.querySelectorAll(".unit-button");
	const sameSystem = document.querySelectorAll("#" + elid);
	const dbg = getComputedStyle(document.documentElement).getPropertyValue('--dbg');
	const bg = getComputedStyle(document.documentElement).getPropertyValue('--bg');

  buttons.forEach(button => {
  	button.style.background = dbg;
  });

  sameSystem.forEach(btn => {
  	btn.style.background = bg;
  });

  if (metric === true){
  	metric = false;

  	document.getElementById("unit-selector-1").checked = false;
  	document.getElementById("unit-selector-2").checked = true;

  	impInput = document.querySelectorAll(".imperial").forEach(input => {
	  	input.style.display = "block";
	  });

	  document.querySelector("#main-weight").setAttribute("min", 90);
	  document.querySelector("#main-weight").setAttribute("max", 450);
	  document.querySelector("#main-weight").value = 130;

	  document.querySelector("#main-height").setAttribute("min", 4);
	  document.querySelector("#main-height").setAttribute("max", 8);
	  document.querySelector("#main-height").value = 5;
  }
  else{
  	metric = true;

  	document.getElementById("unit-selector-1").checked = true;
  	document.getElementById("unit-selector-2").checked = false;

  	impInput = document.querySelectorAll(".imperial").forEach(input => {
	  	input.style.display = "none";
	  });

	  document.querySelector("#main-weight").setAttribute("min", 40);
	  document.querySelector("#main-weight").setAttribute("max", 200);
	  document.querySelector("#main-weight").value = 50;

	  document.querySelector("#main-height").setAttribute("min", 130);
	  document.querySelector("#main-height").setAttribute("max", 250);
	  document.querySelector("#main-height").value = 175;
  }
}

function selectFirstUnit(){
	const sameSystem = document.querySelectorAll("#m");
	const bg = getComputedStyle(document.documentElement).getPropertyValue('--bg');

	sameSystem.forEach(btn => {
  	btn.style.background = bg;
  });

  document.getElementById("unit-selector-1").checked = true;
}