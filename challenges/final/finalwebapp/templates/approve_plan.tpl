% rebase('templates/base.tpl')
<div id="plans">
  <table class="u-full-width">
      % for plan in plans:
        <tr>
          <td>
            <div>
             <h6><strong>{{!plan['title']}}</strong></h6>
             <div id="text">{{!plan['description']}}</div>

             <form method="POST" action="/approve_plan" id="approve">
              <input type="hidden" id="id" name="id" value={{plan['id']}}/>
              <input class="button-primary" type="submit" value="Approve Plan"/>
             </form>
            </div>
           </td>
          </tr>
      % end
  </table>
</div>
