var modal = document.getElementById("exampleModal");
modal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;
    var recipient = button.getAttribute('data-whatever');
    modal.querySelector(".modal-title").innerHTML = recipient;
    modal.querySelector(".otherTitle").innerHTML = recipient + " - Chesse";
    modal.querySelector(".valueTitle").value = recipient + " - Chesse";
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