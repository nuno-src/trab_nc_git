

function ajax(){

    var aj;
    var xmlHttp;
    if(window.XMLHttpRequest){
        xmlHttp = new XMLHttpRequest;

    }else{
    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP")
    }



    xmlHttp.onreadystatechange = function(){
        if(xmlHttp.readyState == 4 && xmlHttp.status == 200){
           console.log(xmlHttp.responseText);
           aj = xmlHttp.responseText;
           //console.log(typeof aj);

           if(xmlHttp.responseText == "logged"){
            window.location.replace('http://localhost:5000/login')
           }
            /*
            aj = xmlHttp.responseText;
            console.log(aj)
            if (aj != null){
                return true;
            }
            else{
                return false;
            }
            */
        }

    }

    xmlHttp.open('GET', 'sessions.txt', true);
    xmlHttp.send();




}
