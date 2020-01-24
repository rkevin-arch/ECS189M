% rebase('templates/base.tpl')
<div class="row">
% if len(errormsg) > 0:
<div class="row errorbox" style="overflow-wrap: break-word;">{{errormsg}}</div>
% end
    <h5 class="eight columns"> Welcome back, <strong>{{username}}</strong>! </h5>
    <div class="u-pull-right">
      <a class="button" href="/posts" style="background: #33C3F0; color: #FFF;">Go to posts</a>
      <a class="button" href="/reset?username={{username}}">Reset Password</a>
      <a class="button" href="/logout" style="background: #f66;">Logout</a>
    </div>
</div>
