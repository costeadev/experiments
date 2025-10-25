
        function buscar(){
            var username = document.getElementsByTagName("input")[0].value;
            if(username) {
                var url = "https://www.chess.com/member/" + username;
                window.location.href = url;
            }
            else {
                alert("Añade un nombre de usuario");
            }
        }