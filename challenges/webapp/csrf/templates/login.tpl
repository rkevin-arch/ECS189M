% rebase('templates/base.tpl')
<form method="POST" action="/" class="six columns offset-by-three border boxshadow">
% if len(errormsg) > 0:
<div class="row errorbox">{{errormsg}}</div>
% end
  <div class="row">
    <label for="username">Username</label>
    <input type="text" placeholder="user@twinpeaks.com" id="username" name="username">
  </div>
  <div class="row">
    <label for="password">Password</label>
    <input type="password" placeholder="" id="password" name="password">
  </div>
  <div class="row">
    <input class="button-primary" type="submit" value="Login" name="logininput">
  </div>
  <div> Note: default password is "slartibartfast"</div>
</form>
