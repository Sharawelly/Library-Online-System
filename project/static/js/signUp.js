function createUser()
{
    let users = JSON.parse(localStorage.getItem('users')) ||  [];
    let newUser = {
        userName: document.getElementById('username').value ,
        password: document.getElementById('password').value ,
        confirm_password: document.getElementById('confirm_password').value,
        email: document.getElementById( 'email' ).value,
        userType : document.getElementById( 'type' ).value
    };
    if (newUser.userName ==="" || newUser.password ==="" || newUser.confirm_password ==="" || newUser.email ==="" ) { 
        alert("There is missing Data!"); 
        return false;
    }

    if(newUser.password !== newUser.confirm_password) {
        alert('Invalid  Password! Please make sure your passwords match');
        return;
        }
    if (users.some(user=>user.userName === newUser.userName && user.password === newUser.password)) {
        alert('User already exist :)');
}   else{
        users.push(newUser);
        localStorage.setItem("users",JSON.stringify(users));
        document.getElementById( "form" ).reset();
        if (newUser.userType === 'admin') {
            window.location.href='AdminHome.html';
        }
        else{
            window.location.href='userHome.html';
        }
}
};
function deleter(){
    localStorage.clear();
}