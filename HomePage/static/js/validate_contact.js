/**
 * Created by DELL on 1/30/2019.
 */
function validateNow() {
    var name = document.getElementById('contact-name').value;
    var number = document.getElementById('contact-number').value;
    var email = document.getElementById('contact-email').value;
    var content = document.getElementById('message').value;
    var pat_name = /^[a-zA-Z\s]+$/;
    var pat_num = /^[0-9\s]+$/;
    var pat_email = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
    var val = false;
    if (!name.match(pat_name)) {
        document.getElementById('contact-name').value = "";
        document.getElementById('contact-name').focus();
        val = false;
    } else {
        if (!number.match(pat_num)) {
            document.getElementById('contact-number').value = "";
            document.getElementById('contact-number').focus();
            val = false;
        } else {
            if (!email.match(pat_email)) {
                document.getElementById('contact-email').value = "";
                document.getElementById('contact-email').focus();
                val = false;
            } else {
                val = true;
            }
        }
    }
    return val;


}