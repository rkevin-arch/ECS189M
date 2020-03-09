% rebase('templates/base.tpl')
<form method="POST" action="/login" class="six columns offset-by-three border boxshadow">
  <div class="row">
    <label for="username">Username</label>
    <input type="text" placeholder="user" id="username" name="username">
  </div>
  <div class="row">
    <label for="password">Password</label>
    <input type="password" placeholder="" id="password" name="password">
  </div>
  <div class="row">
    <input class="button-primary" type="submit" value="Login" name="logininput">
    <input class="button-secondary" type="submit" formaction="/register" value="Register" name="signupinput">
  </div>
  <div> Note: default password after a password reset is "password"</div>
</form>



