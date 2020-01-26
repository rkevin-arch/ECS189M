% rebase('templates/base.tpl')
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
<div id="newpost">
    <form method="POST" action="/" class="border boxshadow">
        <input type="text" placeholder="Your name" name="name"><br>
        <textarea class="u-full-width" placeholder="Enter a comment here..." id="posttext" name="posttext" maxlength=200 style="min-height: 200px;"></textarea>
        <input class="button-primary" type="submit" value="Comment!" >
    </form>
</div>
<hr/>
