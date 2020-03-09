% rebase('templates/base.tpl')
<form method="POST" action="/submitplan" class="nine columns offset-by-one border boxshadow">
  <div style="font-size: 1.2em">Note: You're 1/3 of the way from solving this challenge. Detail how you got here in your writeup and you will have at least 175 points from this challenge.</div><br>
  <div style="font-size: 1.2em">Welcome! You are now logged in as {{user}}. You may submit any evil plans you might have for Redshift, and the operator will read through them and decide if we go through with the plan or not. Please enter your ideas below for review:</div><br><br>
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
