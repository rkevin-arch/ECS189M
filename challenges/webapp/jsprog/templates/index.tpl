% rebase('templates/base.tpl')
<div class="row">This challenge asks you to write some Javascript. Your goal is to define two functions.</div>
<div class="row">1. You should write a function called <code>add</code>, that takes in two integers, adds them, and returns the result.</div>
<div class="row">2. You should write a function called <code>visit</code>, that takes in a string as a URL, and returns the result of visiting that URL (i.e. the page contents).</div>
<form method="POST">
    <textarea class="u-full-width" placeholder="code" name="code" style="min-height: 200px;font-family: monospace;">{{code}}</textarea>
    <button type="submit">Submit</button><br>
</form>
% if len(msg) > 0:
<div class="row" style="overflow-wrap: break-word;">
% for line in msg:
    {{line}}<br>
% end
</div>
% end
