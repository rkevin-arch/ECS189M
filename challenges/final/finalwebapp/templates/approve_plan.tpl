% rebase('templates/base.tpl')
<div style="font-size: 1.2em">Note: You're 2/3 of the way from solving this challenge! Detail how you got here in your writeup and you will have at least 350 points from this challenge.</div><br>
<div style="font-size: 1.2em">Welcome back, operator! Here is the list of plans awaiting your approval. You can also filter plans by keywords. Once you approve a plan, it will go into a separate table in the database.</div><br><br>
<form>
    <input type="text" placeholder="Filter string" name="filter" class="nine columns console">
    <button class="button-primary" type="submit">Filter</button>
</form>
<hr>
<div id="plans">
  <table class="u-full-width">
      % for plan in plans:
        <tr>
          <td>
            <div>
             <h6><strong>{{!plan['title']}}</strong></h6>
             <div id="text">{{!plan['description']}}</div>

             <form method="POST" action="/approveplan" id="approve">
              <input type="hidden" id="id" name="id" value={{plan['id']}}/>
              <input class="button-primary" type="submit" value="Approve Plan"/>
             </form>
            </div>
           </td>
          </tr>
      % end
  </table>
</div>
