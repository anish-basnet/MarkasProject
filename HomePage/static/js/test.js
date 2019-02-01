function validate_replay(){
    var name=document.getElementById('contact-nam').value;
    var email=document.getElementById('contact-emai').value;
    var pat_name=/^[a-zA-Z\s]+$/;
    var pat_email=/^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
    var val=false;
    if(!name.match(pat_name)){
        document.getElementById('contact-nam').value="";
        document.getElementById('contact-nam').focus();
        val=false;
    }else {
            if(!email.match(pat_email)){
                document.getElementById('contact-emai').value="";
                document.getElementById('contact-emai').focus();
                val=false;
            }else{
                val=true;
            }
    }
    return val;
}
