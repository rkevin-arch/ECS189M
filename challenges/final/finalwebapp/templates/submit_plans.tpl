% rebase('templates/base.tpl')
<form method="POST" action="/submitplan" class="nine columns offset-by-one border boxshadow">
  <div class="row">
    <label for="title">Title</label>
    <input type="text" placeholder="Title" id="title" name="title"/>
  </div>
  <div class="row">
    <label for="plan">Secret Plan</label>
    <textarea class="console u-full-width" placeholder="Enter your secret plan here..." id="plan" name="plan" maxlength=201 style="min-height: 300px;"></textarea>
 
  </div>
  <div class="row">
    <input class="button-primary" type="submit" value="Submit Plan" name="submit">
  </div>

    <div class="row">
    % if len(msg) > 0:
        <div class="row errorbox" style="overflow-wrap: break-word;">{{msg}}</div>
    % end
</form>
