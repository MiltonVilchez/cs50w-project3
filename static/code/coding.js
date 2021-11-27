var modal = document.getElementById("exampleModal");
modal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;
    var recipient = button.getAttribute('data-whatever');
    var type = button.getAttribute('data-type');
    modal.querySelector(".modal-title").innerHTML = recipient;
    modal.querySelector(".otherTitle").innerHTML = recipient + " - Chesse";
    modal.querySelector(".valueTitle").value = recipient + " - Chesse";
    if (type == "Special"){
      modal.querySelector(".letters").innerHTML = "If you want, you can add 6 toppings:"; 
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