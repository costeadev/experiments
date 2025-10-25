function Display(value){
    document.getElementById("display").value += value;
}
function reset(){
    document.getElementById("display").value = "";
}
function calculate(){
    var displayvalue = document.getElementById("display").value;
    var result = eval(displayvalue);
    document.getElementById("display").value = result;
        if (result === undefined){
            document.getElementById("display").value = "";
        }
}