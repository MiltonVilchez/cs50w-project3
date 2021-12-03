var modal = document.getElementById("exampleModal");
modal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;
    var recipient = button.getAttribute('data-whatever');
    var type = button.getAttribute('data-type');
    modal.querySelector(".modal-title").innerHTML = recipient;
    console.log(recipient);
    modal.querySelector(".valueTitle").value = recipient;
    if (type == "Special"){
      const s = "If you want, you can add 6 toppings:";
      modal.querySelector(".letters").innerHTML = s; 
    }
});

function Desabilita(esto) {
    var numcheckbox = 0;
    if (esto.checked) {
      if (numcheckbox >= 3) {
        esto.checked = false;
        alert("Son solo 3 Toppings");
      } else {
        numcheckbox++;
      }
    } else {
      numcheckbox--;
    }
  }

//Ya manqueamos
