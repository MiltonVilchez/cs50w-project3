var modal = document.getElementById("exampleModal");
    console.log(modal);
    modal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        console.log(button);
        var recipient = button.getAttribute('data-whatever');
        modal.querySelector(".modal-title").innerHTML = recipient;       
    })