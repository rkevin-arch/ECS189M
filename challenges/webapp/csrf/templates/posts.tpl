% rebase('templates/base.tpl')
<div id="newpost">
    <form method="POST" action="/post" class="border boxshadow">
        <textarea class="console u-full-width" placeholder="Enter something here..." id="posttext" name="posttext" style="min-height: 200px;"></textarea>
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
<a class="button" href="/main">Go back</a>
</div>
