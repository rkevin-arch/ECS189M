% rebase('templates/base.tpl')
<div class="row">
% if len(errormsg) > 0:
<div class="row errorbox">{{errormsg}}</div>
% end
    <h5 class="eight columns"> Welcome back, <strong>{{username}}</strong>! </h5>
    <div class="u-pull-right">
      <a class="button" href="/?reset=1&username={{username}}">Reset Password</a>
      <a class="button" href="/?logout=1" style="background: #f66;">Logout</a>
    </div>
</div>
<hr/>
<div id="newpost">
    <form method="POST" action="/posts" class="border boxshadow">
        <textarea class="u-full-width" placeholder="Enter something here..." id="posttext" name="posttext" maxlength=140></textarea>
        <input class="button-primary" type="submit" value="Create Post" >

    </form>
</div>
<h3>Posts</h3>
<hr/>
<div id="posts">
<table class="u-full-width">
    % for post in posts:
        <tr>
            <td>
                <div>
                    <h6><strong>{{post.name}}</strong> says</h6>
                    <div id="text" style="padding-left: 2rem">{{!post.text}}</div>
                </div>
            </td>
        </tr>
    % end
</table>
</div>
