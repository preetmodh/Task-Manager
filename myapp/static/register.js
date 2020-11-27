document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#register').addEventListener('click',register);
    document.querySelector('#pass').addEventListener('click',pass);

  });
function register(){
    const name=document.querySelector('[name="name"]').value;
    const email=document.querySelector('[name="email"]').value;
    const password=document.querySelector('[name="password"]').value;
    const confirmation=document.querySelector('[name="confirmation"]').value;
    if (password!=confirmation){
        document.querySelector('#passc').innerHTML="<span style=margin:10px;color:darkred>Passwords must match!</span>";
    }
    else if (name.length==0){
        document.querySelector('#passc').innerHTML="<span style=margin:10px;color:darkred>Username field is empty!</span>";
    }
    else if (email.length==0){
        document.querySelector('#passc').innerHTML="<span style=margin:10px;color:darkred>Email field is empty!</span>";
        
    }
    else if (password.length==0){
        document.querySelector('#passc').innerHTML="<span style=margin:10px;color:darkred>Password field is empty!</span>";
    }
    else {
        $.ajax({
            url: '/register',
            data: {
                'email': email,
                'name':name,
                'password':password
        },
            type: 'POST'
          })
          document.location.href="/";
          
    }
}


function pass(){
document.getElementById('popup').style.display = 'block';
}


