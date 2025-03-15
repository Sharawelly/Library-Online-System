let users = JSON.parse(localStorage.getItem('users')) ||  [];
console.log(users);
function check(form){
    let flag = 0;

    if((form.username.value==="")||(form.password.value==="")){
        alert( "Please enter both username and password" );
        return;
    } 
    for (let i = 0; i < users.length; i++) {

        if (form.username.value === users[i].userName && form.password.value === users[i].password && users[i].userType === 'admin') 
        {
            flag = 1;
        }
        else if (form.username.value === users[i].userName && form.password.value === users[i].password && users[i].userType === 'user')
        {
            flag = -1;
        }  
    }

    console.log(flag);
    switch (flag) {
        case 1:
            document.getElementById('form').innerHTML+='';
            window.location.href="AdminHome.html";
            break;

        case -1:
            document.getElementById('form').innerHTML+='';
            window.location.href="userHome.html";
            break;
    
        default:
        alert("Wrong Username or Password");
    }
}
