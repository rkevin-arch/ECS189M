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
  </div>

    <div class="row">
    % if len(msg) > 0:
        <div class="row errorbox" style="overflow-wrap: break-word;">{{msg}}</div>
    % end
</form>
