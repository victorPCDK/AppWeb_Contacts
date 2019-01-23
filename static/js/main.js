var btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete){
    const btnArray= Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('Estas seguro?')){
                e.preventDefault();
            }
        });
    });
}

var btnValidar = document.querySelectorAll('.btn-validar')
if(btnValidar){
    var name = document.getElementById("fullname").value;
    var phone = document.getElementById("phone").value;
    var email = document.getElementById("email").value;
    if(name == "" || phone == "" || email==""){
        alert("Llena el campo");
        return false;
    }

}